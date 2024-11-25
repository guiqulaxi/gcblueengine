#include "tcSpaceDBObject.h"

#include "tcDatabase.h"
#include "tcFlightportDBObject.h"
#include "database/tcSqlReader.h"
#include "tcSpaceObject.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

tcDatabaseObject* tcSpaceDBObject::AsDatabaseObject()
{
    return this;
}

void tcSpaceDBObject::CalculateParams()
{

}

tcFlightportDBObject* tcSpaceDBObject::GetFlightport()
{
    tcFlightportDBObject* flightport = dynamic_cast<tcFlightportDBObject*>
        (database->GetObject(flightportClass.c_str()));

    if (!flightport)
    {
        fprintf(stderr, "Error - Class: %s - flightport (%s) not found\n",
                mzClass.c_str(), flightportClass.c_str());
    }
    return flightport;
}

float tcSpaceDBObject::GetFuelConsumptionConstant(float speed_kts) const
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

void tcSpaceDBObject::PrintToFile(tcFile& file)
{
    tcString s;

    tcPlatformDBObject::PrintToFile(file);
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcSpaceDBObject::AddSqlColumns(std::string& columnString)
{
    tcPlatformDBObject::AddSqlColumns(columnString);
}

void tcSpaceDBObject::ReadSql(tcSqlReader& entry)
{
    tcPlatformDBObject::ReadSql(entry);

    CalculateParams();
}

void tcSpaceDBObject::WriteSql(std::string& valueString) const
{
    tcPlatformDBObject::WriteSql(valueString);
}

void tcSpaceDBObject::WritePythonValue(std::string &valueString) const
{
    tcPlatformDBObject::WritePythonValue(valueString);
    valueString+="    dbObj.flightportClass="+strutil::to_python_value(flightportClass.c_str())+"\n";

}

void tcSpaceDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcSpaceDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";
}


tcSpaceDBObject::tcSpaceDBObject() :
    tcPlatformDBObject()
{
    mnModelType = MTYPE_SPACE;
}

tcSpaceDBObject::tcSpaceDBObject(const tcSpaceDBObject& obj)
    : tcPlatformDBObject(obj)

{
}

tcSpaceDBObject::~tcSpaceDBObject()
{
}

tcGameObject *tcSpaceDBObject::CreateGameObject()
{
 return new tcSpaceObject(this);
}

}
