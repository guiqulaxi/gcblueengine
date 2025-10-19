#include "tcCommPlatformDBObject.h"

#include <tcDatabase.h>
#include <tcDatabaseObject.h>
#include "rapidjson/document.h"


using namespace database;
void tcCommPlatformDBObject::PrintToFile(tcFile& file)
{
}


/**
* Updates sensorId vector with database ids for each sensor
*/
void tcCommPlatformDBObject::UpdateCommList()
{
    commId.clear();

    tcDatabase* database = tcDatabase::Get();

    for(size_t n=0; n<commClass.size(); n++)
    {
        std::shared_ptr<tcDatabaseObject> obj = database->GetObject(commClass[n]);
        if (obj)
        {
            commId.push_back(obj->mnKey);
        }
        else
        {
            fprintf(stderr, "Error - tcCommPlatformDBObject::UpdateSensorList - sensor %s not found\n",
                    commClass[n].c_str());
            commId.push_back(-1);
        }
    }
}

/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcCommPlatformDBObject::AddSqlColumns(std::string& columnString)
{
    // no inter needed since all covered by platform_sensors table
    /*
    columnString += ",";

    for(int i=0;i<MAXSENSORS;i++)
    {
        tcString s;
        s.Format("S%d_class varchar(30),",i+1);
        columnString += s.GetBuffer();

        s.Format("S%d_az number(8)",i+1);
        columnString += s.GetBuffer();

        if (i < MAXSENSORS - 1) columnString += ",";
    }
    */


}

void tcCommPlatformDBObject::ReadSql(tcSqlReader& entry)
{
    commClass.clear();
    commAz.clear();
    commId.clear();

    // no inter needed since all covered by platform_sensors table
    //
    //for(int i=0;i<MAXSENSORS;i++)
    //{
    //	std::string className;
    //	tcString s;

    //	s.Format("S%d_class", i+1);
    //	className = entry.GetString(s.GetBuffer());

    //	if (className.size() > 0)
    //	{
    //		sensorClass.push_back(className);

    //		s.Format("S%d_az", i+1);
    //		sensorAz.push_back(entry.GetDouble(s.GetBuffer()));
    //	}

    //}

}

void tcCommPlatformDBObject::WriteSql(std::string& valueString) const
{
    // no inter needed since all covered by platform_sensors table
    /*
    std::stringstream s;

    s << ",";


    for(size_t i=0; i<MAXSENSORS; i++)
    {
        if (i < sensorClass.size())
        {
            s << "'" << sensorClass[i] << "',";
            s << sensorAz[i];
        }
        else
        {
            s << "'',";
            s << "0";
        }
        if (i < MAXSENSORS - 1) s << ",";
    }



    valueString += s.str();
    */

}

void tcCommPlatformDBObject::WritePythonValue(const std::string &mzClass, std::string& valueString) const
{
    valueString+="    commPlatformDBObject=pygcb.tcCommPlatformDBObject()\n";
    valueString+="    commPlatformDBObject.commClass="+strutil::to_python_value(commClass)+"\n";
    valueString+="    commPlatformDBObject.commAz="+strutil::to_python_value(commAz)+"\n";
    valueString+="    dbObj.AddComponent(commPlatformDBObject)\n";

}

void tcCommPlatformDBObject::WritePython(const std::string&mzClass, std::string& valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcCommPlatformDBObject()\n";
    WritePythonValue(mzClass,valueString);
    valueString+="    return dbObj\n";
}



tcCommPlatformDBObject::tcCommPlatformDBObject(const tcCommPlatformDBObject& obj)
    : commClass(obj.commClass),
    commAz(obj.commAz),
    commId(obj.commId)
{

}

tcCommPlatformDBObject::~tcCommPlatformDBObject()
{
}

void tcCommPlatformDBObject::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    tcComponentDBObject::SerializeToJson(obj, allocator);

    rapidjson::Value arrClass(rapidjson::kArrayType);
    for (const auto& s : commClass) arrClass.PushBack(rapidjson::Value(s.c_str(), allocator).Move(), allocator);
    obj.AddMember(rapidjson::Value("commClass", allocator).Move(), arrClass, allocator);

    rapidjson::Value arrId(rapidjson::kArrayType);
    for (const auto& id : commId) arrId.PushBack(id, allocator);
    obj.AddMember(rapidjson::Value("commId", allocator).Move(), arrId, allocator);

    rapidjson::Value arrAz(rapidjson::kArrayType);
    for (const auto& f : commAz) arrAz.PushBack(f, allocator);
    obj.AddMember(rapidjson::Value("commAz", allocator).Move(), arrAz, allocator);
}
