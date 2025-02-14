/**  
**  @file tcSonobuoyDBObject.cpp
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

#include "tcSonobuoyDBObject.h"
#include "database/tcSqlReader.h"
#include <sstream>
#include "tcSonobuoy.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

void tcSonobuoyDBObject::PrintToFile(tcFile& file)
{
    tcDatabaseObject::PrintToFile(file);
    GetComponent<tcSensorPlatformDBObject>()->PrintToFile(file);
}



/**
	* Adds sql column definitions to columnString. This is used for
	* SQL create table command
	*/
void tcSonobuoyDBObject::AddSqlColumns(std::string& columnString)
{
    tcDatabaseObject::AddSqlColumns(columnString);
    tcSensorPlatformDBObject::AddSqlColumns(columnString);
    tcWaterDetectionDBObject::AddSqlColumns(columnString);

    columnString += ",";

    columnString += "BatteryLife_s number(5),";
    columnString += "CommRange_km number(5)";
}

void tcSonobuoyDBObject::ReadSql(tcSqlReader& entry)
{
    tcDatabaseObject::ReadSql(entry);
    auto sensorPlatformDBObject=std::make_shared<tcSensorPlatformDBObject>();
    sensorPlatformDBObject->ReadSql(entry);
    components.push_back(sensorPlatformDBObject);
    auto waterDetectionDBObject =std::make_shared<tcWaterDetectionDBObject>();
    waterDetectionDBObject->ReadSql(entry);
    components.push_back(waterDetectionDBObject);

    batteryLife_s = entry.GetDouble("BatteryLife_s");
    commRange_km = entry.GetDouble("CommRange_km");
}

void tcSonobuoyDBObject::WriteSql(std::string& valueString) const
{
    tcDatabaseObject::WriteSql(valueString);
    GetComponent<tcSensorPlatformDBObject>()->WriteSql(valueString);
    GetComponent<tcWaterDetectionDBObject>()->WriteSql(valueString);

    std::stringstream s;

    s << ",";

    s << batteryLife_s << ",";
    s << commRange_km;

    valueString += s.str();
}

void tcSonobuoyDBObject::WritePythonValue(std::string &valueString) const
{
    tcDatabaseObject::WritePythonValue(valueString);
    GetComponent<tcSensorPlatformDBObject>()->WritePythonValue(mzClass,valueString);
    GetComponent<tcWaterDetectionDBObject>()->WritePythonValue(mzClass,valueString);
    valueString+="    dbObj.batteryLife_s="+strutil::to_python_value(batteryLife_s)+"\n";
    valueString+="    dbObj.commRange_km="+strutil::to_python_value(commRange_km)+"\n";

}

void tcSonobuoyDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcSonobuoyDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";
}




tcSonobuoyDBObject::tcSonobuoyDBObject() : tcDatabaseObject()
{
    mzClass = "Default Sonobuoy";
}

tcSonobuoyDBObject::tcSonobuoyDBObject(tcSonobuoyDBObject& obj)
    : tcDatabaseObject(obj),
    batteryLife_s(obj.batteryLife_s),
    commRange_km(obj.commRange_km)
{

}

tcSonobuoyDBObject::~tcSonobuoyDBObject()
{
}

std::shared_ptr<tcGameObject>tcSonobuoyDBObject::CreateGameObject()
{
    auto obj= std::make_shared<tcSonobuoy>(std::dynamic_pointer_cast<tcSonobuoyDBObject>(tcDatabaseObject::tcDatabaseObject::shared_from_this()));
    obj->Construct();
    return obj;
}

}

