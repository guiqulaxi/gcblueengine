/**
**  @file tcESMSensor.h
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

#ifndef _TCESMSENSOR_H_
#define _TCESMSENSOR_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include "tcSensorState.h"
#include "tcDatabase.h"
#include "tcESMDBObject.h"

class tcGameObject;
class tcECM;
class tcRadar;
class tcStream;
class tcGameStream;
class tcUpdateStream;

using namespace database;

/**
 * 电子支援措施（ESM）是频谱空间中的“侦察兵”。依靠高灵敏度的接收机，电子支援系统可以截获周边的雷达信号，测定辐射源的工作频率、方位、脉冲宽度、脉冲重复频率等参数。
 */
class tcESMSensor : public tcSensorState
{
    friend class tcPlatformDebugPopup;
public:
    std::shared_ptr<tcESMDBObject> mpDBObj;

    virtual bool CanDetectTarget(std::shared_ptr<const tcGameObject> target, float& range_km, bool useRandom=true);
    virtual bool InitFromDatabase(long key); ///< initializes sensor using database data at key
    bool IsDetected(std::shared_ptr<const tcSensorState> emitter, float ERP_dBW, float& az_rad);
    bool IsDetectedECM( std::shared_ptr<const tcECM> emitter, float& az_rad);
    bool IsDetectedRadar(std::shared_ptr<const tcRadar> emitter, float& az_rad);
    virtual bool IsESM() const;
    void Serialize(tcFile& file, bool mbLoad);
    virtual void Update(double t);

    unsigned char GetRWRWarningLevel() const;

    tcESMSensor& operator=(tcESMSensor& ss);
    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);
    virtual tcUpdateStream& operator<<(tcUpdateStream& stream);
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream);

    //virtual tcStream& operator<<(tcStream& stream);
    //virtual tcStream& operator>>(tcStream& stream);
    std::shared_ptr<tcESMSensor> Clone(void);
    tcESMSensor();
    tcESMSensor(std::shared_ptr<tcESMDBObject> dbObj);
    virtual ~tcESMSensor();

private:
    double lastRWRupdate;
    unsigned char rwrWarningLevel; ///< 0 - none, 1 - targeted non-missile, 2 - targeted missile


	static float targetRange_km; ///< target range from last call to IsDetected
    static float last_margin_dB; ///< from last call to IsDetected
    static float last_ERP_dBW; ///< from last call to IsDetected
    static bool rwrUpdate; ///< a hack to signal we're in an RWR update

    bool UpdateScanRWR(double t);
	void ProcessESMDetection(std::shared_ptr<tcGameObject> target, double t);
    void UpdateSensorMap(std::shared_ptr<const tcGameObject> target, long* emitters, unsigned int nEmitters,
		float az_rad, double t);
	void UpdateSeeker(double t);
	void UpdateSurveillance(double t);
    void UpdateSurveillanceRWR(double t);
    void UpdateTrack(std::shared_ptr<const tcGameObject> target, double t);
};
#endif
