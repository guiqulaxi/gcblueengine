/**
**  @file tcWaterDetectionDBObject.cpp
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


#include "tcWaterDetectionDBObject.h"
#include "database/tcSqlReader.h"
#include "database/tcSignatureModel.h"
#include "database/tcAcousticModel.h"
#include "database/tcDatabase.h"
#include "math_constants.h"

#include <sstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcWaterDetectionDBObject::AddSqlColumns(std::string& columnString)
{
	columnString += ",";

    columnString += "TS numeric,";   
    columnString += "TS_Model text,";   
	columnString += "AcousticModel text,";
    columnString += "SL_Model text";
}

void tcWaterDetectionDBObject::ReadSql(tcSqlReader& entry)
{
	TS = entry.GetDouble("TS");
    TS_Model = entry.GetString("TS_Model");
	acousticModel = entry.GetString("AcousticModel");
    SL_Model = entry.GetString("SL_Model");

    BindSignatureModels();
}

void tcWaterDetectionDBObject::WriteSql(std::string& valueString) const
{
	std::stringstream s;

	s << ",";

	s << TS << ",";
    s << "'" << TS_Model.c_str() << "',";
    s << "'" << acousticModel.c_str() << "',";
    s << "'" << SL_Model.c_str() << "'";

	valueString += s.str();
}

void tcWaterDetectionDBObject::WritePythonValue(const std::string &mzClass, std::string &valueString) const
{
    valueString+="    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()\n";
    valueString+="    waterDetectionDBObject.TS="+strutil::to_python_value(TS)+"\n";
    valueString+="    waterDetectionDBObject.TS_Model="+strutil::to_python_value(TS_Model)+"\n";
    valueString+="    waterDetectionDBObject.acousticModel="+strutil::to_python_value(acousticModel)+"\n";
    valueString+="    waterDetectionDBObject.SL_Model="+strutil::to_python_value(SL_Model)+"\n";
    valueString+="    waterDetectionDBObject.BindSignatureModels()\n";
    valueString+="    dbObj.AddComponent(waterDetectionDBObject)\n";


}

void tcWaterDetectionDBObject::WritePython(const std::string &mzClass, std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcWaterDetectionDBObject()\n";
    WritePythonValue(mzClass,valueString);
    valueString+="    return dbObj\n";
}

void tcWaterDetectionDBObject::BindSignatureModels()
{
    tcDatabase* database = tcDatabase::Get();

    auto _TS_pattern = database->GetSignatureModel(TS_Model);
    auto _SL_pattern = database->GetSignatureModel(SL_Model);
    auto _acousticNoise = database->GetAcousticModel(acousticModel);

    if (!_TS_pattern)
    {
        TS_pattern = *(database->GetSignatureModel("Default"));
        fprintf(stderr, "tcWaterDetectionDBObject::BindSignatureModels - TS pattern (%s) missing\n",
            TS_Model.c_str());
    }
    else
            TS_pattern=*_TS_pattern;
    if (!_SL_pattern )
    {
        SL_pattern = *(database->GetSignatureModel("Default"));
        fprintf(stderr, "tcWaterDetectionDBObject::BindSignatureModels - SL pattern (%s) missing\n",
            SL_Model.c_str());
    }
    else
        SL_pattern=*_SL_pattern;
    if (!_acousticNoise)
    {
        acousticNoise = *(database->GetAcousticModel("Default"));
        fprintf(stderr, "tcWaterDetectionDBObject::BindSignatureModels - acoustic model (%s) missing\n",
            SL_Model.c_str());
    }
    else
        acousticNoise=*_acousticNoise;
}

float tcWaterDetectionDBObject::GetCavitatingSourceLevel() const
{
    return acousticNoise.cavitationSL_dB;
}

float tcWaterDetectionDBObject::GetCavitationSpeedKts(float depth_m) const
{
    return acousticNoise.GetCavitationSpeedKts(depth_m);
}

float tcWaterDetectionDBObject::GetMinNonCavitatingDepth(float speed_kts) const
{
    return acousticNoise.GetCavitationDepth(speed_kts);
}

float tcWaterDetectionDBObject::GetNoiseLevelForSpeed(float speed_mps) const
{
    return acousticNoise.GetNoiseLevelForSpeed(speed_mps);
}

float tcWaterDetectionDBObject::GetNoiseLevelForSpeedKts(float speed_kts) const
{
    return acousticNoise.GetNoiseLevelForSpeedKts(speed_kts);
}

float tcWaterDetectionDBObject::GetSnorkelingSourceLevel() const
{
    return acousticNoise.snorkelingSL_dB;
}

/**
* Gets radiated SL of this object
* @param speed_mps speed of this obj
* @param depth_m depth of this obj
* @param az_deg relative aspect, e.g. 0 is bow, 90 stbd beam, 180 stern
*/
float tcWaterDetectionDBObject::GetSourceLevel(float speed_mps, float depth_m, float az_deg) const
{
    float SL_base = acousticNoise.GetSourceLevel(C_MPSTOKTS*speed_mps, depth_m);
    float patternModifier = SL_pattern.GetModifier(az_deg, 0);

    return SL_base + patternModifier;
}

float tcWaterDetectionDBObject::GetTargetStrength(float az_deg) const
{
    return TS + TS_pattern.GetModifier(az_deg, 0);
}


tcWaterDetectionDBObject::tcWaterDetectionDBObject()
:   TS(0)
    // ,
    // TS_pattern(0),
    // SL_pattern(0),
    // acousticNoise(0)
{

}

tcWaterDetectionDBObject::tcWaterDetectionDBObject(const tcWaterDetectionDBObject& obj)
:   TS(obj.TS),
    TS_pattern(obj.TS_pattern),
    SL_pattern(obj.SL_pattern),
    acousticNoise(obj.acousticNoise)
{
    
}

tcWaterDetectionDBObject::~tcWaterDetectionDBObject() 
{
}

}
