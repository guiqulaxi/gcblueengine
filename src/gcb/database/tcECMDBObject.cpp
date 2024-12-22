/**  
**  @file tcECMDBObject.cpp
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

#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000


#include "tcECMDBObject.h"
#include "tcECM.h"

#include "CsvTranslator.h"
#include <sstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

std::shared_ptr<tcSensorState> tcECMDBObject::CreateSensor(std::shared_ptr<tcGameObject> parent)
{
    std::shared_ptr<tcECM> ecm = std::make_shared<tcECM>(dynamic_pointer_cast<tcECMDBObject>(tcDatabaseObject::shared_from_this()));
	ecm->SetParent(parent);
	
	return ecm;
}

const char* tcECMDBObject::GetTypeDescription() const
{
    static std::string s;

    s = "ECM ";
    s += ecmType;

    return s.c_str();
}


void tcECMDBObject::PrintToFile(tcFile& file) 
{
    //char zBuff[128];

    tcSensorDBObject::PrintToFile(file);
}

/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcECMDBObject::AddSqlColumns(std::string& columnString)
{
	tcSensorDBObject::AddSqlColumns(columnString);

	columnString += ",";

	columnString += "EcmType varchar(30),"; 
	columnString += "ERP_dBW number(3),";
	columnString += "EffectivenessRating number(5),";
	columnString += "IsEffectiveVsSurveillance number(1),";
	columnString += "IsEffectiveVsSeeker number(1)";

}

void tcECMDBObject::ReadSql(tcSqlReader& entry)
{
	tcSensorDBObject::ReadSql(entry);

	ecmType = entry.GetString("EcmType").c_str();
	ERP_dBW = entry.GetDouble("ERP_dBW");
	effectivenessRating = entry.GetDouble("EffectivenessRating");
	isEffectiveVsSurveillance = entry.GetInt("IsEffectiveVsSurveillance") != 0;
	isEffectiveVsSeeker = entry.GetInt("IsEffectiveVsSeeker") != 0;
}

void tcECMDBObject::WriteSql(std::string& valueString) const
{
	tcSensorDBObject::WriteSql(valueString);

	std::stringstream s;

	s << ",";

	s << "'" << ecmType.c_str() << "',";
	s << ERP_dBW << ",";
	s << effectivenessRating << ",";
	s << (long)isEffectiveVsSurveillance << ",";
	s << (long)isEffectiveVsSeeker;

	valueString += s.str();
}

void tcECMDBObject::WritePythonValue(std::string &valueString) const
{
    tcSensorDBObject::WritePythonValue(valueString);
    valueString+="    dbObj.ecmType="+strutil::to_python_value(ecmType)+"\n";
    valueString+="    dbObj.ERP_dBW="+strutil::to_python_value(ERP_dBW)+"\n";
    valueString+="    dbObj.effectivenessRating="+strutil::to_python_value(effectivenessRating)+"\n";
    valueString+="    dbObj.isEffectiveVsSurveillance="+strutil::to_python_value(isEffectiveVsSurveillance)+"\n";
    valueString+="    dbObj.isEffectiveVsSeeker="+strutil::to_python_value(isEffectiveVsSeeker)+"\n";

}

void tcECMDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcECMDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";
}


tcECMDBObject::tcECMDBObject() : tcSensorDBObject(),
    ecmType("Undefined"),
	ERP_dBW(0),
	effectivenessRating(0.5f),
	isEffectiveVsSurveillance(false),
	isEffectiveVsSeeker(false)
{
    mzClass = "Default ECM";

    mfMaxRange_km = 100.0f;
    mfRefRange_km = 80.0f;
    mfFieldOfView_deg = 360.0f;
    mfScanPeriod_s = 4.0f;
}

tcECMDBObject::tcECMDBObject(tcECMDBObject& obj) 
: tcSensorDBObject(obj) 
{
}

tcECMDBObject::~tcECMDBObject() 
{
}


}
