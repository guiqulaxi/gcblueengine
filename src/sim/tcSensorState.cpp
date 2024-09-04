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


bool tcSensorState::CanDetectTarget(const tcGameObject* target, float& range_km, bool useRandom)
{
	assert(false); // derived class method should always be called
	return false;
}


/**
* @param alt_m target altitude in meters
* @return false if no alt estimate can be made, too far or not enough el accuracy for at least +/-500 m
*/
bool tcSensorState::GetAltitudeEstimate(float& altitudeEstimate_m, float& altitudeVariance, float range_km, float az_rad, float alt_m)
{
    if (mpDBObj->elevationError_deg < 5.0f)
    {
        float elError = mpDBObj->elevationError_rad *
            tcSensorState::GetErrorFactor(parent->mnID + 50, mpDBObj->mnKey, az_rad);

        float range_m = 1000.0f * range_km;
        float el_rad = atanf((alt_m - parent->mcKin.mfAlt_m) / range_m);
        float elEstimate_rad = el_rad + elError;

        altitudeEstimate_m = parent->mcKin.mfAlt_m + range_m * tanf(elEstimate_rad);
        altitudeVariance = mpDBObj->elevationError_rad * range_m;
        altitudeVariance = C_U2GVAR * altitudeVariance * altitudeVariance;

        return true;
    }
    else
    {
        altitudeEstimate_m = 0;
        altitudeVariance = 4e6f;

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
tcRadar* tcSensorState::GetFireControlRadar()
{
	tcSensorState* sensor = GetFireControlSensor();
    tcRadar* radar = dynamic_cast<tcRadar*>(sensor);
    return radar;
}

tcOpticalSensor* tcSensorState::GetLaserDesignator()
{
    tcSensorState* sensor = GetFireControlSensor();
    return dynamic_cast<tcOpticalSensor*>(sensor);
}

/**
* @return fire control sensor or 0 if not a radar or does not exist
*/
tcSensorState* tcSensorState::GetFireControlSensor()
{
    assert(simState);

    tcPlatformObject *platform = 
        dynamic_cast<tcPlatformObject*>(simState->GetObject(fireControlId));

    if (platform == 0) return 0; // platform doesn't exist

    return platform->GetSensorMutable(fireControlIdx);
}

/**
 *
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
bool tcSensorState::HasLOS(const tcGameObject* target)
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

    mpDBObj = dynamic_cast<tcSensorDBObject*>(database->GetObject(key));
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
* Adds randomness to detection with Pd that varies with SNR margin
* Pd varies linearly over hard-coded window, with Pd = 0.5 at 0 dB margin
* @return true if detected, false otherwise
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

void tcSensorState::SetParent(tcGameObject* obj) 
{
	parent = obj;
	sensorPlatform = dynamic_cast<tcSensorPlatform*>(obj);

    if (tcMissileObject* missile = dynamic_cast<tcMissileObject*>(obj))
    {
        assert(missile->mpDBObject != 0);
        SetCommandReceiver(missile->mpDBObject->IsCommandLaunched());
    }
}


void tcSensorState::Update(double t)
{
}

/**
* Updates lat, lon, altitude, and covariance for active report
* @param az_rad true bearing to target
* @param range_km true range to target
* @param alt_m true altitude of target
*/
void tcSensorState::UpdateActiveReport(tcSensorReport* report, double t, float az_rad, float range_km, float alt_m, 
                                       const tcSensorMapTrack* track)
{
    bool newReport = report->IsNew();
    if (newReport) 
    {
        report->startTime = t;
    }
    report->timeStamp = t;

    report->validFlags = tcSensorReport::LONLAT_VALID;

    // (slant) range estimate
    float rangeError_km = 0.001f * mpDBObj->rangeError * 
            tcSensorState::GetErrorFactor(parent->mnID + 100, mpDBObj->mnKey, az_rad);
    float rangeEstimate_km = range_km + rangeError_km;

    // altitude estimate
    // don't bother checking altitude for surface ships and ground targets
    float altEst_m = 0;
    float altVar = 0;
    bool surfaceAltitude = (alt_m == 0) || (track->IsSurface() || track->IsGround());
    bool subsurface = (track->mnClassification & PTYPE_SUBSURFACE) != 0;

    if (!surfaceAltitude && GetAltitudeEstimate(report->altEstimate_m, report->altVariance, rangeEstimate_km, az_rad, alt_m))
    {
        report->validFlags |= tcSensorReport::ALT_VALID;
        altEst_m = report->altEstimate_m;
        altVar = report->altVariance;
        if (!subsurface)
        {
            altEst_m = std::max(altEst_m, 1.0f); // don't allow altitudes at or below surface
        }
        else
        {
            altEst_m = std::min(altEst_m, 0.0f); // don't allow altitudes above surface
        }
    }
    else if (track->IsAltitudeValid())
    {
        altEst_m = track->mfAlt_m;
        altVar = 10000.0f; // 100 m 1-sigma, really should have var in track data
    }
    else if (track->IsAir() || track->IsMissile())
    {
        altEst_m = parent->mcKin.mfAlt_m;
        altVar = 1000000.0f;
    }

    // ground range estimate
    float altDiff_km = 0.001f * (altEst_m - parent->mcKin.mfAlt_m);
    float groundRange_km = 0;
    if ((altDiff_km > -rangeEstimate_km) && (altDiff_km < rangeEstimate_km))
    {
        groundRange_km = sqrtf(rangeEstimate_km*rangeEstimate_km - altDiff_km*altDiff_km);
    }
    else
    {
        groundRange_km = 0;
    }
    float sigmaGroundRange_m = sqrtf(altVar) * altDiff_km / range_km; // due to altitude errors

#ifdef _DEBUG
    const tcGameObject* target = track->GetAssociatedConst();
    float trueSlantRange_km = target->mcKin.RangeToKmAlt(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m);
    float trueGroundRange_km = target->RangeTo(*parent);
#endif

    // add az and range error
    float azError = mpDBObj->angleError_rad *
        tcSensorState::GetErrorFactor(parent->mnID, mpDBObj->mnKey, az_rad);

    float azEstimate_rad = az_rad + azError;
    
    float dist_rad = C_KMTORAD * groundRange_km;
    report->latEstimate_rad = parent->mcKin.mfLat_rad + dist_rad*cosf(azEstimate_rad);
    float latAvg_rad = 0.5f*(parent->mcKin.mfLat_rad + report->latEstimate_rad);
    report->lonEstimate_rad = parent->mcKin.mfLon_rad + dist_rad*sinf(azEstimate_rad) / cosf(latAvg_rad);


    float sigmaDownRange_m = sqrtf((mpDBObj->rangeError*mpDBObj->rangeError) + (sigmaGroundRange_m*sigmaGroundRange_m));
    float sigmaCrossRange_m = 1000.0f * rangeEstimate_km * mpDBObj->angleError_rad;

    CalculateLonLatCovariance(azEstimate_rad, report->latEstimate_rad, sigmaCrossRange_m, sigmaDownRange_m,
        report->C11, report->C22, report->C12);

    if (track->IsSub() && ((report->validFlags & tcSensorReport::SPEED_VALID) != 0))
    {
        assert(fabsf(report->speedEstimate_mps) < 20.0f);
    }
    assert(!_isnan(report->latEstimate_rad));
    assert(!_isnan(report->lonEstimate_rad));
}



// 更新被动报告的函数
void tcSensorState::UpdatePassiveReport(tcSensorReport* report, double t, float az_rad, float range_km,
                                        const tcSensorMapTrack* track)
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
        tcESMSensor* esm = dynamic_cast<tcESMSensor*>(this);
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
tcSensorState& tcSensorState::operator=(tcSensorState& ss) 
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
	sensorPlatform = 0;
	fireControlId = ss.fireControlId;
	fireControlIdx = ss.fireControlIdx;
    lastCounterMeasureTime = ss.lastCounterMeasureTime;
    isCommandReceiver = ss.isCommandReceiver;

    return(*this);
}

/**
 *
 */
tcSensorState* tcSensorState::Clone() const
{
    assert(false); // is this method used?

    // TODO: should use a copy constructor (if this method is used)
    tcSensorState *pNew = new tcSensorState(*this); 
    return pNew;
}

/**
 * Used to initialize tcSimState::mcDefaultRadar for detect before
 * create seeker test.
 */
tcSensorState::tcSensorState() :
    mbActive(false),
    isDamaged(false),
	isHidden(false),
    mnMode(0), 
    mpDBObj(0),
    mnDBKey(-1),
    mfLastScan(0),
    mfCurrentScanPeriod_s(30.0f),
    parent(0),
	sensorPlatform(0),
	fireControlId(-1),
	fireControlIdx(0),
    lastCounterMeasureTime(0),
    isCommandReceiver(false),
    sensorId(nextSensorId++)
{
    mcTrack.mnID = NULL_INDEX;

	if (database == 0)
	{
		database = tcDatabase::Get();
	}
}

tcSensorState::tcSensorState(tcSensorDBObject* dbObj)
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
	sensorPlatform(0),
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
        if (tcSensorState *illuminator = GetFireControlSensor())
        {
            illuminator->ReleaseTrack(mcTrack.mnID);
        }
    }
}


