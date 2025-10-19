#ifndef TCCOMMPLATFORMDBOBJECT_H
#define TCCOMMPLATFORMDBOBJECT_H
#include "tcComponentDBObject.h"
#include "tcSqlReader.h"
class tcFile;
#include <vector>
namespace database
{
class tcCommPlatformDBObject : public tcComponentDBObject
{
public:
    tcCommPlatformDBObject();
    enum
    {
        MAXCOMMS = 16   ///< number of sensor entries supported in database
    };

    std::vector<std::string> commClass;


    std::vector<int> commId; ///< database id's of sensors
    std::vector<float> commAz; ///< pointing angles of sensors in degrees


    virtual const char* GetClassName() const {return "Generic";} ///< returns class name of database object

    bool HasAllEmitters(std::vector<int>& emitters);

    void PrintToFile(tcFile& file);

    void ReadSql(tcSqlReader& entry);
    void WriteSql(std::string& valueString) const;
    void WritePythonValue(const std::string &mzClass, std::string& valueString) const;
    void WritePython(const std::string&mzClass, std::string& valueString) const;

    static void AddSqlColumns(std::string& columnString);

    tcCommPlatformDBObject(const tcCommPlatformDBObject& obj); ///< copy constructor
    virtual ~tcCommPlatformDBObject();
    void UpdateCommList();
    void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

};
};

#endif // TCCOMMPLATFORMDBOBJECT_H
