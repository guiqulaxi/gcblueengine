/**
**  @file tcAeroAirObject.cpp
*/
/*
**  Copyright (c) 2014, GCBLUE PROJECT
**  All rights reserved.
**
**  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
**
**  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
**
**  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the 
**     documentation and/or other materials provided with the distribution.
**
**  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from 
**     this software without specific prior written permission.
**
**  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
**  NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
**  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
**  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
**  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
**  IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/


//#include "stdwx.h"

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcAeroAirObject.h"
#include "tcAirObject.h"
#include "tcJetDBObject.h"
#include "tcAero.h"
#include "math_constants.h"
////#include "tc3DModel.h"
//#include "tcParticleEffect.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "tcScenarioLogger.h"
#include "strutil.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"

using namespace database;


tcCommandStream& tcAeroAirObject::operator<<(tcCommandStream& stream)
{
    ClearNewCommand();

    tcAirObject::operator<<(stream);

    stream >> throttleFraction;

    //fprintf(stdout, "received aero guidance update, id: %d, HSA %f, %f, %f\n", mnID,
    //	mcGS.mfGoalHeading_deg, mcGS.mfGoalSpeed_kts, mcGS.mfGoalAltitude_m);

    return stream;
}

tcCommandStream& tcAeroAirObject::operator>>(tcCommandStream& stream)
{
    tcAirObject::operator>>(stream);

    stream << throttleFraction;

    //fprintf(stdout, "sending aero guidance update, id: %d, HSA %f, %f, %f\n", mnID,
    //	mcGS.mfGoalHeading_deg, mcGS.mfGoalSpeed_kts, mcGS.mfGoalAltitude_m);
    return stream;
}

/**
* Load
*/
tcGameStream& tcAeroAirObject::operator<<(tcGameStream& stream)
{
    tcAirObject::operator<<(stream);

    stream >> throttleFraction;
    stream >> levelThrottleFraction;
    stream >> levelThrust_N;
    stream >> angleOfAttack;
    stream >> lastThrust_N;
    stream >> lastWeight_N;

    commandObj << stream;

    return stream;
}

/**
* Save
*/
tcGameStream& tcAeroAirObject::operator>>(tcGameStream& stream)
{
    tcAirObject::operator>>(stream);

    stream << throttleFraction;
    stream << levelThrottleFraction;
    stream << levelThrust_N;
    stream << angleOfAttack;
    stream << lastThrust_N;
    stream << lastWeight_N;

    commandObj >> stream;

    return stream;
}



void tcAeroAirObject::ClearNewCommand()
{
    tcAirObject::ClearNewCommand();
    commandObj.ClearNewCommand();
}

bool tcAeroAirObject::HasNewCommand() const
{
    return tcAirObject::HasNewCommand() || commandObj.HasNewCommand();
}

/**
* Computationally expensive, avoid calling this method frequently
* @param rho set to air density for this altitude [kg/m3]
* @return speed solution in m/s
*/
float tcAeroAirObject::SolveForSpeed(float throttle, float altitude_m, float& rho, float damageLevel, std::shared_ptr<const tcJetDBObject> airData)
{
    // 计算空气密度
    rho = Aero::GetAirDensity(altitude_m);
    // 计算声速
    float vsound = Aero::GetSoundSpeed(altitude_m);
    // 计算声速的倒数
    float inv_vsound = 1.0f / vsound;
    // 获取推力系数
    float thrustFactor = airData->GetThrustFactor(altitude_m);
    // 获取诱导阻力系数
    float cdi = airData->GetInducedDragCoefficient();
    // 寻找近似解
    // find approximate solution
    float bestSolution_mps = 0;
    float bestThrustMargin = 0;

    for (float speed_mps = 100.0f; speed_mps<=1000.0f; speed_mps+=15.0f)
    {
        // 计算推力
        float thrust_N = GetThrust(throttle, thrustFactor, speed_mps, airData);
        // 计算马赫数
        float vmach = speed_mps * inv_vsound;
        // 获取寄生阻力系数
        float cdp = airData->GetParasiticDragCoefficient(vmach);
        // 计算空气密度平方
        float rhov2 = rho*speed_mps*speed_mps;
        // 计算阻力
        float drag_N = (cdp*rhov2) + (cdi/rhov2);
        // 额外的阻力因子，用于损伤（必须与UpdateSpeed中的计算匹配）
        drag_N *= (1 + damageLevel); // additional drag factor for damage (must match calc in UpdateSpeed)
        // 计算推力余量
        float thrustMargin = thrust_N - drag_N;

        if (thrustMargin >= 0)
        {
            bestSolution_mps = speed_mps;
            bestThrustMargin = thrustMargin;
        }
    }

    // 如果没有找到合适的速度解，返回0
    if (bestSolution_mps == 0) return 0;

    // 牛顿法迭代以优化近似解
    // newton's method iterations to refine approximate solution
    const float maxError = 100.0f;
    unsigned nIterations = 0;
    float dv = 1.0f;
    float v = bestSolution_mps;
    float y = bestThrustMargin;
    while ((fabsf(y) > maxError) && (++nIterations < 7))
    {
        // 更新速度值
        float vn = v + dv;
        // 计算马赫数
        float vn_mach = vn * inv_vsound;
        // 计算推力
        float thrust_N = GetThrust(throttle, thrustFactor, vn, airData);
        // 获取寄生阻力系数
        float cdp = airData->GetParasiticDragCoefficient(vn_mach);
        // 计算空气密度平方
        float rhov2 = rho*vn*vn;
        // 计算阻力
        float drag_N = (cdp*rhov2) + (cdi/rhov2);
        drag_N *= (1 + damageLevel);
        // 计算新的推力余量
        float yn = thrust_N - drag_N;
        // 计算速度变化率
        float dvdy = dv / (yn - y);
        // 更新速度变化量
        dv = -yn * dvdy;
        // 更新速度值
        v = vn;
        // 更新推力余量
        y = yn;
    }
    // 返回最小速度值，不超过最大速度限制

    assert(nIterations < 8); // means we hit max iteration count, bad solution?
    return std::min(v, airData->mfMaxSpeed_kts*C_KTSTOMPS);
}


/*
* @return throttle fraction to achieve speed_mps at altitude_m
* @ 返回在指定高度，要达到指定速度油门
*/
float tcAeroAirObject::SolveForThrottle(float speed_mps, float altitude_m, float damageLevel, std::shared_ptr<const tcJetDBObject> airData)
{
    // 计算空气密度
    float rho = Aero::GetAirDensity(altitude_m);
    // 计算声速
    float vsound = Aero::GetSoundSpeed(altitude_m);
    // 计算声速的倒数
    float inv_vsound = 1.0f / vsound;
    // 计算马赫数
    float speed_mach = speed_mps * inv_vsound;

    // 获取寄生阻力系数
    float cdp = airData->GetParasiticDragCoefficient(speed_mach);
    // 获取诱导阻力系数
    float cdi = airData->GetInducedDragCoefficient();

    // 计算阻力
    float rhov2 = rho*speed_mps*speed_mps;
    float drag_N = (cdp*rhov2) + (cdi/rhov2);
    // 考虑损坏对阻力的影响
    drag_N *= (1 + damageLevel); // additional drag factor for damage (must match calc in UpdateSpeed)

    // 计算期望推力
    float thrustDesired_N = drag_N;

    // 获取推力因子
    float thrustFactor = airData->GetThrustFactor(altitude_m);

    // 计算最大军用推力
    float maxMilThrust_N = GetThrust(1.0f, thrustFactor, speed_mps, airData);
    // 计算最大加力推力
    float maxABThrust_N = GetThrust(2.0f, thrustFactor, speed_mps, airData);

    // 如果期望推力小于等于最大军用推力，则返回推力比
    if (thrustDesired_N <= maxMilThrust_N)
    {
        return thrustDesired_N / maxMilThrust_N;
    }
    // 如果期望推力小于等于最大加力推力，则计算并返回油门比例
    else if (thrustDesired_N <= maxABThrust_N)
    {
        float throttle = (thrustDesired_N + maxABThrust_N - 2.0f*maxMilThrust_N) /
                         (maxABThrust_N - maxMilThrust_N);
        return throttle;
    }
    // 如果期望推力大于最大加力推力，则返回2.0（全油门）
    else
    {
        return 2.0f;
    }
}

/**
* @return mil throttle setting (max 1.0) to achieve thrust_N for current aeroAirObj 计算指定推力需要的油门
*
*/
float tcAeroAirObject::MilThrottleForThrust(float thrust_N) const
{
    // 获取当前高度下的动力因子
    float thrustFactor = mpDBObject->GetThrustFactor(mcKin.mfAlt_m);
    // 计算最大军用推力（单位：牛顿）
    float maxMilThrust_N = GetThrust(1.0f, thrustFactor, C_KTSTOMPS*mcKin.mfSpeed_kts, mpDBObject);

    // 如果所需推力小于等于最大军用推力
    if (thrust_N <= maxMilThrust_N)
    {
        // 返回所需推力与最大军用推力的比值，确保结果不小于0
        return std::max(thrust_N / maxMilThrust_N, 0.0f);
    }
    else
    {
        // 如果所需推力大于最大军用推力，则返回1.0（全油门）
        return 1.0f;
    }
}

/**
* @return fuel rate in kg/s
*/
float tcAeroAirObject::CalculateFuelRate(float speed_mps, float alt_m) const
{
    float throttleSolution = SolveForThrottle(speed_mps, alt_m, mfDamageLevel, mpDBObject);

    float thrustFactor = 0;
    float fuelEfficiencyFactor = 0;
    mpDBObject->GetThrustAndEfficiencyFactors(alt_m, thrustFactor, fuelEfficiencyFactor);

    return GetFuelRate(throttleSolution, fuelEfficiencyFactor, thrustFactor, mfDamageLevel, mpDBObject);
}

/**
* Method to calculate speed and fuel consumption vs. altitude and throttle setting
*/
void tcAeroAirObject::CalculateSpeedParams(float altitude_m, float throttle,
                                           float& maxSpeed_mps, float& fuelRate_kgps, float damageLevel, std::shared_ptr<const tcJetDBObject> airData)
{
    assert(airData != 0);
    float rho = 1.0f;
    float speed_mps = SolveForSpeed(throttle, altitude_m, rho, damageLevel, airData);

    float thrustFactor;
    float fuelEfficiencyFactor;
    airData->GetThrustAndEfficiencyFactors(altitude_m, thrustFactor, fuelEfficiencyFactor);

    fuelRate_kgps = GetFuelRate(throttle, fuelEfficiencyFactor, thrustFactor, damageLevel, airData);

    // disabled this 1 MAY 2011, may need to do this stall check in calling functions

    //float stallSpeed_mps = airData->stallSpeed_mps * powf(tcJetDBObject::inv_rho_sealevel * rho, -0.5f); // stall speed at altitude
    /* if (speed_mps >= stallSpeed_mps)
    {
        float thrustFactor;
        float fuelEfficiencyFactor;
        airData->GetThrustAndEfficiencyFactors(altitude_m, thrustFactor, fuelEfficiencyFactor);

        fuelRate_kgps = GetFuelRate(throttle, fuelEfficiencyFactor, thrustFactor, damageLevel, airData);
    }
    else
    {
        speed_mps = stallSpeed_mps;
        fuelRate_kgps = 99.0f;
    }*/

    maxSpeed_mps = speed_mps;
}

float tcAeroAirObject::GetCruiseRangeKm(float alt_m) const
{
    float vcruise_mps = 0;
    return GetAeroCruiseRangeKm(alt_m, fuel_kg, mfDamageLevel, mpDBObject, vcruise_mps);
}

float tcAeroAirObject::GetAeroCruiseRangeKm(float alt_m, float fuelLoad_kg, float damageLevel, std::shared_ptr<const tcJetDBObject> airData, float& cruise_mps)
{
    // 确保传入的airData不为空指针
    assert(airData != 0);
    // 根据高度计算巡航速度
    cruise_mps = airData->GetCruiseSpeedForAltitude(alt_m);

    // 求解油门设置，使飞机达到巡航速度
    float throttleSolution = SolveForThrottle(cruise_mps, alt_m, damageLevel, airData);
    // 如果油门设置大于1.0，将其限制为1.0，并重新计算巡航速度
    if (throttleSolution > 1.0f)
    {
        float rho_temp;
        throttleSolution = 1.0f;
        cruise_mps = SolveForSpeed(throttleSolution, alt_m, rho_temp, damageLevel, airData);
    }

    // 获取推力因子和燃油效率因子
    float thrustFactor = 0;
    float fuelEfficiencyFactor = 0;
    airData->GetThrustAndEfficiencyFactors(alt_m, thrustFactor, fuelEfficiencyFactor);

    // 计算燃油消耗速率
    float fuelRate_kgps = GetFuelRate(throttleSolution, fuelEfficiencyFactor, thrustFactor, damageLevel, airData);
    // 确保燃油消耗速率不为负数
    assert(fuelRate_kgps >= 0);

    // 计算飞行时间
    float time_s = fuelLoad_kg / (fuelRate_kgps + 0.0001f);
    // 计算飞行距离（单位：千米）
    float distance_km = 0.001f * cruise_mps * time_s;

    return distance_km;
}

/**
* Expensive, don't call this too often 计算飞的最远的巡航高度
* Checks for best cruise altitude every 1000 m between 6000 m and 13000 m altitude
*/
float tcAeroAirObject::GetCruiseAltitude() const
{
    float bestCruiseAlt_m = 1000.0f;
    float bestCruiseRange_km = 0.0f;

    for (float alt_m=6000.0f; alt_m<=13000.0f; alt_m += 1000.0f)
    {
        float range_km = GetCruiseRangeKm(alt_m);
        if (range_km > bestCruiseRange_km)
        {
            bestCruiseAlt_m = alt_m;
            bestCruiseRange_km = range_km;
        }
    }

    return bestCruiseAlt_m;
}

/**
* @return cruise speed in kts
*/
float tcAeroAirObject::GetCruiseSpeedForAltitude(float alt_m) const
{
    return C_MPSTOKTS * mpDBObject->GetCruiseSpeedForAltitude(alt_m);
}


/**
* @return stall speed in kts
*/
float tcAeroAirObject::GetStallSpeedForAltitude(float alt_m) const
{
    return C_MPSTOKTS * mpDBObject->GetStallSpeedForAltitude(alt_m);
}



/**
* @return current fuel burn rate in kg/s
* This info could be saved during Update() instead of being recalculated here
*/
float tcAeroAirObject::GetCurrentFuelRate() const
{
    float thrustFactor;
    float fuelEfficiencyFactor;
    mpDBObject->GetThrustAndEfficiencyFactors(mcKin.mfAlt_m, thrustFactor, fuelEfficiencyFactor);

    return GetFuelRate(throttleFraction, fuelEfficiencyFactor, thrustFactor, mfDamageLevel, mpDBObject);
}


float tcAeroAirObject::GetOpticalCrossSection() const
{
    return mpDBObject->GetComponent<tcAirDetectionDBObject>()->opticalCrossSection_dBsm;
}



float tcAeroAirObject::GetIRSignature(float az_deg) const
{
    bool isSupersonic = (mcKin.mfSpeed_kts > 600.0f); // a rough test, no altitude variation
    bool afterburnersOn = (GetThrottleFraction() > 1.0f);

    if (!isSupersonic)
    {
        if (!afterburnersOn)
        {
            return mpDBObject->GetComponent<tcAirDetectionDBObject>()->GetIRSig_dB(az_deg, tcAirDetectionDBObject::IRMODELA);
        }
        else
        {
            return mpDBObject->GetComponent<tcAirDetectionDBObject>()->GetIRSig_dB(az_deg, tcAirDetectionDBObject::IRMODELB);
        }
    }
    else
    {
        if (!afterburnersOn)
        {
            return mpDBObject->GetComponent<tcAirDetectionDBObject>()->GetIRSig_dB(az_deg, tcAirDetectionDBObject::IRMODELC);
        }
        else
        {
            return std::max(mpDBObject->GetComponent<tcAirDetectionDBObject>()->GetIRSig_dB(az_deg, tcAirDetectionDBObject::IRMODELB),
                            mpDBObject->GetComponent<tcAirDetectionDBObject>()->GetIRSig_dB(az_deg, tcAirDetectionDBObject::IRMODELC));
        }
    }

}


void tcAeroAirObject::Clear()  
{  
    tcAirObject::Clear();
}


void tcAeroAirObject::RandInitNear(float afLon_deg, float afLat_deg)
{
    if (mpDBObject == NULL) {return;}
    tcAirObject::RandInitNear(afLon_deg, afLat_deg);

    // overwrite tcAirObject random suffix
    mzUnit = "AIRX_";
    mzUnit=strutil::AssignRandomSuffix(mzUnit);

    throttleFraction = 0.7f;
    angleOfAttack = 0;
}

void tcAeroAirObject::PrintToFile(tcFile& file) 
{
    tcAirObject::PrintToFile(file);
}

void tcAeroAirObject::SaveToFile(tcFile& file) 
{
    tcAirObject::SaveToFile(file); 
    file.Write(&throttleFraction,sizeof(throttleFraction)); 
    file.Write(&angleOfAttack,sizeof(angleOfAttack));
}

void tcAeroAirObject::LoadFromFile(tcFile& file) 
{
    tcAirObject::LoadFromFile(file); 
    file.Read(&throttleFraction,sizeof(throttleFraction));
    file.Read(&angleOfAttack,sizeof(angleOfAttack));
}

void tcAeroAirObject::Serialize(tcFile& file, bool mbLoad) 
{
    if (mbLoad) 
    {
        LoadFromFile(file);
    }
    else 
    {
        SaveToFile(file);
    }
}

void tcAeroAirObject::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    // call parent serialization
    tcAirObject::SerializeToJson(obj, allocator);

    // aerodynamic-specific fields
    obj.AddMember("throttleFraction", rapidjson::Value().SetFloat(throttleFraction), allocator);
    obj.AddMember("levelThrottleFraction", rapidjson::Value().SetFloat(levelThrottleFraction), allocator);
    obj.AddMember("levelThrust_N", rapidjson::Value().SetFloat(levelThrust_N), allocator);
    obj.AddMember("angleOfAttack", rapidjson::Value().SetFloat(angleOfAttack), allocator);
    obj.AddMember("lastThrust_N", rapidjson::Value().SetFloat(lastThrust_N), allocator);
    obj.AddMember("lastWeight_N", rapidjson::Value().SetFloat(lastWeight_N), allocator);
}

void tcAeroAirObject::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{
    std::string s;

    tcPlatformObject::SaveToPython(logger);

    s=strutil::format("UI.SetThrottle(%f)", GetThrottleFraction());
    logger.AddScenarioText(s);
}

/**
* Solve for throttle setting for requested speed and
* set throttle with result
*/
void tcAeroAirObject::SetSpeed(float newSpeed) 
{
    tcPlatformObject::SetSpeed(newSpeed);

    float throttle = SolveForThrottle(C_KTSTOMPS*newSpeed, mcKin.mfAlt_m, mfDamageLevel, mpDBObject);

    SetThrottleFraction(throttle);
}

/**
* New throttle fraction system for afterburners, 
* 2.0 is max afterburner, 1.0-2.0 varies afterburner thrust continuously. This
* isn't realistic for most aircraft, but makes formation flying at afterburners 
* a lot easier
* *新的油门分数系统，用于加力燃烧器，
* 2.0是最大加力燃烧器推力，1.0-2.0可以连续变化加力燃烧器的推力。这
* 对大多数飞机来说并不现实，但使得在加力燃烧器状态下进行编队飞行变得容易得多。
*/
void tcAeroAirObject::SetThrottleFraction(float fract) 
{
    throttleFraction = std::min(fract, 2.0f);
    levelThrottleFraction = 0; // cancel any automatic climb throttle adjust

    commandObj.SetNewCommand(THROTTLE_CMD);
}

void tcAeroAirObject::ApplyRestrictions() 
{
    tcAirObject::ApplyRestrictions();
}



/**
* Has problems for large time steps, > about 1 sec
*/
void tcAeroAirObject::UpdateClimb(float dt_s) 
{
    // 保存初始爬升角度，用于自动油门调整计算
    float climbAngleStart_rad = mcKin.mfClimbAngle_rad;

    // 调用父类的UpdateClimb方法更新爬升状态
    tcAirObject::UpdateClimb(dt_s);
    // 设置俯仰角为攻角加上爬升角
    mcKin.mfPitch_rad = angleOfAttack + mcKin.mfClimbAngle_rad;

    // 如果爬升角为0且水平油门分数也为0，则直接返回
    if ((mcKin.mfClimbAngle_rad == 0) && (levelThrottleFraction == 0))
    {
        return;
    }

    // 如果爬升角为0但水平油门分数不为0，恢复旧的油门设置
    if ((mcKin.mfClimbAngle_rad == 0) && (levelThrottleFraction != 0))
    {
        throttleFraction = levelThrottleFraction; // 恢复之前的油门设置
        levelThrottleFraction = 0;
        levelThrust_N = 0;
        return;
    }

    // 如果水平油门分数为0，保存水平油门和推力设置
    if (levelThrottleFraction == 0)
    {
        levelThrottleFraction = throttleFraction;
        throttleFraction = std::max(throttleFraction, 1.0f);
        levelThrust_N = lastThrust_N;
    }

    // 判断爬升角是否发生变化
    bool climbChanging = (mcKin.mfClimbAngle_rad != climbAngleStart_rad);

    // 如果爬升角发生变化，计算所需的推力并设置油门
    if (climbChanging)
    {
        float thrustNeededed_N = levelThrust_N + lastWeight_N * sinf(mcKin.mfClimbAngle_rad);
        throttleFraction = MilThrottleForThrust(thrustNeededed_N);
    }
}


void tcAeroAirObject::UpdateEffects()
{
    //    if (model)
    //    {
    //		if (mfDamageLevel > 0.1f)
    //		{
    //			model->SetSmokeMode(tc3DModel::DAMAGE);
    //		}
    //        else if (throttleFraction > 1.0f)
    //        {
    //            model->SetSmokeMode(tc3DModel::AFTERBURNER);
    //        }
    //        else
    //        {
    //            model->SetSmokeMode(tc3DModel::OFF);
    //        }
    //        model->UpdateEffects();
    //    }
}

void tcAeroAirObject::UpdateHeading(float dt_s) 
{
    tcAirObject::UpdateHeading(dt_s);
}

void tcAeroAirObject::Update(double afStatusTime) 
{
    const float min_update_s = 0.0f;
    float dt_s = (float)(afStatusTime - mfStatusTime);

    // shouldn't be called for child objects
    if (parent != NULL) {return;} // captive, let parent update if applicable
    if ((dt_s <= min_update_s)  && !tcGameObject::IsEditMode())
    {
        return;
    } // added for pause case

    assert(mpDBObject);
    
    UpdateEffects();

    if (mfDamageLevel >= 1.0f)
    {
        UpdateDestroyed(afStatusTime);
        mfStatusTime = afStatusTime;
        return;
    }

    /* In multiplayer mode, skip command based updates for client objects not controlled
	** by client. This will cause object to jump more but avoids having to broadcast command
	** changes to all alliance clients. The controller of the object will see smoother
	** behavior.
    ** CHANGED 24AUG2008 to remove the IsControlled() case, this jumps around too much at the client, defeating the purpose
	*/
    if (!IsClientMode())
    {

        formation.Update(std::dynamic_pointer_cast<tcAirObject>(tcGameObject::shared_from_this()));

        UpdateInFlightRefuel(dt_s);

        UpdateHeading(dt_s);

        UpdateSpeed(dt_s);

        UpdateClimb(dt_s);

        ApplyRestrictions();
    }
    else if (IsControlled())
    {
        UpdateHeading(dt_s);
    }

    Move(dt_s);

    UpdateLauncherState(dt_s);

    UpdateSensors(afStatusTime);

    UpdateAI(afStatusTime);

    //    Update3D();

    mfStatusTime = afStatusTime; 
}

/**
* @param vmach Speed divided by speed of sound (mach number)
* @return parasitic drag coeff including 0.5 factor
*/
float tcAeroAirObject::GetParasiticDragCoefficient(float vmach) const
{
    return mpDBObject->GetParasiticDragCoefficient(vmach);
}

/**
* @return kg/s fuel consumption
*/
float tcAeroAirObject::GetFuelRate(float throttle, float efficiencyFactor, float thrustFactor, float damageLevel, 
                                   std::shared_ptr<const tcJetDBObject> airData)
{
    // 计算损坏对燃料消耗的影响，损坏程度越高，燃料消耗越多
    float damagePenalty = 1.0f + 9.0f*damageLevel;
    // 确保油门值在有效范围内
    assert((throttle >= 0) && (throttle <= 2.0f));
    // 如果油门值小于等于1.0，计算标准燃料消耗率
    if (throttle <= 1.0f)
    {
        return throttle * thrustFactor * efficiencyFactor *
               damagePenalty * airData->mfFuelRate_kgps;
    }
    else
    {
        // 计算非加力燃烧阶段的燃料消耗率
        float standardRate = (2.0f - throttle) * thrustFactor * efficiencyFactor *
                             airData->mfFuelRate_kgps;

        // 计算加力燃烧阶段的燃料消耗率
        float afterburnerRate = (throttle - 1.0f)*airData->mfAfterburnFuelRate_kgps;

        // 返回总燃料消耗率，包括损坏惩罚和加力燃烧阶段
        return damagePenalty * (standardRate + afterburnerRate);
    }
}

/**
* @param thrustFactor altitude dependent thrust factor (applied to military and afterburner thrust)
* @return thrust in Newtons
*/
/**
* 计算飞行器的推力，考虑海拔高度、油门和速度等因素。
* @param thrustFactor 海拔高度依赖的推力系数（应用于军事和加力燃烧器的推力）
* @param throttle 油门值，范围为0到2
* @param speed_mps 飞行器的速度，单位为米/秒
* @param airData 飞行器的空气动力学数据对象指针
* @return 返回推力值，单位为牛顿
*/
float tcAeroAirObject::GetThrust(float throttle, float thrustFactor, float speed_mps,  std::shared_ptr<const tcJetDBObject> airData)
{
    assert(airData != 0); // 确保传入的airData不为空
    assert(throttle <= 2.0f); // 确保油门值在有效范围内

    // 获取军事推力速度斜率和加力燃烧器推力速度斜率
    float a_mil = airData->militaryThrustSpeedSlope;
    float a_ab = airData->abThrustSpeedSlope;
    // 计算调整后的军事推力
    float adjustedMilThrust = airData->militaryThrust_N * (1.0f + (a_mil * speed_mps));

    if (throttle <= 1.0f)
    {
        // 如果油门小于等于1，则返回调整后的军事推力乘以油门和推力系数
        return adjustedMilThrust * throttle * thrustFactor;
    }
    else
    {
        // 如果油门大于1，则计算标准推力和加力燃烧器推力
        float standardThrust_N = adjustedMilThrust * (2.0f - throttle);
        float adjustedABThrust = airData->mfAfterburnThrust_N * (1.0f + (a_ab * speed_mps));
        float burnerThrust_N = adjustedABThrust * (throttle - 1.0f);

        // 返回推力系数乘以标准推力和加力燃烧器推力的和
        return thrustFactor * (standardThrust_N + burnerThrust_N);
    }
}
/**
* Calculate thrust and fuel consumption. Update fuel.
* @return thrust in Newtons
*/
/**
* 计算推力和燃料消耗。更新燃料。
* @return 推力，单位为牛顿
*/
float tcAeroAirObject::UpdateThrust(float dt_s)
{
    // 如果燃料大于0
    if (fuel_kg > 0)
    {
        // 根据高度计算推力衰减因子
        float thrustFactor;
        float fuelEfficiencyFactor;
        mpDBObject->GetThrustAndEfficiencyFactors(mcKin.mfAlt_m, thrustFactor, fuelEfficiencyFactor);

        // 计算燃料消耗速率，考虑油门位置、燃料效率因子、推力因子、损坏等级和飞行器数据库对象
        float fuelRate_kgps = GetFuelRate(throttleFraction, fuelEfficiencyFactor, thrustFactor,
                                          mfDamageLevel, mpDBObject);
        // 计算推力，考虑油门位置、推力因子、速度（千米/小时转换为米/秒）和飞行器数据库对象
        float thrust_N = GetThrust(throttleFraction, thrustFactor, mcKin.mfSpeed_kts*C_KTSTOMPS, mpDBObject);

        // 更新燃料量，减去燃料消耗速率乘以时间间隔
        fuel_kg -= fuelRate_kgps * dt_s;
        // 如果燃料小于0，将燃料设置为0（烧尽后重新加满）
        if (fuel_kg < 0) fuel_kg = 0;

        // 返回推力值
        return thrust_N;
    }
    else
    {
        // 燃料耗尽，返回0
        return 0;
    }
}

/**
* 使用气动模型更新速度。
* @param dt_s 自上次更新以来的时间步长
*/
void tcAeroAirObject::UpdateSpeed(float dt_s)
{
    // 声明变量
    float rhv2;
    float K_dp;
    float vmach, vsound;
    float fDrag_N, fThrust_N;

    tcKinematics& k = mcKin;

    // 计算速度和密度
    float mfSpeed_mps = k.mfSpeed_kts*C_KTSTOMPS;
    float rho = Aero::GetAirDensity(k.mfAlt_m);
    rhv2 = rho*mfSpeed_mps*mfSpeed_mps;
    vsound = Aero::GetSoundSpeed(k.mfAlt_m);
    vmach = mfSpeed_mps/vsound;

    // 计算指示空速和其倒数
    float ias_mps = sqrtf(0.8f * rho) * mfSpeed_mps; // 近似指示空速
    float inv_ias_mps = 1.0 / ias_mps;
    float not_stall = float(ias_mps > mpDBObject->stallSpeed_mps);

    // 计算阻力系数
    K_dp = GetParasiticDragCoefficient(vmach);

    // 计算阻力
    fDrag_N = (K_dp * rhv2) + not_stall*(mpDBObject->GetInducedDragCoefficient() / rhv2);
    fDrag_N *= (1.0f + mfDamageLevel); // 阻力随部分损坏程度增加而增加

    // 计算质量、重力和推力
    float mass_kg = mpDBObject->weight_kg + fuel_kg;
    float weight_N = 0.5f * C_G * mass_kg; // 0.5是临时因子
    lastWeight_N = weight_N;

    // 计算平衡重量所需的升力
    //float lift_N = weight_N * cosf(k.mfClimbAngle_rad);
    //float Cl = lift_N / (rhv2 * mpDBObject->mfWingArea_sm);

    // 计算推力
    fThrust_N = UpdateThrust(dt_s);
    lastThrust_N = fThrust_N;

    // 计算攻角
    const float aoaConstant = 5.0f; // 用于近似，aoa = C / IAS
    angleOfAttack = aoaConstant * inv_ias_mps;

    // 计算失速俯仰角
    const float stallPitch = -0.1f; // 10:1滑翔比

    // 根据空速调整油门、最大俯仰角和失速角度
    if (ias_mps <= mpDBObject->stallSpeed_mps)
    {
        throttleFraction = 1.0f;
        //mcGS.mfGoalAltitude_m = k.mfAlt_m - 50.0f; // 避免与失速调整相关的连接洪水
        maxPitch_rad = std::min(maxPitch_rad, stallPitch);
    }
    else if (ias_mps < mpDBObject->stallSpeed_mps + 50.0f)
    {
        maxPitch_rad = std::min(maxPitch_rad, stallPitch + 0.02f * (ias_mps - mpDBObject->stallSpeed_mps));
    }
    else
    {
        if (maxPitch_rad < 0) maxPitch_rad = MAX_PITCH_RAD; // 重置为默认值
    }

    // 计算净力、加速度和速度
    float netForce_N = fThrust_N - fDrag_N - weight_N *sinf(k.mfClimbAngle_rad);

    /* 阻力模型有问题：加速度太慢，可以通过爬升然后下降来获得更快的加速度，这是错误的。
    ** 通过添加一个4.0因子来加速加速度/减速
    */
    float accel_mps2 = 4.0f * netForce_N / mass_kg;

    k.mfSpeed_kts += (accel_mps2 * dt_s)*C_MPSTOKTS;

    if (k.mfSpeed_kts > mpDBObject->mfMaxSpeed_kts) k.mfSpeed_kts = mpDBObject->mfMaxSpeed_kts;
    else if (k.mfSpeed_kts <= 40.0)
    {
        // 不应该发生，但限制速度为40，在这种情况下缓慢下降
        k.mfSpeed_kts = 40.0;
        if (k.mfClimbAngle_rad > -0.1) k.mfClimbAngle_rad -= dt_s * 0.1f;
    }
}


/**
* Shouldn't use this form.
*/
tcAeroAirObject::tcAeroAirObject() 
    : tcAirObject()
{
    assert(false);
    mnModelType = MTYPE_FIXEDWINGX;
}

/**
* Constructor that initializes using info from database entry.
*/
tcAeroAirObject::tcAeroAirObject(std::shared_ptr<tcJetDBObject>obj)
    : tcAirObject(obj),
    levelThrottleFraction(0),
    levelThrust_N(0),
    angleOfAttack(0),
    lastThrust_N(0),
    lastWeight_N(1)
{
    mpDBObject = obj;
    mnModelType = MTYPE_FIXEDWINGX;
    SetThrottleFraction(1.0f);
}

tcAeroAirObject::~tcAeroAirObject()
{
}
