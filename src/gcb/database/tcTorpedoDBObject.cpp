/*  
**  @file tcTorpedoDBObject.cpp
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


#include "tcTorpedoDBObject.h"
#include "tcSonarDBObject.h"
#include "math_constants.h"
#include "tcDatabase.h"
#include "database/tcSqlReader.h"
#include <sstream>
#include<cassert>
#include "tcTorpedoObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


namespace database
{

    /**
    * Calculate parameters based on database values.
    */
    void tcTorpedoDBObject::CalculateParams()
    {
        tcWeaponDBObject::CalculateParams();
        maxTurnRate_radps = C_PIOVER180 * maxTurnRate_degps;
        batteryRate_kWpkt = batteryRate_kW / maxSpeed_kts;

		if ((weaponType == TORPEDO) || (weaponType == BOTTOM_MINE_CAPTOR))
		{
            if(batteryRate_kW>0)
            {
                // calculate range for simple model (overwrite param loaded from db)
                maxRange_km = (battery_kJ / batteryRate_kW) * maxSpeed_kts * 0.001f * C_KTSTOMPS;
            }

		}

    }


    std::shared_ptr<tcSonarDBObject> tcTorpedoDBObject::GetSeekerDBObj() const
    {
        assert(database);
        return std::dynamic_pointer_cast<tcSonarDBObject>(database->GetObject(sonarClass));
    }


    void tcTorpedoDBObject::PrintToFile(tcFile& file) 
    {
        tcString s;

        tcWeaponDBObject::PrintToFile(file);

        s.Format(" No torpedo info avail.");
        file.WriteString(s.GetBuffer());
    }


    /**
    * Adds sql column definitions to columnString. This is used for
    * SQL create table command
    */
    void tcTorpedoDBObject::AddSqlColumns(std::string& columnString)
    {
        tcWeaponDBObject::AddSqlColumns(columnString);
        tcWaterDetectionDBObject::AddSqlColumns(columnString);

        columnString += ",";

        columnString += "maxTurnRate_degps number(8),";
        columnString += "maxDepth_m number(8),";
        columnString += "battery_kJ number(8),";
        columnString += "batteryRate_kW number(8),";
        columnString += "maxSpeed_kts number(8),";
        columnString += "acceleration_ktsps number(8),";
        columnString += "sonarClass varchar(30),";
        columnString += "wireGuidance number(1),";
        columnString += "preEnableSpeed_kts real,";
        columnString += "WeaponType numeric";
    }

    void tcTorpedoDBObject::ReadSql(tcSqlReader& entry)
    {
        tcWeaponDBObject::ReadSql(entry);
        auto waterDetectionDBObject =std::make_shared<tcWaterDetectionDBObject>();
        waterDetectionDBObject->ReadSql(entry);
        components.push_back(waterDetectionDBObject);
        maxTurnRate_degps = entry.GetDouble("maxTurnRate_degps");
        maxDepth_m = entry.GetDouble("maxDepth_m");
        battery_kJ = entry.GetDouble("battery_kJ");
        batteryRate_kW = entry.GetDouble("batteryRate_kW");
        maxSpeed_kts = entry.GetDouble("maxSpeed_kts");
        acceleration_ktsps = entry.GetDouble("acceleration_ktsps");
        sonarClass = entry.GetString("sonarClass");
        wireGuidance = entry.GetInt("wireGuidance") != 0;
        preEnableSpeed_kts = entry.GetDouble("preEnableSpeed_kts");
        weaponType = entry.GetInt("WeaponType");

        // CalculateParams();
    }

    void tcTorpedoDBObject::WriteSql(std::string& valueString) const
    {
        tcWeaponDBObject::WriteSql(valueString);
        GetComponent<tcWaterDetectionDBObject>()->WriteSql(valueString);

        std::stringstream s;

        s << ",";

        s << maxTurnRate_degps << ",";
        s << maxDepth_m << ",";
        s << battery_kJ << ",";
        s << batteryRate_kW << ",";
        s << maxSpeed_kts << ",";
        s << acceleration_ktsps << ",";
        s << "'" << sonarClass.c_str() << "'" << ",";
        s << wireGuidance << ",";
        s << preEnableSpeed_kts << ",";
        s << weaponType;


        valueString += s.str();

    }

    void tcTorpedoDBObject::WritePythonValue(std::string &valueString) const
    {
        tcWeaponDBObject::WritePythonValue(valueString);
        GetComponent<tcWaterDetectionDBObject>()->WritePythonValue(mzClass,valueString);
        valueString+="    dbObj.maxTurnRate_degps="+strutil::to_python_value(maxTurnRate_degps)+"\n";
        valueString+="    dbObj.maxDepth_m="+strutil::to_python_value(maxDepth_m)+"\n";
        valueString+="    dbObj.battery_kJ="+strutil::to_python_value(battery_kJ)+"\n";
        valueString+="    dbObj.batteryRate_kW="+strutil::to_python_value(batteryRate_kW)+"\n";
        valueString+="    dbObj.maxSpeed_kts="+strutil::to_python_value(maxSpeed_kts)+"\n";
        valueString+="    dbObj.acceleration_ktsps="+strutil::to_python_value(acceleration_ktsps)+"\n";
        valueString+="    dbObj.sonarClass="+strutil::to_python_value(sonarClass)+"\n";
        valueString+="    dbObj.wireGuidance="+strutil::to_python_value(wireGuidance)+"\n";
        valueString+="    dbObj.preEnableSpeed_kts="+strutil::to_python_value(preEnableSpeed_kts)+"\n";
        valueString+="    dbObj.weaponType="+strutil::to_python_value(weaponType)+"\n";

    }

    void tcTorpedoDBObject::WritePython(std::string &valueString) const
    {
        valueString+="import pygcb\n";
        valueString+="def CreateDBObject():\n";
        valueString+="    dbObj=pygcb.tcTorpedoDBObject()\n";
        WritePythonValue(valueString);
        valueString+="    dbObj.CalculateParams()\n";
        valueString+="    return dbObj\n";
    }


    tcTorpedoDBObject::tcTorpedoDBObject(const tcTorpedoDBObject& obj) 
        : tcWeaponDBObject(obj),
          maxTurnRate_degps(obj.maxTurnRate_degps),
          maxDepth_m(obj.maxDepth_m),
          battery_kJ(obj.battery_kJ),
          batteryRate_kW(obj.batteryRate_kW),
          maxSpeed_kts(obj.maxSpeed_kts),               
          acceleration_ktsps(obj.acceleration_ktsps),
          sonarClass(obj.sonarClass),
          wireGuidance(obj.wireGuidance),
          preEnableSpeed_kts(obj.preEnableSpeed_kts),
          weaponType(obj.weaponType)
    {
        mnModelType = MTYPE_TORPEDO;
        mnType = PTYPE_TORPEDO;

        CalculateParams();
    }

    tcTorpedoDBObject::tcTorpedoDBObject() : tcWeaponDBObject() ,
          maxTurnRate_degps(5),
          maxDepth_m(500),
          battery_kJ(100),
          batteryRate_kW(1),
          maxSpeed_kts(40),               
          acceleration_ktsps(3),
          sonarClass(""),
          wireGuidance(false),
          preEnableSpeed_kts(35),
          weaponType(TORPEDO)
    {
        mnModelType = MTYPE_TORPEDO;
        mnType = PTYPE_TORPEDO;

        CalculateParams();
    }

    tcTorpedoDBObject::~tcTorpedoDBObject() 
    {
    }

    std::shared_ptr<tcGameObject>tcTorpedoDBObject::CreateGameObject()
    {
        auto obj= std::make_shared<tcTorpedoObject>(std::dynamic_pointer_cast<tcTorpedoDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }

} // namespace database

