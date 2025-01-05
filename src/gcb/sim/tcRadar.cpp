/**
**  @file tcRadar.cpp
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
#include "tcCommandQueue.h"
#include "nsNav.h"
#include "tcRadar.h"
#include "tcGameObject.h"

#include "tcAirfieldObject.h"
#include "tcAirObject.h"
#include "tcBallisticWeapon.h"

#include "tcMissileObject.h"
#include "tcSubObject.h"
#include "tcSurfaceObject.h"
#include "tcAirCM.h"

#include "tcMissileDBObject.h"
#include "tcCounterMeasureDBObject.h"
#include "tcSimState.h"
#include "tcGameObjIterator.h"
#include "tcSensorTrackIterator.h"
#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "tcAllianceInfo.h"
#include "tcEventManager.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// break up this file later


float tcRadar::lastTargetRCS_dBsm = -88.0f;
float tcRadar::last_snr_margin_dB = -88.0f;
float tcRadar::lastTargetElevation_rad = 1.72787596f;

/**
* Load state from stream
*/
tcUpdateStream& tcRadar::operator<<(tcUpdateStream& stream)
{
    tcSensorState::operator<<(stream);

	unsigned char fireControlTrackCount;
    stream >> fireControlTrackCount;
	fireControlTracks.clear();

	for (unsigned char n=0; n<fireControlTrackCount; n++)
	{
		long trackId;
		stream >> trackId;
		fireControlTracks.push_back(trackId);
	}

    //stream >> isSemiactive;

    return stream;
}

/**
* Save state to stream
*/
tcUpdateStream& tcRadar::operator>>(tcUpdateStream& stream)
{
    tcSensorState::operator>>(stream);

	assert(fireControlTracks.size() < 256);
	unsigned char fireControlTrackCount = (unsigned char)fireControlTracks.size();
    stream << fireControlTrackCount;

	for (unsigned char n=0; n<fireControlTrackCount; n++)
	{
		stream << fireControlTracks[n];
	}

    //stream << isSemiactive;

    return stream;
}

tcGameStream& tcRadar::operator<<(tcGameStream& stream)
{    
    tcSensorState::operator<<(stream);

	unsigned char fireControlTrackCount;
    stream >> fireControlTrackCount;
	fireControlTracks.clear();

	for (unsigned char n=0; n<fireControlTrackCount; n++)
	{
		long trackId;
		stream >> trackId;
		fireControlTracks.push_back(trackId);
	}

    stream >> isSemiactive;
	stream >> last_range_km;

	stream >> target_x_offset_m;
    stream >> target_y_offset_m;

    jamMap.clear();
    size_t nJam;
    stream >> nJam;

    for (size_t k=0; k<nJam; k++)
    {
        JamInfo ji;
        long id;

        stream >> id;
        stream >> ji.az_rad;
        stream >> ji.JNR_dB;

        jamMap[id] = ji;
    }

    stream >> jammingDegradation_dB;
    stream >> jamTime_s;
    stream >> isJammed;

    stream.ReadCheckValue(3785);

    return stream;
}

tcGameStream& tcRadar::operator>>(tcGameStream& stream)
{
    tcSensorState::operator>>(stream);

	assert(fireControlTracks.size() < 256);
	unsigned char fireControlTrackCount = (unsigned char)fireControlTracks.size();
    stream << fireControlTrackCount;

	for (unsigned char n=0; n<fireControlTrackCount; n++)
	{
		stream << fireControlTracks[n];
	}

    stream << isSemiactive;
	stream << last_range_km; ///< [km] target range from last call to CanDetectTarget

	stream << target_x_offset_m; ///< offset for seeker target point in model coords
    stream << target_y_offset_m; ///< may want to move params like this to a seeker derived class

    size_t nJam = jamMap.size();
    stream << nJam;
    std::map<long, JamInfo>::const_iterator iter = jamMap.begin();

    for (; iter != jamMap.end(); ++iter)
    {
        long id = iter->first;

        stream << id;
        stream << (float)iter->second.az_rad;
        stream << (float)iter->second.JNR_dB;
    }

    stream << jammingDegradation_dB;
    stream << jamTime_s;
    stream << isJammed;

    stream.WriteCheckValue(3785);

    return stream;
}

/**
*
*/
tcRadar& tcRadar::operator=(tcRadar& ss) 
{
    tcSensorState::operator =(ss);

    mpDBObj = ss.mpDBObj;
    return(*this);
}

/**
* This will not work correctly if there is more than one active jammer on the same platform
* that affects this radar. Need generalized key that includes sensor idx to do this correctly.
* @param JNR_dB mainbeam JNR, sidelobes are modeled for jammer out of az/el beam to target
* 如果同一平台上存在多个影响此雷达的主动干扰器，则此函数将无法正确工作。
* 为了正确执行，需要一个包含传感器索引的通用键。
* @param id 干扰器的唯一标识符。
* @param JNR_dB 主波束的干扰噪声比（Jamming to Noise Ratio），
* 对于不在雷达方位角/俯仰角波束指向目标的干扰器，其旁瓣已被建模。
* @param az_rad 干扰器相对于雷达的方位角（以弧度为单位）。
* @param el_rad 干扰器相对于雷达的俯仰角（以弧度为单位）。
*/
void tcRadar::AddOrUpdateJammer(long id, float JNR_dB, float az_rad, float el_rad)
{
    std::map<long, JamInfo>::iterator iter = jamMap.find(id);
    if (iter != jamMap.end())
    {
        // update
        iter->second.JNR_dB = JNR_dB;
        iter->second.az_rad = az_rad;
        iter->second.el_rad = el_rad;
    }
    else
    {
        JamInfo jamInfo;
        jamInfo.JNR_dB = JNR_dB;
        jamInfo.az_rad = az_rad;
        jamInfo.el_rad = el_rad;
        
        jamMap[id] = jamInfo;
#ifdef _DEBUG
        fprintf(stdout, "New jammer, %d jamming %d, az: %f, JNR_dB: %f\n", id, parent->mnID, az_rad, JNR_dB);
#endif
    }
}


float tcRadar::CalculateJammingDegradation()
{
    assert(false); // obsolete
    return 0;
#if 0
    if (jamMap.size() == 0) return 0;

    /* Iterate through jam map
    ** Find max jammer power in coverage (don't add powers for now)
    **
    ** Interference power is dropped 30 dB for jammers outside of sensor coverage. 
    ** Eventually upgrade this (or add realism option) to recalculate for each target based on separation between 
    ** jammer and target angle.
    */

    // calculate az coverage
    bool covers360 = false;
    float az1_rad = 0;
    float az2_rad = 0;
    if (mpDBObj->mfFieldOfView_deg >= 360.0f) 
    {
        covers360 = true;
    }
    else 
    {
        float lookAz_rad = parent->mcKin.mfHeading_rad + mountAz_rad;

        float fHalfFOV_rad = (0.5f*C_PIOVER180)*mpDBObj->mfFieldOfView_deg;
        az1_rad = lookAz_rad - fHalfFOV_rad;
        az2_rad = lookAz_rad + fHalfFOV_rad;
    }


    float maxPdens_dB = -999.0f;

    std::map<long, JamInfo>::iterator iter = jamMap.begin();
    for(;iter != jamMap.end(); ++iter)
    {
        float effectivePowerDensity = iter->second.powerDensity;

        if (covers360 || (AngleWithinRange(iter->second.az_rad, az1_rad, az2_rad) != 0))
        {   
        }
        else
        {
            effectivePowerDensity -= 30.0f; // 30 dB sidelobes
        }
        
        if (effectivePowerDensity > maxPdens_dB) maxPdens_dB = effectivePowerDensity;
    }

    float JtoN_dB = maxPdens_dB + jamConstant;
    
    // approximation of power add
    if (JtoN_dB < -6.0) return 0;
    else if (JtoN_dB < 6.0) return (3.0f + 0.5*JtoN_dB);
    else return JtoN_dB;
#endif
}

/**
* Calculates jamming degradation vs target at az_rad, el_rad accounting for az and el beamwidth
* @returns jamming degradation factor in dB, 0 dB is no degradation
*/
float tcRadar::CalculateJammingDegradation2(float az_rad, float el_rad)
{
    // 如果干扰映射表为空，则返回0，表示没有干扰降级
    if (jamMap.size() == 0) return 0;

    // 初始化变量，用于计算方位角覆盖范围
    bool covers360 = false; // 是否覆盖360度
    float az1_rad = 0; // 方位角覆盖范围的起始角度（弧度）
    float az2_rad = 0; // 方位角覆盖范围的结束角度（弧度）
    // 如果雷达的视场角大于等于360度，则设置covers360为true
    if (mpDBObj->mfFieldOfView_deg >= 360.0f)
    {
        covers360 = true;
    }
    else
    {
        // 计算雷达当前朝向的方位角（弧度）
        float lookAz_rad = parent->mcKin.mfHeading_rad + mountAz_rad;

        // 计算半视场角（弧度）
        float fHalfFOV_rad = (0.5f*C_PIOVER180)*mpDBObj->mfFieldOfView_deg;
        // 计算方位角覆盖范围的起始和结束角度（弧度）
        az1_rad = lookAz_rad - fHalfFOV_rad;
        az2_rad = lookAz_rad + fHalfFOV_rad;

        // 断言目标（不一定是干扰源）在雷达的方位角和俯仰角覆盖范围内
        assert(AngleWithinRange(az_rad, az1_rad, az2_rad) != 0);
    }

    // 初始化变量，用于累加干扰源的干扰功率（线性值，非dB）
    float jnr_sum = 0;

    // 遍历干扰映射表
    std::map<long, JamInfo>::iterator iter = jamMap.begin();
    for(;iter != jamMap.end(); ++iter)
    {
        // 获取当前干扰源的干扰噪声比（dB值）
        float effectiveJNR = iter->second.JNR_dB;

        // 计算当前干扰源与目标之间的方位角差（弧度）
        float daz_rad = iter->second.az_rad - az_rad;
        // 调整方位角差，确保其在[-π, π]范围内
        daz_rad += C_TWOPI * (float(daz_rad < -C_PI) - float(daz_rad > C_PI));

        // 计算方位角差相对于方位波束宽度的倍数
        float daz_beamwidths = fabsf(C_180OVERPI * daz_rad) * mpDBObj->invAzBeamwidth_deg;

        // 根据方位角差调整干扰噪声比
        if (daz_beamwidths > 2)
        {
            effectiveJNR += mpDBObj->effectiveSidelobes_dB; // 如果超出主瓣范围两倍以上，使用有效旁瓣电平
        }
        else if (daz_beamwidths > 1)
        {
            effectiveJNR += (daz_beamwidths - 1) * mpDBObj->effectiveSidelobes_dB; // 如果在主瓣和两倍主瓣之间，按比例调整
        }
        else // 如果在方位波束宽度内，则进一步检查俯仰角偏移
        {
            // 计算当前干扰源与目标之间的俯仰角差（弧度）
            float del_rad = iter->second.el_rad - el_rad;
            // 计算俯仰角差相对于俯仰波束宽度的倍数
            float del_beamwidths = fabsf(C_180OVERPI * del_rad) * mpDBObj->invElBeamwidth_deg;

            // 根据俯仰角差调整干扰噪声比
            if (del_beamwidths > 2) effectiveJNR += mpDBObj->effectiveSidelobes_dB;
            else if (del_beamwidths > 1) effectiveJNR += (del_beamwidths - 1) * mpDBObj->effectiveSidelobes_dB;
        }

        // 将调整后的干扰噪声比（线性值）累加到总和中
        jnr_sum += powf(10.0f, 0.1f * effectiveJNR);
    }

    // 计算总的干扰降级（dB值）
    float noise_degradation_dB = 10.0f * log10f(1.0f + jnr_sum);

    // 返回总的干扰降级（dB值）
    return noise_degradation_dB;
}

/**
* For missile seekers call to check for switch
* to countermeasure target
*/
void tcRadar::CounterMeasureTest(double t)
{
    const unsigned int maxAttempts = 4; // don't test any more than this number of CMs

    lastCounterMeasureTime = t;

    std::shared_ptr<tcGameObject> target = simState->GetObject(mcTrack.mnID);
    if (target == 0)
    {
        assert(false); // called with no target
        return;
    }

    if (std::shared_ptr<tcAirCM> cm = std::dynamic_pointer_cast<tcAirCM>(target))
    {
        // already tracking a CM, don't check for switch back right now
        return;
    }

    
    float targetRangeRate_mps = parent->mcKin.CalculateRangeRate(target->mcKin);
    assert(target != 0);
    float targetRange_km = parent->mcKin.RangeToKmAlt(target->mcKin);
    // float targetRange_km = parent->mcKin.RangeToKmAlt(target);

    float targetHeight_m = 0; // equivalent height of target for radar horizon
    float fTargetAz_rad = 0;
    // could probably find way to use rcs from parent routine
    float targetRCS_dBsm = CalculateTargetRCS_dBsm(target, fTargetAz_rad, targetHeight_m); 

    tcGeoRect region;
    region.Set(target->mcKin.mfLon_rad, target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfLat_rad);
    float dy_rad = C_MTORAD*500.0f;
    float dx_rad = dy_rad / cosf(target->mcKin.mfLat_rad);
    region.Expand(dx_rad, dy_rad);

    unsigned int attempts = 0;
    tcGameObjIterator iter(region);

    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcGameObject> obj = iter.Get();

        assert(obj != 0);
        std::shared_ptr<tcCounterMeasureDBObject> cmData = std::dynamic_pointer_cast<tcCounterMeasureDBObject>(obj->mpDBObject);

        bool isEligible = (cmData != 0) && (cmData->subType == "Chaff") &&
            (obj->mpDBObject->mnType == PTYPE_AIRCM);
        float range_km;

        if (isEligible && CanDetectTarget(obj, range_km))
        {
            float objRangeRate_mps = parent->mcKin.CalculateRangeRate(obj->mcKin);
            float objRange_km = parent->mcKin.RangeToKmAlt(obj->mcKin);
            float objRCS_dBsm = lastTargetRCS_dBsm;

            float rangeRateFactor = (objRangeRate_mps < (targetRangeRate_mps - 30.0f)) ? 0.5f : 1.0f;
            float rangeFactor = (fabsf(objRange_km - targetRange_km) > 0.25f) ? 0.5f : 1.0f;
            float rcsFactor = (objRCS_dBsm < (targetRCS_dBsm - 3)) ? 0.5f : 1.0f;
            
            float prob_success = mpDBObj->counterMeasureFactor * cmData->effectiveness * 
                rangeRateFactor * rangeFactor * rcsFactor;
            if (randf() < prob_success)
            {
                mcTrack.mnID = obj->mnID;
                UpdateTrack(obj, t);
                return;
            }
            else
            {
                if (++attempts >= maxAttempts) return;
            }
            
        }
    }
}

bool tcRadar::IsJammed() const
{
    return isJammed;
}

void tcRadar::RemoveAllJammers()
{
    jamMap.clear();
}

void tcRadar::RemoveJammer(long id)
{
    std::map<long, JamInfo>::iterator iter = jamMap.find(id);
    if (iter != jamMap.end())
    {
        jamMap.erase(iter);
    }
}

void tcRadar::UpdateJammingDegradation()
{
    float dt_s = mfLastScan - jamTime_s; // time since last jammer update
    if (dt_s > 30.0f) // periodically clear jam stats to allow new updates
    {
        jammingDegradation_dB = 0;
        isJammed = false;
        jamTime_s = mfLastScan;
    }

    assert(jammingDegradation_dB >= 0);
}

float tcRadar::CalculateTargetRCS_dBsm( std::shared_ptr<const tcGameObject> target, float& targetAz_rad, float& targetHeight_m) const
{
    assert(target != 0); // 确保目标对象不为空

    const tcKinematics *rdr_kin = &parent->mcKin;  // 雷达父对象的运动状态
    const tcKinematics *tgt_kin = &target->mcKin;  // 目标对象的运动状态

    targetHeight_m = tgt_kin->mfAlt_m; // 获取目标对象的高度

    if (std::shared_ptr<const tcAirDetectionDBObject> detectionData = std::dynamic_pointer_cast<const tcAirDetectionDBObject>(target->mpDBObject)) // 如果目标对象是飞机探测数据库对象
    {
        // 计算目标方位角，考虑目标航向
        targetAz_rad = nsNav::GCHeadingApprox_rad(rdr_kin->mfLat_rad, rdr_kin->mfLon_rad,
                                                  tgt_kin->mfLat_rad, tgt_kin->mfLon_rad);

        float aspect_rad = targetAz_rad - tgt_kin->mfHeading_rad + C_PI; // 计算目标相对雷达的方位角
        aspect_rad += (float(aspect_rad >= C_TWOPI))*(-C_TWOPI) + (float(aspect_rad < -C_TWOPI))*C_TWOPI;
        //if (aspect_rad >= C_TWOPI) aspect_rad -= C_TWOPI;

        float rcs_dBsm = detectionData->GetRCS_dBsm(C_180OVERPI*aspect_rad); // 获取目标的雷达散射截面（RCS）值
        targetHeight_m += detectionData->effectiveHeight_m; // 加上目标的有效高度

        // 根据雷达盲速调整RCS值
        if (mpDBObj->blindSpeed_mps > 0)
        {
            // 目标径向速度（无符号）
            float radial_mps = fabsf(C_KTSTOMPS*target->mcKin.mfSpeed_kts*cosf(aspect_rad));

            float radial_fraction = radial_mps * mpDBObj->invBlindSpeed_mps; // 1.0如果达到盲速

            // 可能不必要的优化，避免分支
            float underBlindSpeed = float(radial_fraction < 1.0f);
            float nearBlindSpeed = float((radial_fraction >= 1.0f) && (radial_fraction < 2.0f));

            // 如果速度小于盲速，则减去24 dB的惩罚；如果速度在2倍盲速到盲速之间，则减去0到24 dB的惩罚
            float speedPenalty = 24.0f*(underBlindSpeed + nearBlindSpeed*(2.0f - radial_fraction));
            rcs_dBsm -= speedPenalty;
        }

        return rcs_dBsm; // 返回调整后的RCS值
    }
    else
    {
        return -999.0f; // 如果目标不是飞机探测数据库对象，则返回-999.0f
    }

}
/**
* @return dB adjustment to RCS based on elevation angle to target and terrain type under target
*/
float tcRadar::CalculateClutterAdjustment_dB(std::shared_ptr<const tcGameObject> target, float targetEl_rad) const
{
    assert(target != 0);

    if (targetEl_rad > ((0.5f*C_PIOVER180)*mpDBObj->elevationBeamwidth_deg))
    {
        return 0;
    }
    else
    {
        bool isOverWater = (target->mcTerrain.mfHeight_m <= 0); // else over land
        float adjustment_dB = isOverWater ? mpDBObj->lookdownWater_dB : mpDBObj->lookdownLand_dB;

        return adjustment_dB;
    }
}

/**
* @return true if target within elevation coverage of radar
*
* @param targetRange_km must be 3D range, otherwise get NaN for some low range geometries
* @param targetEl_rad elevation assuming platform is level
*/
bool tcRadar::TargetInElevationCoverage(std::shared_ptr<const tcGameObject> target, float targetRange_km, float& targetEl_rad) const
{
    assert((target != 0)&&(parent != 0));

    if ( std::shared_ptr<const tcWeaponObject> weapon = std::dynamic_pointer_cast<const tcWeaponObject>(parent))
    {
        return TargetInElevationCoverageWeapon(target, targetRange_km, targetEl_rad);
    }

    float dalt_m = target->mcKin.mfAlt_m - parent->mcKin.mfAlt_m;

    assert(fabsf(dalt_m) <= (1000.0f*targetRange_km));

    targetEl_rad = asinf(dalt_m / (1000.0f*targetRange_km));

    lastTargetElevation_rad = targetEl_rad;

    bool inCoverage = (targetEl_rad >= mpDBObj->minElevation_rad) && (targetEl_rad <= mpDBObj->maxElevation_rad);

    return inCoverage;
}

/**
* @return true if target within elevation coverage of radar
* This version uses cone angle between platform boresight (assumes forward-looking radar) and target
*
* @param targetRange_km must be 3D range, otherwise get NaN for some low range geometries
* @param targetEl_rad cone angle from parent boresight to target
*/
bool tcRadar::TargetInElevationCoverageWeapon(std::shared_ptr<const tcGameObject> target, float targetRange_km, float& targetEl_rad) const
{
    assert((target != 0)&&(parent != 0));

    float cos_pitch_parent = cosf(parent->mcKin.mfPitch_rad);
    float zplatform = sinf(parent->mcKin.mfPitch_rad);
    float xplatform = cos_pitch_parent * cosf(parent->mcKin.mfHeading_rad);
    float yplatform = cos_pitch_parent * sinf(parent->mcKin.mfHeading_rad);

    float bearing_rad = parent->BearingToRad(*target);
    float dalt_m = target->mcKin.mfAlt_m - parent->mcKin.mfAlt_m;
    assert(fabsf(dalt_m) <= (1000.0f*targetRange_km));
    float sin_el_target = dalt_m / (1000.0f*targetRange_km);
    float cos_el_target = sqrtf(1.0 - sin_el_target*sin_el_target);

    float ztarget = sin_el_target;
    float xtarget = cos_el_target * cosf(bearing_rad);
    float ytarget = cos_el_target * sinf(bearing_rad);
    
    float cos_cone = xplatform*xtarget + yplatform*ytarget + zplatform*ztarget;
    targetEl_rad = acosf(cos_cone);

    bool inCoverage = (targetEl_rad <= mpDBObj->maxElevation_rad);

    return inCoverage;
}


/**
*
*/
bool tcRadar::CanDetectTarget(std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom)
{

    float fTargetRange_km; // 目标距离（千米）
    float fCoverageAz1, fCoverageAz2; // 覆盖角度
    bool bInSearchVolume = false; // 是否在搜索区域内
    last_snr_margin_dB = -99.0f; // 上次信噪比边际（分贝）
    lastTargetElevation_rad = 1.72787596f; // 上次目标仰角（弧度）

    assert((mpDBObj != 0) && (target != 0)); // 确保传感器和目标对象有效

    if (!mbActive && !isCommandReceiver) return false; // 如果传感器不活跃或不是指令接收器，返回false

    float illuminatorTargetRange_km = 1e8; // 照明器目标范围（千米）
    if (isSemiactive || isCommandReceiver)
    {
        std::shared_ptr<tcRadar> illum = GetFireControlRadar(); // 获取火控雷达
        if (illum == NULL) return false; // 如果雷达为空，返回false
        if (!illum->CanDetectTarget(target, illuminatorTargetRange_km, false)) return false; // 假设照明器接收器是导弹，因此不做随机检测
        if (isCommandReceiver) return true; // 如果指令接收器，则返回true
    }

    lastTargetRCS_dBsm = -999.0f; // 上次目标RCS（分贝平方米）

    const tcKinematics *rdr_kin = &parent->mcKin; // 雷达父对象的运动状态
    const tcKinematics *tgt_kin = &target->mcKin; // 目标对象的状态

    float targetHeight_m = 0; // 目标高度的等效值，用于雷达地平线计算
    float fTargetAz_rad = 0; // 目标方位角（弧度）

    float rcs_dBsm = CalculateTargetRCS_dBsm(target, fTargetAz_rad, targetHeight_m); // 计算目标RCS（分贝平方米）

    if ((targetHeight_m < 0) || (rcs_dBsm < -100.0f)) // 如果目标高度低于零或RCS小于-100分贝平方米，返回false
    {
        return false; // 水下潜艇或雷达无法探测到的目标返回false
    }

    lastTargetRCS_dBsm = rcs_dBsm; // 更新最后的目标RCS

    // PTYPE常量定义不同类型目标的标志位，如：表面、小型表面、大型表面、飞机等。
    unsigned int classification = target->mpDBObject->mnType; // 获取目标的类型标志位

    bool isSurface = ((classification & PTYPE_SURFACE) != 0) || (classification == PTYPE_AIRCM); // 如果标志位包含表面类型，则为真。否则根据其他条件判断。
    bool isAir = (classification & PTYPE_AIR) != 0; // 如果标志位包含空气类型，则为真。否则根据其他条件判断。
    bool isMissile = (classification & PTYPE_MISSILE) != 0; // 如果标志位包含导弹类型，则为真。否则根据其他条件判断。
    bool isGround = (classification & PTYPE_GROUND) != 0; // 如果标志位包含地面类型，则为真。否则根据其他条件判断。
    bool isSub = (classification & PTYPE_SUBSURFACE) != 0; // 如果标志位包含潜艇类型，则为真。否则根据其他条件判断。

    if (isMissile && (target->mcKin.mfSpeed_kts < 600.0f)) // 如果目标是导弹且速度低于约1马赫，则视为空中目标，为真。否则根据其他条件判断。
    {
        isAir = true; // 如果导弹的速度达到约1马赫，则视为空中目标，为真。否则根据其他条件判断。
    }

    if (isSub) isSurface = true; // 如果目标是一个潜射物体，则将其视为表面目标，为真。否则根据其他条件判断。

    if (mpDBObj->mfFieldOfView_deg >= 360.0f) // 如果视场角大于等于360度，则为真。否则根据其他条件判断。
    {
        bInSearchVolume = true; // 如果目标在搜索区域内，则为真。否则根据其他条件判断。
    }
    else
    {
        float lookAz_rad = parent->mcKin.mfHeading_rad + mountAz_rad;  // 计算传感器的视场中心线相对于北的方位角
        float fHalfFOV_rad = 0.5f*C_PIOVER180*mpDBObj->mfFieldOfView_deg;  // 计算半视场宽度（弧度）
        fCoverageAz1 = lookAz_rad - fHalfFOV_rad;  // 计算覆盖范围的起始方位角
        fCoverageAz2 = lookAz_rad + fHalfFOV_rad;  // 计算覆盖范围的结束方位角
        bInSearchVolume = AngleWithinRange(fTargetAz_rad,fCoverageAz1,fCoverageAz2) != 0;  // 判断目标是否在传感器搜索范围内
        if (!bInSearchVolume) {range_km=0;return false;}  // 如果不在搜索范围内，返回false
    }

    float clutterHorizon_km = C_RADARHOR * sqrtf(rdr_kin->mfAlt_m + mfSensorHeight_m);  // 计算雷达杂波地平线距离
    float fRadarHorizon = C_RADARHOR*sqrtf(targetHeight_m) + clutterHorizon_km;  // 计算雷达地平线距离

    fTargetRange_km = C_RADTOKM*nsNav::GCDistanceApprox_rad(rdr_kin->mfLat_rad, rdr_kin->mfLon_rad,  // 计算目标到传感器的距离
                                                              tgt_kin->mfLat_rad,tgt_kin->mfLon_rad, rdr_kin->mfAlt_m, tgt_kin->mfAlt_m);
    range_km = fTargetRange_km;  // 更新距离值
    last_range_km = range_km;  // 记录上一次的距离值

    if (fTargetRange_km > fRadarHorizon)  // 如果目标距离大于雷达地平线距离
    {
        return false;  // 返回false
    }

    float targetEl_rad = 0;  // 初始化目标俯仰角为0
    bool inElevationCoverage = TargetInElevationCoverage(target, fTargetRange_km, targetEl_rad);  // 判断目标是否在俯仰覆盖范围内

    if (!inElevationCoverage || !HasLOS(target)) return false;  // 如果不在俯仰覆盖范围或没有视线，返回false

    // adjustment for "look-down" geometry, can also apply to targets near horizon for surface based radars
    if (fTargetRange_km <= clutterHorizon_km)  // 如果目标距离小于等于雷达杂波地平线距离
    {
        float clutterAdjustment_dB = CalculateClutterAdjustment_dB(target, targetEl_rad);  // 计算杂波调整值
        rcs_dBsm += clutterAdjustment_dB;  // 更新雷达散射截面积
        lastTargetRCS_dBsm = rcs_dBsm;  // 记录上一次的雷达散射截面积
    }

    bool bTargetTypeMatch = (mpDBObj->mbDetectsAir && isAir) ||  // 判断目标类型是否匹配
                            (mpDBObj->mbDetectsMissile && isMissile) ||
                            (mpDBObj->mbDetectsSurface && isSurface) ||
                            (mpDBObj->mbDetectsGround && isGround);

    if (bTargetTypeMatch == false) return false;  // 如果目标类型不匹配，返回false

    float margin_dB; // SNR margin

    if (isSemiactive)  // 如果是半主动雷达
    {
        margin_dB =
            20.0f*(2.0f*log10f(mpDBObj->mfRefRange_km)
                     - log10f(fTargetRange_km)
                     - log10f(illuminatorTargetRange_km)
                     ) + rcs_dBsm;  // 计算信噪比余量
    }
    else
    {
        margin_dB =
            40.0f*(log10f(mpDBObj->mfRefRange_km) - log10f(fTargetRange_km)) + rcs_dBsm;  // 计算信噪比余量
    }

    float targetJammingDegradation_dB =
        CalculateJammingDegradation2(fTargetAz_rad, targetEl_rad);  // 计算目标干扰衰减值
    if (targetJammingDegradation_dB >= jammingDegradation_dB)  // 如果目标干扰衰减值大于等于当前干扰衰减值
    {
        jammingDegradation_dB = targetJammingDegradation_dB;  // 更新干扰衰减值
        isJammed = (jammingDegradation_dB > 0);  // 判断是否被干扰
        jamTime_s = target->mfStatusTime; // not sure if tcSensorState::mfLastScan is updated at this point so use target time  // 记录干扰时间
    }

    margin_dB = margin_dB - targetJammingDegradation_dB;  // 更新信噪比余量
    last_snr_margin_dB = margin_dB;  // 记录上一次的信噪比余量

    // don't do random detections for missiles (problem where launched with lock that disappears in transition region)
    if (((mnMode == SSMODE_SURVEILLANCE) || (mnMode == SSMODE_SEEKERSEARCH)) && useRandom)  // 如果模式为监视或搜索且使用随机检测
    {
        return RandomDetect(margin_dB);  // 进行随机检测并返回结果
    }
    else
    {
        return margin_dB >= 0;  // 如果信噪比余量大于等于0，返回true，否则返回false
    }
}


/**
* @return false if key not found in database
*/
bool tcRadar::InitFromDatabase(long key)
{
	assert(database);

    tcSensorState::InitFromDatabase(key);

	std::shared_ptr<tcDatabaseObject> databaseObj = database->GetObject(key);
	if (databaseObj == 0)
	{
        fprintf(stderr, "Error - tcRadar::InitFromDatabase - Not found in db\n");
        return false;
	}

    mpDBObj = std::dynamic_pointer_cast<tcRadarDBObject>(databaseObj);
    if (mpDBObj == 0) 
    {
        fprintf(stderr, "Error - tcRadar::InitFromDatabase - Not a radar database class (%s)\n",
			databaseObj->mzClass.c_str());
        return false;
    }

    if (mpDBObj->isSurveillance)
    {
        mnMode = SSMODE_SURVEILLANCE;
    }
    else
    {
        mnMode = SSMODE_FC;
    }
    mfSensorHeight_m = 10.0f;

    isSemiactive = mpDBObj->isSemiactive;

    return true;
}

/**
*
*/
void tcRadar::Serialize(tcFile& file, bool mbLoad) 
{
    tcSensorState::Serialize(file, mbLoad);
}


/**
* Sets illuminator info for semi-active radars and command receivers.
* isCommandReceiver indicates the "radar" is a simple receiver of command
* guidance from the fire control radar.
*/
void tcRadar::SetFireControlSensor(long id, unsigned char idx)
{
    assert((id == -1) || isSemiactive || isCommandReceiver);

	tcSensorState::SetFireControlSensor(id, idx);
}


/**
*
*/
std::shared_ptr<tcRadar> tcRadar::Clone(void) 
{
    // tcRadar *pNew = new tcRadar();
    std::shared_ptr<tcRadar> pNew=std::make_shared<tcRadar>();
    *pNew = *this;
    return pNew;
}


unsigned tcRadar::GetFireControlTrackCount() const
{
	return (unsigned)fireControlTracks.size();
}

unsigned tcRadar::GetMaxFireControlTracks() const
{
	return mpDBObj->maxFireControlTracks;
}

/**
* Alternative to dynamic_cast
*/
bool tcRadar::IsRadar() const
{
    return true;
}

/**
* Does not test if radar can detect target.
* @return true if track is available.
*/
bool tcRadar::IsTrackAvailable()
{
    return (GetFireControlTrackCount() < mpDBObj->maxFireControlTracks);
}

/**
* if track is available, reserve a track.
* The current approach to semi-active guidance is to require each 
* missile to request one track per target, even if it is the same 
* target as a pre-existing track.
* Calling method must check if target is detectable for this to
* work properly.
*/
bool tcRadar::RequestTrack(long targetId)
{
	if (!IsTrackAvailable())
	{
		return false;
	}

	fireControlTracks.push_back(targetId);

	if ((parent != 0) && (!parent->IsClientMode()))
	{
        tcSimState* simState = tcSimState::Get();

        if (std::shared_ptr<tcGameObject> newTargetObj = simState->GetObject(targetId))
        {
            newTargetObj->AddTargeter(parent->mnID);
        }
    }

	return true;
}

bool tcRadar::ReleaseTrack(long targetId)
{
	std::vector<long> updatedTracks;
	for (size_t n=0; n<fireControlTracks.size(); n++)
	{
		if (fireControlTracks[n] != targetId)
		{
			updatedTracks.push_back(fireControlTracks[n]);
		}
	}

	if (updatedTracks.size() == fireControlTracks.size())
	{
		fprintf(stderr, "tcRadar::ReleaseTrack targetId not found (%d)", targetId);
		return false;
	}

	fireControlTracks = updatedTracks;

	if ((parent != 0) && (parent->IsClientMode())) return true;

	// after releasing track, check if any other radars on parent platform have active fire control track. If not, remove parent from targeter list
    assert((parent != 0) && (parent->GetComponent<tcSensorPlatform>()!= 0));

	bool isTrackingTarget = false;
    unsigned int nParentSensors = parent->GetComponent<tcSensorPlatform>()->GetSensorCount();
	for (unsigned int n=0; n<nParentSensors; n++)
	{
        std::shared_ptr<const tcSensorState> sensor = parent->GetComponent<tcSensorPlatform>()->GetSensor(n);
		isTrackingTarget = isTrackingTarget || sensor->IsTrackingWithRadar(targetId);
	}

	if (!isTrackingTarget)
	{
		std::shared_ptr<tcGameObject> target = simState->GetObject(targetId);
		if (target != 0)
		{
			target->RemoveTargeter(parent->mnID);
		}
	}

	return true;

}

/**
* @return true if this radar has any active fire control tracks on targetId
*/
bool tcRadar::IsTrackingWithRadar(long targetId) const
{
	size_t nFireControlTracks = fireControlTracks.size();
	for (size_t n=0; n<nFireControlTracks; n++)
	{
		if (fireControlTracks[n] == targetId) return true;
	}

	return false;
}

/**
* Updates missile seeker radar.
*/
void tcRadar::UpdateSeeker(double t)
{
    long nTargetID;
    std::shared_ptr<tcGameObject>ptarget = 0;
    bool bFound = false;
    bool isEligible = false;
    std::shared_ptr<tcMissileObject> missile = std::dynamic_pointer_cast<tcMissileObject>(parent);

    switch (mnMode) 
    {
    case SSMODE_SEEKERACQUIRE:        // fall through to SEEKERTRACK
        if (missile != 0) missile->SetSeekerTarget(mcTrack.mnID);

    case SSMODE_SEEKERTRACK:
        nTargetID = mcTrack.mnID;
        if (nTargetID != parent->mnID)
        { 
            bFound = simState->maPlatformState.Lookup(nTargetID,ptarget);
        } 
        else // no self detection
        {
            bFound = false;
        }

        if ((missile != 0) && bFound && (missile->mfInterceptTime < 5.0f) && 
            (lastCounterMeasureTime < (t - 1.0)))
        {
            CounterMeasureTest(t);
        }

        if (bFound) 
        {  // own-alliance is allowed
            float fRange_km;

            bool surfacedSub = (ptarget->mpDBObject->mnType == PTYPE_SUBMARINE) && 
                (ptarget->mcKin.mfAlt_m > -2.0f);

            isEligible = surfacedSub || 
                ((ptarget->mpDBObject->mnType & 
                (PTYPE_AIR | PTYPE_GROUND | PTYPE_MISSILE | PTYPE_SURFACE)) != 0);

            if (isEligible && CanDetectTarget(ptarget, fRange_km)) 
            {
                UpdateTrack(ptarget, t);
                return;
            }
            else
            {
#ifdef _DEBUG
                bool result = CanDetectTarget(ptarget, fRange_km);
#endif
            }
        }

		// shut down missile if target doesn't exist or can't detect
		/*{
            parent->SelfDestruct();
            mcTrack.mnID = -1;
#ifdef _DEBUG
            if(simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) 
            {
                char zBuff[128];
				_snprintf(zBuff, 128, "Mis %d shut down (%s)\n", parent->mnID, parent->mzClass.c_str());
                simState->mpCommandInterface->DisplayInfoMessage(zBuff);
            }
#endif
            return;
		}*/


        if (missile != 0)
        {
            /* if range to target is close enough, assume this is a terminal missile
            ** and ignore failed detection */
            const float terminalRange_km = 0.5f;
            bool cheatUpdate = (ptarget != 0) && ((missile->RangeTo(*ptarget) < terminalRange_km) || (missile->msKState.mfFlightTime < 3.0f)); 

            if ((ptarget != 0) && isEligible && cheatUpdate)
            {
                UpdateTrack(ptarget, t);
                return;
            }

            mcTrack.mnID = -1;
            missile->goalHeading_rad = missile->mcKin.mfHeading_rad;
            missile->goalPitch_rad = missile->mcKin.mfPitch_rad;

            bool hasSegments = (missile->mpDBObject->mnNumSegments > 0);
            bool datumLaunched = hasSegments && (missile->mpDBObject->maFlightProfile[0].meGuidanceMode == GM_NAV);

            if (datumLaunched)
            {
                mnMode = SSMODE_SEEKERSEARCH; 
            }
            else
            {
                parent->SelfDestruct();
            }
        }
        else
        {
            parent->SelfDestruct();
        }
        


        // shut down missile if track lost for > 7 seconds
        //if ((mnMode == SSMODE_SEEKERTRACK)&&
        //    (t - mcTrack.mfTimestamp) > 7.0)
        //{
        //    parent->mfDamageLevel = 1.0f; 
        //    mcTrack.mnID = NULL_INDEX;
        //    if(simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) 
        //    {
        //        char zBuff[128];
        //        sprintf(zBuff,"Missile %d shut down\n", parent->mnID);
        //        simState->mpCommandInterface->DisplayInfoMessage(zBuff);
        //    }
        //    return;
        //}

        // this code to enter search mode after track lost

        break;
    case SSMODE_SEEKERSEARCH:
        {
            // get list of candidate tracks/detections
            tcGeoRect region;   
            GetTestArea(region);

            tcGameObjIterator iter(region);
            float minRange = 1e15f;
            float maxRCS = -12345.0f;
            long minID = NULL_INDEX;

            // find closest detectable target
            for (iter.First();iter.NotDone();iter.Next())
            {
                std::shared_ptr<tcGameObject>target = iter.Get();
                if (target != parent) // no self detection
                {
                    float range_km = 0;
                    /* Substitute this to disable own-alliance seeker detections:
                    ** bool bDetected = (parent->GetAlliance() != target->GetAlliance()) &&
                    **    CanDetectTarget(target,range_km);
                    */
                    bool bDetected = CanDetectTarget(target, range_km);
                    float rcs_dBsm = lastTargetRCS_dBsm;

                    bDetected = bDetected && (range_km > 1.0f); // don't allow lock inside 1.0 km range

                    bool targetPreferred = (range_km < minRange) ||
                        ((range_km < minRange + 1.0f) && (rcs_dBsm > maxRCS));

                    if (bDetected && targetPreferred)
                    {
                        minID = target->mnID;
                        minRange = range_km;
                        maxRCS = rcs_dBsm;
                    }
                }
            }
           
            if (minID==NULL_INDEX) return; // no targets found

            // if seeker has locked on a countermeasure, roll against the effectiveness * cm_factor to start a track
            if (std::shared_ptr<tcAirCM> airCM =  std::dynamic_pointer_cast<tcAirCM>(simState->GetObject(minID)))
            {
                float prob_success = mpDBObj->counterMeasureFactor * airCM->mpDBObject->effectiveness;
                if (randf() > prob_success)
                {
                    return; // CM rejected
                }
            }

            parent->DesignateTarget(minID); // select closest as target
        }
    }
}

/**
* Called after a surveillance detection to update sensor map for
* appropriate alliance.
*/
void tcRadar::UpdateSensorMap(double t, std::shared_ptr<const tcGameObject> target, float range_km)
{
    std::shared_ptr<tcSensorMapTrack> pSMTrack = 0;
    tcSensorReport* report = simState->mcSensorMap.GetOrCreateReport(parent->mnID, mpDBObj->mnKey, target->mnID,
        pSMTrack, parent->GetAlliance());

    if (report == 0) return;

    float az_rad = parent->mcKin.HeadingToRad(target->mcKin);

    tcSensorState::UpdateActiveReport(report, t, az_rad, range_km, target->mcKin.mfAlt_m, pSMTrack);


    double trackLife = report->timeStamp - report->startTime;
    if (trackLife >= 16.0) 
    {
        report->speedEstimate_mps = C_KTSTOMPS * target->mcKin.mfSpeed_kts * cosf(target->mcKin.mfClimbAngle_rad);
        report->speedVariance = 1.0f;
        report->headingEstimate_rad = target->mcKin.mfHeading_rad;
        report->headingVariance = 0.001f;
        report->validFlags |= tcSensorReport::SPEED_VALID | tcSensorReport::HEADING_VALID;

        if (last_snr_margin_dB >= mpDBObj->idThreshold_dB)
        {
            report->alliance = target->GetAlliance();
            report->databaseID = target->mnDBKey;
        }
    }


    if (trackLife > 10.0)
    {
        unsigned int classification = target->mpDBObject->mnType;

        // surfaced sub classified as small surface
        if (classification == PTYPE_SUBMARINE)
        {
            classification = PTYPE_SMALLSURFACE; 
        }
        else if (classification == PTYPE_CARRIER)
        {
            classification = PTYPE_LARGESURFACE;
        }

        report->classification = classification;

        if ((classification & PTYPE_MISSILE) != 0) 
        {
            report->alliance = target->GetAlliance();
        }
    }
    else
    {
        report->classification = 0;
        report->alliance = 0;
    }

    bool bNewDetection = pSMTrack->IsNew();
    if (bNewDetection) 
    {
        pSMTrack->UpdateTrack(0);
        
        tcEventManager::Get()->NewContact(parent->GetAlliance(), pSMTrack);

        if (simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) 
        {
//            tcSound::Get()->PlayEffect("Ping");
        }

        //fprintf(stdout, "target %d detected at %3.1f km at time %.1f [a:%d]\n",
        //    target->mnID,range_km,t,parent->GetAlliance());

    }

}

void tcRadar::UpdateSurveillance(double t)
{
    tcGeoRect region;
    GetTestArea(region);

    tcGameObjIterator iter(region);

    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcGameObject>target = iter.Get();
        if (target != parent) // no self detection
        {
            float range_km = 0;

            bool surfacedSub = (target->mpDBObject->mnType == PTYPE_SUBMARINE) && 
                (target->mcKin.mfAlt_m > -2.0f);

            bool isEligible = surfacedSub || 
                ((target->mpDBObject->mnType & 
                (PTYPE_AIR | PTYPE_GROUND | PTYPE_MISSILE | PTYPE_SURFACE)) != 0);
          
            bool bDetected = (parent->GetAlliance() != target->GetAlliance()) &&
                isEligible &&
                CanDetectTarget(target,range_km);
            if (bDetected) UpdateSensorMap(t, target, range_km);

        }
    }
}


/**
* Loops through existing sensor map tracks and updates those in range with track data from this sensor
* Used to model cued track_only type sensors that do not provide initial detection
*/
void tcRadar::UpdateTrackData(double t)
{
    tcGeoRect region;
    GetTestArea(region);

    unsigned int classificationMask = 0;
    if (mpDBObj->mbDetectsAir) classificationMask |= PTYPE_AIR;
    if (mpDBObj->mbDetectsMissile) classificationMask |= PTYPE_MISSILE;
    if (mpDBObj->mbDetectsGround) classificationMask |= PTYPE_GROUND;
    if (mpDBObj->mbDetectsSurface) classificationMask |= (PTYPE_SURFACE | PTYPE_SUBSURFACE); // sub might be surfaced so add to mask

    tcSensorTrackIterator iter(parent->GetAlliance(), classificationMask, region);

    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcSensorMapTrack> track = iter.Get();
        assert(track != 0);

        bool isActiveTrack = (track != 0) && (track->errorPoly.size() == 0) && ((track->mnFlags & TRACK_ACTIVE) != 0);

        // only check tracks that are tracked with active sensor
        if (isActiveTrack)
        {
            std::shared_ptr<tcGameObject> target = track->GetAssociated();

            float range_km = 0;
            bool isDetected = CanDetectTarget(target, range_km);
            if (isDetected && (target != 0))
            {
                UpdateSensorMapTrackMode(target, track, t, range_km);
            }
        }
    }
}

void tcRadar::UpdateSensorMapTrackMode(std::shared_ptr<const tcGameObject> target, std::shared_ptr<tcSensorMapTrack> track, double t, float range_km)
{
    assert(target->mnID == track->mnID);

    if (track->mnFlags)
    if (mpDBObj->angleError_deg < 5.0f)
    {
        track->mfLat_rad = (float)target->mcKin.mfLat_rad;
        track->mfLon_rad = (float)target->mcKin.mfLon_rad;
        track->mfSpeed_kts = target->mcKin.mfSpeed_kts * cosf(target->mcKin.mfClimbAngle_rad);
        track->mfHeading_rad = target->mcKin.mfHeading_rad;
        track->mfTimestamp = t;
    }

    float altitudeEstimate_m;
    float altitudeVariance;
    float az_rad = parent->mcKin.HeadingToRad(target->mcKin);
    if (GetAltitudeEstimate(altitudeEstimate_m, altitudeVariance, range_km, az_rad, target->mcKin.mfAlt_m))
    {
        track->mfAlt_m = altitudeEstimate_m;
    }
}


/**
* Update sensor track with target state. Normally used with
* missile seekers.
*/
void tcRadar::UpdateTrack(std::shared_ptr<const tcGameObject> target, double t)
{

    mcTrack.mfLat_rad = (float)target->mcKin.mfLat_rad;
    mcTrack.mfLon_rad = (float)target->mcKin.mfLon_rad;
    mcTrack.mfAlt_m = target->mcKin.mfAlt_m;
    mcTrack.mfSpeed_kts = target->mcKin.mfSpeed_kts;
    mcTrack.mfHeading_rad = target->mcKin.mfHeading_rad;
    mcTrack.mfClimbAngle_rad = target->mcKin.mfClimbAngle_rad;
    mcTrack.mfTimestamp = t;
    mcTrack.mnFlags = (TRACK_HEADING_VALID | TRACK_SPEED_VALID 
        | TRACK_ALT_VALID | TRACK_CLIMB_VALID);
    if ((mnMode == SSMODE_SEEKERACQUIRE)  && !isCommandReceiver)
    {
        mnMode = SSMODE_SEEKERTRACK;
//#ifdef _DEBUG
//        if (simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) 
//        {
//            tcSound::Get()->PlayEffect("TwoBeeps");
//        }
//#endif
    }

	AdjustTrackForFineTargeting(target);
}

/**
* If sufficiently close to target, adjust track to lock on to random feature
* of target. Intended to add more realism so that weapons do not always strike 
* origin of target model.
* 用于在雷达锁定目标时对其进行微调，以增加模拟的真实性，使武器不会总是击中目标的原点
*/
void tcRadar::AdjustTrackForFineTargeting(std::shared_ptr<const tcGameObject> target)
{
	if (last_range_km > 1.0f) return;

	/* if target offset has not been selected yet, randomly select
	** based on box around target model. This assumes that only one
	** target will be engaged throughout life of seeker */
    if ((target_x_offset_m == 0) && (target_y_offset_m == 0))
	{
        std::shared_ptr<const tcGameObject> targetMutable = std::dynamic_pointer_cast<const tcGameObject>(target); // TV3D making me do this
        Vector3d finePos = targetMutable->GetRandomExteriorPoint();

        target_x_offset_m = finePos.x();
        target_y_offset_m = finePos.y();
	}
	Vector3d worldOffset = 
        target->ConvertModelCoordinatesToWorld(Vector3d(target_x_offset_m, target_y_offset_m, 0));

	float lon_corr = C_MTORAD / cosf(mcTrack.mfLat_rad);
    mcTrack.mfAlt_m += worldOffset.z();
	if (mcTrack.mfAlt_m < 1) mcTrack.mfAlt_m = 1;
    mcTrack.mfLat_rad += C_MTORAD * worldOffset.y();
    mcTrack.mfLon_rad += lon_corr * worldOffset.x();
}


void tcRadar::Update(double t)
{    
    assert(parent->GetComponent<tcSensorPlatform>());
	if (mbActive != 0)
	{
        parent->GetComponent<tcSensorPlatform>()->SetActivityFlag(tcSensorPlatform::RADAR_ACTIVE);
	}

    if (!UpdateScan(t)) return; // only update once per scan period

    UpdateJammingDegradation();

    if (mnMode == SSMODE_SURVEILLANCE)
    {
        UpdateSurveillance(t);
    }
    else if ((mnMode == SSMODE_SEEKERTRACK)||(mnMode == SSMODE_SEEKERSEARCH)
        ||(mnMode == SSMODE_SEEKERACQUIRE))
    {
        UpdateSeeker(t);
    }

}

/**
*
*/
tcRadar::tcRadar() 
:   tcSensorState(),
    mpDBObj(0)
{
}

tcRadar::tcRadar(std::shared_ptr<tcRadarDBObject> dbObj)
:   tcSensorState(dbObj),
    mpDBObj(dbObj),
    isSemiactive(mpDBObj->isSemiactive),
	last_range_km(0),
	target_x_offset_m(0),
    target_y_offset_m(0),
    isJammed(false),
    jammingDegradation_dB(0)
{
	assert(dbObj);

    if (dbObj->isSurveillance)
    {
        mnMode = SSMODE_SURVEILLANCE;
    }
    else
    {
        mnMode = SSMODE_FC; // do not do surveillance updates
    }

    mfSensorHeight_m = 10.0f;
}

/**
*
*/
tcRadar::~tcRadar() 
{

}
