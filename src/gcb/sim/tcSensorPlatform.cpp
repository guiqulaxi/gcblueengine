/** 
**  @file tcSensorPlatform.cpp
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

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcSensorPlatform.h"
#include "tcSensorPlatformDBObject.h"
#include "tcSonarDBObject.h"
#include "tcGameObject.h"
#include "tcESMSensor.h"
#include "tcOpticalSensor.h"
#include "tcRadar.h"
#include "tcSonar.h"

#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "common/tcString.h"
#include "tcMissileObject.h"
#include "tcScenarioLogger.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



/**
* sensor can fail from damage in 3 ways: 
*    ARM takes out radar, damage directly hits sensor, platform damage causes secondary failure of sensor
* @return true if any sensors were damaged
* @param newDamage new damage done to host platform, used for general failure test
*/
bool tcSensorPlatform::ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager, float damageLevel)
{
    bool result = false;

    // if damager is missile with ESM seeker (anti-rad), apply high damage to first active radar
    // (nothing to keep track of which emitter seeker is tracking so pick first one)
    bool ARMdamage = false;
    if (std::shared_ptr<tcMissileObject> missile =  std::dynamic_pointer_cast<tcMissileObject>(damager))
    {
        if (std::shared_ptr<tcESMSensor> esm = std::dynamic_pointer_cast<tcESMSensor>(missile->GetSeekerSensor()))
        {
            ARMdamage = true;
        }
    }
    unsigned int nSensors = GetSensorCount();

    
    if (ARMdamage)
    {
        bool searchingForRadar = true;
        for (unsigned int n=0; (n<nSensors)&&searchingForRadar; n++)
        {
            std::shared_ptr<tcSensorState> sensor = GetSensorMutable(n);
            assert(sensor);

            std::shared_ptr<tcRadar> radar =  std::dynamic_pointer_cast<tcRadar>(sensor);
            if (radar && radar->IsActive())
            {
                if (!radar->IsDamaged() && (randf() < 0.9f))
                {
                    radar->SetDamaged(true);
                    result = true;
                }
                searchingForRadar = false;
            }
        }
    }

    // next go through every sensor and apply damage

    for (unsigned int n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState> sensor = GetSensorMutable(n);
        assert(sensor);
        
        result = result || sensor->ApplyAdvancedDamage(damage);
    }

    // last apply general damage
    if (damageLevel <= 0) return result;

    float scaledDamage = damageLevel; //(damageLevel < 0.5f) ? (0.4f * damageLevel) : damageLevel;

    for (unsigned int n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState> sensor = GetSensorMutable(n);

        if (!sensor->IsDamaged() && (randf() <= scaledDamage))
        {
            sensor->SetDamaged(true);
            result = true;
        }
    }

    return result;
}



void tcSensorPlatform::ClearActivityFlags()
{
	sensorActivityFlags = 0;
}


/**
* @return first sensor with matching database id
*/
std::shared_ptr<const tcSensorState> tcSensorPlatform::GetSensorByDatabaseID(int id) const
{
    unsigned nSensors = GetSensorCount();
	for (unsigned n=0; n < nSensors; n++)
	{
        std::shared_ptr<const tcSensorState> sensor = GetSensor(n);
        if (sensor->mnDBKey == id) return sensor;
    }

    return 0;
}

/**
* @return number of sensors on platform
*/
unsigned tcSensorPlatform::GetSensorCount() const
{
    return (unsigned)sensorState.size();
}

/**
* @return description of sensors for display
*/
std::string tcSensorPlatform::GetSensorDescription()
{
    static std::string errorString = "Error";
	std::string description;

	unsigned nSensors = GetSensorCount();
	for (unsigned n=0; n < nSensors; n++)
	{
        
        std::shared_ptr<const tcSensorState> sensor = GetSensor(n);
		
		const char* text = (sensor != 0) && (sensor->mpDBObj != 0) ?
		    sensor->mpDBObj->mzClass.c_str() : errorString.c_str();
		description += strutil::format("%s\n", text);
	}

	if (nSensors == 0)
	{
		description = "No sensors\n";
	}

	return description;
}

/**
* consider all active (mbActive) sensors
*/
bool tcSensorPlatform::HasActivatedSensor() 
{
    int nSensors = (int)sensorState.size();
    for (int k=0;k<nSensors;k++) 
    {
        std::shared_ptr<tcSensorState>pSensorState = sensorState[k];
        if (pSensorState->IsActive()) {return true;}
    }
    return false;
}

bool tcSensorPlatform::IsEnsonifying() const
{
	return (sensorActivityFlags & ACTIVE_SONAR_ACTIVE) != 0;
}


/**
* consider only active radars and ECM
*/
bool tcSensorPlatform::IsRadiating() const
{
	return (sensorActivityFlags & (RADAR_ACTIVE | ECM_ACTIVE)) != 0;
}



std::shared_ptr<const tcSensorState> tcSensorPlatform::GetSensor(unsigned int idx) const
{
    if (idx >= sensorState.size()) return 0;
    else return sensorState[idx];
}

/**
* This version is used for non-const access to the sensor
*/
std::shared_ptr<tcSensorState> tcSensorPlatform::GetSensorMutable(unsigned idx) const
{
    if (idx >= sensorState.size()) return 0;
    else return sensorState[idx];
}

/**
* @returns mutable pointer to first sensor matching sensorClass or 0 if not found
*/
std::shared_ptr<tcSensorState> tcSensorPlatform::GetSensorMutable(const std::string& sensorClass) const
{
    for(size_t n=0; n<sensorState.size(); n++)
    {
        if (sensorClass == sensorState[n]->mpDBObj->mzClass.c_str())
        {
            return sensorState[n];
        }
    }
    
    return 0;
}

std::shared_ptr<tcSensorState> tcSensorPlatform::GetSensorMutable(const std::string& sensorClass, unsigned int& idx) const
{
    for (size_t n=0; n<sensorState.size(); n++)
    {
        if (sensorClass == sensorState[n]->mpDBObj->mzClass.c_str())
        {
            idx = n;
            return sensorState[n];
        }
    }

    idx = 0;
    return 0;
}

const std::shared_ptr<tcSonar> tcSensorPlatform::GetStrongestActiveSonar() const
{
	float maxSL = -999.0f;
    std::shared_ptr<tcSonar> strongest = 0;

	for(size_t n=0; n<sensorState.size(); n++)
	{
		std::shared_ptr<tcSensorState> sensor = sensorState[n];
		if (sensor->IsSonar())
		{
            std::shared_ptr<tcSonar> sonar = std::dynamic_pointer_cast<tcSonar>(sensor);
			if (sonar->IsActive() && (!sonar->IsPassive()) && (sonar->mpDBObj->SL > maxSL))
			{
				strongest = sonar;
				maxSL = sonar->mpDBObj->SL;
			}
		}
	}

	return strongest;
}

void tcSensorPlatform::SetActivityFlag(unsigned int flag)
{
	sensorActivityFlags |= flag;
}

/**
* Used to active/deactive sensor on platform
*/
void tcSensorPlatform::SetSensorState(unsigned idx, bool state)
{
    if (idx >= sensorState.size()) return; // error

	std::shared_ptr<tcSensorState> sensor = sensorState[idx];
	if (sensor->IsActive() == state) return; // no change, return

    sensorState[idx]->SetActive(state);
    sensorCommandObj.SetNewCommand(0x01 << idx);
}



void tcSensorPlatform::PrintToFile(tcFile& file) 
{
    tcString s;

    int nSensors = (int)sensorState.size();
    for(int i=0;i<nSensors;i++) 
    {
        std::shared_ptr<tcSensorState>& pSS = sensorState[i];
        if (pSS != NULL) 
        {
            s.Format("   SENSOR%d: %s\n", i, pSS->mpDBObj->mzClass.c_str());
        }
        else 
        {
            s = "   BAD SENSOR\n";
        }
        file.WriteString(s.GetBuffer());
    }
}

void tcSensorPlatform::SaveToFile(tcFile& file) 
{
    size_t nSensors = sensorState.size();
    for(size_t i=0;i<nSensors;i++) 
    {
        std::shared_ptr<tcSensorState>& pss = sensorState[i];
        pss->Serialize(file, false);
    }
}

/**
*
*/
void tcSensorPlatform::LoadFromFile(tcFile& file) 
{
    // assumes that sensors already created by higher level serialize method
    size_t nSensors = sensorState.size();
    for(size_t i=0;i<nSensors;i++) 
    {
        std::shared_ptr<tcSensorState>& pss = sensorState[i];
        pss->Serialize(file,true);
    }
}

/**
*
*/
void tcSensorPlatform::Serialize(tcFile& file, bool mbLoad)
 {
    if (mbLoad)
    {
        LoadFromFile(file);
    }
    else 
    {
        SaveToFile(file);
    }
}


void tcSensorPlatform::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{   
    std::string s;

    size_t nSensors = sensorState.size();
    for(size_t n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState>sensor = sensorState[n];
        assert(sensor);
        
        bool setState = false; // true to write command in py file to set state of sensor (i.e. isnt in default state)

        if (std::shared_ptr<tcRadar> radar =  std::dynamic_pointer_cast<tcRadar>(sensor))
        {
            setState = sensor->mbActive != 0;
        }
        else if (std::shared_ptr<tcESMSensor> esm = std::dynamic_pointer_cast<tcESMSensor>(sensor))
        {
            setState = !sensor->mbActive;
        }
        else if (std::shared_ptr<tcOpticalSensor> optical =  std::dynamic_pointer_cast<tcOpticalSensor>(sensor))
        {
            setState = !sensor->mbActive;
        }
        else if (std::shared_ptr<tcSonar> sonar = std::dynamic_pointer_cast<tcSonar>(sensor))
        {
            bool isPassive = sonar->IsPassive();
            setState = (isPassive && !sensor->mbActive) || (!isPassive && sensor->mbActive);
        }
        else
        {
            setState = true;
        }

        if (setState)
        {
            s=strutil::format("UI.SetSensorState(%d, %d)", n, sensor->mbActive);
            logger.AddScenarioText(s);
        }
    } 

}


/**
* Loads state from command stream
*/
tcCommandStream& tcSensorPlatform::operator<<(tcCommandStream& stream)
{
    size_t nSensors = sensorState.size();
    for(size_t n=0; n < nSensors; n++)
    {
		stream >> sensorState[n]->mbActive;
    }

    return stream;
}

/**
* Saves state to command stream
*/
tcCommandStream& tcSensorPlatform::operator>>(tcCommandStream& stream)
{
    size_t nSensors = sensorState.size();
    for(size_t n=0; n < nSensors; n++)
    {
        stream << sensorState[n]->mbActive;
    }

    return stream;
}

/**
* Loads state from create stream
*/
tcCreateStream& tcSensorPlatform::operator<<(tcCreateStream& stream)
{
    return stream;
}

/**
* Saves state to create stream
*/
tcCreateStream& tcSensorPlatform::operator>>(tcCreateStream& stream)
{
    return stream;
}


/**
* Loads state from update stream
*/
tcUpdateStream& tcSensorPlatform::operator<<(tcUpdateStream& stream)
{
    unsigned short sensorDamage;
    stream >> sensorDamage;
    

    unsigned short damageFlag = 0x0001;
    
    size_t nSensors = sensorState.size();
    assert(nSensors <= 8*sizeof(sensorDamage));

    for(size_t n=0; n < nSensors; n++)
    {
        bool damageState = (sensorDamage & damageFlag) != 0;
        sensorState[n]->SetDamaged(damageState);
        
        damageFlag = damageFlag << 1;
    }

    return stream;
}

/**
* Saves state to update stream
*/
tcUpdateStream& tcSensorPlatform::operator>>(tcUpdateStream& stream)
{
    unsigned short sensorDamage = 0;
    
    unsigned short damageFlag = 0x0001;
    
    size_t nSensors = sensorState.size();
    assert(nSensors <= 8*sizeof(sensorDamage));
    
    for(size_t n=0; n < nSensors; n++)
    {
        if (sensorState[n]->IsDamaged())
        {
            sensorDamage |= damageFlag;
        }
        damageFlag = damageFlag << 1;
    }   
    
    stream << sensorDamage;
    
    return stream;
}

/**
* Loads state from game stream
*/
tcGameStream& tcSensorPlatform::operator<<(tcGameStream& stream)
{
    unsigned int nSensors;
    stream >> nSensors;
    assert((size_t)nSensors == sensorState.size());

    stream >> sensorActivityFlags;
    sensorCommandObj << stream;

    for (size_t k=0; k<sensorState.size(); k++)
    {
        sensorState[k]->operator<<(stream);
    }

    stream.ReadCheckValue(678);

    return stream;
}

/**
* Saves state to game stream
*/
tcGameStream& tcSensorPlatform::operator>>(tcGameStream& stream)
{
    unsigned int nSensors = (unsigned int)sensorState.size();
    stream << nSensors;

    stream << sensorActivityFlags;
    sensorCommandObj >> stream;

    for (size_t k=0; k<sensorState.size(); k++)
    {
        sensorState[k]->operator>>(stream);
    }

    stream.WriteCheckValue(678);

    return stream;
}


void tcSensorPlatform::ClearNewCommand()
{
    sensorCommandObj.ClearNewCommand();
}

bool tcSensorPlatform::HasNewCommand() const
{
    return sensorCommandObj.HasNewCommand();
}


/**
* If the default constructor is used, this should be used to initialize
* this object.
*/
void tcSensorPlatform::Init(std::shared_ptr<tcSensorPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent)
{
    using namespace database;

    // add sensors
    if (obj->sensorClass.size() > tcSensorPlatformDBObject::MAXSENSORS) 
    {
        fprintf(stderr, "tcSensorPlatform::Init - Warning - "
            "DB sensor count exceeded recommended limit (%s)\n", parent->mzClass.c_str());
    }
    sensorState.clear();

    tcDatabase* database = tcDatabase::Get();
    
    for(size_t i=0; i<obj->sensorClass.size(); i++) 
    {
        std::shared_ptr<tcDatabaseObject>pDBObj = database->GetObject(obj->sensorClass[i]);

        if (std::shared_ptr<tcSensorDBObject>pSensorDBObj =  std::dynamic_pointer_cast<tcSensorDBObject>(pDBObj))
		{
			std::shared_ptr<tcSensorState> sensor = pSensorDBObj->CreateSensor(parent); // factory method
			assert(sensor);
			float lookAz_rad = C_PIOVER180 * obj->sensorAz[i];
			sensor->SetMountAz(lookAz_rad);
			sensorState.push_back(sensor);
		}
		else
		{
            std::string msg=strutil::format("Error - tcSensorPlatform::Init - Sensor (%s) not found when initializing platform (%s)\n", obj->sensorClass[i].c_str(), parent->mzClass.c_str());
//            msg.Printf("Error - tcSensorPlatform::Init - Sensor (%s) not found when initializing platform (%s)\n", obj->sensorClass[i].c_str(), parent->mzClass.c_str());
            //wxMessageBox(msg);
            fprintf(stderr, msg.c_str());
		}
        
    }
}

void tcSensorPlatform::Init(const char* databaseClass, std::shared_ptr<tcGameObject> parent)
{
	if (strlen(databaseClass) == 0)
	{
		return; // platform has no sensor
	}

    std::shared_ptr<tcSensorDBObject> sensorData =  std::dynamic_pointer_cast<tcSensorDBObject>(
		tcDatabase::Get()->GetObject(databaseClass));

	if (sensorData == 0)
	{
		fprintf(stderr, "Error - tcSensorPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent)"
			" - Sensor not found in database (%s)\n", databaseClass);
		assert(false);
		return;
	}

	std::shared_ptr<tcSensorState> sensor = sensorData->CreateSensor(parent); // factory method
	assert(sensor);

	sensor->mfSensorHeight_m = 0.8f * parent->GetZmax(); //< guess sensor height is 80% of zmax
	sensor->SetMountAz(0);
	sensorState.push_back(sensor);
}


/**
*
*/
void tcSensorPlatform::Update(double t)
{
	ClearActivityFlags(); // flags are updated in Update() methods of child sensors

    size_t nSensors = sensorState.size();
    for(size_t n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState>sensor = sensorState[n];
        assert(sensor);
        sensor->Update(t);
    } 
}

/**
*
*/
tcSensorPlatform::tcSensorPlatform()    
{
}


tcSensorPlatform::tcSensorPlatform(std::shared_ptr<tcSensorPlatformDBObject> obj, std::shared_ptr<tcGameObject> parent)
:   sensorActivityFlags(0)
{
    Init(obj, parent); // This way avoids using this pointer in base class initializer
}

/**
* Version for single sensor platforms (e.g. missiles)
* Sensor is assumed to be pointed forward
*/
tcSensorPlatform::tcSensorPlatform(const char* databaseClass, std::shared_ptr<tcGameObject> parent)
{
	Init(databaseClass, parent);
}


/**
*
*/
tcSensorPlatform::tcSensorPlatform(const tcSensorPlatform& o) : 
    sensorCommandObj(o.sensorCommandObj)
{
    // copy sensor state array
    sensorState.clear();
    size_t nSensors = o.sensorState.size();
    for (size_t n=0;n<nSensors;n++) 
    {
        std::shared_ptr<const tcSensorState> pSensorState = o.sensorState[n];
        std::shared_ptr<tcSensorState> pNewSensorState = pSensorState->Clone();
        sensorState.push_back(pNewSensorState);
    }
}

/**
*
*/
tcSensorPlatform::~tcSensorPlatform()
{
    size_t nSensors = sensorState.size();
    for (size_t n=0; n<nSensors; n++) 
    {
        //delete sensorState[n];
    }
}

/**
* Serialize sensor platform data to JSON
*/
void tcSensorPlatform::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    obj.SetObject();
    
    // Serialize sensorActivityFlags
    obj.AddMember(rapidjson::Value("sensorActivityFlags", allocator).Move(), sensorActivityFlags, allocator);
    rapidjson::Value typeName;
    typeName.SetString(GetType().c_str(), static_cast<rapidjson::SizeType>(GetType().length()), allocator);
    obj.AddMember(rapidjson::Value("typeName", allocator).Move(), typeName, allocator);
    // Serialize sensor states
    if (!sensorState.empty())
    {
        rapidjson::Value sensorsArray(rapidjson::kArrayType);
        for (const auto& sensor : sensorState)
        {
            if (sensor)
            {
                rapidjson::Value sensorObj(rapidjson::kObjectType);
                sensor->SerializeToJson(sensorObj, allocator);
                sensorsArray.PushBack(sensorObj, allocator);
            }
        }
        obj.AddMember(rapidjson::Value("sensorState", allocator).Move(), sensorsArray, allocator);
    }
    
    // Serialize sensor command object
    rapidjson::Value commandObj(rapidjson::kObjectType);
    // TODO: Implement tcCommandObject serialization when available
    // sensorCommandObj.SerializeToJson(commandObj, allocator);
    obj.AddMember(rapidjson::Value("sensorCommandObj", allocator).Move(), commandObj, allocator);
}


