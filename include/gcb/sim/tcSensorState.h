/** 
**  @file tcSensorState.h
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

#if _MSC_VER > 1000
#pragma once
#endif

#ifndef _TCSENSORSTATE_H_
#define _TCSENSORSTATE_H_

#include "tcPool.h"
#include "simmath.h"
#include "rapidjson/document.h"

namespace database
{
	class tcDatabase;
	class tcSensorDBObject;
}

using database::tcDatabase;
using database::tcSensorDBObject;

#define SSMODE_NULL 0 ///< seeker that doesn't exist or damaged
#define SSMODE_SURVEILLANCE 1 ///< surveillance or both FC and surveillance
#define SSMODE_SEEKERTRACK 2  ///< seeker is tracking target
#define SSMODE_SEEKERSEARCH 3 ///< seeker searching for target
#define SSMODE_SEEKERACQUIRE 4 ///< seeker has target cue and attempting to track
#define SSMODE_FC 5 // fire control only

class tcRadar;
class tcOpticalSensor;
class tcSimState;
class tcGameObject;
class tcUpdateStream;
class tcGameStream;
class tcSensorPlatform;
class tcSensorReport;
class tcLOS;
struct Damage;
class tcSensorMapTrack;

/**
 * Represents the state of a sensor.
 */
class tcSensorState: public std::enable_shared_from_this<tcSensorState>
{
	friend class tcGameSerializer;
public:
    short int mbActive;
    std::shared_ptr<tcGameObject> parent;
    // std::shared_ptr<tcSensorPlatform> sensorPlatform; ///< parent should always be a sensor plat, this is a down-cast for convenience
    int mnDBKey;
    std::shared_ptr<tcSensorDBObject> mpDBObj;
    double mfLastScan; ///记录上一次扫描的时间。
    float mfCurrentScanPeriod_s;
    short int mnMode;
    tcTrack mcTrack;
    //GeoPoint msCurrentPos; ///< current true position of sensor
    //float mfLookAz_rad;      ///< azimuth of center of coverage relative to north
    float mountAz_rad;       ///< mounted azimuth of boresight relative to nose/bow of platform 安装方位角，这是瞄准镜安装后的方位角，相对于平台的机头/船头。
    float mfSensorHeight_m;     ///< height of sensor relative to platform altitude 传感器高度，即传感器相对于平台高度的高度差

    static void AttachDatabase(tcDatabase* db) {database = db;}
    static void AttachSimState(tcSimState* ss) {simState = ss;}
    static void AttachLOS();//附加视线
	virtual bool CanDetectTarget(std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom=true);

    std::shared_ptr<tcRadar> GetFireControlRadar(); //获取火控雷达
    std::shared_ptr<tcOpticalSensor> GetLaserDesignator(); //获取激光指示器
    std::shared_ptr<tcSensorState> GetFireControlSensor(); //获取火控传感器
    void GetTestArea(tcRect& region);
	bool GetTrack(tcTrack& track_);
    int GetFireControlPlatform() const;
    bool HasFireControlSensor() const;

    virtual unsigned GetFireControlTrackCount() const;
    virtual unsigned GetMaxFireControlTracks() const;
    virtual bool IsTrackAvailable();
    virtual bool RequestTrack(int targetId);
    virtual bool ReleaseTrack(int targetId);
	virtual bool IsTrackingWithRadar(int targetId) const;

    virtual bool InitFromDatabase(int key); ///< initializes sensor using database data at key
	bool IsActive() const;
	bool IsDamaged() const;
    bool IsHidden() const;
    
    virtual bool IsECM() const; //是否是电子对抗措施
    virtual bool IsESM() const; //是否是电子支援措施
    virtual bool IsRadar() const;
    virtual bool IsSonar() const;
    virtual bool IsOptical() const;

    void Serialize(tcFile& file, bool mbLoad);
    virtual tcUpdateStream& operator<<(tcUpdateStream& stream);
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream);
    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

    virtual void SetActive(bool active);
    void SetCommandReceiver(bool state);
    bool IsCommandReceiver() const;
    void SetDamaged(bool state);
	virtual void SetFireControlSensor(int id, unsigned char idx);
    void SetMountAz(float az);
    void SetParent(std::shared_ptr<tcGameObject> obj);
    virtual void Update(double t);
    int UpdateScan(double afTime);
    tcSensorState& operator=(const tcSensorState& ss);

    // JSON serialization
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const;

    static void InitErrorFactor();

    bool ApplyAdvancedDamage(const Damage& damage);

    std::shared_ptr<tcSensorState> Clone() const;
    tcSensorState();
    tcSensorState(std::shared_ptr<tcSensorDBObject> dbObj);
    virtual ~tcSensorState();

protected:
    enum {N_ERROR_FACTOR=4096};
    static tcSimState* simState;
	static tcDatabase* database;
    static tcLOS* los;
    static int nextSensorId; ///< for assigning sensorId
    static float errorFactor[N_ERROR_FACTOR];

	bool isHidden; ///< hidden sensors are not displayed in object control view
    bool isDamaged;
    int fireControlId; ///< id of platform with fire control sensor (semi-active illuminator, or command guidance sensor)
    unsigned char fireControlIdx; ///< sensor index of fire control sensor platform
    const int sensorId; ///< unique id for this sensor (used for sonar TL cache)
    double lastCounterMeasureTime; ///< last time that sensor checked vs. countermeasures
    bool isCommandReceiver;


	bool RandomDetect(float margin_dB);
    void UpdateActiveReport(tcSensorReport* report, double t, float az_rad, float range_km, float alt_m, 
        std::shared_ptr<const tcSensorMapTrack> track);
    void UpdatePassiveReport(tcSensorReport* report, double t, float az_rad, float range_km,
		std::shared_ptr<const tcSensorMapTrack> track);
    bool HasLOS(std::shared_ptr<const tcGameObject> target);
    void CalculateLonLatCovariance(float az_rad, float lat_rad, float sigmaCrossRange_m, float sigmaDownRange_m,
        float& C11, float& C22, float& C12);
    bool GetAltitudeEstimate(float& altitudeEstimate_m, float& altitudeVariance, float range_km, float az_rad, float alt_m);

    static float GetErrorFactor(int platformId, int sensorId, float targetAz_rad);
};
#endif
