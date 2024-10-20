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

#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000

#include "tcSonobuoyDBObject.h"
#include "tinyxml2.h"
#include "database/tcSqlReader.h"
#include <sstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

	void tcSonobuoyDBObject::PrintToFile(tcFile& file) 
	{ 
		tcDatabaseObject::PrintToFile(file);
        tcSensorPlatformDBObject::PrintToFile(file);
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
        tcSensorPlatformDBObject::ReadSql(entry);
        tcWaterDetectionDBObject::ReadSql(entry);

        batteryLife_s = entry.GetDouble("BatteryLife_s");
        commRange_km = entry.GetDouble("CommRange_km");
	}

	void tcSonobuoyDBObject::WriteSql(std::string& valueString)
	{
        tcDatabaseObject::WriteSql(valueString);
        tcSensorPlatformDBObject::WriteSql(valueString);
        tcWaterDetectionDBObject::WriteSql(valueString);

        std::stringstream s;

        s << ",";

        s << batteryLife_s << ",";
        s << commRange_km;

        valueString += s.str();
	}


	tcSonobuoyDBObject::tcSonobuoyDBObject() : tcDatabaseObject(),
        tcSensorPlatformDBObject(),
        tcWaterDetectionDBObject()
	{
		mzClass = "Default Sonobuoy";
	}

	tcSonobuoyDBObject::tcSonobuoyDBObject(tcSonobuoyDBObject& obj) 
		: tcDatabaseObject(obj), tcSensorPlatformDBObject(obj), 
          tcWaterDetectionDBObject(obj),
          batteryLife_s(obj.batteryLife_s),
          commRange_km(obj.commRange_km)
	{

	}

	tcSonobuoyDBObject::~tcSonobuoyDBObject() 
	{
	}

}

