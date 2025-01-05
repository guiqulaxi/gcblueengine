/**  
**  @file tcSensorState.cpp
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

#include "tcDatabase.h"
#include "tcSensorDBObject.h"
#include "tcSensorState.h"
#include "aerror.h"
#include "tcSimState.h"
#include "tcGameObject.h"
#include "tcRadar.h"
#include "tcOpticalSensor.h"
#include "tcMissileObject.h"

#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "tcDamageModel.h"
#include "tcLOS.h"
#include "tcFloatCompressor.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

tcDatabase* tcSensorState::database = 0;
tcSimState* tcSensorState::simState = 0;
tcLOS* tcSensorState::los = 0;

long tcSensorState::nextSensorId = 1000;
float tcSensorState::errorFactor[N_ERROR_FACTOR];


void tcSensorState::AttachLOS()
{
    los = tcLOS::Get();
}

/**
* @return true if sensor is damaged
*/
bool tcSensorState::ApplyAdvancedDamage(const Damage& damage)
{
    if (IsDamaged()) return false; // already damaged;

    const database::tcDamageEffect* damageEffect = 
        database->GetDamageEffectData(mpDBObj->damageEffect);

    if (damageEffect == 0)
    {
        fprintf(stderr, "tcSensorState::ApplyAdvancedDamage -- NULL damageEffect for %s\n",
            mpDBObj->mzClass.c_str());
        assert(false);
        return false;
    }


    float blastDamage = damageEffect->GetBlastDamageFactor(damage.blast_psi);
    float waterBlastDamage = damageEffect->GetWaterBlastDamageFactor(damage.waterBlast_psi);
    float thermalDamage = damageEffect->GetRadiationDamageFactor(damage.thermal_J_cm2);

    // arbitrarily declare nFragments x 5% chance of fragment hitting this sensor
    bool fragmentHits = (randf() < 0.05*damage.fragHits); 

    float fragDamage = fragmentHits ? damageEffect->GetFragmentDamageFactor(damage.fragEnergy_J) : 0;

    blastDamage = std::min(blastDamage, 1.0f);
    waterBlastDamage = std::min(blastDamage, 1.0f);
    thermalDamage = std::min(blastDamage, 1.0f);
    fragDamage = std::min(blastDamage, 1.0f);

    float pFail = 1.0f - ((1.0f-blastDamage) * (1.0f-waterBlastDamage) * (1.0f-thermalDamage) * (1.0f-fragDamage));
    
    if (randf() < pFail)
    {
        SetDamaged(true);
        return true;
    }
    else
    {
        return false;
    }
    
}


/**
* @return error factor from -1 to 1
* Intent is that error is random but consistent if track is dropped and redetected in same location
* 根据platformId和sensorId计算误差保证误差不会乱跳
*/
float tcSensorState::GetErrorFactor(long platformId, long sensorId, float targetAz_rad)
{
    assert((platformId >= 0) && (sensorId >= 0));
    float az_factor = sinf(2*targetAz_rad);
    az_factor = az_factor*az_factor; // sin^2(2*az)


    const unsigned int indexMask = 0x0FFF; // 12 bit mask
    unsigned int idx1 = ((unsigned(platformId) << 4) + (sensorId & 0x000F)) & indexMask;
    unsigned int idx2 = (idx1 + 1) & indexMask;

    return az_factor*errorFactor[idx1] + (1.0f-az_factor)*errorFactor[idx2];
}

/**
* Needs to be called once at game initialization
* Technically this should be saved off with game state for save/load
*/
void tcSensorState::InitErrorFactor()
{
    for (unsigned int k=0; k<N_ERROR_FACTOR; k++)
    {
        errorFactor[k] = randfc(2.0f);
    }

    // check a few values in DEBUG build
    assert((errorFactor[0]>=-1.0f) && (errorFactor[0]<=1.0f));
    assert((errorFactor[1]>=-1.0f) && (errorFactor[1]<=1.0f));
    assert((errorFactor[2]>=-1.0f) && (errorFactor[2]<=1.0f));
    assert((errorFactor[N_ERROR_FACTOR-1]>=-1.0f) && (errorFactor[N_ERROR_FACTOR-1]<=1.0f));
}


/**
* Load state from stream
*/
tcUpdateStream& tcSensorState::operator<<(tcUpdateStream& stream)
{
    stream >> mbActive;
    tcIntervalCompressor intervalCompressor= tcIntervalCompressor(mfCurrentScanPeriod_s, 0.0f, 300.0f);
    stream >>intervalCompressor;  // need for antenna animation
    
    //mcTrack << stream;

    //stream >> mnDBKey; 
    //stream >> mfLastScan;
    //stream >> mnMode;
	//stream >> fireControlId;
    //stream >> fireControlIdx;
    //stream >> mountAz_rad;
    //stream >> mfSensorHeight_m;

    return stream;
}

/**
* Save state to stream
*/
tcUpdateStream& tcSensorState::operator>>(tcUpdateStream& stream)
{
    stream << mbActive;

    stream << tcIntervalCompressor(mfCurrentScanPeriod_s, 0.0f, 300.0f);
    
    //mcTrack >> stream;

    //stream << mnDBKey; 
    //stream << mfLastScan;
    //stream << mnMode;
	//stream << fireControlId;
    //stream << fireControlIdx;
    //stream << mountAz_rad;
    //stream << mfSensorHeight_m;

    return stream;
}

/**
* Loads state from stream
*/
tcGameStream& tcSensorState::operator<<(tcGameStream& stream)
{
    stream >> mbActive;

    std::string databaseClass;
    stream >> databaseClass;
    mnDBKey = database->GetKey(databaseClass.c_str());

    stream >> mfLastScan;
    stream >> mfCurrentScanPeriod_s;
    stream >> mnMode;
    mcTrack << stream;
    stream >> mfSensorHeight_m;
    stream >> isHidden; ///< hidden sensors are not displayed in object control view
    stream >> isDamaged;
    stream >> fireControlId; ///< id of platform with fire control sensor (semi-active illuminator, or command guidance sensor)
    stream >> fireControlIdx; ///< sensor index of fire control sensor platform
    stream >> lastCounterMeasureTime;
    stream >> isCommandReceiver;

    return stream;
}

/**
* Saves state to stream
*/
tcGameStream& tcSensorState::operator>>(tcGameStream& stream)
{
    stream << mbActive;

    std::string databaseClass = database->GetObjectClassName(mnDBKey);
    stream << databaseClass;

    stream << mfLastScan;
    stream << mfCurrentScanPeriod_s;
    stream << mnMode;
    mcTrack >> stream;
    stream << mfSensorHeight_m;
    stream << isHidden; ///< hidden sensors are not displayed in object control view
    stream << isDamaged;
    stream << fireControlId; ///< id of platform with fire control sensor (semi-active illuminator, or command guidance sensor)
    stream << fireControlIdx; ///< sensor index of fire control sensor platform
    stream << lastCounterMeasureTime;
    stream << isCommandReceiver;

    return stream;
}

void tcSensorState::CalculateLonLatCovariance(float az_rad, float lat_rad, float sigmaCrossRange_m, float sigmaDownRange_m,
        float& C11, float& C22, float& C12)
{
    float lat_factor = 1.0 / cosf(lat_rad);
    float cos_az = cosf(az_rad);
    float sin_az = sinf(az_rad);
    float cos2_az = cos_az * cos_az;
    float sin2_az = sin_az * sin_az;

    float sigmaCrossRange_rad = C_MTORAD * sigmaCrossRange_m;
    float sigmaDownRange_rad = C_MTORAD * sigmaDownRange_m;
    float varCross = sigmaCrossRange_rad * sigmaCrossRange_rad;
    float varDown = sigmaDownRange_rad * sigmaDownRange_rad;

    C11 = (varCross*cos2_az + varDown*sin2_az) * lat_factor * lat_factor;
    C22 = (varCross*sin2_az + varDown*cos2_az);
    C12 = (varDown - varCross) * cos_az * sin_az * lat_factor;

#ifdef _DEBUG
    double det = (C11*C22) - (C12*C12);
    assert(det > -1e-30);
#endif
}


bool tcSensorState::CanDetectTarget(std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom)
{
	assert(false); // derived class method should always be called
	return false;
}


/**
* @param alt_m 目标高度，单位为米
* @return 如果无法估计高度（太远或精度不足以达到至少±500米的范围），则返回false
*/
bool tcSensorState::GetAltitudeEstimate(float& altitudeEstimate_m, float& altitudeVariance, float range_km, float az_rad, float alt_m)
{
    // 如果仰角误差小于5度
    if (mpDBObj->elevationError_deg < 5.0f)
    {
        // 计算考虑误差因子后的仰角误差，误差因子根据传感器ID、数据库键和方位角计算
        float elError = mpDBObj->elevationError_rad *
                        tcSensorState::GetErrorFactor(parent->mnID + 50, mpDBObj->mnKey, az_rad);

        // 将距离从公里转换为米
        float range_m = 1000.0f * range_km;

        // 计算目标相对于传感器当前高度的仰角（弧度）
        float el_rad = atanf((alt_m - parent->mcKin.mfAlt_m) / range_m);

        // 计算估计的仰角，加上误差
        float elEstimate_rad = el_rad + elError;

        // 根据估计的仰角和距离计算估计的高度
        altitudeEstimate_m = parent->mcKin.mfAlt_m + range_m * tanf(elEstimate_rad);
        // 如果计算得到的高度估计值为负，则进行无操作（这里可能是为了调试，实际使用中应去除）
        if(altitudeEstimate_m<0)
        {
            int a=0;
        }
        // 计算高度估计的方差，考虑了仰角误差和距离
        altitudeVariance = mpDBObj->elevationError_rad * range_m;
        // 使用常数C_U2GVAR对方差进行缩放
        altitudeVariance = C_U2GVAR * altitudeVariance * altitudeVariance;

        // 如果计算成功，返回true
        return true;
    }
    else
    {
        // 如果仰角误差太大，则设置高度估计为0，方差为一个很大的值（表示不确定性很大）
        altitudeEstimate_m = 0;
        altitudeVariance = 4e6f;

        // 返回false，表示无法进行有效的高度估计
        return false;
    }
}

/**
* @return platform id that is fire control parent for this sensor, -1 for none
*/
long tcSensorState::GetFireControlPlatform() const
{
    return fireControlId;
}

/**
* @return fire control sensor as a radar or 0 if not a radar or does not exist
*/
std::shared_ptr<tcRadar> tcSensorState::GetFireControlRadar()
{
	std::shared_ptr<tcSensorState> sensor = GetFireControlSensor();
    std::shared_ptr<tcRadar> radar = std::dynamic_pointer_cast<tcRadar>(sensor);
    return radar;
}

std::shared_ptr<tcOpticalSensor> tcSensorState::GetLaserDesignator()
{
    std::shared_ptr<tcSensorState> sensor = GetFireControlSensor();
    return std::dynamic_pointer_cast<tcOpticalSensor>(sensor);
}

/**
* @return fire control sensor or 0 if not a radar or does not exist
*/
std::shared_ptr<tcSensorState> tcSensorState::GetFireControlSensor()
{
    assert(simState);

    std::shared_ptr<tcPlatformObject>platform = 
        std::dynamic_pointer_cast<tcPlatformObject>(simState->GetObject(fireControlId));

    if (platform == 0) return 0; // platform doesn't exist

    return platform->GetComponent<tcSensorPlatform>()->GetSensorMutable(fireControlIdx);
}

/**
 *获得最大的探测范围区域
 */
void tcSensorState::GetTestArea(tcRect& region) 
{
    assert(mpDBObj);
    assert(parent);
    //if (mpDBObj==NULL) {return;}
    float fRangeX_rad, fRangeY_rad; 
    fRangeY_rad = C_KMTORAD*mpDBObj->mfMaxRange_km;
    fRangeX_rad = fRangeY_rad/cosf(parent->mcKin.mfLat_rad);

    region.left = parent->mcKin.mfLon_rad - fRangeX_rad;
    region.right = parent->mcKin.mfLon_rad + fRangeX_rad;
    region.bottom = parent->mcKin.mfLat_rad - fRangeY_rad;
    region.top = parent->mcKin.mfLat_rad + fRangeY_rad;
}

/**
* @return true if track is valid
*/
bool tcSensorState::GetTrack(tcTrack& track_)
{
	track_ = mcTrack;

	return (mbActive != 0) && (mnMode == SSMODE_SEEKERTRACK);
}

/**
* @return true if this sensor has a fire control sensor
*/
bool tcSensorState::HasFireControlSensor() const
{
	return fireControlId != -1;
}


unsigned tcSensorState::GetFireControlTrackCount() const
{
    assert(false);
    return 0;
}

unsigned tcSensorState::GetMaxFireControlTracks() const
{
    assert(false);
    return 0;
}

bool tcSensorState::IsTrackAvailable()
{
    assert(false);
    return false;
}

bool tcSensorState::RequestTrack(long targetId)
{
    assert(false);
    return false;
}

bool tcSensorState::ReleaseTrack(long targetId)
{
    assert(false);
    return false;
}

/**
* tcRadar overrides this, otherwise not a radar so return false
*/
bool tcSensorState::IsTrackingWithRadar(long targetId) const
{
	return false;
}

/**
* Sets command state of sensor
* @param state true to use command track from "illuminator" platform, false to use seeker
*/
void tcSensorState::SetCommandReceiver(bool state)
{
    isCommandReceiver = state;
}

bool tcSensorState::IsCommandReceiver() const
{
    return isCommandReceiver;
}

/**
* @return true if sensor has line of sight to target
*/
bool tcSensorState::HasLOS(std::shared_ptr<const tcGameObject> target)
{
    assert(parent != 0);
    assert(target != 0);
    
    long key = 0;
    GeoPoint p1;
    GeoPoint p2;

    if (parent->mnID > target->mnID)
    {
        key = ((parent->mnID & 0x00FF) << 16) + (target->mnID & 0x00FF);
        p1.Set(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m);
        p2.Set(target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfAlt_m);
    }
    else
    {
        key = ((target->mnID & 0x00FF) << 16) + (parent->mnID & 0x00FF);
        p1.Set(target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfAlt_m);
        p2.Set(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m);
    }

    return los->HasLOS(key, mfLastScan, p1, p2);
}


/**
* @return false if key not found in database
*/
bool tcSensorState::InitFromDatabase(long key)
{
	assert(database);

    mpDBObj =  std::dynamic_pointer_cast<tcSensorDBObject>(database->GetObject(key));
    if (mpDBObj == NULL) 
    {
        fprintf(stderr, "Error - tcSensorState::InitFromDatabase - Not found in db or bad class for key\n");
        return false;
    }
    mnDBKey = key;
    mbActive = false;
	isHidden = false;
    mfLastScan = randf(mpDBObj->mfScanPeriod_s);
    mfCurrentScanPeriod_s = mpDBObj->mfScanPeriod_s;
    mfSensorHeight_m = 0;
    mountAz_rad = 0;
    return true;
}

bool tcSensorState::IsActive() const 
{
	return mbActive != 0;
}

bool tcSensorState::IsDamaged() const
{
    return isDamaged;
}

bool tcSensorState::IsHidden() const
{
    return isHidden;
}

bool tcSensorState::IsECM() const
{
	return false;
}

/**
* Alternative to dynamic_cast
*/
bool tcSensorState::IsESM() const
{
    return false;
}

/**
* Alternative to dynamic_cast
*/
bool tcSensorState::IsRadar() const
{
    return false;
}

/**
* Alternative to dynamic_cast
*/
bool tcSensorState::IsSonar() const
{
    return false;
}

/**
* Alternative to dynamic_cast
*/
bool tcSensorState::IsOptical() const
{
    return false;
}

/**
*通过与信噪比（SNR）裕量相关的随机性来增加检测的不确定性
*检测概率（Pd）在硬编码窗口内线性变化，在0 dB裕量时Pd为0.5
*@return 如果检测到，则返回true；否则返回false
*/
bool tcSensorState::RandomDetect(float margin_dB)
{
    // 定义SNR的窗口大小，用于调整检测概率（Pd）的线性变化范围
    const float snr_window_dB = 3.0f;

    // 定义Pd随SNR margin变化的斜率，用于计算在不同margin下的Pd值
    // 注意：这里的斜率是根据Pd = 0.5 at 0 dB margin 和 window 大小为 3 dB 计算的，
    // 使得在 margin_dB = -3 dB 时 Pd = 0, 在 margin_dB = 3 dB 时 Pd = 1（但实际情况受限于随机数生成）
    const float pd_scale = 0.1666f; // 等于 1 / (2 * snr_window_dB)，用于将margin_dB映射到0到1之间的Pd值

    // 如果SNR margin小于-snr_window_dB，则检测概率太低，直接返回未检测到
    if (margin_dB < -snr_window_dB)
    {
        return false;
    }

    // 如果SNR margin大于或等于snr_window_dB，则检测概率足够高，直接返回检测到
    else if (margin_dB >= snr_window_dB)
    {
        return true;
    }

    // 对于SNR margin在-snr_window_dB和snr_window_dB之间的情况，
    // 使用随机数来模拟检测的不确定性
    // 使用pd_scale将margin_dB映射到一个0到1之间的Pd值，并与随机数比较
    // 如果随机数小于或等于计算出的Pd值，则认为检测到目标
    else
    {
        // 假设randf()是一个返回0到1之间浮点数的随机数生成函数
        // 注意：这里假设randf()是存在的，实际中可能需要使用其他方式生成随机数，如std::uniform_real_distribution
        return ( randf() <= (pd_scale * (margin_dB + snr_window_dB)) );
    }
}

/**
 *
 */
void tcSensorState::Serialize(tcFile& file, bool mbLoad) 
{
    if (mbLoad) 
    {
        file.Read(&mbActive,sizeof(mbActive));
        file.Read(&mcTrack,sizeof(mcTrack));
        file.Read(&mfCurrentScanPeriod_s,sizeof(mfCurrentScanPeriod_s));
        file.Read(&mfLastScan,sizeof(mfLastScan));
        file.Read(&mountAz_rad,sizeof(mountAz_rad));
        file.Read(&mfSensorHeight_m,sizeof(mfSensorHeight_m));
        file.Read(&mnMode,sizeof(mnMode));
        file.Read(&isHidden,sizeof(isHidden));
    }
    else 
    {
        file.Write(&mbActive,sizeof(mbActive));
        file.Write(&mcTrack,sizeof(mcTrack));
        file.Write(&mfCurrentScanPeriod_s,sizeof(mfCurrentScanPeriod_s));
        file.Write(&mfLastScan,sizeof(mfLastScan));
        file.Write(&mountAz_rad,sizeof(mountAz_rad));
        file.Write(&mfSensorHeight_m,sizeof(mfSensorHeight_m));
        file.Write(&mnMode,sizeof(mnMode));
        file.Write(&isHidden,sizeof(isHidden));
    }
}

/**
* Activate or deactivate sensor. If activated mfLastScan is
* set to current time to give one scan delay for new detections
*/
void tcSensorState::SetActive(bool active)
{
    if (mbActive == (int)active) return;
    if (active)
    {
        mfLastScan = simState->GetTime();
    }
    mbActive = active;
}

void tcSensorState::SetDamaged(bool state)
{
    isDamaged = state;
}

/**
* Sets the info to indentify the fire contorl sensor used by this sensor.
* If this method is not called, no fire control sensor is used.
*/
void tcSensorState::SetFireControlSensor(long id, unsigned char idx)
{
	fireControlId = id;
	fireControlIdx = idx;
}

/**
* @param az azimuth of center of coverage in radians, 0 points forward
*/
void tcSensorState::SetMountAz(float az) 
{
	mountAz_rad = az;
}

void tcSensorState::SetParent(std::shared_ptr<tcGameObject> obj)
{
	parent = obj;
    // sensorPlatform = std::dynamic_pointer_cast<tcSensorPlatform>(obj);

    if (std::shared_ptr<tcMissileObject> missile =  std::dynamic_pointer_cast<tcMissileObject>(obj))
    {
        assert(missile->mpDBObject != 0);
        SetCommandReceiver(missile->mpDBObject->IsCommandLaunched());
    }
}


void tcSensorState::Update(double t)
{
}

/**
* 更新活动报告中的纬度、经度、高度和协方差
* @param report 指向tcSensorReport的指针，表示要更新的报告
* @param t 当前时间戳
* @param az_rad 目标相对于传感器的真实方位角（弧度）
* @param range_km 目标相对于传感器的真实距离（千米）
* @param alt_m 目标的真实高度（米）
* @param track 指向tcSensorMapTrack的指针，表示目标的跟踪信息
*/
void tcSensorState::UpdateActiveReport(tcSensorReport* report, double t, float az_rad, float range_km, float alt_m,
                                       std::shared_ptr<const tcSensorMapTrack> track)
{
    // 检查报告是否为新报告
    bool newReport = report->IsNew();
    if (newReport)
    {
        report->startTime = t; // 设置报告的起始时间
    }
    report->timeStamp = t; // 更新报告的时间戳

    report->validFlags = tcSensorReport::LONLAT_VALID; // 标记经纬度有效

    // 计算（斜距）距离估计
    float rangeError_km = 0.001f * mpDBObj->rangeError *
                          tcSensorState::GetErrorFactor(parent->mnID + 100, mpDBObj->mnKey, az_rad); // 计算距离误差
    float rangeEstimate_km = range_km + rangeError_km; // 计算距离估计

    // 高度估计
    float altEst_m = 0; // 高度估计值
    float altVar = 0; // 高度估计的方差
    bool surfaceAltitude = (alt_m == 0) || (track->IsSurface() || track->IsGround()); // 检查是否为水面或地面目标
    bool subsurface = (track->mnClassification & PTYPE_SUBSURFACE) != 0; // 检查是否为水下目标

    // 如果不是水面或地面目标，并且能获取高度估计
    if (!surfaceAltitude && GetAltitudeEstimate(report->altEstimate_m, report->altVariance, rangeEstimate_km, az_rad, alt_m))
    {
        report->validFlags |= tcSensorReport::ALT_VALID; // 标记高度有效
        altEst_m = report->altEstimate_m; // 更新高度估计值
        altVar = report->altVariance; // 更新高度估计的方差
        if (!subsurface)
        {
            altEst_m = std::max(altEst_m, 1.0f); // 对于非水下目标，高度不低于地面
        }
        else
        {
            altEst_m = std::min(altEst_m, 0.0f); // 对于水下目标，高度不高于水面
        }
    }
    // 如果跟踪信息中高度有效
    else if (track->IsAltitudeValid())
    {
        altEst_m = track->mfAlt_m; // 使用跟踪信息中的高度
        altVar = 10000.0f; // 高度方差设为100米（1-sigma），实际应使用跟踪信息中的方差
    }
    // 如果目标是空中或导弹
    else if (track->IsAir() || track->IsMissile())
    {
        altEst_m = parent->mcKin.mfAlt_m; // 使用传感器自身的高度
        altVar = 1000000.0f; // 高度方差设为较大值
    }

    // 地面距离估计
    float altDiff_km = 0.001f * (altEst_m - parent->mcKin.mfAlt_m); // 高度差（千米）
    float groundRange_km = 0; // 地面距离估计值
    if ((altDiff_km > -rangeEstimate_km) && (altDiff_km < rangeEstimate_km))
    {
        groundRange_km = sqrtf(rangeEstimate_km*rangeEstimate_km - altDiff_km*altDiff_km); // 使用勾股定理计算地面距离
    }
    else
    {
        groundRange_km = 0; // 如果高度差超出范围，则地面距离为0
    }
    float sigmaGroundRange_m = sqrtf(altVar) * altDiff_km / range_km; // 由于高度误差导致的地面距离误差

#ifdef _DEBUG
    std::shared_ptr<const tcGameObject> target = track->GetAssociatedConst(); // 获取目标对象
    float trueSlantRange_km = target->mcKin.RangeToKmAlt(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m); // 计算真实斜距
    float trueGroundRange_km = target->RangeTo(*parent); // 计算真实地面距离
#endif

    // 添加方位角和距离误差
    float azError = mpDBObj->angleError_rad *
                    tcSensorState::GetErrorFactor(parent->mnID, mpDBObj->mnKey, az_rad); // 计算方位角误差

    float azEstimate_rad = az_rad + azError; // 计算方位角估计值

    float dist_rad = C_KMTORAD * groundRange_km; // 将地面距离转换为弧度
    report->latEstimate_rad = parent->mcKin.mfLat_rad + dist_rad*cosf(azEstimate_rad); // 计算纬度估计值
    float latAvg_rad = 0.5f*(parent->mcKin.mfLat_rad + report->latEstimate_rad); // 计算平均纬度
    report->lonEstimate_rad = parent->mcKin.mfLon_rad + dist_rad*sinf(azEstimate_rad) / cosf(latAvg_rad); // 计算经度估计值

    // 计算位置估计的协方差
    float sigmaDownRange_m = sqrtf((mpDBObj->rangeError*mpDBObj->rangeError) + (sigmaGroundRange_m*sigmaGroundRange_m)); // 纵向误差
    float sigmaCrossRange_m = 1000.0f * rangeEstimate_km * mpDBObj->angleError_rad; // 横向误差

    CalculateLonLatCovariance(azEstimate_rad, report->latEstimate_rad, sigmaCrossRange_m, sigmaDownRange_m,
                              report->C11, report->C22, report->C12); // 计算经纬度协方差

    // 如果目标是潜艇且速度有效，则进行断言检查
    if (track->IsSub() && ((report->validFlags & tcSensorReport::SPEED_VALID) != 0))
    {
        assert(fabsf(report->speedEstimate_mps) < 20.0f); // 断言速度估计值在合理范围内
    }
    // 断言检查纬度和经度估计值不是NaN
    assert(!_isnan(report->latEstimate_rad));
    assert(!_isnan(report->lonEstimate_rad));
}



// 更新被动报告的函数
void tcSensorState::UpdatePassiveReport(tcSensorReport* report, double t, float az_rad, float range_km,
                                        std::shared_ptr<const tcSensorMapTrack> track)
{
    // 检查报告是否是新生成的
    bool newReport = report->IsNew();
    if (newReport)
    {
        // 如果是新报告，则设置开始时间为当前时间
        report->startTime = t;
    }
    // 更新报告的时间戳
    report->timeStamp = t;

    // 计算方位角的误差
    float azError = mpDBObj->angleError_rad *
                    tcSensorState::GetErrorFactor(parent->mnID, mpDBObj->mnKey, az_rad);
    // 计算带误差的方位角估计值
    float azEstimate_rad = az_rad + azError;

    // 初始化有效距离误差
    float effectiveRangeError = mpDBObj->rangeError; // 带有近距离修正的距离误差
    float rangeEstimate_km = range_km; // 原始距离估计值
    float rangeError_km = 0; // 距离误差

    // 解释距离误差为真实距离的一个分数误差
    if ((mpDBObj->rangeError > 0) && (mpDBObj->rangeError <= 0.5))
    {
        // 如果传感器是ESM类型且在近距离内，则减小距离误差
        std::shared_ptr<tcESMSensor> esm = std::dynamic_pointer_cast<tcESMSensor>(shared_from_this());
        if ((esm != 0) && (range_km < 3.0))
        {
            effectiveRangeError = 0.5f*mpDBObj->rangeError;
        }

        // 这里原本有计算距离尺度误差的代码，现在被注释掉了
        // +100 to get an independent error
        // scale factor error is range_error^([-1,1])
        //rangeScaleError = powf(1.0f - effectiveRangeError,
        //    tcSensorState::GetErrorFactor(parent->mnID + 100, mpDBObj->mnKey, az_rad));
        //rangeEstimate_km = rangeScaleError*range_km;
        // 计算距离误差
        rangeError_km = range_km * effectiveRangeError;
        // 计算随机距离误差
        float randomError_km = rangeError_km * tcSensorState::GetErrorFactor(parent->mnID + 100, mpDBObj->mnKey, az_rad);
        // 计算带随机误差的距离估计值
        rangeEstimate_km = range_km + randomError_km;
    }
    else // "仅方位"的情况
    {
        // 假设距离误差大于0.5且小于等于1.0
        assert((mpDBObj->rangeError > 0.5f) && (mpDBObj->rangeError <= 1.0f));
        // 计算最大可能的距离误差
        float maxRangeError_km = range_km * (4.0f + randf(4.0f));
        // 限制距离估计值不超过200公里
        rangeEstimate_km = std::min(200.0f, maxRangeError_km);

        // 如果存在多个贡献者，则使用tcSensorMapTrack的距离来提高精度
        if ((track != 0) && (track->GetContributorCount() > 1))
        {
            rangeEstimate_km = parent->mcKin.RangeToKm(*track);
        }

        // 在这种情况下，距离误差等于距离估计值
        rangeError_km = rangeEstimate_km;
    }

    // 使用估计的距离和方位角来计算地理坐标
    GeoPoint p(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, 0);
    p.Offset(rangeEstimate_km, azEstimate_rad);

    // 更新报告的经纬度估计值
    report->lonEstimate_rad = (float)p.mfLon_rad;
    report->latEstimate_rad = (float)p.mfLat_rad;

    // 计算沿距离方向和跨距离方向的标准差
    float sigmaDownRange_m = 1000.0f * C_U2GSIG * rangeError_km; // 向下距离的标准差
    float sigmaCrossRange_m = 1000.0f * C_U2GSIG * rangeEstimate_km * mpDBObj->angleError_rad; // 跨距离的标准差

    // 计算经纬度协方差
    CalculateLonLatCovariance(azEstimate_rad, report->latEstimate_rad, sigmaCrossRange_m, sigmaDownRange_m,
                              report->C11, report->C22, report->C12);

    // 标记报告的经纬度为有效
    report->validFlags = tcSensorReport::LONLAT_VALID;
}// 函数结束
/**
 *
 *
 * @return non-zero if new scan should be processed, otherwise zero
 */
int tcSensorState::UpdateScan(double afTime) 
{
    assert(mpDBObj);

    if (isDamaged) mbActive = false;

    if (!mbActive) return 0;

    if ((afTime - mfLastScan) >= mfCurrentScanPeriod_s) 
    {
        mfLastScan = afTime;
        return 1;
    }
    else 
    {
        return 0;
    }
}

/**
 *
 */
tcSensorState& tcSensorState::operator=(const tcSensorState &ss)
{
    assert(false); // is this method used?

    mbActive = ss.mbActive;
	isHidden = ss.isHidden;
    mcTrack = ss.mcTrack;
    mfCurrentScanPeriod_s = ss.mfCurrentScanPeriod_s; 
    mfLastScan = ss.mfLastScan;
    mountAz_rad = ss.mountAz_rad;
    mfSensorHeight_m = ss.mfSensorHeight_m;
    mnDBKey = ss.mnDBKey;
    mnMode = ss.mnMode;
    mpDBObj = ss.mpDBObj;
    parent = 0;
    // sensorPlatform = 0;
	fireControlId = ss.fireControlId;
	fireControlIdx = ss.fireControlIdx;
    lastCounterMeasureTime = ss.lastCounterMeasureTime;
    isCommandReceiver = ss.isCommandReceiver;

    return(*this);
}

/**
 *
 */
std::shared_ptr<tcSensorState> tcSensorState::Clone() const
{
    assert(false); // is this method used?

    // TODO: should use a copy constructor (if this method is used)
    std::shared_ptr<tcSensorState>pNew = std::make_shared<tcSensorState>();
    *pNew = *this;
    return pNew;
}

/**
 * Used to initialize tcSimState::mcDefaultRadar for detect before
 * create seeker test.
 */
tcSensorState::tcSensorState() :
    mbActive(false),
    parent(0),
    mnDBKey(-1),
    mpDBObj(0),
    mfLastScan(0),
    mfCurrentScanPeriod_s(30.0f),
    mnMode(0),
    isHidden(false),
    isDamaged(false),
    // sensorPlatform(0),
	fireControlId(-1),
	fireControlIdx(0),
    sensorId(nextSensorId++),
    lastCounterMeasureTime(0),
    isCommandReceiver(false)
{
    mcTrack.mnID = NULL_INDEX;

	if (database == 0)
	{
		database = tcDatabase::Get();
	}
}

tcSensorState::tcSensorState(std::shared_ptr<tcSensorDBObject> dbObj)
: mpDBObj(dbObj),
  	mnDBKey(dbObj->mnKey),
    mbActive(false),
    mnMode(0), 
    mfCurrentScanPeriod_s(mpDBObj->mfScanPeriod_s),
    mfSensorHeight_m(0),
    mountAz_rad(0),
    isDamaged(false),
	isHidden(false),
	fireControlId(-1),
	fireControlIdx(0),
    lastCounterMeasureTime(0),
    isCommandReceiver(false),
	parent(0),
    // sensorPlatform(0),
    sensorId(nextSensorId++)
{
	assert(dbObj);

    mfLastScan = randf(mpDBObj->mfScanPeriod_s);

    mcTrack.mnID = NULL_INDEX;

	if (database == NULL)
	{
		database = tcDatabase::Get();
	}
}

/**
 *
 */
tcSensorState::~tcSensorState()
{
    // release fire control track
    if ((!simState->IsMultiplayerClient()) && (fireControlId != -1))
    {
        if (std::shared_ptr<tcSensorState>illuminator = GetFireControlSensor())
        {
            illuminator->ReleaseTrack(mcTrack.mnID);
        }
    }
}


