/**
**  @file tcSubObject.h
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

#ifndef _SUBOBJECT_H_
#define _SUBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include "tcPlatformObject.h"
#include "tcCommandObject.h"

class tcUpdateStream;
class tcCommandStream;
class tcGameStream;
namespace database
{
	class tcSubDBObject;
}


/**
* Models air object that can land
*/
class tcSubObject : public tcPlatformObject 
{
public:
    std::shared_ptr<tcSubDBObject> mpDBObject;
    virtual void SetKinematics(
            double fLon_rad,              ///< intitude [rad]
            double fLat_rad,               ///< latitude [rad]
            float fAlt_m,                  ///< altitude, negative is subsurface depth [m]
            float fHeading_rad,           ///< relative to north [rad] 顺时针
            float fYaw_rad,                ///< orientation in azimuthal plane
            float fPitch_rad,              ///< orientation in elevation plane
            float fRoll_rad, 			   ///< orienation about roll axis
            float fSpeed_kts             ///< [kts])
    ) override;
    virtual void ApplyRestrictions() override;
    virtual void Clear()override;
    virtual bool IsDestroyed()override;
    virtual void RandInitNear(float afLon_deg, float afLat_deg)override;
    virtual void UpdateClimb(float dt_s)override;
    virtual void Update(double afStatusTime)override;

    void PrintToFile(tcFile& file)override;
    void SaveToFile(tcFile& file)override;
    void LoadFromFile(tcFile& file)override;
    virtual void Serialize(tcFile& file, bool mbLoad)override;

    // JSON serialization
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

	float GetBatteryCharge() const;
    float GetPeriscopeDepth() const;
    bool GetPeriscopeState() const;
    bool GetRadarMastState() const;
	float GetMaxSpeedForDepth(float altitude_m) const;

    virtual float GetSonarSourceLevel(float az_deg) const;
    bool IsAtPeriscopeDepth() const;
	bool IsDieselElectric() const;
	bool IsSnorkeling() const;
    bool IsSurfaced() const;
    void SetPeriscopeState(bool state);
    void SetRadarMastState(bool state);
	void SetSnorkelState(bool state);
    virtual void SetAltitude(float new_altitude_m)override;
    float GetMaxQuietSpeedKts() const;

    virtual float GetOpticalCrossSection() const override;
    virtual float GetIRSignature(float az_deg) const override;

    virtual tcCommandStream& operator<<(tcCommandStream& stream)override;
    virtual tcUpdateStream& operator<<(tcUpdateStream& stream)override;
    virtual tcGameStream& operator<<(tcGameStream& stream)override;

    virtual tcCommandStream& operator>>(tcCommandStream& stream)override;
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream)override;
    virtual tcGameStream& operator>>(tcGameStream& stream)override;

    virtual void ClearNewCommand()override;
    virtual bool HasNewCommand() const override;

    tcSubObject();
    tcSubObject(tcSubObject&);
    tcSubObject(std::shared_ptr<tcSubDBObject> obj);
    virtual ~tcSubObject();
    virtual void Construct() override;
protected:
	enum
	{
		MAST_CMD = 0x01 ///< flag for periscope, radar mast, or snorkeling cmds
	};
	enum
	{
		PERISCOPE = 0x01,
		RADARMAST = 0x02,
		SNORKEL = 0x04
	};
    tcCommandObject commandObj;
    const float maxPitch_rad;
    bool radarMastRaised;
    bool periscopeRaised;
	bool isSnorkeling; ///< true if diesel generator active and snorkeling (DE subs only)
    float periscopeDepth_m; ///< periscope depth (positive number)
    float invPeriscopeDepth; ///< 1/periscopeDepth_m
    float lastDepth_m; ///< for depth notification messages
    bool doneSinking;
	float batteryCharge; ///< current battery charge (DE subs only)

    void UpdateDestroyed(double t);
//    virtual void UpdateEffects();
    virtual void UpdateHeading(float dt_s) override;
    virtual void UpdateMessages();
    virtual void UpdateSensors(double t) override;
    virtual void UpdateSpeed(float dt_s) override;
};

#endif
