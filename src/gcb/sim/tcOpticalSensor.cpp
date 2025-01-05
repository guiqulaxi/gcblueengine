/**
**  @file tcOpticalSensor.cpp
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
#include "aerror.h"
#include "tcCommandQueue.h"
#include "nsNav.h"
#include "tcOpticalSensor.h"
#include "tcGameObject.h"
#include "tcSurfaceObject.h"
#include "tcAeroAirObject.h"
#include "tcAirObject.h"
#include "tcMissileObject.h"
#include "tcAirfieldObject.h"
#include "tcBallisticWeapon.h"
#include "tcAirCM.h"
#include "ai/Brain.h"

#include "tcPlatformDBObject.h"
#include "tcMissileDBObject.h"
#include "tcCounterMeasureDBObject.h"
#include "tcSimState.h"
#include "tcGameObjIterator.h"
#include "common/tcObjStream.h"
#include "tcEventManager.h"
#include "tcSonarEnvironment.h"
//#include "tcMessageInterface.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

float tcOpticalSensor::lastTargetSignature_dB = -99.0f;
float tcOpticalSensor::last_az_rad = -77.0f;

// break up this file later

/**
* Load state from stream
*/
tcUpdateStream& tcOpticalSensor::operator<<(tcUpdateStream& stream)
{
    tcSensorState::operator<<(stream);

    return stream;
}

/**
* Save state to stream
*/
tcUpdateStream& tcOpticalSensor::operator>>(tcUpdateStream& stream)
{
    tcSensorState::operator>>(stream);

    return stream;
}

float tcOpticalSensor::CalculateNightPenalty(std::shared_ptr<const tcGameObject> target) const
{
    // 定义一个静态的日期时间对象
    static tcDateTime dt;

    // 从模拟状态中获取当前的日期和时间，并存储到dt对象中
    simState->GetDateTime(dt);

    // 计算本地时间的小时数，考虑了目标的经度（以弧度为单位）和常数C_RADTOHRS的转换
    // 这里是将目标的经度转换为时间差，以调整到目标的本地时间
    float localHours = float(dt.GetHour()) + C_RADTOHRS * target->mcKin.mfLon_rad;

    // 确保本地时间在0到24小时之间
    if (localHours >= 24.0) localHours -= 24.0; // 如果超过24小时，减去24小时
    else if (localHours < 0) localHours += 24.0; // 如果小于0小时，加上24小时

    // 判断当前是否是夜间（定义为非6点到18点之间的时间）
    if ((localHours < 6) || (localHours > 18))
    {
        // 如果是夜间，返回夜间惩罚因子（从数据库对象中获取）
        return mpDBObj->nightFactor;
    }
    else
    {
        // 如果不是夜间，返回1.0（表示没有惩罚）
        return 1.0f;
    }
}

/**
 * @returns 根据传感器类型，返回目标的红外特征（以分贝[dB]为单位）或电光特征（以分贝平方米[dBsm]为单位）
 */
float tcOpticalSensor::CalculateTargetSignature(std::shared_ptr<const tcGameObject> target, float& targetAz_rad, float& targetAlt_m) const
{
    // 获取雷达父对象的运动状态
    const tcKinematics *parent_kin = &parent->mcKin;
    // 获取目标对象的运动状态
    const tcKinematics *tgt_kin = &target->mcKin;

    // 尝试将目标的数据对象转换为空气探测数据对象
    std::shared_ptr<tcAirDetectionDBObject> detectionData = target->mpDBObject->GetComponent<tcAirDetectionDBObject>();
    // 如果转换失败（即目标不是空气探测对象），则返回-999.0f表示无效特征
    if (detectionData == nullptr) return -999.0f;

    // 计算目标相对于雷达父对象的方位角（以弧度为单位）
    targetAz_rad = nsNav::GCHeadingApprox_rad(parent_kin->mfLat_rad, parent_kin->mfLon_rad,
                                              tgt_kin->mfLat_rad, tgt_kin->mfLon_rad);
    // 计算目标的有效高度（目标高度加上有效高度修正）
    targetAlt_m = target->mcKin.mfAlt_m + detectionData->effectiveHeight_m;

    // 初始化特征值为-123.4f（一个无效或占位值）
    float signature = -123.4f;
    // 如果传感器是红外传感器
    if (mpDBObj->isIR)
    {
        // 计算目标的方位角相对于其朝向的差值（以弧度为单位），并调整到0到2π之间
        float aspect_rad = targetAz_rad - tgt_kin->mfHeading_rad + C_PI;
        if (aspect_rad >= C_TWOPI) aspect_rad -= C_TWOPI;

        // 根据目标的红外特征和方位角差值计算红外特征值
        signature = target->GetIRSignature(C_180OVERPI * aspect_rad);
    }
    else
    {
        // 获取目标的分类
        unsigned int targetClassification = target->mpDBObject->mnType;
        // 如果目标是地面目标
        if (targetClassification & PTYPE_SURFACE)
        {
            // 根据雷达父对象的高度和目标到雷达父对象的距离计算电光特征值
            signature = target->GetOpticalCrossSection(parent_kin->mfAlt_m, parent_kin->RangeToKm(tgt_kin->mfLon_rad, tgt_kin->mfLat_rad));
        }
        else
        {
            // 对于非地面目标，直接计算电光特征值（可能不考虑高度和距离）
            signature = target->GetOpticalCrossSection();
        }
    }

    // 返回计算得到的特征值
    return signature;
}


/**
 * 判断光学传感器是否能够检测到目标。
 */
bool tcOpticalSensor::CanDetectTarget(std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom)
{
    // 初始化变量
    float targetRange_km;           // 目标距离
    float coverageAz1, coverageAz2; // 传感器覆盖的方位角范围
    bool bInSearchVolume = false;   // 目标是否在搜索体积内

    // 确保数据库对象存在
    assert(mpDBObj);

    // 记录当前检测的目标ID
    detectionCandidate = target->mnID;
    // 初始化最后计算的边距和特征值为无效值
    last_margin_dB = -99.9f;
    lastTargetSignature_dB = -999.0f;
    last_az_rad = -99.9f;

    // 如果传感器不处于活动状态，则无法检测目标
    if (!mbActive) return false;

    // 如果是半主动模式
    if (isSemiactive)
    {
        float designatorRange_km = 0; // 激光指示器的距离
        std::shared_ptr<tcOpticalSensor> designator = GetLaserDesignator(); // 获取激光指示器
        // 如果没有指示器或指示器无法检测到目标，则无法检测目标
        if (designator == nullptr || !designator->CanDetectTarget(target, designatorRange_km)) return false;
    }

    // 计算目标的方位角和高度，以及目标的特征值
    float targetAz_rad = 0;
    float targetAlt_m = -999.0f;
    float targetCrossSection_dBsm = CalculateTargetSignature(target, targetAz_rad, targetAlt_m);
    last_az_rad = targetAz_rad; // 记录目标的方位角

    // 获取雷达父对象和目标的运动状态
    const tcKinematics *parent_kin = &parent->mcKin;
    const tcKinematics *tgt_kin = &target->mcKin;
    lastTargetSignature_dB = targetCrossSection_dBsm; // 记录目标的特征值

    // 根据目标的分类判断其是否为潜艇（在水下），如果是且高度大于等于-18米，则视为地面目标
    unsigned int targetClassification = target->mpDBObject->mnType;
    if (targetClassification & PTYPE_SUBSURFACE)
    {
        if (target->mcKin.mfAlt_m >= -18.0f)
        {
            targetClassification |= PTYPE_SURFACE;
        }
    }

    // 根据传感器的配置确定其能够检测的目标类型
    unsigned int targetMask = 0;
    if (mpDBObj->mbDetectsAir) targetMask |= PTYPE_AIR;
    if (mpDBObj->mbDetectsMissile) targetMask |= PTYPE_MISSILE;
    if (mpDBObj->mbDetectsSurface) targetMask |= PTYPE_SURFACE;
    if (mpDBObj->mbDetectsGround) targetMask |= PTYPE_GROUND;

    // 判断目标类型是否与传感器能够检测的类型匹配
    bool bTargetTypeMatch = (targetClassification & targetMask) != 0;
    bTargetTypeMatch = bTargetTypeMatch || (mpDBObj->mbDetectsAir && (targetClassification == PTYPE_AIRCM)); // 将对抗导弹视为潜在空中目标

    // 如果目标类型不匹配，则无法检测目标
    if (!bTargetTypeMatch) return false;

    // 如果传感器的视场大于等于360度，则目标一定在搜索体积内
    if (mpDBObj->mfFieldOfView_deg >= 360.0f)
    {
        bInSearchVolume = true;
    }
    else
    {
        // 计算传感器的搜索方位角范围
        float lookAz_rad = parent->mcKin.mfHeading_rad + mountAz_rad; // 传感器指向的方位角
        float fHalfFOV_rad = 0.5f * C_PIOVER180 * mpDBObj->mfFieldOfView_deg; // 传感器视场的一半（以弧度为单位）
        coverageAz1 = lookAz_rad - fHalfFOV_rad; // 搜索方位角范围的下限
        coverageAz2 = lookAz_rad + fHalfFOV_rad; // 搜索方位角范围的上限
        // 判断目标是否在搜索方位角范围内
        bInSearchVolume = AngleWithinRange(targetAz_rad, coverageAz1, coverageAz2) != 0;
        // 如果不在搜索体积内，则设置距离为0并返回false
        if (!bInSearchVolume) { range_km = 0; return false; }
    }

    // 计算地平线距离（即传感器和目标之间由于地球曲率而无法直接看到的最大距离）
    float horizonRange_km = C_VISUALHOR * (sqrtf(targetAlt_m) + sqrtf(parent_kin->mfAlt_m + mfSensorHeight_m));

    // 计算传感器和目标之间的实际距离
    targetRange_km = C_RADTOKM * nsNav::GCDistanceApprox_rad(parent_kin->mfLat_rad, parent_kin->mfLon_rad,
                                                             tgt_kin->mfLat_rad, tgt_kin->mfLon_rad, parent_kin->mfAlt_m, tgt_kin->mfAlt_m);
    range_km = targetRange_km; // 记录实际距离

    // 如果目标距离超过地平线距离或传感器的最大检测距离，则无法检测目标
    if ((targetRange_km > horizonRange_km) || (targetRange_km > mpDBObj->mfMaxRange_km))
    {
        return false;
    }

    // 如果没有与目标之间的视距（即被遮挡），则无法检测目标
    if (!HasLOS(target)) return false;

    // 如果是半主动模式或指示器模式且传感器不是监视模式，则假设能够检测到目标（因为指示器足够亮，半主动传感器足够敏感）
    if ((isSemiactive || isDesignator) && !mpDBObj->isSurveillance)
    {
        last_margin_dB = 99.9f; // 设置边距为无效值（表示足够大的边距）
        return true; // 返回true表示能够检测到目标
    }

    // 计算大气衰减（根据目标和传感器的高度以及大气密度）
    int SeaState = tcSonarEnvironment::Get()->GetSeaState(); // 获取海况
    float extinction1 = Aero::GetAirDensity(tgt_kin->mfAlt_m) / 1.255 * 0.75; // 目标高度处的大气衰减系数
    float extinction2 = Aero::GetAirDensity(parent_kin->mfAlt_m) / 1.225 * 0.75; // 传感器高度处的大气衰减系数
    float extinction = (extinction1 + extinction2) * 0.5; // 平均大气衰减系数
    extinction = (mpDBObj->isIR) ? 0.25 : extinction; // 对于红外传感器，不修改大气衰减系数
    float atmosphericAtten_dB = extinction * (mpDBObj->mfRefRange_km - targetRange_km); // 计算大气衰减（以分贝为单位）

    // 计算夜间惩罚（即夜间检测时由于光线不足而导致的检测难度增加）
    float nightPenalty = CalculateNightPenalty(target);

    // 计算边距（即传感器检测到的信号强度与目标特征值、距离和大气衰减等因素的综合比较）
    float margin_dB = 20.0f * (log10f(nightPenalty * mpDBObj->mfRefRange_km) - log10f(targetRange_km)) + targetCrossSection_dBsm + atmosphericAtten_dB;
    last_margin_dB = margin_dB; // 记录边距

    // 如果是监视模式，则根据边距和随机数判断是否检测到目标（模拟不确定性）
    if (mnMode == SSMODE_SURVEILLANCE)
    {
        return RandomDetect(margin_dB); // 根据边距和随机数返回true或false
    }
    else
    {
        // 对于非监视模式，如果边距大于等于0，则表示能够检测到目标
        return margin_dB >= 0;
    }
}

/**
* @return false if key not found in database
*/
bool tcOpticalSensor::InitFromDatabase(long key)
{
    assert(database);

    tcSensorState::InitFromDatabase(key);

    mpDBObj =  std::dynamic_pointer_cast<tcOpticalDBObject>(database->GetObject(key));
    if (mpDBObj == NULL) 
    {
        fprintf(stderr, "Error - tcOpticalSensor::InitFromDatabase - Not found in db or bad class for key\n");
        return false;
    }

    mfSensorHeight_m = 10.0f;
    mnMode = SSMODE_SURVEILLANCE;
    mbActive = true;

    return true;
}

bool tcOpticalSensor::IsDesignator() const
{
    return isDesignator;
}

/**
* Alternative to dynamic_cast
*/
bool tcOpticalSensor::IsOptical() const
{
    return true;
}

/**
*
*/
void tcOpticalSensor::Serialize(tcFile& file, bool mbLoad) 
{
    tcSensorState::Serialize(file, mbLoad);
}



/**
*
*/
tcOpticalSensor& tcOpticalSensor::operator=(tcOpticalSensor& ss) 
{
    tcSensorState::operator =(ss);

    mpDBObj = ss.mpDBObj;
    return(*this);
}

/**
*
*/
std::shared_ptr<tcOpticalSensor> tcOpticalSensor::Clone(void) 
{
    std::shared_ptr<tcOpticalSensor>pNew = std::make_shared<tcOpticalSensor>();
    *pNew = *this;
    return pNew;
}



/**
* 导弹搜索器调用此函数以检查是否切换到对抗措施目标，
* 此函数的主要目的是导弹搜索器在跟踪目标时，检查是否存在更优先的对抗措施目标（如诱饵弹），
* 并根据一系列因子计算切换到对抗措施目标的概率。如果成功切换到对抗措施目标，则更新跟踪信息。
*/
void tcOpticalSensor::CounterMeasureTest(double t)
{
    const unsigned int maxAttempts = 4; // 最多测试此数量的对抗措施（CM）

    lastCounterMeasureTime = t; // 记录上次对抗措施测试的时间

    std::shared_ptr<tcGameObject> target = simState->GetObject(mcTrack.mnID); // 获取当前跟踪的目标对象
    if (target == 0)
    {
        assert(false); // 如果没有目标，则断言失败
        return;
    }

    // 如果已经在跟踪一个对抗措施目标，则现在不要检查切换回原目标
    if (std::shared_ptr<tcAirCM> cm =  std::dynamic_pointer_cast<tcAirCM>(target))
    {
        return;
    }

    // 计算目标相对于父对象的距离（千米）和方位角（弧度）
    float targetRange_km = parent->mcKin.RangeToKmAlt(target->mcKin);
    float targetBearing_rad = parent->mcKin.HeadingToRad(target->mcKin);

    float targetHeight_m = 0; // 目标相对于雷达地平线的等效高度
    float fTargetAz_rad = 0; // 目标方位角（未在此函数中使用）
    // 可能可以找到方法使用父例程中的雷达散射截面（RCS）
    float targetSignature_dB = CalculateTargetSignature(target, fTargetAz_rad, targetHeight_m); // 计算目标的雷达散射截面（dB）

    tcGeoRect region; // 定义一个地理矩形区域
    region.Set(target->mcKin.mfLon_rad, target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfLat_rad); // 将区域设置为目标的位置（经纬度）
    float dy_rad = C_MTORAD*500.0f; // 纬度方向上的扩展（弧度）
    float dx_rad = dy_rad / cosf(target->mcKin.mfLat_rad); // 经度方向上的扩展（弧度），根据纬度进行调整
    region.Expand(dx_rad, dy_rad); // 扩展地理矩形区域

    unsigned int attempts = 0; // 记录尝试次数
    tcGameObjIterator iter(region); // 创建一个迭代器，用于遍历地理矩形区域内的游戏对象

    // 遍历区域内的所有游戏对象
    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcGameObject> obj = iter.Get(); // 获取当前遍历到的游戏对象

        assert(obj != 0); // 确保对象不为空
        std::shared_ptr<tcCounterMeasureDBObject> cmData =  std::dynamic_pointer_cast<tcCounterMeasureDBObject>(obj->mpDBObject); // 尝试将对象的数据库对象转换为对抗措施数据库对象

        // 检查对象是否是对抗措施（flare）且类型为空中对抗措施（PTYPE_AIRCM）
        bool isEligible = (cmData != 0) && cmData->IsFlare() &&
                          (obj->mpDBObject->mnType == PTYPE_AIRCM);
        float range_km; // 对象距离（未在此处初始化，但在后续使用）

        // 如果对象是符合条件的对抗措施且可以检测到
        if (isEligible && CanDetectTarget(obj, range_km))
        {
            // 计算对象相对于父对象的距离（千米）和方位角（弧度）
            float objRange_km = parent->mcKin.RangeToKmAlt(obj->mcKin);
            float objSignature_dB = lastTargetSignature_dB; // 对象的雷达散射截面（dB），这里使用了上一次目标的雷达散射截面，可能是一个错误或简化
            float objBearing_rad = parent->mcKin.HeadingToRad(obj->mcKin);

            // 计算对象方位角与目标方位角之间的差异
            float dBearing_rad = fabsf(objBearing_rad - targetBearing_rad);
            if (dBearing_rad > C_PI) dBearing_rad = C_TWOPI - dBearing_rad;

            // 计算距离因子、RCS因子和方位角因子
            float rangeFactor = (fabsf(objRange_km - targetRange_km) > 0.25f) ? 0.5f : 1.0f;
            float rcsFactor = (objSignature_dB < (targetSignature_dB - 3)) ? 0.5f : 1.0f;
            float bearingFactor = (dBearing_rad > 0.349) ? 0.25f: 1.0f; // 如果方位角差异超过20度，则进行惩罚

            // 计算成功切换到对抗措施目标的概率
            float prob_success = mpDBObj->counterMeasureFactor * cmData->effectiveness *
                                 rangeFactor * rcsFactor * bearingFactor;
            // 如果随机数小于成功概率，则切换到对抗措施目标
            if (randf() < prob_success)
            {
                mcTrack.mnID = obj->mnID; // 更新跟踪的目标ID
                UpdateTrack(obj, t); // 更新跟踪信息
                return; // 成功切换，退出函数
            }
            else
            {
                // 如果尝试次数达到最大值，则退出循环
                if (++attempts >= maxAttempts) return;
            }

        }
    }
}

unsigned tcOpticalSensor::GetFireControlTrackCount() const
{
    return fireControlTrackCount;
}

unsigned tcOpticalSensor::GetMaxFireControlTracks() const
{
    return mpDBObj->maxFireControlTracks;
}

bool tcOpticalSensor::IsSemiactive() const
{
    return isSemiactive;
}

/**
* Does not test if radar can detect target.
* @return true if track is available.
*/
bool tcOpticalSensor::IsTrackAvailable()
{
    return (fireControlTrackCount < mpDBObj->maxFireControlTracks);
}

/**
* if track is available, reserve a track.
* The current approach to semi-active guidance is to require each 
* missile to request one track per target, even if it is the same 
* target as a pre-existing track.
* Calling method must check if target is detectable for this to
* work properly.
*/
bool tcOpticalSensor::RequestTrack(long targetId)
{
    if (IsTrackAvailable())
    {
        fireControlTrackCount++;
        return true;
    }
    else
    {
        return false;
    }
}

bool tcOpticalSensor::ReleaseTrack(long targetId)
{
    if (fireControlTrackCount > 0)
    {
        fireControlTrackCount--;
        return true;
    }
    else
    {
        fprintf(stderr, "tcRadar::tcOpticalSensor called with no tracks\n");
        return false;
    }
}


/**
* 更新导弹的寻的雷达。
*/
void tcOpticalSensor::UpdateSeeker(double t)
{
    long nTargetID; // 目标ID
    std::shared_ptr<tcGameObject>ptarget = 0; // 目标对象指针，初始化为0（空）
    int bFound; // 是否找到目标的标志
    std::shared_ptr<tcMissileObject> missile = 0; // 导弹对象指针，初始化为0（空）

    // 根据当前模式执行不同操作
    switch (mnMode)
    {
    case SSMODE_SEEKERACQUIRE:        // 寻的获取模式，穿透到寻的跟踪模式
    case SSMODE_SEEKERTRACK:          // 寻的跟踪模式
        nTargetID = mcTrack.mnID; // 获取当前跟踪的目标ID
        // 如果目标ID等于父对象（导弹）的ID，则不进行自我检测
        if (nTargetID == parent->mnID)
        {
            bFound = false; // 未找到目标
        }
        else
        {
            // 在平台状态表中查找目标
            bFound = simState->maPlatformState.Lookup(nTargetID,ptarget);
        }

        // 将父对象转换为导弹对象
        missile =  std::dynamic_pointer_cast<tcMissileObject>(parent);
        // 如果导弹存在，找到了目标，导弹的拦截时间小于5秒，并且最后一次反制措施的时间超过1秒前
        if ((missile != 0) && bFound && (missile->mfInterceptTime < 5.0f) &&
            (lastCounterMeasureTime < (t - 1.0)))
        {
            CounterMeasureTest(t); // 测试反制措施
        }

        // 如果找到了目标
        if (bFound)
        {  // 允许检测同阵营的目标
            float fRange_km; // 目标距离（千米）
            // 如果可以检测到目标，则更新跟踪信息
            if (CanDetectTarget(ptarget, fRange_km))
            {
                UpdateTrack(ptarget, t); // 更新跟踪信息
                return; // 结束函数
            }
        }
        // 如果跟踪丢失超过7秒，则关闭导弹
        parent->SetHeading(parent->mcKin.mfHeading_rad); // 停止转向
        if ((mnMode == SSMODE_SEEKERTRACK)&& // 如果当前是寻的跟踪模式
            (t - mcTrack.mfTimestamp) > 7.0) // 并且跟踪丢失时间超过7秒
        {
            parent->SelfDestruct(); // 导弹自毁
            mcTrack.mnID = NULL_INDEX; // 清空跟踪的目标ID
#ifdef _DEBUG
            // 如果是己方阵营的导弹，则显示信息
            if(simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance()))
            {
                char zBuff[128];
                _snprintf(zBuff, 128, "%s shut down (%s)\n", parent->mzUnit.c_str(), parent->mzClass.c_str());
                simState->mpCommandInterface->DisplayInfoMessage(zBuff);
            }
#endif
            return; // 结束函数
        }
        // 此代码用于在跟踪丢失后进入搜索模式（已注释）
        //pTrack->mnID = NULL_INDEX;
        //apRadarSS->mnMode = SSMODE_SEEKERSEARCH;
        break;
    case SSMODE_SEEKERSEARCH: // 寻的搜索模式
    {
        // 获取搜索区域
        tcGeoRect region;
        GetTestArea(region);

        // 创建迭代器，遍历搜索区域内的对象
        tcGameObjIterator iter(region);
        float minRange = 1e15f; // 初始化最小距离为极大值
        long minID = NULL_INDEX; // 初始化最小距离的目标ID为空

        // 查找可检测到的最近目标
        for (iter.First();iter.NotDone();iter.Next())
        {
            std::shared_ptr<tcGameObject>target = iter.Get(); // 获取当前对象
            if (target != parent) // 不进行自我检测
            {
                float range_km; // 当前目标距离（千米）
                /* 注释掉的部分用于禁用同阵营目标的检测：
                    ** bool bDetected = (parent->GetAlliance() != target->GetAlliance()) &&
                    **    CanDetectTarget(target,range_km);
                    */
                bool bDetected = CanDetectTarget(target, range_km); // 检测是否可以检测到目标
                if ((bDetected) && (range_km < minRange)) // 如果可以检测到，并且距离更近
                {
                    minID = target->mnID; // 更新最小距离的目标ID
                    minRange = range_km; // 更新最小距离
                }
            }
        }

        // 如果没有找到目标，则返回
        if (minID==NULL_INDEX) return;

        // 如果寻的器锁定了反制措施，则根据反制措施的有效性和系数进行概率判断
        if (std::shared_ptr<tcAirCM> airCM =  std::dynamic_pointer_cast<tcAirCM>(simState->GetObject(minID)))
        {
            float prob_success = mpDBObj->counterMeasureFactor * airCM->mpDBObject->effectiveness; // 计算成功概率
            if (randf() > prob_success) // 如果随机数大于成功概率
            {
                return; // 反制措施被拒绝
            }
        }

        // 指定最近的目标为攻击目标
        parent->DesignateTarget(minID);
        mfLastScan = t - 30.0f; // 为了强制光学寻的快速切换到跟踪模式
    }
    }
}

/**
* 监控检测后调用，以更新相应联盟的传感器地图。
*/
void tcOpticalSensor::UpdateSensorMap(double t, std::shared_ptr<const tcGameObject> target, float range_km, float az_rad)
{
    // 断言检测候选对象与目标对象的ID匹配
    assert(detectionCandidate == target->mnID);

    // 初始化传感器地图跟踪指针为0
    std::shared_ptr<tcSensorMapTrack> pSMTrack = 0;
    // 获取或创建传感器报告
    tcSensorReport* report = simState->mcSensorMap.GetOrCreateReport(parent->mnID, mpDBObj->mnKey, target->mnID,
                                                                     pSMTrack, parent->GetAlliance());
    // 如果报告为空，则返回
    if (report == 0) return;

    // 检查应使用主动还是被动模型
    assert(mpDBObj->rangeError > 0);
    // 如果范围误差大于1，则为主动光学
    bool activeOptical = mpDBObj->rangeError > 1.0f; // 值0+到1为被动范围误差的比例，>1为主动误差的绝对值

    if (activeOptical)
    {
        // 更新主动报告
        tcSensorState::UpdateActiveReport(report, t, az_rad, range_km, target->mcKin.mfAlt_m, pSMTrack);

        // 设置速度估计和方差
        report->speedEstimate_mps = C_KTSTOMPS * target->mcKin.mfSpeed_kts * cosf(target->mcKin.mfClimbAngle_rad);
        report->speedVariance = 1.0f;
        // 设置航向估计和方差
        report->headingEstimate_rad = target->mcKin.mfHeading_rad;
        report->headingVariance = 0.001f;
        // 标记速度和航向有效
        report->validFlags |= tcSensorReport::SPEED_VALID | tcSensorReport::HEADING_VALID;
    }
    else
    {
        // 更新被动报告
        tcSensorState::UpdatePassiveReport(report, t, az_rad, range_km, pSMTrack);
    }

    // 断言传感器地图跟踪指针不为0
    assert(pSMTrack != 0);
    // 如果传感器地图跟踪指针为0，则返回
    if (pSMTrack == 0) return;

    // 更新分类
    report->classification = target->mpDBObject->mnType;
    // 如果目标为导弹，则设置报告联盟为目标联盟
    if ((report->classification & PTYPE_MISSILE) != 0)
    {
        report->alliance = target->GetAlliance();
    }

    // 如果最后测量的信噪比边缘值大于等于ID阈值
    if (last_margin_dB >= mpDBObj->idThreshold_dB)
    {
        // 设置报告联盟为目标联盟，数据库ID为目标数据库键
        report->alliance = target->GetAlliance();
        report->databaseID = target->mnDBKey;
    }

    // 检查是否为新检测
    bool bNewDetection = pSMTrack->IsNew();
    if (bNewDetection)
    {
        // 更新跟踪信息
        pSMTrack->UpdateTrack(0);
        // 如果当前对象的联盟是玩家联盟
        if (simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance()))
        {
            // 播放音效（此处代码被注释）
            // tcSound::Get()->PlayEffect("LowBeep");
        }
        // 打印检测信息（此处代码被注释）
        //fprintf(stdout, "target %d detected (optical) at %3.1f km at time %.1f [a:%d]\n",
        //    target->mnID,range_km,t,parent->GetAlliance());
        // 触发新接触事件
        tcEventManager::Get()->NewContact(parent->GetAlliance(), pSMTrack);
    }

}

void tcOpticalSensor::UpdateSurveillance(double t)
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
            bool bDetected = (parent->GetAlliance() != target->GetAlliance()) &&
                             CanDetectTarget(target,range_km);
            if (bDetected) UpdateSensorMap(t, target, range_km, last_az_rad);

        }
    }
}

/**
* Update sensor track with target state. Normally used with
* missile seekers.
*/
void tcOpticalSensor::UpdateTrack(std::shared_ptr<const tcGameObject> target, double t)
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
    if (mnMode == SSMODE_SEEKERACQUIRE) 
    {
        mnMode = SSMODE_SEEKERTRACK;
        //if (simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) 
        //{
        //    tcSound::Get()->PlayEffect("TwoBeeps");
        //}
    }
}

void tcOpticalSensor::Update(double t)
{
    if (!UpdateScan(t)) return; // only update once per scan period
    assert(parent);

    switch (mnMode)
    {
    case SSMODE_SURVEILLANCE:
    {
        UpdateSurveillance(t);
    }
    break;
    case SSMODE_SEEKERTRACK:
    case SSMODE_SEEKERSEARCH:
    case SSMODE_SEEKERACQUIRE:
    {
        UpdateSeeker(t);
    }
    case SSMODE_FC:
        break;
    default:
        assert(false);
        break;
    }

}

/**
*
*/
tcOpticalSensor::tcOpticalSensor() 
    : tcSensorState(),
    last_margin_dB(0)
{
    mpDBObj = NULL;
}

tcOpticalSensor::tcOpticalSensor(std::shared_ptr<tcOpticalDBObject> dbObj)
    : tcSensorState(dbObj),
    mpDBObj(dbObj),
    last_margin_dB(0),
    fireControlTrackCount(0),
    isSemiactive(mpDBObj->isSemiactive),
    isDesignator(mpDBObj->isDesignator)
{
    assert(dbObj);

    mnMode = dbObj->isSurveillance ? SSMODE_SURVEILLANCE : SSMODE_FC;
    mfSensorHeight_m = 10.0f;
    mbActive = true; // optical defaults to always on

    if (!dbObj->isDesignator)
    {
        isHidden = true; // hide optical sensors
    }
    else
    {
        isHidden = false;
    }
}

/**
*
*/
tcOpticalSensor::~tcOpticalSensor() 
{

}
