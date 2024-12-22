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

    std::string flightportClass; ///< database class name of flightport (or empty if none) 飞行港（或如果没有则为空）的数据库类名
    // std::shared_ptr<tcDatabaseObject> AsDatabaseObject();
    virtual const char* GetClassName() const {return "Ship";} ///< returns class name of database object
    std::shared_ptr<tcFlightportDBObject> GetFlightport();
    virtual float GetFuelConsumptionConstant(float speed_kts = 0) const;

    virtual void PrintToFile(tcFile& file);

    static void AddSqlColumns(std::string& columnString);
    void ReadSql(tcSqlReader& entry);
    void WriteSql(std::string& valueString) const;

    void WritePythonValue(std::string& valueString) const;
    void WritePython(std::string &valueString) const;

    tcSpaceDBObject();
    tcSpaceDBObject(const tcSpaceDBObject& obj); ///< copy constructor
    virtual ~tcSpaceDBObject();
virtual std::shared_ptr<tcGameObject>CreateGameObject() override;
private:
    void CalculateParams();

};

}





#endif // TCSPACEDBOBJECT_H
