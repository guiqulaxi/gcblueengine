/**
**  @file tcGroundDBObject.cpp
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
#endif

#include "tcGroundDBObject.h"
#include "tcDatabase.h"
#include "tcFlightportDBObject.h"

#include "database/tcSqlReader.h"
#include <sstream>
#include "tcAirfieldObject.h"
#include "tcGroundVehicleObject.h"
#include "tcGroundObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


namespace database
{

// std::shared_ptr<tcDatabaseObject> tcGroundDBObject::AsDatabaseObject()
// {
// 	return this;
// }

std::shared_ptr<tcFlightportDBObject> tcGroundDBObject::GetFlightport()
{
    std::shared_ptr<tcFlightportDBObject> flightport = std::dynamic_pointer_cast<tcFlightportDBObject>
        (database->GetObject(flightportClass.c_str()));

    if (!flightport)
	{
		fprintf(stderr, "Error - Class: %s - flightport (%s) not found\n",
			mzClass.c_str(), flightportClass.c_str());
	}
	return flightport;
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcGroundDBObject::AddSqlColumns(std::string& columnString)
{
	tcPlatformDBObject::AddSqlColumns(columnString);

    columnString += ",";

    columnString += "FlightportClass varchar(30)";

    tcAirDetectionDBObject::AddSqlColumns(columnString);
}

void tcGroundDBObject::ReadSql(tcSqlReader& entry)
{
	tcPlatformDBObject::ReadSql(entry);

    flightportClass = entry.GetString("FlightportClass").c_str();

    auto airDetectionDBObject =std::make_shared<tcAirDetectionDBObject>();
    airDetectionDBObject->ReadSql(entry);
    components.push_back(airDetectionDBObject);

}

void tcGroundDBObject::WriteSql(std::string& valueString) const
{
	tcPlatformDBObject::WriteSql(valueString);

    std::stringstream s;

	s << ",";

	s << "'" << flightportClass.c_str() << "'";

	valueString += s.str();

    GetComponent<tcAirDetectionDBObject>()[0]->WriteSql(valueString);
}

void tcGroundDBObject::WritePythonValue(std::string &valueString) const
{
    tcPlatformDBObject::WritePythonValue(valueString);
    GetComponent<tcAirDetectionDBObject>()[0]->WritePythonValue(mzClass,valueString);
    valueString+="    dbObj.flightportClass="+strutil::to_python_value(flightportClass.c_str())+"\n";

}

void tcGroundDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcGroundDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";;

}

void tcGroundDBObject::CalculateParams()
{
    tcPlatformDBObject::CalculateParams();
}
tcGroundDBObject::tcGroundDBObject() : 
    tcPlatformDBObject()
{
    mnModelType = MTYPE_OBJECT;
}

tcGroundDBObject::tcGroundDBObject(const tcGroundDBObject& obj)
: tcPlatformDBObject(obj), 

  flightportClass(obj.flightportClass)
{
}

tcGroundDBObject::~tcGroundDBObject() 
{
}

std::shared_ptr<tcGameObject>tcGroundDBObject::CreateGameObject()
{
    /* these types are defined in tcDatabase.h */
    switch (this->mnModelType)
    {
    case MTYPE_AIRFIELD:
        {
        auto obj= std::make_shared<tcAirfieldObject>(std::dynamic_pointer_cast<tcGroundDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;
    case MTYPE_FIXED:
    {
        auto obj= std::make_shared< tcGroundObject>(std::dynamic_pointer_cast<tcGroundDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;

    case MTYPE_GROUNDVEHICLE:
    {
        auto obj= std::make_shared< tcGroundVehicleObject>(std::dynamic_pointer_cast<tcGroundDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;
    default:
        fprintf(stderr, "tcSimState::CreateGameObject - "
                        "Invalid model type for ground DB obj (%d)\n", this->mnModelType);
        return nullptr;
    }
}

}
