#ifndef TCSPACEDBOBJECT_H
#define TCSPACEDBOBJECT_H

#include "tcDatabaseObject.h"
#include "tcPlatformDBObject.h"
#include "tcAirDetectionDBObject.h"
#include "tcWaterDetectionDBObject.h"



namespace database
{

class tcFlightportDBObject;
class tcSqlReader;

/**
    * Models a surface ship platform. Specialization of old tcGenericDBObject
    */
class tcSpaceDBObject :  public tcPlatformDBObject
{
public:

    tcDBString flightportClass; ///< database class name of flightport (or empty if none) 飞行港（或如果没有则为空）的数据库类名
    tcDatabaseObject* AsDatabaseObject();
    virtual const char* GetClassName() const {return "Ship";} ///< returns class name of database object
    tcFlightportDBObject* GetFlightport();
    virtual float GetFuelConsumptionConstant(float speed_kts = 0) const;

    virtual void PrintToFile(tcFile& file);

    static void AddSqlColumns(std::string& columnString);
    void ReadSql(tcSqlReader& entry);
    void WriteSql(std::string& valueString);



    tcSpaceDBObject();
    tcSpaceDBObject(const tcSpaceDBObject& obj); ///< copy constructor
    virtual ~tcSpaceDBObject();

private:
    void CalculateParams();

};

}





#endif // TCSPACEDBOBJECT_H
