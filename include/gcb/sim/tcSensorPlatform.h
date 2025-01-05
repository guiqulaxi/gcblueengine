/** 
**  @file tcSensorPlatform.h
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

#ifndef _TCSENSORPLATFORM_H_
#define _TCSENSORPLATFORM_H_


#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcFile.h"
#include "tcLaunchRequest.h"
#include "tcSensorState.h"
#include "tcGuidanceState.h"
#include "tcCommandObject.h"
#include <vector>
#include "tcComponent.h"

class tcStream;
class tcCommandStream;
class tcCreateStream;
class tcUpdateStream;
class tcGameStream;
class tcGameObject;
class tcSonar;

struct Damage;

namespace database
{
    class tcSensorPlatformDBObject;
}

namespace scriptinterface
{
	class tcScenarioLogger;
}

using database::tcSensorPlatformDBObject;

/**
* Handles sensor-related aspects of platform
*
*/
class tcSensorPlatform:public tcComponent
{
public:
	enum
	{
		RADAR_ACTIVE = 1,
		ACTIVE_SONAR_ACTIVE = 2,
        ECM_ACTIVE = 4
	};

    std::vector<std::shared_ptr<tcSensorState>> sensorState;

    tcCommandObject sensorCommandObj; ///< ugly, could fix by handling sensors like launchers

    unsigned int GetSensorCount() const;
    bool HasActivatedSensor();
	bool IsEnsonifying() const;
    bool IsRadiating() const;
    std::shared_ptr<const tcSensorState> GetSensor(unsigned idx) const;
	std::string GetSensorDescription();
    std::shared_ptr<tcSensorState> GetSensorMutable(unsigned idx) const;
    std::shared_ptr<tcSensorState> GetSensorMutable(const std::string& sensorClass) const;    
    std::shared_ptr<tcSensorState> GetSensorMutable(const std::string& sensorClass, unsigned int& idx) const;
    std::shared_ptr<const tcSensorState> GetSensorByDatabaseID(long id) const;
    const std::shared_ptr<tcSonar> GetStrongestActiveSonar() const;
    void Init(std::shared_ptr<tcSensorPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent); 
	void Init(const char* databaseClass, std::shared_ptr<tcGameObject> parent); 
	void SetActivityFlag(unsigned int flag);
    void SetSensorState(unsigned idx, bool state);
    
    void Update(double t);

    void PrintToFile(tcFile&) ;
    void SaveToFile(tcFile& file) ;
    void LoadFromFile(tcFile& file);
    void Serialize(tcFile& file, bool mbLoad);
	void SaveToPython(scriptinterface::tcScenarioLogger& logger);

    bool ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager, float damageLevel);

    tcCommandStream& operator<<(tcCommandStream& stream);
    tcCreateStream& operator<<(tcCreateStream& stream);
    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcGameStream& operator<<(tcGameStream& stream);

    tcCommandStream& operator>>(tcCommandStream& stream);
    tcCreateStream& operator>>(tcCreateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    void ClearNewCommand();
    bool HasNewCommand() const;

    tcSensorPlatform();
    tcSensorPlatform(const tcSensorPlatform&);
    tcSensorPlatform(std::shared_ptr<tcSensorPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent); 
	tcSensorPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent);
    virtual ~tcSensorPlatform();

protected:
	unsigned int sensorActivityFlags; ///< flags for faster check of activity state of diff sensor types

	void ClearActivityFlags();
};

#endif
