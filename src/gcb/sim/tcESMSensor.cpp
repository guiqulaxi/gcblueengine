/**  
**  @file tcESMSensor.cpp
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

#include "tcESMSensor.h"
#include "aerror.h"
#include "nsNav.h"
#include "tcGameObject.h"
#include "tcMissileObject.h"
#include "tcPlatformObject.h"
#include "tcECM.h"
#include "tcRadar.h"
#include "common/tcStream.h"
#include "common/tcGameStream.h"
#include "common/tcObjStream.h"
#include "tcGameObjIterator.h"
#include "tcSimState.h"
////#include "tcMessageInterface.h"
#include "tcEventManager.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


float tcESMSensor::targetRange_km = -88.8f; 
float tcESMSensor::last_margin_dB = -88.8f;
float tcESMSensor::last_ERP_dBW = -88.8f;
bool tcESMSensor::rwrUpdate = false;


tcGameStream& tcESMSensor::operator<<(tcGameStream& stream)
{    
    tcSensorState::operator<<(stream);

    stream >> lastRWRupdate;
    stream >> rwrWarningLevel;

    return stream;
}

tcGameStream& tcESMSensor::operator>>(tcGameStream& stream)
{
    tcSensorState::operator>>(stream);

    stream << lastRWRupdate;
    stream << rwrWarningLevel;

    return stream;
}


/**
* Load state from stream
*/
tcUpdateStream& tcESMSensor::operator<<(tcUpdateStream& stream)
{
    tcSensorState::operator<<(stream);

    stream >> rwrWarningLevel;

    return stream;
}

/**
* Save state to stream
*/
tcUpdateStream& tcESMSensor::operator>>(tcUpdateStream& stream)
{
    tcSensorState::operator>>(stream);

    stream << rwrWarningLevel;

    return stream;
}




/**
* 这个方法用于被动寻的器（反辐射或干扰寻的）的检测测试。
* 它不会像ProcessESMDetection方法那样构建发射器ID列表。
*
* TODO: 与ProcessESMDetection方法合并，查看使用最大接收功率与距离进行搜索的方法（是否作弊？）
*/
bool tcESMSensor::CanDetectTarget( std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom)
{
    float fAz_rad = 0; // 方位角（弧度），初始化为0
    range_km = 0; // 目标距离（千米），初始化为0
    last_margin_dB = -99.0f; ///< 上次调用IsDetected时得到的余量（分贝），初始化为-99.0分贝
    last_ERP_dBW = -99.0f; ///< 上次调用IsDetected时得到的等效辐射功率（分贝瓦），初始化为-99.0分贝瓦

    // 尝试将目标对象转换为导弹对象
    if ( std::shared_ptr<const tcMissileObject>pMissileObj = std::dynamic_pointer_cast<const tcMissileObject>(target))
    {
        // 如果导弹对象有寻的雷达（一些空对地导弹没有传感器）
        if (std::shared_ptr<tcRadar> emitter = pMissileObj->GetSeekerRadar())
        {
            // 调用IsDetectedRadar方法检测雷达
            bool bDetected = IsDetectedRadar(emitter, fAz_rad);
            range_km = targetRange_km; // 设置检测到的目标距离
            return bDetected; // 返回是否检测到
        }
        else
        {
            return false; // 没有寻的雷达，返回未检测到
        }
    }
    // 尝试将目标对象转换为平台对象（如飞机、舰船等）
    else if ( std::shared_ptr<const tcPlatformObject>pPlatformObj = std::dynamic_pointer_cast<const tcPlatformObject>(target))
    {
        // 如果平台对象没有辐射（不是雷达或电子战设备的工作状态），则返回未检测到
        if (!pPlatformObj->GetComponent<tcSensorPlatform>()->IsRadiating()) return false;

        bool bDetected = false; // 初始化检测状态为未检测到
        unsigned nSensors = pPlatformObj->GetComponent<tcSensorPlatform>()->GetSensorCount(); // 获取平台对象的传感器数量
        for (unsigned n=0; (n<nSensors) && (!bDetected); n++) // 遍历所有传感器，直到检测到或遍历完所有传感器
        {
             std::shared_ptr<const tcSensorState> sensor = pPlatformObj->GetComponent<tcSensorPlatform>()->GetSensor(n); // 获取当前传感器状态
            // 尝试将传感器转换为雷达对象
            if ( std::shared_ptr<const tcRadar> emitter = std::dynamic_pointer_cast<const tcRadar>(sensor))
            {
                // 检测雷达，并更新检测状态和距离
                bDetected = bDetected || IsDetectedRadar(emitter, fAz_rad);
                range_km = targetRange_km;
            }
            // 尝试将传感器转换为电子战（ECM）设备对象
            else if ( std::shared_ptr<const tcECM> emitter = std::dynamic_pointer_cast<const tcECM>(sensor))
            {
                // 检测电子战设备，并更新检测状态和距离
                bDetected = bDetected || IsDetectedECM(emitter, fAz_rad);
                range_km = targetRange_km;
            }
        }

        return bDetected; // 返回是否检测到
    }

    return false; // 目标类别不包含雷达或电子战设备，因此无法检测到
}
/**
* @return false if key not found in database
*/
bool tcESMSensor::InitFromDatabase(long key)
{
	assert(database);

    tcSensorState::InitFromDatabase(key);

    mpDBObj = std::dynamic_pointer_cast<tcESMDBObject>(database->GetObject(key));
    if (mpDBObj == NULL) 
    {
        fprintf(stderr, "Error - tcESMSensor::InitFromDatabase - Not found in db or bad class for key\n");
        return false;
    }

	mfSensorHeight_m = 10.0f;
    mnMode = SSMODE_SURVEILLANCE;
    mbActive = true;

    return true;
}


bool tcESMSensor::IsDetectedECM(std::shared_ptr<const tcECM> emitter, float& az_rad)
{
    assert(emitter);
    if (emitter == 0) return false;

    float ERP_dBW = emitter->mpDBObj->ERP_dBW; // make ECM easier to detect until model is improved

    return IsDetected(emitter, ERP_dBW, az_rad);

}

bool tcESMSensor::IsDetectedRadar( std::shared_ptr<const tcRadar> emitter, float& az_rad)
{
    assert(emitter);
    if (emitter == 0) return false;
    if (emitter->IsSemiactive()) return false;

    float ERP_dBW = emitter->mpDBObj->ERPpeak_dBW;//有效辐射功率，峰值

    return IsDetected(emitter, ERP_dBW, az_rad);
}

/**
 *
 */
bool tcESMSensor::IsDetected( std::shared_ptr<const tcSensorState> emitter, float ERP_dBW, float& az_rad)
{
    // 断言确保emitter指针不为空
    assert(emitter);
    // 断言确保emitter的parent指针不为空
    assert(emitter->parent);

    // 重置目标范围（单位：公里）
    targetRange_km = 0;
    // 重置最后计算的余量（单位：dB）
    last_margin_dB = -99.0f;
    // 重置最后使用的ERP（单位：dBW）
    last_ERP_dBW = -99.0f;

    // 如果传感器或发射器不处于活动状态，则直接返回false
    if ((!mbActive) || (!emitter->IsActive())) return false;

    // 获取发射器的频率（单位：Hz）
    float emitterFreq_Hz = emitter->mpDBObj->averageFrequency_Hz;
    // 检查发射器频率是否在传感器的检测频段内
    bool inBand = (mpDBObj->minFrequency_Hz <= emitterFreq_Hz) &&
                  (mpDBObj->maxFrequency_Hz >= emitterFreq_Hz);
    // 如果不在频段内，则直接返回false
    if (!inBand)
    {
        return false;
    }

    // 获取发射器的运动学状态
    const tcKinematics& emitter_kin = emitter->parent->mcKin;

    // 使用传入的ERP值
    float emitterERP_dBW = ERP_dBW;
    last_ERP_dBW = ERP_dBW;
    // 计算发射器的视场角（单位：弧度）
    float emitterFOV_rad = C_PIOVER180*emitter->mpDBObj->mfFieldOfView_deg;

    // 计算发射器相对于北方的方位角（可能需要调整）
    // 注意：这里注释掉的代码可能是旧方案
    // float lookAz_rad = parent->mcKin.mfHeading_rad + mountAz_rad;
    // 计算发射器自身的方位角
    float emitterAz_rad = emitter_kin.mfHeading_rad + emitter->mountAz_rad;

    // 初始化目标方位角等变量
    float fTargetAz_rad;
    float fCoverageAz1, fCoverageAz2;
    bool bInSearchVolume = false; // 是否在传感器的搜索范围内
    bool bInEmitterScan = false; // 是否在发射器的扫描范围内

    // 断言确保mpDBObj和parent不为空
    assert(mpDBObj);
    assert(parent);

    // 获取传感器的运动学状态
    const tcKinematics& sensor_kin = parent->mcKin;

    // 计算从传感器到发射器的方位角
    fTargetAz_rad = nsNav::GCHeadingApprox_rad(sensor_kin.mfLat_rad, sensor_kin.mfLon_rad,
                                               emitter_kin.mfLat_rad, emitter_kin.mfLon_rad);
    // 更新外部传入的方位角变量
    az_rad = fTargetAz_rad;
    // 如果方位角为负，则调整到0到2π之间
    if (az_rad < 0) {az_rad += C_TWOPI;}

    // 如果传感器的视场角大于等于360度，则认为发射器在搜索范围内
    if (mpDBObj->mfFieldOfView_deg >= 360.0f)
    {
        bInSearchVolume = true;
    }
    else
    {
        // 计算传感器的搜索范围
        float lookAz_rad = sensor_kin.mfHeading_rad + mountAz_rad;
        float fHalfFOV_rad = 0.5f*C_PIOVER180*mpDBObj->mfFieldOfView_deg;
        fCoverageAz1 = lookAz_rad - fHalfFOV_rad;
        fCoverageAz2 = lookAz_rad + fHalfFOV_rad;
        // 检查发射器是否在搜索范围内
        bInSearchVolume = AngleWithinRange(fTargetAz_rad, fCoverageAz1, fCoverageAz2) != 0;


        if (!bInEmitterScan) {return false;}
    }

    // 计算雷达的地平线距离，基于发射器和传感器的海拔高度
    float fRadarHorizon = C_RADARHOR*(sqrtf(emitter_kin.mfAlt_m + emitter->mfSensorHeight_m) + sqrtf(sensor_kin.mfAlt_m + mfSensorHeight_m));

    // 计算目标距离（以公里为单位），基于发射器和传感器的经纬度
    targetRange_km = C_RADTOKM*nsNav::GCDistanceApprox_rad(
                         sensor_kin.mfLat_rad, sensor_kin.mfLon_rad, // 传感器的经纬度
                         emitter_kin.mfLat_rad, emitter_kin.mfLon_rad); // 发射器的经纬度

    // 如果目标距离超过了雷达的地平线距离，则无法检测到目标
    if (targetRange_km > fRadarHorizon)
    {
        return false; // 返回false，表示目标不在雷达的探测范围内
    }
    // 检查是否存在视线（LOS）障碍
    if (!HasLOS(emitter->parent)) return false; // 如果视线被阻挡，返回false
    // 计算信号的信噪比（SNR），基于发射器的等效辐射功率（ERP）和目标距离
    float fSNR = emitterERP_dBW // 发射器的等效辐射功率（dBW）
                 + 20.0f*(log10f(mpDBObj->mfRefRange_km)-log10f(targetRange_km)); // 使用自由空间路径损耗模型计算SNR

    // 更新最后的SNR（信噪比）边际值
    last_margin_dB = fSNR;

    // 根据SNR值随机判断是否检测到目标
    return RandomDetect(fSNR); // 调用RandomDetect函数，根据SNR和可能的随机因素判断是否检测到目标
}


bool tcESMSensor::IsESM() const
{
	return true;
}



/**
 *
 */
void tcESMSensor::Serialize(tcFile& file, bool mbLoad) 
{
    tcSensorState::Serialize(file, mbLoad);
}


void tcESMSensor::Update(double t)
{
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
 * 特殊更新函数，仅查看正在瞄准父对象（可能是指载有该传感器的平台）的平台上的传感器
 */
bool tcESMSensor::UpdateScanRWR(double t)
{
    // 如果传感器不处于活动状态，或者其所属的数据库对象不是RWR（雷达告警接收机）类型
    if (!mbActive || (!mpDBObj->isRWR))
    {
        // 将RWR警告等级设置为0
        rwrWarningLevel = 0;
        // 返回false，表示没有进行更新
        return false;
    }

    // 如果当前时间与上次RWR更新的时间差大于或等于2秒
    if ((t - lastRWRupdate) >= 2.0f)
    {
        // 更新上次RWR更新的时间为当前时间
        lastRWRupdate = t;
        // 返回true，表示进行了更新
        return true;
    }
    else
    {
        // 如果时间差小于2秒，则不进行更新
        // 返回false，表示没有进行更新
        return false;
    }
}

/**
 * 更新反辐射型导引头
 */
void tcESMSensor::UpdateSeeker(double t)
{
    // 如果在当前扫描周期内已经更新过，则直接返回
    if (!UpdateScan(t)) return;

    // 目标ID
    long nTargetID;
    // 目标对象指针
    std::shared_ptr<tcGameObject>ptarget = 0;
    // 是否找到目标的标志
    int bFound;

    // 根据导引头的工作模式进行不同的处理
    switch (mnMode)
    {
    case SSMODE_SEEKERACQUIRE: // 捕获模式，会穿透到跟踪模式处理
    case SSMODE_SEEKERTRACK:   // 跟踪模式
        // 获取当前跟踪的目标ID
        nTargetID = mcTrack.mnID;
        // 如果跟踪的是自己（自检测），则标记为未找到
        if (nTargetID == parent->mnID)
        {
            bFound = false;
        }
        else
        {
            // 在平台状态表中查找目标对象
            bFound = simState->maPlatformState.Lookup(nTargetID, ptarget);
        }

        // 如果找到了目标
        if (bFound)
        {  // 允许检测同联盟的目标（根据实际需求可能有所不同）
            float fRange_km; // 目标距离（千米）
            // 如果能够检测到目标
            if (CanDetectTarget(ptarget, fRange_km))
            {
                // 更新跟踪信息
                UpdateTrack(ptarget, t);
                return;
            }
        }

        // 如果在跟踪模式下丢失目标太久（例如300秒），则自毁导弹
        if ((mnMode == SSMODE_SEEKERTRACK)&&
            (t - mcTrack.mfTimestamp) > 300.0) // 暂时设置为较高的值以允许导弹继续飞行
        {
            // 导弹自毁
            parent->SelfDestruct();

            // 清空跟踪的目标ID
            mcTrack.mnID = NULL_INDEX;
#ifdef _DEBUG
            // 如果是自己的联盟，则输出调试信息
            if(simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance()))
            {
                char zBuff[128];
                _snprintf(zBuff, 128, "导弹 %d 关闭 (%s)\n", parent->mnID, parent->mzClass.c_str());
                tcMessageInterface::Get()->ConsoleMessage(zBuff);
            }
#endif
            return;
        }
        // 此处代码用于在丢失跟踪后进入搜索模式（已被注释掉）
        //pTrack->mnID = NULL_INDEX;
        //apRadarSS->mnMode = SSMODE_SEEKERSEARCH;
        break;

    case SSMODE_SEEKERSEARCH: // 搜索模式
    {
        // 获取测试区域（搜索范围）
        tcGeoRect region;
        GetTestArea(region);

        // 创建迭代器以遍历测试区域内的所有对象
        tcGameObjIterator iter(region);
        float minRange = 1e15f; // 初始化最小距离为极大值
        long minID = NULL_INDEX; // 初始化最小距离对应的目标ID为无效值

        // 查找可检测到的最近目标
        for (iter.First(); iter.NotDone(); iter.Next())
        {
            std::shared_ptr<tcGameObject>target = iter.Get();
            // 如果目标不是自己（自检测）
            if (target != parent)
            {
                float range_km; // 目标距离（千米）
                // 检测目标（此处未限制同联盟的检测，可根据实际需求调整）
                bool bDetected = CanDetectTarget(target, range_km);
                // 如果检测到目标且距离更近
                if ((bDetected) && (range_km < minRange))
                {
                    minID = target->mnID; // 更新最小距离对应的目标ID
                    minRange = range_km; // 更新最小距离
                }
            }
        }

        // 如果没有找到目标，则直接返回
        if (minID == NULL_INDEX) return;
        // 指定最近的目标为攻击目标
        parent->DesignateTarget(minID);
    }
    }
}


void tcESMSensor::UpdateSurveillance(double t)
{
    if (UpdateScanRWR(t))
    {
        UpdateSurveillanceRWR(t);
    }

    if (!UpdateScan(t)) return; // only update once per scan period

    tcGeoRect region;
    GetTestArea(region);

    tcGameObjIterator iter(region);

    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcGameObject>target = iter.Get();

		ProcessESMDetection(target, t);
    }
}

void tcESMSensor::UpdateSurveillanceRWR(double t)
{
    assert(mpDBObj->isRWR);

    rwrUpdate = true;
    rwrWarningLevel = 0;

    std::vector<long> targetersToRemove;

    size_t nTargeters = parent->targeters.size();
    for (size_t n=0; n<nTargeters; n++)
    {
        long targeterId = parent->targeters[n];
        if (std::shared_ptr<tcGameObject> target = simState->GetObject(targeterId))
        {
            float range_km = parent->RangeTo(*target);
            if (range_km < mpDBObj->mfMaxRange_km)
            {
                ProcessESMDetection(target, t);
            }
        }
        else
        {
            targetersToRemove.push_back(targeterId);
        }
    }

    for (size_t n=0; n<targetersToRemove.size(); n++)
    {
        parent->RemoveTargeter(targetersToRemove[n]);
    }

    rwrUpdate = false;
}

/**
* Update sensor track with target state. Normally used with
* missile seekers.
* This version cheats since passive sensor can't directly measure range.
*/
void tcESMSensor::UpdateTrack(std::shared_ptr<const tcGameObject> target, double t)
{
    mcTrack.mfLat_rad = (float)target->mcKin.mfLat_rad;
    mcTrack.mfLon_rad = (float)target->mcKin.mfLon_rad;

	// perturb the latitude to simulate track inaccuracy at longer range
	if (targetRange_km > 1.0f)
	{
		mcTrack.mfLat_rad += randfc(1.6e-6 * targetRange_km); // about 100 m of error at 10 km
	}

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



// 定义tcESMSensor类的ProcessESMDetection成员函数，用于处理ESM（电子支援措施）检测
void tcESMSensor::ProcessESMDetection(std::shared_ptr<tcGameObject> target, double t)
{
    // 定义一个枚举常量，表示最大发射器数量
    enum {MAX_EMITTERS=4};
    // 初始化方位角（弧度）为0
    float fAz_rad = 0;

    // 断言确保父对象存在
    assert(parent);

    // 如果父对象和目标的联盟相同，则直接返回
    if (parent->GetAlliance() == target->GetAlliance()) return;

    // 初始化检测标志为false
    bool bDetected = false;
    // 用于存储检测到的发射器数据库键的数组
    long maEmitter[MAX_EMITTERS];
    // 初始化检测到的发射器数量为0
    int nEmitters = 0;

    // 尝试将目标动态转换为tcMissileObject类型
    if (std::shared_ptr<tcMissileObject>pMissileObj = std::dynamic_pointer_cast<tcMissileObject>(target))
    {
        // 如果导弹对象搜寻雷达
        if (std::shared_ptr<tcRadar> emitter = pMissileObj->GetSeekerRadar()) // 有些空对地导弹没有传感器
        {
            // 检测是否检测到雷达
            bDetected = IsDetectedRadar(emitter, fAz_rad);
            // 如果检测到且未超过最大发射器数量
            if ((bDetected) && (nEmitters < MAX_EMITTERS))
            {
                // 记录发射器的数据库键
                maEmitter[nEmitters++] = emitter->mnDBKey;
            }
            // 如果RWR（雷达告警接收机）更新且检测到，则设置告警级别为2
            if (rwrUpdate && bDetected) rwrWarningLevel = 2;
        }
    }
    // 尝试将目标动态转换为tcPlatformObject类型（平台对象，如飞机、舰船等）
    else if (std::shared_ptr<tcPlatformObject>pPlatformObj = std::dynamic_pointer_cast<tcPlatformObject>(target))
    {
        // 如果平台对象没有辐射电磁波，则返回
        if (!pPlatformObj->GetComponent<tcSensorPlatform>()->IsRadiating()) return;

        // 获取平台对象的传感器数量
        unsigned nSensors = pPlatformObj->GetComponent<tcSensorPlatform>()->GetSensorCount();
        // 遍历所有传感器
        for (unsigned n=0; n<nSensors; n++)
        {
            // 获取当前传感器
             std::shared_ptr<const tcSensorState> sensor = pPlatformObj->GetComponent<tcSensorPlatform>()->GetSensor(n);
            // 尝试将传感器动态转换为tcRadar类型
            if ( std::shared_ptr<const tcRadar> emitter = std::dynamic_pointer_cast<const tcRadar>(sensor))
            {
                // 如果检测到雷达
                if (IsDetectedRadar(emitter, fAz_rad))
                {
                    // 设置检测标志为true
                    bDetected = true;
                    // 如果未超过最大发射器数量，记录发射器的数据库键
                    if (nEmitters < MAX_EMITTERS)
                    {
                        maEmitter[nEmitters++] = emitter->mnDBKey;
                    }
                    // 如果RWR更新且之前未设置告警级别，则设置告警级别为1
                    if (rwrUpdate && (rwrWarningLevel == 0)) rwrWarningLevel = 1;
                }
            }
            // 尝试将传感器动态转换为tcECM类型（电子对抗设备）
            else if ( std::shared_ptr<const tcECM> emitter = std::dynamic_pointer_cast<const tcECM>(sensor))
            {
                // 如果检测到ECM
                if (IsDetectedECM(emitter, fAz_rad))
                {
                    // 设置检测标志为true
                    bDetected = true;
                    // 如果未超过最大发射器数量，记录发射器的数据库键
                    if (nEmitters < MAX_EMITTERS)
                    {
                        maEmitter[nEmitters++] = emitter->mnDBKey;
                    }
                }
            }
        }
    }

    // 如果没有检测到任何发射器，则返回
    if (!bDetected) {return;}

    // 更新传感器映射信息
    UpdateSensorMap(target, maEmitter, nEmitters, fAz_rad, t);
}
/**
* 在ESM检测后调用以更新传感器地图
*/
void tcESMSensor::UpdateSensorMap(std::shared_ptr<const tcGameObject> target, long* emitters, unsigned int nEmitters,
                                  float az_rad, double t)
{
    std::shared_ptr<tcSensorMapTrack> pSMTrack = nullptr; // 初始化传感器地图跟踪指针为0

    assert(simState); // 断言模拟状态不为空
    assert(emitters); // 断言发射器数组不为空

    if (targetRange_km == 0) // 如果目标距离未设置
    {
        assert(target != 0); // 断言目标对象不为空
        // 计算并设置目标距离（考虑到目标上可能有多个发射器，目标距离可能未更新）
        targetRange_km = parent->mcKin.RangeToKmAlt(target->mcKin);
        // targetRange_km = parent->mcKin.RangeToKmAlt(target); // 上一行代码的注释版本，功能相同
    }

    // 调用更新函数以检查此报告是否已在跟踪中，或者是否有空槽可用
    tcSensorReport* report =
        simState->mcSensorMap.GetOrCreateReport(parent->mnID, mpDBObj->mnKey, target->mnID, pSMTrack, parent->GetAlliance());

    // 如果报告存在，则更新被动报告
    if (report != 0)
    {
        // 此部分代码被注释，原本用于处理新检测报告的起始时间
        //bool bNewReport = report->IsNew();
        //if (bNewReport) // 如果是新检测报告
        //{
        //    // RWR报告更快地跳到分类和范围信息
        //    report->startTime = rwrUpdate ? t - 60.0f : t;
        //}
        // 更新被动报告
        tcSensorState::UpdatePassiveReport(report, t, az_rad, targetRange_km, pSMTrack);

        double trackLife = report->GetTrackLife(); // 获取报告跟踪的生命周期

        unsigned int nClassification = target->mpDBObject->mnType; // 获取目标的分类
        bool isMissile = (nClassification & PTYPE_MISSILE) != 0; // 判断目标是否为导弹
        bool updateClassification = (isMissile || (trackLife > 30.0)); // 判断是否需要更新分类

        // TODO: 这里存在雷达和ESM更新竞争的问题
        // 需要合并更新，而不是只取第一个
        if (updateClassification) // 如果需要更新分类
        {
            report->classification = nClassification & 0xFFF0; // 更新报告的分类
            if (isMissile) // 如果是导弹
            {
                report->alliance = target->GetAlliance(); // 更新报告的联盟信息
            }

            // 此部分代码被注释，原本用于更新跟踪分类和联盟信息
            //tcAllianceInfo::Affiliation eAffil = tcAllianceInfo::UNKNOWN;
            //if (isMissile)
            //{
            //    eAffil = tcAllianceInfo::HOSTILE;
            //}
            //pSMTrack->UpdateClassification(nClassification & 0xFFF0, eAffil, NULL_INDEX);

            // 触发更新接触事件
            //tcEventManager::Get()->UpdatedContact(parent->GetAlliance(), pSMTrack);
        }
        else
        {
            report->classification = 0; // 如果不需要更新分类，则清除分类信息
        }
        // 检查是否为新检测
        bool bNewDetection = pSMTrack->IsNew();
        if (bNewDetection) // 如果是新检测
        {
            pSMTrack->UpdateTrack(0); // 更新跟踪信息

            // 触发新接触事件
            tcEventManager::Get()->NewContact(parent->GetAlliance(), pSMTrack);

            if (simState->mpUserInfo->IsOwnAlliance(parent->GetAlliance())) // 如果检测到的是己方联盟的目标
            {
                // 播放音效代码被注释
                //tcSound::Get()->PlayEffect("Ping");
            }
            // 打印检测信息的代码被注释
            //char zBuff[128];
            //sprintf(zBuff, "target %d detected with ESM at %3.1f deg at time %.1f [a:%d]",
            //    target->mnID, az_rad, t, parent->GetAlliance());
            //WTLC(zBuff);
        }

        /* 即使没有空闲报告可用，也会调用此部分代码，
        ** 以便ESM可以更新分类和发射器信息
        */

        // 更新发射器信息
        report->emitterList.clear(); // 清空发射器列表
        if (last_margin_dB >= mpDBObj->idThreshold_dB) // 如果最后检测到的边距大于数据库对象的阈值
        {
            for (unsigned int n=0; n<nEmitters; n++) // 遍历所有发射器
            {
                report->emitterList.push_back(emitters[n]); // 将发射器添加到报告中
            }
        }

    }

}


/**
 *
 */
tcESMSensor& tcESMSensor::operator=(tcESMSensor& ss) 
{
    tcSensorState::operator =(ss);

    mpDBObj = ss.mpDBObj;
    return(*this);
}
#if 0
/**
* Load state from stream
*/
tcStream& tcESMSensor::operator<<(tcStream& stream)
{
    tcSensorState::operator<<(stream);

    return stream;
}

/**
* Save state to stream
*/
tcStream& tcESMSensor::operator>>(tcStream& stream)
{
    tcSensorState::operator>>(stream);

    return stream;
}
#endif
/**
 *
 */
std::shared_ptr<tcESMSensor> tcESMSensor::Clone(void)
{
    // tcESMSensor *pNew = new tcESMSensor();
    // *pNew = *this;
    // return pNew;
    std::shared_ptr<tcESMSensor> pNew=std::make_shared<tcESMSensor>();
    *pNew = *this;
    return pNew;
}

unsigned char tcESMSensor::GetRWRWarningLevel() const
{
    return rwrWarningLevel;
}



/**
 *
 */
tcESMSensor::tcESMSensor() 
: tcSensorState()
{
    mpDBObj = NULL;
}

tcESMSensor::tcESMSensor(std::shared_ptr<tcESMDBObject> dbObj)
: tcSensorState(dbObj),
  mpDBObj(dbObj),
  lastRWRupdate(0),
  rwrWarningLevel(0)
{
	assert(dbObj);

    mfSensorHeight_m = 10.0f;
    mnMode = SSMODE_SURVEILLANCE;
    mbActive = true;
}

/**
 *
 */
tcESMSensor::~tcESMSensor() {}
