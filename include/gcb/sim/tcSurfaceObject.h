/**  
**  @file tcSurfaceObject.h
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

#ifndef _TCSURFACEOBJECT_H_
#define _TCSURFACEOBJECT_H_

#include "tcFile.h"
#include "tcPlatformObject.h"
#include <deque>

class tcGameStream;

namespace database
{
	class tcShipDBObject;
}

/**
* Represents a platform that resides on the water's surface.
*
* @see tcPlatformObject
*/
class tcSurfaceObject : public tcPlatformObject
{
public:
    std::shared_ptr<tcShipDBObject> mpDBObject;

    virtual void Clear() override;
    virtual void SetKinematics(
            double fLon_rad,              ///< longitude [rad]
            double fLat_rad,               ///< latitude [rad]
            float fAlt_m,                  ///< altitude, negative is subsurface depth [m]
            float fHeading_rad,           ///< relative to north [rad] 顺时针
            float fYaw_rad,                ///< orientation in azimuthal plane
            float fPitch_rad,              ///< orientation in elevation plane
            float fRoll_rad, 			   ///< orienation about roll axis
            float fSpeed_kts             ///< [kts])
    ) override;
    virtual float GetSonarSourceLevel(float az_deg) const override;
    virtual bool IsDestroyed() override;
    virtual void RandInitNear(float afLon_deg, float afLat_deg)override;
    virtual void Update(double afStatusTime)override;
    //virtual void UpdateEffects();
    virtual void UpdateHeading(float dt_s)override;

    void PrintToFile(tcFile& file)override;
	void SaveToFile(tcFile& file) override;
    void LoadFromFile(tcFile& file) override;
    virtual void Serialize(tcFile& file, bool mbLoad)override;

    virtual float GetOpticalCrossSection(float view_alt_m, float view_dist_km) const override;
    virtual float GetIRSignature(float az_deg) const override ;

    const std::deque<tcPoint>& GetPositionHistory() const;
    bool IsNearWake(const tcPoint& pos, float distance_m, tcPoint& nextPos, size_t& leg) const;

    virtual tcGameStream& operator>>(tcGameStream& stream);
    virtual tcGameStream& operator<<(tcGameStream& stream);

	tcSurfaceObject();
	tcSurfaceObject(tcSurfaceObject&);
	tcSurfaceObject(std::shared_ptr<tcShipDBObject> obj);
	~tcSurfaceObject();
   virtual void Construct() override;
protected:
    enum {MAX_HISTORY = 64};
	bool doneSinking;
    double lastHistoryUpdate; ///< time that positionHistory was last updated

    std::deque<tcPoint> positionHistory; ///< deque of (lon_rad,lat_rad) platform position, front is most recent


	virtual void ApplyRestrictions(void);
	virtual void UpdateClimb(float dt_s) {} // do nothing for surface objs
	virtual void UpdateDestroyed(double t);
    virtual void UpdateHistory(double t);

};

#endif
