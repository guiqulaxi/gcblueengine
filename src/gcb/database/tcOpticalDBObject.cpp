/** 
**  @file tcOpticalDBObject.cpp
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

#include "strutil.h"
#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000

#include "tcOpticalDBObject.h"
#include "tcOpticalSensor.h"


#include "tinyxml2.h"
#include "database/tcSqlReader.h"
#include <sstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

namespace database
{

std::shared_ptr<tcSensorState> tcOpticalDBObject::CreateSensor(std::shared_ptr<tcGameObject> parent)
{
    std::shared_ptr<tcOpticalSensor> optical = std::make_shared<tcOpticalSensor>(dynamic_pointer_cast<tcOpticalDBObject>(tcDatabaseObject::shared_from_this()));
	optical->SetParent(parent);
	
	return optical;
}


float tcOpticalDBObject::EstimateDetectionRange(float signature_dB, bool isNight) const
{
	float baseRange_km = mfRefRange_km * powf(10.0f, 0.1f*signature_dB);
	float detectionRange = isNight ? nightFactor * baseRange_km : baseRange_km;
							
	return detectionRange;
}

const char* tcOpticalDBObject::GetTypeDescription() const
{
    static std::string s;

    s = "";

    if (isSurveillance)
    {
        if (!isIR)
        {
            s += "Optical Search";
        }
        else
        {
            s += "EO/IR Search";
        }
        if (isDesignator)
        {
            s += " & Designator";
        }
    }
    else
    {
        if (isDesignator)
        {
            s += "Laser Designator";
        }
    }

    return s.c_str();
}

/**
*
*/
void tcOpticalDBObject::PrintToFile(tcFile& file) 
{
   tcString s;
   
   tcDatabaseObject::PrintToFile(file);
   
   s.Format("   ref range: %3.1f km, night: %.2f, IR: %d\n", 
	   mfRefRange_km, nightFactor, isIR);
   file.WriteString(s.GetBuffer());
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcOpticalDBObject::AddSqlColumns(std::string& columnString)
{
	tcSensorDBObject::AddSqlColumns(columnString);

	columnString += ",";

    columnString +=  "MaxFireControlTracks number(3),";
	columnString +=  "IsSemiactive number(1),";
    columnString +=  "IsDesignator number(1),";
	columnString +=  "DetectsSurface number(1),";
	columnString +=  "DetectsAir number(1),";
	columnString +=  "DetectsMissile number(1),";
	columnString +=  "DetectsGround number(1),";
	columnString +=  "IsIR number(1),";
	columnString +=  "NightFactor number(5)";

}

void tcOpticalDBObject::ReadSql(tcSqlReader& entry)
{
	tcSensorDBObject::ReadSql(entry);

    maxFireControlTracks = entry.GetInt("MaxFireControlTracks");
	isSemiactive = entry.GetInt("IsSemiactive") != 0;
    isDesignator = entry.GetInt("IsDesignator") != 0;
	mbDetectsSurface = entry.GetInt("DetectsSurface") != 0;
	mbDetectsAir = entry.GetInt("DetectsAir") != 0;
	mbDetectsMissile = entry.GetInt("DetectsMissile") != 0;
	mbDetectsGround = entry.GetInt("DetectsGround") != 0;
	isIR = entry.GetInt("IsIR") != 0;
	nightFactor = entry.GetDouble("NightFactor");

    if (rangeError <= 0) rangeError = 1.5f; // 0 previously interpreted as active sensor with perfect range, now 0 < x <= 1 is passive, > 1 is active
}

void tcOpticalDBObject::WriteSql(std::string& valueString) const
{
	tcSensorDBObject::WriteSql(valueString);

	std::stringstream s;

	s << ",";

    s << (int)maxFireControlTracks << ",";
    s << (int)isSemiactive << ",";
    s << (int)isDesignator << ",";
    s << (int)mbDetectsSurface << ",";
    s << (int)mbDetectsAir << ",";
    s << (int)mbDetectsMissile << ",";
    s << (int)mbDetectsGround << ",";
    s << (int)isIR << ",";
	s << nightFactor;

	valueString += s.str();

    //if (rangeError <= 0) rangeError = 1.5f; // 0+ to 1 interpreted as fractional range error, > 1 as absolute error

}

void tcOpticalDBObject::WritePythonValue(std::string &valueString) const
{

    tcSensorDBObject::WritePythonValue(valueString);
    valueString+="    dbObj.maxFireControlTracks="+strutil::to_python_value(maxFireControlTracks)+"\n";
    valueString+="    dbObj.isSemiactive="+strutil::to_python_value(isSemiactive)+"\n";
    valueString+="    dbObj.isDesignator="+strutil::to_python_value(isDesignator)+"\n";
    valueString+="    dbObj.mbDetectsSurface="+strutil::to_python_value(mbDetectsSurface)+"\n";
    valueString+="    dbObj.mbDetectsAir="+strutil::to_python_value(mbDetectsAir)+"\n";
    valueString+="    dbObj.mbDetectsMissile="+strutil::to_python_value(mbDetectsMissile)+"\n";
    valueString+="    dbObj.mbDetectsGround="+strutil::to_python_value(mbDetectsGround)+"\n";
    valueString+="    dbObj.isIR="+strutil::to_python_value(isIR)+"\n";
    valueString+="    dbObj.nightFactor="+strutil::to_python_value(nightFactor)+"\n";

}

void tcOpticalDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcOpticalDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";

    valueString+="    return dbObj\n";;
}

void tcOpticalDBObject::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    tcSensorDBObject::SerializeToJson(obj, allocator);

    obj.AddMember(rapidjson::Value("maxFireControlTracks", allocator).Move(), maxFireControlTracks, allocator);
    obj.AddMember(rapidjson::Value("isSemiactive", allocator).Move(), isSemiactive ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("isDesignator", allocator).Move(), isDesignator ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("mbDetectsSurface", allocator).Move(), mbDetectsSurface ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("mbDetectsAir", allocator).Move(), mbDetectsAir ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("mbDetectsMissile", allocator).Move(), mbDetectsMissile ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("mbDetectsGround", allocator).Move(), mbDetectsGround ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("isIR", allocator).Move(), isIR ? 1 : 0, allocator);
    obj.AddMember(rapidjson::Value("nightFactor", allocator).Move(), nightFactor, allocator);
}

tcOpticalDBObject::tcOpticalDBObject() : tcSensorDBObject() 
{
   mzClass = "Default Optical";

   mfMaxRange_km = 20.0f;
   mfRefRange_km = 0.5f;
   mfFieldOfView_deg = 360.0f;
   mfScanPeriod_s = 5.0f;
  
   mbDetectsSurface = true;
   mbDetectsAir = true;
   mbDetectsMissile = true;
   mbDetectsGround = true;
   isIR = false;
   nightFactor = 1.0f;
   isSemiactive = false;
   isDesignator = false;
}

tcOpticalDBObject::tcOpticalDBObject(const tcOpticalDBObject& obj) 
: tcSensorDBObject(obj),
    maxFireControlTracks(obj.maxFireControlTracks),
    isSemiactive(obj.isSemiactive),
    isDesignator(obj.isDesignator),
    mbDetectsSurface(obj.mbDetectsSurface),
    mbDetectsAir(obj.mbDetectsAir),
	mbDetectsMissile(obj.mbDetectsMissile),
    mbDetectsGround(obj.mbDetectsGround),
    isIR(obj.isIR),
	nightFactor(obj.nightFactor)
{

}

tcOpticalDBObject::~tcOpticalDBObject() 
{
}


}

