/**
**  @file tcShipDBObject.cpp
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

#include "tcShipDBObject.h"
#include "tcDatabase.h"
#include "tcFlightportDBObject.h"

#include "database/tcSqlReader.h"
#include <sstream>
#include "tcCarrierObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

// std::shared_ptr<tcDatabaseObject> tcShipDBObject::AsDatabaseObject()
// {
//     return this;
// }

void tcShipDBObject::CalculateParams()
{
    tcPlatformDBObject::CalculateParams();

}

std::shared_ptr<tcFlightportDBObject>tcShipDBObject::GetFlightport()
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

float tcShipDBObject::GetFuelConsumptionConstant(float speed_kts) const
{
    // Fuel burn penalty:
    // penalty = 0 for speed <= 2/3 max, above 2/3 penalty increases to 2 at max speed
    float excess_speed_penalty = 6.0 * ((speed_kts * invMaxSpeed) - 0.67f);

    if (excess_speed_penalty < 0)
    {
        return fuelConsumptionConstant;
    }
    else
    {
        return fuelConsumptionConstant * (1.0 + excess_speed_penalty);
    }
}

void tcShipDBObject::PrintToFile(tcFile& file) 
{
    tcString s;

    tcPlatformDBObject::PrintToFile(file);
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcShipDBObject::AddSqlColumns(std::string& columnString)
{
    tcPlatformDBObject::AddSqlColumns(columnString);

    columnString += ",";

    columnString += "Draft_m real,";

    columnString += "Length_m real";
    columnString += "Beam_m real";
    columnString += "PowerPlantType text";
    columnString += "TotalShaft_HP real";
    columnString += "ExhaustStacks real";
    columnString += "PropulsionShafts real";
    columnString += "PropulsiveEfficiency real";
    columnString += "CivilianPaintScheme real";
    columnString += "FlashyPaintScheme real";
    columnString += "FlightportClass varchar(30)";
    

    tcAirDetectionDBObject::AddSqlColumns(columnString);

    tcWaterDetectionDBObject::AddSqlColumns(columnString);


}

void tcShipDBObject::ReadSql(tcSqlReader& entry)
{
    tcPlatformDBObject::ReadSql(entry);

    draft_m = (float)entry.GetDouble("Draft_m");

    length_m = (float)entry.GetDouble("Length_m");
    beam_m = (float)entry.GetDouble("Beam_m");
    PowerPlantType = (float)entry.GetDouble("PowerPlantType");
    TotalShaft_HP = (float)entry.GetDouble("TotalShaft_HP");
    ExhaustStacks = (float)entry.GetDouble("ExhaustStacks");
    PropulsionShafts = (float)entry.GetDouble("PropulsionShafts");
    PropulsiveEfficiency = (float)entry.GetDouble("PropulsiveEfficiency");
    CivilianPaintScheme = (float)entry.GetDouble("CivilianPaintScheme");
    FlashyPaintScheme = (float)entry.GetDouble("FlashyPaintScheme");
    flightportClass = entry.GetString("FlightportClass").c_str();
    auto airDetectionDBObject =std::make_shared<tcAirDetectionDBObject>();
    airDetectionDBObject->ReadSql(entry);
    components.push_back(airDetectionDBObject);
    auto waterDetectionDBObject =std::make_shared<tcWaterDetectionDBObject>();
    waterDetectionDBObject->ReadSql(entry);
    components.push_back(waterDetectionDBObject);

    //CalculateParams();
}

void tcShipDBObject::WriteSql(std::string& valueString) const
{
    tcPlatformDBObject::WriteSql(valueString);

    std::stringstream s;

    s << ",";

    s << draft_m << ",";
    s << length_m << ",";
    s << beam_m << ",";
    s << PowerPlantType << ",";
    s << TotalShaft_HP << ",";
    s << ExhaustStacks << ",";
    s << PropulsionShafts << ",";
    s << PropulsiveEfficiency << ",";
    s << CivilianPaintScheme << ",";
    s << FlashyPaintScheme << ",";

    s << "'" << flightportClass.c_str() << "'";

    valueString += s.str();

    GetComponent<tcAirDetectionDBObject>()->WriteSql(valueString);

    GetComponent<tcWaterDetectionDBObject>()->WriteSql(valueString);
}

void tcShipDBObject::WritePythonValue(std::string &valueString) const
{
 tcPlatformDBObject::WritePythonValue(valueString);
    GetComponent<tcAirDetectionDBObject>()->WritePythonValue(mzClass,valueString);
    GetComponent<tcWaterDetectionDBObject>()->WritePythonValue(mzClass,valueString);
    valueString+="    dbObj.draft_m="+strutil::to_python_value(draft_m)+"\n";
    valueString+="    dbObj.beam_m="+strutil::to_python_value(beam_m)+"\n";
    valueString+="    dbObj.PowerPlantType="+strutil::to_python_value(PowerPlantType)+"\n";
    valueString+="    dbObj.TotalShaft_HP="+strutil::to_python_value(TotalShaft_HP)+"\n";
    valueString+="    dbObj.ExhaustStacks="+strutil::to_python_value(ExhaustStacks)+"\n";
    valueString+="    dbObj.PropulsionShafts="+strutil::to_python_value(PropulsionShafts)+"\n";
    valueString+="    dbObj.PropulsiveEfficiency="+strutil::to_python_value(PropulsiveEfficiency)+"\n";
    valueString+="    dbObj.CivilianPaintScheme="+strutil::to_python_value(CivilianPaintScheme)+"\n";
    valueString+="    dbObj.FlashyPaintScheme="+strutil::to_python_value(FlashyPaintScheme)+"\n";
    valueString+="    dbObj.flightportClass="+strutil::to_python_value(flightportClass)+"\n";
}

void tcShipDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcShipDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";

}


tcShipDBObject::tcShipDBObject() : 
    tcPlatformDBObject()
{
    mnModelType = MTYPE_SURFACE;
}

tcShipDBObject::tcShipDBObject(const tcShipDBObject& obj)
    : tcPlatformDBObject(obj),


    draft_m(obj.draft_m),
    length_m(obj.length_m),
    beam_m(obj.beam_m),
    PowerPlantType(obj.PowerPlantType),
    TotalShaft_HP(obj.TotalShaft_HP),
    ExhaustStacks(obj.ExhaustStacks),
    PropulsionShafts(obj.PropulsionShafts),
    PropulsiveEfficiency(obj.PropulsiveEfficiency),
    CivilianPaintScheme(obj.CivilianPaintScheme),
    FlashyPaintScheme(obj.FlashyPaintScheme),
    flightportClass(obj.flightportClass)
{
}

tcShipDBObject::~tcShipDBObject() 
{
}

std::shared_ptr<tcGameObject>tcShipDBObject::CreateGameObject()
{
    auto mpDatabase =tcDatabase::Get();
    switch (this->mnModelType)
    {
    case MTYPE_CARRIER:
    {
        if (mpDatabase->GetObject(this->flightportClass.c_str()) != 0)
        {
           auto sss= std::dynamic_pointer_cast<tcShipDBObject>(tcDatabaseObject::shared_from_this());

            auto obj= std::make_shared<tcCarrierObject>(std::dynamic_pointer_cast<tcShipDBObject>(tcDatabaseObject::shared_from_this()));
            obj->Construct();
            return obj;
        }
        else
        {
            std::string msg = strutil::format("Error creating carrier type surface ship (%s), reverting to non-carrier model. Invalid flightport class (%s). Check database.",
                                              this->mzClass.c_str(), this->flightportClass.c_str());
            fprintf(stderr, "%s\n", msg.c_str());
#ifdef _DEBUG \
    //wxMessageBox(msg, "Object Create Error");
#endif

            auto obj=  std::make_shared<tcSurfaceObject>(std::dynamic_pointer_cast<tcShipDBObject>(tcDatabaseObject::shared_from_this()));
            obj->Construct();
            return obj;
        }
    }
    break;
    case MTYPE_SURFACE:
    {
        auto obj=  std::make_shared<tcSurfaceObject>(std::dynamic_pointer_cast<tcShipDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;
    default:
        fprintf(stderr, "tcSimState::CreateGameObject - "
                        "Invalid model type for Ship DB obj (%d)\n", this->mnModelType);
        return nullptr;
    }
}

}
