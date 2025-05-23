/**
**  @file tcDatabase.cpp
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


#include "tcDatabase.h"

#include "AError.h"
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <iomanip>
#include <tcSpaceDBObject.h>
#include "CsvTranslator.h"
#include "tcDBObjSerializer.h"
#include "tcDBObjSerializerSql.h"
#include "tcDBMapSerializerSql.h"
#include "tcPlatformDBObject.h"
#include "tcItemDBObject.h"
#include "tcMissileDBObject.h"
#include "tcLauncherDBObject.h"
#include "tcSensorDBObject.h"
#include "tcRadarDBObject.h"
#include "tcOpticalDBObject.h"
#include "tcOptions.h"
#include "tcESMDBObject.h"
#include "tcECMDBObject.h"
#include "tcJetDBObject.h"
#include "tcBallisticDBObject.h"
#include "tcFlightportDBObject.h"
#include "tcGroundDBObject.h"
#include "tcFuelTankDBObject.h"
#include "tcShipDBObject.h"
#include "tcSimpleAirDBObject.h"
#include "tcStoresDBObject.h"
#include "tcSonarDBObject.h"
#include "tcSonobuoyDBObject.h"
#include "tcSubDBObject.h"
#include "tcTorpedoDBObject.h"
#include "tcCounterMeasureDBObject.h"
#include "tcBallisticMissileDBObject.h"
#include "tcSignatureModel.h"
#include "tcAcousticModel.h"
#include "tcDatabaseIterator.h"
#include "tinyxml2.h"
#include "sqlite/sqlite3x.hpp"
//#include "wx/file.h"
//#include "wx/textfile.h"
//#include "wx/progdlg.h"
#include "tcLoadoutData.h"
#include "tcCountryData.h"
#include "tcCountryNameChanges.h"
//#include "tcTexture2D.h"
//#include "tc3DWindow2.h"
#include "tcSimState.h"
#include "tcTime.h"
//#include "tcTextDialog.h"

#include "common/tcGameStream.h"
#include "common/tcObjStream.h"
#include "strutil.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{
std::vector<std::string> tcDatabase::mvTables;
/**
* Method for accessing singleton instance.
*/
tcDatabase* tcDatabase::Get()
{
    static tcDatabase instance;

    return &instance;
}

void tcDatabase::addTable(std::string tablebName)
{
    mvTables.push_back(tablebName);
}

/**
* Saves database classnames and keys to enable this to be replicated when scenario is loaded
*/
tcGameStream& tcDatabase::operator>>(tcGameStream& stream)
{
    tcDatabaseIterator iter(0);

    unsigned long nRecords = (unsigned long)(mcObjectData.GetCount());
    stream << nRecords;

    unsigned long nIterated = 0;
    for (iter.First(); !iter.IsDone(); iter.Next())
    {
        std::shared_ptr<tcDatabaseObject> obj = iter.Get();

        std::string databaseClass(obj->mzClass.c_str());
        stream << databaseClass;
        stream << obj->mnKey;
        nIterated++;
    }

    assert(nRecords == nIterated);
    if (nRecords != nIterated)
    {
        fprintf(stderr, "tcDatabase::operator>>(tcGameStream& stream) - nRecords != nIterated\n");
    }

    return stream;
}

/**
* Loads database classnames with forced keys to replicate database image from scenario
*/
tcGameStream& tcDatabase::operator<<(tcGameStream& stream)
{
    ClearForNewScenario();

    unsigned long nRecords;
    stream >> nRecords;


    std::vector<long> loadedKeys;

    std::string databaseClass;
    long key;
    bool allOK = true;
    std::string missingRecords;
    for (unsigned long n=0; n<nRecords; n++)
    {
        stream >> databaseClass;
        stream >> key;
        bool success = LoadRecordSqlForceKey(databaseClass.c_str(), key);
        if (success)
        {
            loadedKeys.push_back(key);
        }
        else
        {
            fprintf(stderr, "ERROR loading save file: failed to find record in database for %s\n",
                    databaseClass.c_str());
            missingRecords += databaseClass.c_str();
            missingRecords += ", ";
            assert(false);
            allOK = false;
        }
    }

    for (size_t n=0; n<loadedKeys.size(); n++)
    {
        LoadRecordOtherTables(loadedKeys[n]);
    }


    if (!allOK)
    {
        ////wxMessageBox("Failed to find some database records: %s database and scenario do not match!", "Database-Scenario Mismatch", wxICON_ERROR);
    }

    return stream;
}


/**
* Should be called once after the database is loaded or modified
*/
void tcDatabase::BuildDictionaries()
{
    nameToKey.clear();

    std::map<std::string, long>::iterator mapIter;

    tcDatabaseIterator iter(0);
    for (iter.First(); !iter.IsDone(); iter.Next())
    {
        std::shared_ptr<tcDatabaseObject> obj = iter.Get();
        assert(obj);
        assert(obj->mnKey != -1);

        std::string className = obj->mzClass.c_str();

        mapIter = nameToKey.find(className);
        if (mapIter == nameToKey.end())
        {
            nameToKey[className] = obj->mnKey;
        }
        else
        {
            fprintf(stderr, "Error - tcDatabase::BuildDictionaries - "
                            "Ignoring duplicate class name in database (%s)\n", className.c_str());
        }

    }
}


/**
* Populates nameToTable and tableToName for faster dynamic loads
*/
void tcDatabase::BuildTableLookup()
{
    tcOptions* options = tcOptions::Get();
    bool useNativeNames = (options->natoNames == 0);

    nameToTable.clear();
    tableSummary.clear();
    tableToIndex.clear();
    nameToDisplayName.clear();
    classSummary.clear();



    // for each table, get list of all database classes in table, and update cross-reference dictionaries
    long table_idx = 0;
    for (size_t n=0; n<mvTables.size(); n++)
    {
        tableToIndex[mvTables[n]] = table_idx++;
        std::vector<RecordSummary> tableRecords;
        std::string command =
            strutil::format("select DatabaseClass,NATO_ASCC,ClassificationId,InitialYear,FinalYear,Country from \"%s\";", mvTables[n].c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader result = sqlCmd.executereader();
        while (result.read())
        {
            std::string databaseClass = result.getstring(0);
            std::string databaseDisplayClass = result.getstring(1);
            if (useNativeNames || (databaseDisplayClass.size() == 0))
            {
                databaseDisplayClass = databaseClass; // empty entry means use default name for NATO/ASCC
            }
            unsigned int classificationId = (unsigned int)result.getint(2);
            float initialYear = (float)result.getdouble(3);
            float finalYear = (float)result.getdouble(4);
            std::string country = result.getstring(5);
            nameToTable[databaseClass] = mvTables[n];
            RecordSummary rs;
            rs.databaseClass = databaseClass;
            rs.databaseDisplayClass = databaseDisplayClass;
            rs.classificationId = classificationId;
            rs.yearStart = initialYear;
            rs.yearStop = finalYear;
            rs.country = country;

            tableRecords.push_back(rs);

            nameToDisplayName[databaseClass] = databaseDisplayClass;
            classSummary[databaseClass] = rs;
        }
        tableSummary[mvTables[n]] = tableRecords;
    }

    // build launcher table
    {
        mvTables.push_back("launcher");
        tableToIndex["launcher"] = table_idx++;
        std::vector<RecordSummary> tableRecords;

        std::string command = "select distinct DatabaseClass from launcher_configuration;";
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader launcherData = sqlCmd.executereader();

        while (launcherData.read())
        {
            std::string databaseClass = launcherData.getstring(0);
            unsigned int classificationId = 0;

            nameToTable[databaseClass] = "launcher";

            RecordSummary rs;
            rs.databaseClass = databaseClass;
            rs.classificationId = classificationId;
            tableRecords.push_back(rs);
        }

        tableSummary["launcher"] = tableRecords;
    }
}

/**
* Check for common database errors e.g. references to class names that don't
* exist in database.
*/
bool tcDatabase::CheckForErrors(const std::string& logFile)
{
    unsigned int errorCount = 0;
    // 打开文件，如果文件不存在则创建它，如果文件存在则清空它
    std::ofstream log(logFile, std::ios::out | std::ios::trunc);

    // 检查文件是否成功打开
    if (!log.is_open()) return false;
    std::chrono::system_clock::time_point dateTime =  std::chrono::system_clock::now();
    auto in_time_t = std::chrono::system_clock::to_time_t(dateTime);
    std::stringstream ss;
    ss << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %X");


    std::string s = strutil::format("%s : Checking database for errors", ss.str());
    log<<s<<std::endl;

    std::vector<std::string> platformTables;
    platformTables.push_back("ship");
    platformTables.push_back("air");
    platformTables.push_back("simpleair");
    platformTables.push_back("sub");
    platformTables.push_back("ground");
    platformTables.push_back("sonobuoy");

    // check for orphaned references
    CheckTableReferences("platform_names", "DatabaseClass", platformTables, "DatabaseClass", log, errorCount);

    CheckTableReferences("platform_setup", "DatabaseClass", platformTables, "DatabaseClass", log, errorCount);

    // *** check platform_sensor table
    std::vector<std::string> sensorTables;
    sensorTables.push_back("radar");
    sensorTables.push_back("sonar");
    sensorTables.push_back("optical");
    sensorTables.push_back("esm");
    sensorTables.push_back("ecm");

    // check for orphaned references
    CheckTableReferences("platform_sensor", "DatabaseClass", platformTables, "DatabaseClass", log, errorCount);

    CheckTableReferences("platform_sensor", "SensorClass", sensorTables, "DatabaseClass", log, errorCount);


    // *** check platform_magazine table
    // check for orphaned references
    CheckTableReferences("platform_magazine", "DatabaseClass", platformTables, "DatabaseClass", log, errorCount);


    std::vector<std::string> magazineTable;
    magazineTable.push_back("stores");
    CheckTableReferences("platform_magazine", "MagazineClass", magazineTable, "DatabaseClass", log, errorCount);


    // *** check platform_launcher table

    // check for orphaned references
    CheckTableReferences("platform_launcher", "DatabaseClass", platformTables, "DatabaseClass", log, errorCount);



    std::vector<std::string> launcherTable;
    launcherTable.push_back("launcher_configuration");
    CheckTableReferences("platform_launcher", "LauncherClass", launcherTable, "DatabaseClass", log, errorCount);


    CheckTableReferences("platform_launcher", "FireControlSensor", sensorTables, "DatabaseClass", log, errorCount);


    CheckTableReferences("platform_launcher", "FireControlSensor2", sensorTables, "DatabaseClass", log, errorCount);


    // missile table
    CheckTableReferences("missile", "SensorClass", sensorTables, "DatabaseClass", log, errorCount);


    std::vector<std::string> payloadTables;
    payloadTables.push_back("torpedo");
    payloadTables.push_back("ballistic");
    payloadTables.push_back("missile");
    CheckTableReferences("missile", "PayloadClass", payloadTables, "DatabaseClass", log, errorCount);


    // torpedo table
    std::vector<std::string> sonarTable;
    sonarTable.push_back("sonar");
    CheckTableReferences("torpedo", "sonarClass", sonarTable, "DatabaseClass", log, errorCount);


    // check RCS_Model references
    std::vector<std::string> sigTable;
    sigTable.push_back("signature");

    std::vector<std::string> rcsModelTables;
    rcsModelTables.push_back("air");
    rcsModelTables.push_back("ground");
    rcsModelTables.push_back("missile");
    rcsModelTables.push_back("ballistic_missile");
    rcsModelTables.push_back("ship");
    rcsModelTables.push_back("simpleair");
    rcsModelTables.push_back("sub");
    for (size_t n=0; n<rcsModelTables.size(); n++)
    {
        CheckTableReferences(rcsModelTables[n].c_str(), "RCS_Model", sigTable, "DatabaseClass", log, errorCount);
    }

    // check IR_Model references
    std::vector<std::string> irModelTables;
    irModelTables.push_back("air");
    irModelTables.push_back("ground");
    irModelTables.push_back("missile");
    irModelTables.push_back("ballistic_missile");
    irModelTables.push_back("ship");
    irModelTables.push_back("simpleair");
    irModelTables.push_back("sub");
    for (size_t n=0; n<irModelTables.size(); n++)
    {
        CheckTableReferences(irModelTables[n].c_str(), "IR_ModelA", sigTable, "DatabaseClass", log, errorCount);
        CheckTableReferences(irModelTables[n].c_str(), "IR_ModelB", sigTable, "DatabaseClass", log, errorCount);
        CheckTableReferences(irModelTables[n].c_str(), "IR_ModelC", sigTable, "DatabaseClass", log, errorCount);
    }

    // check DamageEffect references
    std::vector<std::string> damageEffect;
    damageEffect.push_back("damage_effect");

    std::vector<std::string> damageEffectTables;
    damageEffectTables.push_back("air");
    damageEffectTables.push_back("ground");
    damageEffectTables.push_back("missile");
    damageEffectTables.push_back("ballistic");
    damageEffectTables.push_back("ballistic_missile");
    damageEffectTables.push_back("torpedo");
    damageEffectTables.push_back("ship");
    damageEffectTables.push_back("simpleair");
    damageEffectTables.push_back("sub");
    damageEffectTables.push_back("radar");
    damageEffectTables.push_back("sonar");
    damageEffectTables.push_back("optical");
    damageEffectTables.push_back("esm");
    for (size_t n=0; n<damageEffectTables.size(); n++)
    {
        CheckTableReferences(damageEffectTables[n].c_str(), "DamageEffect", damageEffect, "DatabaseClass", log, errorCount);
    }

    // check FlightportClass references
    std::vector<std::string> flightport;
    flightport.push_back("flightport");

    std::vector<std::string> flightportClassTables;
    flightportClassTables.push_back("ship");
    flightportClassTables.push_back("ground");
    for (size_t n=0; n<flightportClassTables.size(); n++)
    {
        CheckTableReferences(flightportClassTables[n].c_str(), "FlightportClass", flightport, "DatabaseClass", log, errorCount);
    }

    // check DamageModel references
    std::vector<std::string> weapon_damage;
    weapon_damage.push_back("weapon_damage");

    std::vector<std::string> damageModelTables;
    damageModelTables.push_back("missile");
    damageModelTables.push_back("ballistic");
    damageModelTables.push_back("ballistic_missile");
    damageModelTables.push_back("torpedo");

    for (size_t n=0; n<damageModelTables.size(); n++)
    {
        CheckTableReferences(damageModelTables[n].c_str(), "DamageModel", weapon_damage, "DatabaseClass", log, errorCount);
    }

    // check launcher_configuration ChildClass references
    std::vector<std::string> launcherChildTables;
    launcherChildTables.push_back("missile");
    launcherChildTables.push_back("ballistic");
    launcherChildTables.push_back("ballistic_missile");
    launcherChildTables.push_back("torpedo");
    launcherChildTables.push_back("cm");
    launcherChildTables.push_back("sonobuoy");
    launcherChildTables.push_back("fueltank");

    CheckTableReferences("launcher_configuration", "ChildClass", launcherChildTables, "DatabaseClass", log, errorCount);

    s=strutil::format("%d errors found", errorCount);

    log.close();

    if (errorCount > 0)
    {
        std::ofstream log(logFile, std::ios::out | std::ios::app);

        // 检查文件是否成功打开
        if (!log.is_open()) return false;


        std::string logText=strutil::format("%d error(s) found in database, see %s\n", errorCount, logFile.c_str());

    }


    else
    {
        // //wxMessageBox("No errors found", "Database Error Check");
    }
    return (errorCount == 0);
}

bool tcDatabase::CheckTableReferences(const char* table,
                                      const char* field,
                                      const std::vector<std::string>& refTables,
                                      const char* refField,
                                      std::ofstream& log,
                                      unsigned int& errorCount)
{
    unsigned int startErrorCount = errorCount;

    std::string command = strutil::format("select distinct %s from %s;", field, table);
    sqlite3_command sqlCmd(*sqlConnection, command);
    sqlite3_reader results = sqlCmd.executereader();

    std::string s;

    while (results.read())
    {
        std::string reference = results.getstring(0);
        bool found = false;

        for (size_t n=0; (n<refTables.size())&&(!found); n++)
        {
            command=strutil::format("select * from %s where %s = \"%s\";", refTables[n].c_str(), refField, reference.c_str());
            sqlite3_command sqlCmd2(*sqlConnection, command);
            sqlite3_reader results2 = sqlCmd2.executereader();
            if (results2.read())
            {
                found = true;
            }
        }

        std::string reference2(reference.c_str());
        bool hasWildcard = strutil::contains(reference2,"*") || strutil::contains(reference2,"?"); // skip references with wildcards

        if (!found && (reference.size() > 0) && (!hasWildcard))
        {
            errorCount++;

            s=strutil::format("%s : \"%s\" not found. Referenced by ", table, reference.c_str());
            
            command=strutil::format("select * from %s where %s = \"%s\";", table, field, reference.c_str());
            sqlite3_command sqlCmd2(*sqlConnection, command);
            sqlite3_reader results2 = sqlCmd2.executereader();

            std::string errorPlatforms;
            while (results2.read())
            {
                errorPlatforms += "\"";
                errorPlatforms += results2.getstring(0).c_str(); // assumes this is databaseclass
                errorPlatforms += "\"";
                errorPlatforms += " ";
            }
            s += errorPlatforms;
            log<<s<<std::endl;
            
        }
        
    }

    return (startErrorCount == errorCount);
}


/**
* Should be called prior to updating database
*/
void tcDatabase::ClearDictionaries()
{
    nameToKey.clear();
}

/**
* Loads cross_reference table from database, used for translating different names to common db record
*/
void tcDatabase::LoadCrossReferenceTable()
{
    crossReference.clear();

    std::string command = strutil::format("select * from cross_reference;");

    try
    {
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            std::string lookupName = tableData.getstring(0);
            std::string referenceName = tableData.getstring(1);

            crossReference[lookupName] = referenceName;
        }
    }
    catch (...)
    {
        ////wxMessageBox("Error trying to load cross_reference table from database", "Error");
    }
}

/**
* Adds launcher data to database for launcher with name <databaseClass>
* @return database key if found or -1 if not found
*/
long tcDatabase::LoadLauncherData(const char* databaseClass, long forcedKey)
{
    std::string launcherName(databaseClass);

    // check launcher name for invalid characters
    size_t nReplacements = strutil::replace_all( launcherName,"\"", "\"\""); // replace " with "" for sqlite query
    if (nReplacements > 0)
    {
        fprintf(stderr, "tcDatabase::LoadLauncherConfigs - Warning: \" in DatabaseClass string (%s)\n",
                databaseClass);
    }

    if (ObjectExists(launcherName))
    {
        //assert(false);
        return -1;
    }

    // create launcher db obj
    std::shared_ptr<tcLauncherDBObject> launcherData = std::make_shared<tcLauncherDBObject>(std::string(launcherName.c_str()));

    // add launcher configurations
    std::string command2 =
        strutil::format("select * from launcher_configuration where DatabaseClass=\"%s\";",
                        launcherName.c_str());
    sqlite3_command sqlCmd2(*sqlConnection, command2);
    sqlite3_reader tableData = sqlCmd2.executereader();
    while (tableData.read())
    {
        std::string childClass = tableData.getstring(1);
        unsigned short childCapacity = (unsigned short)tableData.getlong(2);
        float loadTime_s = (float)tableData.getdouble(3);
        float cycleTime_s = (float)tableData.getdouble(4);

        assert(childCapacity > 0);
        launcherData->AddConfig(childClass, childCapacity, loadTime_s, cycleTime_s);
    }

    if (launcherData->GetNumberConfigurations() > 0)
    {
        if (forcedKey == -1)
        {
            // add launcher to database
            long key = -1;
            mcObjectData.AddElement(launcherData, key); // add to database, key gets new key val
            launcherData->mnKey = key;

            return key;
        }
        else
        {
            mcObjectData.AddElementForceKey(launcherData, forcedKey);
            launcherData->mnKey = forcedKey;
            return forcedKey;
        }
    }
    else
    {
        fprintf(stderr, "LoadLauncherData - %s not found in launcher_configuration table\n", launcherName.c_str());
        return -1;
    }
}

/**
* Loads ALL launcher data
* Also builds tcLauncherDBObject data with "select distinct DatabaseClass from launcher_configuration"
*/
void tcDatabase::LoadLauncherConfigs()
{
    // build tcLauncherDBObject data
    std::string command = "select distinct DatabaseClass from launcher_configuration;";
    sqlite3_command sqlCmd(*sqlConnection, command);
    sqlite3_reader launcherData = sqlCmd.executereader();
    while (launcherData.read())
    {
        std::string launcherName(launcherData.getstring(0));
        LoadLauncherData(launcherName.c_str());
    }

}


void tcDatabase::LoadPlatformTables()
{
    // iterate through database
    int nCount = mcObjectData.GetCount();
    long currentPos = mcObjectData.GetStartPosition();
    std::shared_ptr<tcDatabaseObject> obj = nullptr;
    long id = -1;

    for (int n=0; n<nCount; n++)
    {
        mcObjectData.GetNextAssoc(currentPos, id, obj);
        if (std::shared_ptr<tcPlatformDBObject> platformData = std::dynamic_pointer_cast<tcPlatformDBObject>(obj))
        {
            // clear old info (for now)
            platformData->maLauncherClass.clear();

            platformData->launcherDescription.clear();
            platformData->launcherName.clear();
            platformData->launcherFOV_deg.clear();
            platformData->launcherAz_deg.clear();
            platformData->launcherEl_deg.clear();
            platformData->launcherFireControl.clear();
            platformData->launcherFireControl2.clear();
            platformData->launcherIsReloadable.clear();
            platformData->launcherId.clear();

            platformData->mnNumLaunchers = 0;
            platformData->maMagazineClass.clear();
            platformData->magazineId.clear();
            platformData->mnNumMagazines = 0;

            // add launchers
            std::string command =
                strutil::format("select * from platform_launcher where DatabaseClass=\"%s\";",
                                obj->mzClass.c_str());
            sqlite3_command sqlCmd(*sqlConnection, command);
            sqlite3_reader tableData = sqlCmd.executereader();
            while ((platformData->mnNumLaunchers < platformData->MAXLAUNCHERS) && tableData.read())
            {

                std::string launcherClass = tableData.getstring(1);
                unsigned int launcherId = (unsigned int)tableData.getint(2);
                std::string launcherDescription = tableData.getstring(3);
                std::string launcherName = tableData.getstring(4);
                float launcherFOV_deg = (float)tableData.getdouble(5);
                float launcherAz_deg = (float)tableData.getdouble(6);
                float launcherEl_deg = (float)tableData.getdouble(7);
                std::string fireControl = tableData.getstring(8);
                std::string fireControl2 = tableData.getstring(9);
                bool isReloadable = tableData.getint(10) != 0;
                //按launcherId 排序插入
                //找到launcherId合适插入的位置
                auto it = std::lower_bound(platformData->launcherId.begin(), platformData->launcherId.end(), launcherId);
                size_t insertindex = std::distance(platformData->launcherId.begin(), it);
                platformData->launcherId.insert(platformData->launcherId.begin()+insertindex, launcherId);
                platformData->maLauncherClass.insert(platformData->maLauncherClass.begin()+insertindex,launcherClass);
                // platformData->maLauncherClass.push_back(launcherClass);
                // platformData->launcherId.push_back(launcherId);
                platformData->launcherDescription.push_back(launcherDescription);
                platformData->launcherName.push_back(launcherName);
                platformData->launcherFOV_deg.push_back(launcherFOV_deg);
                platformData->launcherAz_deg.push_back(launcherAz_deg);
                platformData->launcherEl_deg.push_back(launcherEl_deg);
                platformData->launcherFireControl.push_back(fireControl);
                platformData->launcherFireControl2.push_back(fireControl2);
                platformData->launcherIsReloadable.push_back(isReloadable);

                platformData->mnNumLaunchers++;
            }
            if ((platformData->mnNumLaunchers == platformData->MAXLAUNCHERS) && tableData.read())
            {
                std::string msg = strutil::format("%s exceeded maximum launcher count (%d), ignoring excess", platformData->MAXLAUNCHERS, platformData->mzClass.c_str());
                ////wxMessageBox(msg);
            }
        }




        // add magazines (separate "if" to make it easier to modularize late)
        if (std::shared_ptr<tcPlatformDBObject> platformData = std::dynamic_pointer_cast<tcPlatformDBObject>(obj))
        {
            std::string command =
                strutil::format("select * from platform_magazine where DatabaseClass=\"%s\";",
                                obj->mzClass.c_str());
            sqlite3_command sqlCmd(*sqlConnection, command);
            sqlite3_reader tableData = sqlCmd.executereader();
            while ((platformData->mnNumMagazines < platformData->MAXMAGAZINES) && tableData.read())
            {
                std::string magazineClass = tableData.getstring(1);
                unsigned int magId = tableData.getint(2);

                auto it = std::lower_bound(platformData->magazineId.begin(),
                                           platformData->magazineId.end(),
                                           magId);
                size_t insertindex = std::distance(platformData->magazineId.begin(), it);
                platformData->magazineId.insert(platformData->magazineId.begin()+insertindex,
                                                magId);
                platformData->maMagazineClass.insert(platformData->maMagazineClass.begin()+insertindex,
                                                     magazineClass);

                // platformData->maMagazineClass.push_back(magazineClass);
                // platformData->magazineId.push_back(magId);

                platformData->mnNumMagazines++;
            }
            assert(platformData->maMagazineClass.size() == platformData->magazineId.size());

            platformData->ReorderMagazines();
        }

        if (std::shared_ptr<tcSensorPlatformDBObject> sensorPlatData =obj->GetComponent<tcSensorPlatformDBObject>())
        {
            // clear old info
            sensorPlatData->sensorClass.clear();
            sensorPlatData->sensorAz.clear();

            // add sensors
            std::string command =
                strutil::format("select * from platform_sensor where DatabaseClass=\"%s\";",
                                obj->mzClass.c_str());
            sqlite3_command sqlCmd(*sqlConnection, command);
            sqlite3_reader tableData = sqlCmd.executereader();
            while (tableData.read())
            {
                std::string sensorClass = tableData.getstring(1);
                float sensorAz = tableData.getdouble(2);

                sensorPlatData->sensorClass.push_back(sensorClass);
                sensorPlatData->sensorAz.push_back(sensorAz);
            }
        }

    }

}

/**
* Loads a single record into the cached database with key forced to value
* Normally used for MP client to synch database with server
* NOTE: LoadRecordOtherTables needs to be called after this method, this force key version does not do
*       this automatically to avoid automatically loading records and getting keys out of order
*
* @return true if found, false otherwise. Loads record into cached database
*/
bool tcDatabase::LoadRecordSqlForceKey(const char* databaseClass, long forcedKey)
{
    std::string databaseClassString(databaseClass);

    if (ObjectExists(databaseClassString))
    {
        assert(false); // duplicate load
        if (GetKey(databaseClass) == forcedKey)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    return LoadRecordSqlForceKeyExecute(databaseClass, forcedKey);
}

void tcDatabase::ReloadRecord(const char* databaseClass)
{
    long forcedKey = -1;
    std::string databaseClassString(databaseClass);
    if (ObjectExists(databaseClassString))
    {
       std::shared_ptr< tcDatabaseObject> data = GetObject(databaseClass);
        if (data != 0)
        {
            forcedKey = data->mnKey;
        }
        else {assert(false);}
    }

    LoadRecordSqlForceKeyExecute(databaseClass, forcedKey);
}


/**
* Loads without checking for duplicates, did this way to avoid copying and duplicating code
*/
bool tcDatabase::LoadRecordSqlForceKeyExecute(const char* databaseClass, long forcedKey)
{
    std::string databaseClassString(databaseClass);

    // find table for this record
    std::map<std::string, std::string>::const_iterator iter =
        nameToTable.find(databaseClassString);

    if (iter == nameToTable.end())
    {
        //assert(false);
        return false;
    }

    std::string tableName(iter->second);

    std::map<std::string, long>::const_iterator iter_idx =
        tableToIndex.find(tableName);

    if (iter_idx == tableToIndex.end())
    {
        assert(false);
        return false;
    }
    long table_idx = iter_idx->second;
    long key = -1;

    switch (table_idx)
    {
    case 0: assert(tableName == "ship");
        {
            tcDBObjSerializerSql<tcShipDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 1: assert(tableName == "simpleair");
        {
            tcDBObjSerializerSql<tcSimpleAirDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 2: assert(tableName == "ground");
        {
            tcDBObjSerializerSql<tcGroundDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 3: assert(tableName == "missile");
        {
            tcDBObjSerializerSql<tcMissileDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 4: assert(tableName == "radar");
        {
            tcDBObjSerializerSql<tcRadarDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 5: assert(tableName == "esm");
        {
            tcDBObjSerializerSql<tcESMDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 6: assert(tableName == "optical");
        {
            tcDBObjSerializerSql<tcOpticalDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 7: assert(tableName == "ecm");
        {
            tcDBObjSerializerSql<tcECMDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 8: assert(tableName == "sonar");
        {
            tcDBObjSerializerSql<tcSonarDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 9: assert(tableName == "air");
        {
            tcDBObjSerializerSql<tcJetDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 10: assert(tableName == "flightport");
        {
            tcDBObjSerializerSql<tcFlightportDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 11: assert(tableName == "ballistic");
        {
            tcDBObjSerializerSql<tcBallisticDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 12: assert(tableName == "stores");
        {
            tcDBObjSerializerSql<tcStoresDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 13: assert(tableName == "torpedo");
        {
            tcDBObjSerializerSql<tcTorpedoDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 14: assert(tableName == "sonobuoy");
        {
            tcDBObjSerializerSql<tcSonobuoyDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 15: assert(tableName == "item");
        {
            tcDBObjSerializerSql<tcItemDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 16: assert(tableName == "sub");
        {
            tcDBObjSerializerSql<tcSubDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 17: assert(tableName == "fueltank");
        {
            tcDBObjSerializerSql<tcFuelTankDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 18: assert(tableName == "cm");
        {
            tcDBObjSerializerSql<tcCounterMeasureDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 19: assert(tableName == "ballistic_missile");
        {
            tcDBObjSerializerSql<tcBallisticMissileDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecordForceKey(databaseClass, forcedKey);
        }
        break;
    case 20: assert(tableName == "launcher");
        {
            key = LoadLauncherData(databaseClass, forcedKey);
        }
        break;
    default:
        assert(false);
        break;
    }

    if (key != -1)
    {
        nameToKey[databaseClassString] = key;

//LoadRecordOtherTables(key); don't do this here, it gets the names-keys out of synch in game serializer load

#ifdef _DEBUG
        fprintf(stdout, "tcDatabase::LoadRecordSql - loaded %s (total %d)\n", databaseClass, mcObjectData.GetCount());
#endif
        return true;
    }
    else
    {
        return false;
    }
}


/**
* Loads a single record into the cached database
*
* @return true if found, false otherwise. Loads record into cached database
*/
bool tcDatabase::LoadRecordSql(const char* databaseClass)
{
    std::string databaseClassString(databaseClass);

    if (ObjectExists(databaseClassString))
    {
        assert(false); // duplicate load
        return true;
    }

    // find table for this record
    std::map<std::string, std::string>::const_iterator iter =
        nameToTable.find(databaseClassString);

    if (iter == nameToTable.end())
    {
        //assert(false);
        return false;
    }

    std::string tableName(iter->second);

    std::map<std::string, long>::const_iterator iter_idx =
        tableToIndex.find(tableName);

    if (iter_idx == tableToIndex.end())
    {
        assert(false);
        return false;
    }
    long table_idx = iter_idx->second;
    long key = -1;

    switch (table_idx)
    {
    case 0: assert(tableName == "ship");
        {
            tcDBObjSerializerSql<tcShipDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 1: assert(tableName == "simpleair");
        {
            tcDBObjSerializerSql<tcSimpleAirDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 2: assert(tableName == "ground");
        {
            tcDBObjSerializerSql<tcGroundDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 3: assert(tableName == "missile");
        {
            tcDBObjSerializerSql<tcMissileDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 4: assert(tableName == "radar");
        {
            tcDBObjSerializerSql<tcRadarDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 5: assert(tableName == "esm");
        {
            tcDBObjSerializerSql<tcESMDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 6: assert(tableName == "optical");
        {
            tcDBObjSerializerSql<tcOpticalDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 7: assert(tableName == "ecm");
        {
            tcDBObjSerializerSql<tcECMDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 8: assert(tableName == "sonar");
        {
            tcDBObjSerializerSql<tcSonarDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 9: assert(tableName == "air");
        {
            tcDBObjSerializerSql<tcJetDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 10: assert(tableName == "flightport");
        {
            tcDBObjSerializerSql<tcFlightportDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 11: assert(tableName == "ballistic");
        {
            tcDBObjSerializerSql<tcBallisticDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 12: assert(tableName == "stores");
        {
            tcDBObjSerializerSql<tcStoresDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 13: assert(tableName == "torpedo");
        {
            tcDBObjSerializerSql<tcTorpedoDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 14: assert(tableName == "sonobuoy");
        {
            tcDBObjSerializerSql<tcSonobuoyDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 15: assert(tableName == "item");
        {
            tcDBObjSerializerSql<tcItemDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 16: assert(tableName == "sub");
        {
            tcDBObjSerializerSql<tcSubDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 17: assert(tableName == "fueltank");
        {
            tcDBObjSerializerSql<tcFuelTankDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 18: assert(tableName == "cm");
        {
            tcDBObjSerializerSql<tcCounterMeasureDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 19: assert(tableName == "ballistic_missile");
        {
            tcDBObjSerializerSql<tcBallisticMissileDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 20: assert(tableName == "space");
        {
            tcDBObjSerializerSql<tcSpaceDBObject> serializer(this, *sqlConnection, tableName);
            key = serializer.LoadRecord(databaseClass);
        }
        break;
    case 21: assert(tableName == "launcher");
        {
            key = LoadLauncherData(databaseClass);
        }
        break;

    default:
        assert(false);
        break;
    }

    if (key != -1)
    {
        nameToKey[databaseClassString] = key;

        LoadRecordOtherTables(key);

#ifdef _DEBUG
        fprintf(stdout, "tcDatabase::LoadRecordSql - loaded %s (total %d)\n", databaseClass, mcObjectData.GetCount());
#endif
        return true;
    }
    else
    {
        return false;
    }
}


/**
* Specialized version of LoadPlatformTables for this record
*/
void tcDatabase::LoadRecordOtherTables(long key)
{
    std::shared_ptr<tcDatabaseObject> obj = GetObject(key);
    assert(obj != 0);

    if (std::shared_ptr<tcPlatformDBObject> platformData = std::dynamic_pointer_cast<tcPlatformDBObject>(obj))
    {
        // clear old info (for now)
        platformData->maLauncherClass.clear();

        platformData->launcherDescription.clear();
        platformData->launcherName.clear();
        platformData->launcherFOV_deg.clear();
        platformData->launcherAz_deg.clear();
        platformData->launcherEl_deg.clear();
        platformData->launcherFireControl.clear();
        platformData->launcherFireControl2.clear();
        platformData->launcherIsReloadable.clear();
        platformData->launcherId.clear();

        platformData->mnNumLaunchers = 0;
        platformData->maMagazineClass.clear();
        platformData->magazineId.clear();
        platformData->mnNumMagazines = 0;
        {   // add launchers
            std::string command =
                strutil::format("select * from platform_launcher where DatabaseClass=\"%s\";",
                                obj->mzClass.c_str());
            sqlite3_command sqlCmd(*sqlConnection, command);
            sqlite3_reader tableData = sqlCmd.executereader();
            while ((platformData->mnNumLaunchers < platformData->MAXLAUNCHERS) && tableData.read())
            {
                std::string launcherClass = tableData.getstring(1);
                unsigned int launcherId = (unsigned int)tableData.getint(2);
                std::string launcherDescription = tableData.getstring(3);
                std::string launcherName = tableData.getstring(4);
                float launcherFOV_deg = (float)tableData.getdouble(5);
                float launcherAz_deg = (float)tableData.getdouble(6);
                float launcherEl_deg = (float)tableData.getdouble(7);
                std::string fireControl = tableData.getstring(8);
                std::string fireControl2 = tableData.getstring(9);
                bool isReloadable = tableData.getint(10) != 0;


                auto it = std::lower_bound(platformData->launcherId.begin(), platformData->launcherId.end(), launcherId);
                size_t insertindex = std::distance(platformData->launcherId.begin(), it);
                platformData->launcherId.insert(platformData->launcherId.begin()+insertindex, launcherId);
                platformData->maLauncherClass.insert(platformData->maLauncherClass.begin()+insertindex,launcherClass);

                // platformData->maLauncherClass.push_back(launcherClass);
                // platformData->launcherId.push_back(launcherId);
                platformData->launcherDescription.push_back(launcherDescription);
                platformData->launcherName.push_back(launcherName);
                platformData->launcherFOV_deg.push_back(launcherFOV_deg);
                platformData->launcherAz_deg.push_back(launcherAz_deg);
                platformData->launcherEl_deg.push_back(launcherEl_deg);
                platformData->launcherFireControl.push_back(fireControl);
                platformData->launcherFireControl2.push_back(fireControl2);
                platformData->launcherIsReloadable.push_back(isReloadable);

                platformData->mnNumLaunchers++;
            }

            if ((platformData->mnNumLaunchers == platformData->MAXLAUNCHERS) && tableData.read())
            {
                std::string msg = strutil::format("%s exceeded maximum launcher count (%d), ignoring excess", platformData->MAXLAUNCHERS, platformData->mzClass.c_str());
                //wxMessageBox(msg);
            }
        }

        { // add magazines
            std::string command =
                strutil::format("select * from platform_magazine where DatabaseClass=\"%s\";",
                                obj->mzClass.c_str());
            sqlite3_command sqlCmd(*sqlConnection, command);
            sqlite3_reader tableData = sqlCmd.executereader();
            while ((platformData->mnNumMagazines < platformData->MAXMAGAZINES) && tableData.read())
            {

                std::string magazineClass = tableData.getstring(1);
                unsigned int magId = tableData.getint(2);

                auto it = std::lower_bound(platformData->magazineId.begin(),
                                           platformData->magazineId.end(),
                                           magId);
                size_t insertindex = std::distance(platformData->magazineId.begin(), it);
                platformData->magazineId.insert(platformData->magazineId.begin()+insertindex,
                                                magId);
                platformData->maMagazineClass.insert(platformData->maMagazineClass.begin()+insertindex,
                                                     magazineClass);

                // std::string magazineClass = tableData.getstring(1);
                // platformData->maMagazineClass.push_back(magazineClass);

                // unsigned int magId = tableData.getint(2);
                // platformData->magazineId.push_back(magId);

                platformData->mnNumMagazines++;
            }

            platformData->ReorderMagazines();
        }

    } // if (tcPlatformDBObject* platformData =

    if (std::shared_ptr<tcSensorPlatformDBObject> sensorPlatData = obj->GetComponent<tcSensorPlatformDBObject>())
    {
        // clear old info
        sensorPlatData->sensorClass.clear();
        sensorPlatData->sensorAz.clear();

        // add sensors
        std::string command =
            strutil::format("select * from platform_sensor where DatabaseClass=\"%s\";",
                            obj->mzClass.c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            std::string sensorClass = tableData.getstring(1);
            float sensorAz = tableData.getdouble(2);

            sensorPlatData->sensorClass.push_back(sensorClass);
            sensorPlatData->sensorAz.push_back(sensorAz);
        }
    } // if (std::shared_ptr<tcSensorPlatformDBObject> sensorPlatData =

}

/**
* loads info from country_data and country_names tables
*/
void tcDatabase::ReadCountryData()
{
    // country_data table
    countryData.clear();

    {
        std::string command = strutil::format("select * from country_data;");

        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            std::string countryName = tableData.getstring(0);
            std::string navalEnsign = tableData.getstring(1);

            tcCountryData temp(countryName, navalEnsign);
            countryData[countryName] = temp;
        }

        //		unknownEnsign = tc3DWindow2::LoadTexture("flags\\negative.png");
    }
    // country_names table
    countryNameChanges.clear();

    {
        // get unique list of area names ("area" because not necessarily a sovereign nation)

        std::string command = "select distinct AreaName from country_names;";

        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();

        while (tableData.read())
        {
            std::string areaName = tableData.getstring(0);

            // get list of records for this areaName, each one is a different substitution to save
            std::string command2 = strutil::format("select * from country_names where AreaName=\"%s\";", areaName.c_str());
            sqlite3_command sqlCmd2(*sqlConnection, command2);
            sqlite3_reader tableData2 = sqlCmd2.executereader();

            tcCountryNameChanges nameChangeInfo;
            nameChangeInfo.countryName = areaName;
            while (tableData2.read())
            {
                tcCountryNameChanges::Substitution sub;

                bool parseError = false;

                std::string::const_iterator iterEnd;
                //                std::time_t now =     std::chrono::system_clock::to_time_t(sub.dateStart);

                //                   std::string s(30, '\0');
                //                   std::strftime(&s[0], s.size(), "%m/%d/%Y", std::localtime(&now));
                //                bool result = sub.dateStart.ParseFormat(tableData2.getstring(1).c_str(), "%m/%d/%Y", &iterEnd);
                //                parseError = parseError || (result == 0);

                //                result = sub.dateStop.ParseFormat(tableData2.getstring(2).c_str(), "%m/%d/%Y", &iterEnd);
                //                parseError = parseError || (result == false);

                sub.name = tableData2.getstring(3);

                if (!parseError)
                {
                    nameChangeInfo.substitutions.push_back(sub);
                }
                else
                {
                    assert(false);
                    fprintf(stderr, "Error parsing dates in country_names table (%s)\n", areaName.c_str());
                }
            }

            countryNameChanges[areaName] = nameChangeInfo;
        }
    }
}


void tcDatabase::ReadWriteSql(const std::string& fileName, bool load)
{
    std::ifstream file(fileName);
    bool fileValid = file.good();

    if (!fileValid)
    {
        std::string s = strutil::format("Database file not found (%s)", fileName.c_str());
        ////wxMessageBox(s, "Database error", wxICON_ERROR);
        return;
    }

    try
    {
        ReportProgress("Database opening file", 0);
        sqlConnectionLocal.close(); // in case it's been previously opened to different filename
        sqlConnectionLocal.open(fileName.c_str());
        sqlConnection = &sqlConnectionLocal;
    }
    catch (sqlite3x::database_error err)
    {
        //        //wxMessageBox(err.what(), "Database error", wxICON_ERROR);
        return;
    }

    ReadWriteSql(sqlConnection, load);
}


void tcDatabase::ReadWriteSql(sqlite3x::sqlite3_connection* sqlConnectionNew, bool load)
{
    sqlConnection = sqlConnectionNew;

    ReportProgress("DB signature models", 0.3f);
    // tcSignatureModel, need these loaded before platform db entries
    {
        tcDBMapSerializerSql<tcSignatureModel>
            serializer(this, signatureModelData, *sqlConnection, "signature");
        if (load) serializer.Load();
        else serializer.Save();
    }

    ReportProgress("DB acoustic models", 0.4f);
    // tcAcousticModel, need these loaded before platform db entries
    {
        tcDBMapSerializerSql<tcAcousticModel>
            serializer(this, acousticModelData, *sqlConnection, "acoustic_noise");
        if (load) serializer.Load();
        else serializer.Save();
    }


    if (load)
    {
        ReportProgress("DB country data", 0.5f);
        ReadCountryData();

        ReportProgress("DB cross-reference", 0.6f);
        LoadCrossReferenceTable();

        ReportProgress("DB weapon damage", 0.7f);
        weaponDamageData.ReadSql(*sqlConnection, "weapon_damage");
        
        ReportProgress("DB damage effect", 0.8f);
        damageEffectData.ReadSql(*sqlConnection, "damage_effect");

        ReportProgress("DB building lookup", 0.9f);
        BuildTableLookup();

        ReportProgress("DB load complete", 0.95f);
    }

    if (useDynamicLoad) return; // load records when needed, return

    // tcShipDBObject
    {
        tcDBObjSerializerSql<tcShipDBObject>
            serializer(this, *sqlConnection, "ship");
        if (load) serializer.Load();
        else serializer.Save();
    }

    // tcSimpleAirDBObject
    {
        tcDBObjSerializerSql<tcSimpleAirDBObject>
            serializer(this, *sqlConnection, "simpleair");
        if (load) serializer.Load();
        else serializer.Save();
    }

    // tcGroundDBObject
    {
        tcDBObjSerializerSql<tcGroundDBObject>
            serializer(this, *sqlConnection, "ground");
        if (load) serializer.Load();
        else serializer.Save();
    }


    // tcMissileDBObject
    {
        tcDBObjSerializerSql<tcMissileDBObject>
            serializer(this, *sqlConnection, "missile");
        if (load) serializer.Load();
        else serializer.Save();
    }

    // launcher table removed 13JUN2009, launcher list is obtained with "select distinct DatabaseClass from launcher_configuration"
    // tcLauncherDBObject
    //{
    //	tcDBObjSerializerSql<tcLauncherDBObject>
    //		serializer(this, sqlConnection, "launcher");
    //	if (load) serializer.Load();
    //	else serializer.Save();
    //}


    // tcRadarDBObject
    {
        tcDBObjSerializerSql<tcRadarDBObject>
            serializer(this, *sqlConnection, "radar");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcESMDBObject
    {
        tcDBObjSerializerSql<tcESMDBObject>
            serializer(this, *sqlConnection, "esm");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcOpticalDBObject
    {
        tcDBObjSerializerSql<tcOpticalDBObject>
            serializer(this, *sqlConnection, "optical");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcECMDBObject
    {
        tcDBObjSerializerSql<tcECMDBObject>
            serializer(this, *sqlConnection, "ecm");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcSonarDBObject
    {
        tcDBObjSerializerSql<tcSonarDBObject>
            serializer(this, *sqlConnection, "sonar");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcJetDBObject
    {
        tcDBObjSerializerSql<tcJetDBObject>
            serializer(this, *sqlConnection, "air");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcFlightportDBObject
    {
        tcDBObjSerializerSql<tcFlightportDBObject>
            serializer(this, *sqlConnection, "flightport");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcBallisticDBObject
    {
        tcDBObjSerializerSql<tcBallisticDBObject>
            serializer(this, *sqlConnection, "ballistic");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcStoresDBObject
    {
        tcDBObjSerializerSql<tcStoresDBObject>
            serializer(this, *sqlConnection, "stores");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcTorpedoDBObject
    {
        tcDBObjSerializerSql<tcTorpedoDBObject>
            serializer(this, *sqlConnection, "torpedo");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcSonobuoyDBObject
    {
        tcDBObjSerializerSql<tcSonobuoyDBObject>
            serializer(this, *sqlConnection, "sonobuoy");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcItemDBObject
    {
        tcDBObjSerializerSql<tcItemDBObject>
            serializer(this, *sqlConnection, "item");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcSubDBObject
    {
        tcDBObjSerializerSql<tcSubDBObject>
            serializer(this, *sqlConnection, "sub");
        if (load) serializer.Load();
        else serializer.Save();
    }
    // tcFuelTankDBObject
    {
        tcDBObjSerializerSql<tcFuelTankDBObject>
            serializer(this, *sqlConnection, "fueltank");
        if (load) serializer.Load();
        else serializer.Save();
    }

    // tcCounterMeasureDBObject
    {
        tcDBObjSerializerSql<tcCounterMeasureDBObject>
            serializer(this, *sqlConnection, "cm");
        if (load) serializer.Load();
        else serializer.Save();
    }

    // tcBallisticMissileDBObject
    {
        tcDBObjSerializerSql<tcBallisticMissileDBObject>
            serializer(this, *sqlConnection, "ballistic_missile");
        if (load) serializer.Load();
        else serializer.Save();
    }



    if (load)
    {
        LoadPlatformTables();
        LoadLauncherConfigs();
    }

    fprintf(stdout, "tcDatabase::ReadWriteSql - full cache mode - %d records loaded\n", mcObjectData.GetCount());

    BuildDictionaries();

    if (load)
    {
        // load loadout info for air platforms
        // do after BuildDictionaries to make validate more efficient
        //LoadLoadouts(); // merged with platform_setup feature SEP 2010
    }
}

/**
* Keep only the first word in each entry.
*/
void tcDatabase::CleanSqlColumnText(std::string& columnText)
{
    std::string s = columnText.c_str();
    columnText = "";

    while (s.size() > 0)
    {
        std::string term = strutil::split(s,',')[0];
        term =strutil::split( term,' ')[0];

        columnText += term;
        s = strutil::split(s,',')[1];
        if (s.size() > 0)
        {
            columnText += ",";
        }
        //        std::string term = s.BeforeFirst(',');
        //        term = term.BeforeFirst(' ');

        //        columnText += term.c_str();
        //        s = s.AfterFirst(',');
        //        if (s.size() > 0)
        //        {
        //            columnText += ",";
        //        }
    }
}

void tcDatabase::LogSqlColumns(const std::string& fileName)
{

    tcFile log;
    log.Open(fileName.c_str(), tcFile::modeCreate | tcFile::modeWrite | tcFile::modeText);
    
    // tcShipDBObject
    {
        log.WriteString("ship,");
        std::string columns;
        tcShipDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcSimpleAirDBObject
    {
        log.WriteString("simpleair,");
        std::string columns;
        tcSimpleAirDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcGroundDBObject
    {
        log.WriteString("ground,");
        std::string columns;
        tcGroundDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcMissileDBObject
    {
        log.WriteString("missile,");
        std::string columns;
        tcMissileDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcLauncherDBObject
    /* @removed launcher table for now, 13JUN2009
    {
        log.WriteString("launcher,");
        std::string columns;
        tcLauncherDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }
    */

    // tcRadarDBObject
    {
        log.WriteString("radar,");
        std::string columns;
        tcRadarDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcESMDBObject
    {
        log.WriteString("esm,");
        std::string columns;
        tcESMDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcOpticalDBObject
    {
        log.WriteString("optical,");
        std::string columns;
        tcOpticalDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcECMDBObject
    {
        log.WriteString("ecm,");
        std::string columns;
        tcECMDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcSonarDBObject
    {
        log.WriteString("sonar,");
        std::string columns;
        tcSonarDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcJetDBObject
    {
        log.WriteString("air,");
        std::string columns;
        tcJetDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcFlightportDBObject
    {
        log.WriteString("flightport,");
        std::string columns;
        tcFlightportDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcBallisticDBObject
    {
        log.WriteString("ballistic,");
        std::string columns;
        tcBallisticDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcStoresDBObject
    {
        log.WriteString("stores,");
        std::string columns;
        tcStoresDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcTorpedoDBObject
    {
        log.WriteString("torpedo,");
        std::string columns;
        tcTorpedoDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcSonobuoyDBObject
    {
        log.WriteString("sonobuoy,");
        std::string columns;
        tcSonobuoyDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcItemDBObject
    {
        log.WriteString("item,");
        std::string columns;
        tcItemDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcSubDBObject
    {
        log.WriteString("sub,");
        std::string columns;
        tcSubDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

    // tcFuelTankDBObject
    {
        log.WriteString("fueltank,");
        std::string columns;
        tcFuelTankDBObject::AddSqlColumns(columns);
        CleanSqlColumnText(columns);
        log.WriteString(columns.c_str());
        log.WriteString("\n");
    }

}


/**
* @param suffix string to append after type name, e.g. "_2b" -> database_2b.sql
* @param load true to load DB from sql database, false to save
*/
void tcDatabase::SerializeSql(const std::string& suffix, bool load)
{
    if (load) // start fresh when Serialize called, unlike UpdateSql that updates
    {
        ClearDictionaries();
        Clear();
    }

    std::string path(DATABASE_PATH);
    std::string fileName = path + string("database") + suffix + ".db";

    if (load)
    {
        fprintf(stdout, "Loading default database %s (previous entries cleared)\n",
                fileName.c_str());
    }

    ReadWriteSql(fileName, load);

    if (load)
    {
        bool checkForErrors = tcOptions::Get()->OptionStringExists("CheckDatabaseReferences");
#ifdef _DEBUG
        //checkForErrors = true;
#endif
        if (checkForErrors)
        {
            ReportProgress("DB checking for errors", 0.95f);
            CheckForErrors("log/database_errors.txt");
        }
    }

}

/**
* Updates database with contents of add-on database. New entries are added. Duplicate
* entries (duplicate class names) are updated with new database entry.
*
* Intent is to allow scenario-specific add-on databases to be loaded from within a
* scenario script.
*/
void tcDatabase::UpdateSql(const std::string& fileName)
{
    fprintf(stdout, "Updating database with %s\n",
            fileName.c_str());


    ReadWriteSql(fileName, true); // true to load
}



void tcDatabase::Clear() 
{
    mcObjectData.RemoveAll();
    ClearDictionaries();
}


/**
* When using useDynamicLoad, this clears platform data before loading new scenario
*/
void tcDatabase::ClearForNewScenario()
{
    if (!useDynamicLoad)
    {
        useDynamicLoad = true; // only dynamic load is supported for loading from save games
    }

    //mcObjectData.RemoveAll();
    //ClearDictionaries();

    fprintf(stdout, "Clearing database for new scenario\n");
}


/**
* Creates a copy of object with key anKey and adds to the database.
* Instance name is tagged with "[COPY]"
*/
int tcDatabase::CreateObjectCopy(long anKey) 
{
    assert(false); // obsolete
    return 0;
#if 0
    return 0;
    std::shared_ptr<tcDatabaseObject>pobj = NULL;
    std::shared_ptr<tcDatabaseObject>pobjcopy = NULL;
    long nKey;

    if (GetObject(anKey,pobj)==false)
    {
        return false; // error, not found
    }

    if (std::shared_ptr<tcPlatformDBObject>pgobj = std::dynamic_pointer_cast<tcPlatformDBObject>(pobj))
    {
        pobjcopy = new tcPlatformDBObject(*pgobj);
    }
    else if (std::shared_ptr<tcLauncherDBObject>plobj = std::dynamic_pointer_cast<tcLauncherDBObject>(pobj))
    {
        pobjcopy = new tcLauncherDBObject(*plobj);
    }
    else if (std::shared_ptr<tcMissileDBObject>pmobj =  std::dynamic_pointer_cast<tcMissileDBObject>(pobj))
    {
        pobjcopy = new tcMissileDBObject(*pmobj);
    }
    else if (tcRadarDBObject *probj =  std::dynamic_pointer_cast<tcRadarDBObject>(pobj))
    {
        pobjcopy  = new tcRadarDBObject(*probj);
    }
    else if (tcESMDBObject *peobj =  std::dynamic_pointer_cast<tcESMDBObject>(pobj))
    {
        pobjcopy = new tcESMDBObject(*peobj);
    }

    if (pobjcopy == NULL)
    {
        assert(false);
        return false;
    }
    else
    {
        // tag name, and add copy to database
        pobjcopy->mzClass += " [COPY]";
        mcObjectData.AddElement(pobjcopy,nKey);
        pobjcopy->mnKey = nKey; // set key to key assigned by AddElement
        return true;
    }
#endif
}

int tcDatabase::DeleteObject(long anKey) 
{
    // first remove the object from the nameToKey lookup
    std::shared_ptr<tcDatabaseObject> obj = GetObject(anKey);
    if (obj == 0)
    {
        assert(false);
        fprintf(stderr, "Error - tcDatabase::DeleteObject - Obj doesn't exist (key %d)\n",
                anKey);
        return 0;
    }

    std::string className(obj->GetName());

    std::map<std::string, long>::iterator mapIter = nameToKey.find(className);
    if (mapIter != nameToKey.end())
    {
        nameToKey.erase(mapIter);
    }
    else
    {
        fprintf(stderr, "Error - tcDatabase::DeleteObject - not found in nameToKey (%s)\n",
                className.c_str());
    }

    return mcObjectData.RemoveKey(anKey);
}

/**
* Method to auto export launcher configuration info for updated DB schema
*/
void tcDatabase::ExportLauncherConfigurations()
{
    FILE* fid_launcher_config = fopen("database\\launcher_configuration.csv", "wt");

    fprintf(fid_launcher_config, "DatabaseClass,ChildClass,ChildCapacity,LoadTime_s\n");

    int nCount = mcObjectData.GetCount();
    long currentPos = mcObjectData.GetStartPosition();
    std::shared_ptr<tcDatabaseObject> obj = 0;
    long id = -1;

    for (int n=0; n<nCount; n++)
    {
        mcObjectData.GetNextAssoc(currentPos, id, obj);
        
        if (std::shared_ptr<tcLauncherDBObject> launcherData = std::dynamic_pointer_cast<tcLauncherDBObject>(obj))
        {
            size_t nConfigs = (size_t)launcherData->GetNumberConfigurations();
            if (nConfigs > 0)
            {
                for (size_t k=0; k<nConfigs; k++)
                {
                    fprintf(fid_launcher_config, "%s,%s,%d,%f\n", obj->mzClass.c_str(),
                            launcherData->GetConfigurationClass(k).c_str(),
                            launcherData->GetConfigurationCapacity(k),
                            launcherData->GetConfigurationLoadTime(k));
                }
            }
            else
            {
                assert(false); // launcher should have at least 1 config
            }
        }

    }

    fclose(fid_launcher_config);
}

/**
* Method to auto export platform launcher info for updated DB schema
*/
void tcDatabase::ExportPlatformTables()
{
    FILE* fid_launcher = fopen("database\\platform_launcher.csv", "wt");
    FILE* fid_sensor = fopen("database\\platform_sensor.csv", "wt");
    FILE* fid_magazine = fopen("database\\platform_mag.csv", "wt");

    fprintf(fid_launcher, "DatabaseClass,LauncherClass,LocalName\n");
    fprintf(fid_sensor, "DatabaseClass,SensorClass,SensorAz\n");
    fprintf(fid_magazine, "DatabaseClass,MagazineClass\n");


    int nCount = mcObjectData.GetCount();
    long currentPos = mcObjectData.GetStartPosition();
    std::shared_ptr<tcDatabaseObject> obj = 0;
    long id = -1;

    for (int n=0; n<nCount; n++)
    {
        mcObjectData.GetNextAssoc(currentPos, id, obj);
        

        if (std::shared_ptr<tcPlatformDBObject> platformData = std::dynamic_pointer_cast<tcPlatformDBObject>(obj))
        {
            size_t nLaunchers = platformData->maLauncherClass.size();
            if (nLaunchers > 0)
            {
                for (size_t k=0; k<nLaunchers; k++)
                {
                    fprintf(fid_launcher, "%s,%s,%s\n", obj->mzClass.c_str(),
                            platformData->maLauncherClass[k].c_str(), platformData->launcherName[k].c_str());
                }
            }

            size_t nMagazines = platformData->maMagazineClass.size();
            if (nMagazines > 0)
            {
                for (size_t k=0; k<nMagazines; k++)
                {
                    fprintf(fid_magazine, "%s,%s,%d\n", obj->mzClass.c_str(),
                            platformData->maMagazineClass[k].c_str(),
                            platformData->magazineId[k]);
                }
            }
        }

        if (std::shared_ptr<tcSensorPlatformDBObject> sensorPlatData = obj->GetComponent<tcSensorPlatformDBObject>())
        {
            size_t nSensors = sensorPlatData->sensorClass.size();
            if (nSensors > 0)
            {
                for (size_t k=0; k<nSensors; k++)
                {
                    fprintf(fid_sensor, "%s,%s,%f\n", obj->mzClass.c_str(),
                            sensorPlatData->sensorClass[k].c_str(), sensorPlatData->sensorAz[k]);
                }
            }

        }
    }

    fclose(fid_launcher);
    fclose(fid_sensor);
    fclose(fid_magazine);
}

/**
* @param searchYear floating point year value for date filtering. Set to zero to ignore this field in search
*/
bool tcDatabase::FindPlatformSetups(const std::string& databaseClass, float searchYear, std::vector<std::string>& setupNames)
{
    float maxInitialYear = searchYear;
    float minFinalYear = searchYear;
    if (searchYear <= 0) // effectively ignore year field
    {
        maxInitialYear = 99999.0f;
        minFinalYear = 0;
    }

    setupNames.clear();

    {
        std::string command =
            strutil::format("select * from platform_setup where DatabaseClass=\"%s\" AND InitialYear <= %f AND FinalYear >= %f;",
                            databaseClass.c_str(), maxInitialYear, minFinalYear);
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            setupNames.push_back(tableData.getstring(1));
        }
    }
    
    return (setupNames.size() > 0);
}

/**
* @return false if setup not found
*/
bool tcDatabase::GetPlatformSetupData(const std::string& databaseClass, const std::string& setupName, 
                                      tcLoadoutData& loadoutData)
{
    bool result = GetPlatformSetupData(databaseClass, setupName,
                                       loadoutData.airComplement, loadoutData.magazineLoadout, loadoutData.launcherLoadout);
    loadoutData.setupName = setupName;
    return result;
}

/**
* @return false if setup not found
*/
bool tcDatabase::GetPlatformSetupData(const std::string& databaseClass, const std::string& setupName, 
                                      std::vector<AirComplement>& airComplement, std::vector<MagazineLoadout>& magazineLoadout,
                                      std::vector<LauncherLoadout>& launcherLoadout)
{
    airComplement.clear();
    magazineLoadout.clear();
    launcherLoadout.clear();

    std::string airComplementName;
    std::string magazineLoadoutName;
    std::string launcherLoadoutName;

    {
        std::string command =
            strutil::format("select * from platform_setup where DatabaseClass=\"%s\" AND SetupName=\"%s\";",
                            databaseClass.c_str(), setupName.c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        if (tableData.read())
        {
            airComplementName = tableData.getstring(4);
            magazineLoadoutName = tableData.getstring(5);
            launcherLoadoutName = tableData.getstring(6);
        }
        else
        {
            return false;
        }
    }



    // populate airComplements
    {
        std::string command =
            strutil::format("select * from air_complement where DatabaseClass=\"%s\";",
                            airComplementName.c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            AirComplement ac;

            ac.airClass = tableData.getstring(1);
            ac.quantity = (unsigned int)tableData.getint(2);
            ac.prefix = tableData.getstring(3);
            ac.readyLevel = (unsigned int)tableData.getint(4);
            
            airComplement.push_back(ac);
        }
    }


    // populate magazineLoadout
    {
        std::string command =
            strutil::format("select * from magazine_loadout where DatabaseClass=\"%s\";",
                            magazineLoadoutName.c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            MagazineLoadout ml;
            
            ml.magazineId = (unsigned int)tableData.getint(1);
            ml.item = tableData.getstring(2);
            ml.quantity = (unsigned int)tableData.getint(3);
            
            magazineLoadout.push_back(ml);
        }
    }

    // populate launcherLoadout
    {
        std::string command =
            strutil::format("select * from launcher_loadout where DatabaseClass=\"%s\";",
                            launcherLoadoutName.c_str());
        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader tableData = sqlCmd.executereader();
        while (tableData.read())
        {
            LauncherLoadout ll;
            
            ll.launcherId = (unsigned int)tableData.getint(1);
            ll.item = tableData.getstring(2);
            ll.quantity = (unsigned int)tableData.getint(3);
            
            launcherLoadout.push_back(ll);
        }
    }

    return true;
}


void tcDatabase::InitDamageDefaults()
{
    weaponDamageDefault.maxRange_m = 10.0;
    weaponDamageDefault.probDetonate = 1.0;
    weaponDamageDefault.blastCharge_kg = 1.0f;
    weaponDamageDefault.fragCharge_kg = 1.0f;
    weaponDamageDefault.radCharge_kg = 1.0f;
    weaponDamageDefault.fragMetal_kg = 1.0f;
    weaponDamageDefault.fragFragment_kg = 0.1f;
    weaponDamageDefault.fragSpread = 1.0f;

    damageEffectDefault.blastEffect.clear();
    database::tcDamageEffect::DamagePoint dp;

    dp.effectLevel = 0;
    dp.damageFactor = 0;
    damageEffectDefault.blastEffect.push_back(dp);

    dp.effectLevel = 1;
    dp.damageFactor = 1;
    damageEffectDefault.blastEffect.push_back(dp);

    dp.effectLevel = 10.0;
    dp.damageFactor = 10;
    damageEffectDefault.blastEffect.push_back(dp);

    damageEffectDefault.waterBlastEffect = damageEffectDefault.blastEffect;
    damageEffectDefault.fragEffect = damageEffectDefault.blastEffect;
    damageEffectDefault.radEffect = damageEffectDefault.blastEffect;
    damageEffectDefault.internalEffect = damageEffectDefault.blastEffect;
}


bool tcDatabase::IsUsingDynamicLoad() const
{
    return useDynamicLoad;
}

/**
* works with old database binary file system
* @return false if mnVersion isn't supported
*/
bool tcDatabase::IsVersionSupported() {
    if ((mnVersion >= VERSION_1_0_1)&&(mnVersion <= VERSION_CURRENT)) {
        return true;
    }
    else {
        return false;
    }
}

/**
* sets the three integer version fields using mnVersion 
* (works with old database binary file system)
*/
void tcDatabase::GetVersion(int& v1, int& v2, int& v3) {
    v3 = (mnVersion) & 0xFF;
    v2 = (mnVersion >> 8) & 0xFF;
    v1 = (mnVersion >> 16) & 0xFF;
}




void tcDatabase::PrintToFile(tcString sFileName) 
{
    tcFile file;
    long nMapSize, nKey, nPoolPos;
    std::shared_ptr<tcDatabaseObject>pdbobj;

    if (file.Open(sFileName.GetBuffer(),tcFile::modeCreate|tcFile::modeWrite)==false)
    {
        //        //wxMessageBox("Error - tcDatabase::PrintToFile - couldn't open file for write", "Error", wxOK);
        return;
    }
    file.WriteString("DB file name: ");
    file.WriteString(mstrCurrentFile.GetBuffer());
    file.WriteString("\n----------------------------------------------------------------------\n");
    nMapSize = mcObjectData.GetCount();
    nPoolPos = mcObjectData.GetStartPosition();
    for(int i=0;i<nMapSize;i++) {
        mcObjectData.GetNextAssoc(nPoolPos,nKey,pdbobj);

        if (pdbobj != NULL) {
            pdbobj->PrintToFile(file);
        }
        else {
            file.WriteString("Error - null object - aborting PrintToFile");
            file.Close();
            return;
        }
    }
    file.Close();
}


const tcWeaponDamage* tcDatabase::GetWeaponDamageData(const std::string& s) const
{

    if ( const tcWeaponDamage* weapDamage=weaponDamageData.GetData(s))
    {
        return weapDamage;
    }
    else
    {
        assert(false);
        fprintf(stderr, "tcDatabase::GetWeaponDamageData -- Weapon damage model not found for %s, using default\n", s.c_str());
        return &weaponDamageDefault;
    }
}

const tcAcousticModel* tcDatabase::GetAcousticModel(const std::string& modelName) const
{
    std::map<std::string, tcAcousticModel>::const_iterator iter =
        acousticModelData.find(modelName);

    if (iter != acousticModelData.end())
    {
        return &iter->second;
    }
    else
    {
        return nullptr;
    }
}


void tcDatabase::GetCountryList(std::vector<std::string>& countryList) const
{
    countryList.clear();

    std::map<std::string, tcCountryData>::const_iterator iter =
        countryData.begin();
    for (;iter != countryData.end(); ++iter)
    {
        countryList.push_back(iter->second.countryName.c_str());
    }
}

const std::string& tcDatabase::GetCountryNameSubstitution(
    const std::string& originalName,
    const std::chrono::system_clock::time_point &dateTime) const
{
    std::map<std::string, tcCountryNameChanges>::const_iterator iter =
        countryNameChanges.find(originalName);

    if (iter == countryNameChanges.end())
    {
        return originalName; // no substitution
    }
    else
    {
        const tcCountryNameChanges& nameChangeInfo = iter->second;
        for (size_t n=0; n<nameChangeInfo.substitutions.size(); n++)
        {
            bool dateInRange = (dateTime >= nameChangeInfo.substitutions[n].dateStart) &&
                               (dateTime < nameChangeInfo.substitutions[n].dateStop);
            if (dateInRange)
            {
                return nameChangeInfo.substitutions[n].name;
            }
        }
        return originalName;
    }
}

const tcDamageEffect* tcDatabase::GetDamageEffectData(const std::string& s) const
{
    if (const tcDamageEffect* damageEffect = damageEffectData.GetData(s))
    {
        return damageEffect;
    }
    else
    {
        fprintf(stderr, "tcDatabase::GetDamageEffectData -- Damage effect data not found for %s, using default\n", s.c_str());
        return &damageEffectDefault;
    }
}

/**
* @return the display name for this platform based on useNatoASCC option
*/
const std::string& tcDatabase::GetDisplayName(const std::string& className) const
{
    static std::string result;

    std::map<std::string, std::string>::const_iterator iter =
        nameToDisplayName.find(className);

    if (iter != nameToDisplayName.end())
    {
        result = iter->second;
    }
    else
    {
        result = ""; // not found
    }

    return result;
}

///**
//* Use this version if not storing texture2D, e.g. to draw immediately
//*/
//tcTexture2D* tcDatabase::GetEnsign(const std::string& country)
//{
//    if (country.size() == 0) return unknownEnsign.get();

//    std::map<std::string, tcCountryData>::iterator iter =
//        countryData.find(country);

//    if (iter != countryData.end())
//    {
//        tcTexture2D* ensign = iter->second.GetEnsignImage();
//        assert(ensign != 0);
//        return ensign;
//    }
//    else
//    {
//        return unknownEnsign.get();
//    }
//}

///**
//* Use this version if storing texture2D in a shared_ptr to avoid reference count errors
//*/
//std::shared_ptr<tcTexture2D> tcDatabase::GetEnsignShared(const std::string& country)
//{
//    if (country.size() == 0) return unknownEnsign;

//    std::map<std::string, tcCountryData>::iterator iter =
//        countryData.find(country);

//    if (iter != countryData.end())
//    {
//        return iter->second.GetEnsignImageShared();
//    }
//    else
//    {
//        return unknownEnsign;
//    }
//}

/**
* @return field values for single record matching <databaseClass> in <table>
* @param fields comma separated string of fields to query
* e.g. GetFieldsForRow("sub", "Country,MaxSpeed_kts,Draft_m")
* SQL is select <fields> from <table> where DatabaseClass=<databaseClass>;
*/
std::vector<std::string> tcDatabase::GetFieldsForRow(const std::string& table, const std::string& databaseClass, const std::string& fields)
{
    std::vector<std::string> result;

    std::string fieldsToQuery(fields);
    fieldsToQuery=strutil::replace_all(fieldsToQuery,";", ",");
    //    fieldsToQuery.Replace(";", ","); // to guard against accidental commands

    std::string temp(fieldsToQuery);
    size_t nCommas= strutil::replace_all(temp,";", ",");
    //    size_t nCommas = temp.Replace(",", "-");
    size_t nFields = nCommas + 1;

    try
    {
        std::string command = strutil::format("select %s from %s where DatabaseClass=\"%s\";",
                                              fieldsToQuery.c_str(), table.c_str(), databaseClass.c_str());

        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader fieldData = sqlCmd.executereader();

        if (fieldData.read())
        {
            for (int n=0; n<int(nFields); n++)
            {
                result.push_back(fieldData.getstring(n));
            }
        }
    }
    catch (...)
    {
        assert(false);
    }

    return result;
}

/**
* @return field values for multiple record matching <databaseClass> in <table>
* @param fields comma separated string of fields to query
* e.g. GetFieldsForAllRows("sub", "Country,MaxSpeed_kts,Draft_m")
* SQL is select <fields> from <table> where DatabaseClass=<databaseClass>;
*/
std::vector<std::vector<std::string>> tcDatabase::GetFieldsForAllRows(const std::string& table, const std::string& databaseClass, const std::string& fields)
{
    std::vector<std::vector<std::string>> result;

    std::string fieldsToQuery(fields);
    fieldsToQuery=strutil::replace_all(fieldsToQuery,";", ",");
    //    fieldsToQuery.Replace(";", ","); // to guard against accidental commands

    std::string temp(fieldsToQuery);
    size_t nCommas= strutil::replace_all(temp,";", ",");
    size_t nFields = nCommas + 1;

    try
    {
        std::string command = strutil::format("select %s from %s where DatabaseClass=\"%s\";",
                                              fieldsToQuery.c_str(), table.c_str(), databaseClass.c_str());

        sqlite3_command sqlCmd(*sqlConnection, command);
        sqlite3_reader fieldData = sqlCmd.executereader();

        unsigned int rowCount = 0;
        const unsigned int maxRowsToReturn = 10000;
        while (fieldData.read() && (rowCount++ < maxRowsToReturn))
        {
            std::vector<std::string> row;
            for (int n=0; n<int(nFields); n++)
            {
                row.push_back(fieldData.getstring(n));
            }
            result.push_back(row);
        }
    }
    catch (...)
    {
        assert(false);
    }

    return result;
}


/**
* @return random database entry matching model type
*
* TODO fix this to guarantee return of object matching model type if one exists
*/
std::shared_ptr<tcDatabaseObject> tcDatabase::GetRandomOfType(UINT model_type)
{
    bool bSearching = true;
    bool bFound = false;
    int nTries = 0;
    std::shared_ptr<tcDatabaseObject>pdata = nullptr;

    while ((bSearching)&&(nTries++ < 256))
    {
        long nKey = GetRandomKey();
        bFound = mcObjectData.Lookup(nKey,pdata);
        if (pdata->mnModelType == model_type) {bSearching = false;}
    }
    if (bSearching)
    {
        WTL("Error - tcDatabase::GetRandomOfType - timed out");
        return NULL;
    }
    if (!bFound)
    {
        WTL("Error - tcDatabase::GetRandomOfType");
        return NULL;
    }

    return pdata;
}

/**
* @return random tcPlatformDBObject, tcMissileDBObject,
* or tcJetDBObject key.
*/
long tcDatabase::GetRandomKey() {
    long nMapSize, nKey = -1, nPoolPos;
    std::shared_ptr<tcDatabaseObject>pdbobj = 0;
    bool bSearching;

    nMapSize = mcObjectData.GetCount();
    bSearching = true;
    while (bSearching) {
        int k = (rand() % nMapSize) + 1;
        nPoolPos = mcObjectData.GetStartPosition();
        for (int i=0;i<k;i++) {
            mcObjectData.GetNextAssoc(nPoolPos,nKey,pdbobj);
        }
        std::string className = pdbobj->GetClassName();

        if ((className == "Ship")||
            (className == "Air")||
            (className == "Jet")||
            (className == "Sub"))
        {
            bSearching = false;
        }
    }
    return nKey;
}

const tcSignatureModel* tcDatabase::GetSignatureModel(const std::string& modelName) const
{
    std::map<std::string, tcSignatureModel>::const_iterator iter =
        signatureModelData.find(modelName);

    if (iter != signatureModelData.end())
    {
        return &iter->second;
    }
    else
    {
        return nullptr;
    }
}

/**
* lookup object by key reference
* @return 0 if not found, non-zero otherwise
*/
bool tcDatabase::GetObject(long anKey, std::shared_ptr<tcDatabaseObject> &rpobj) {
    return mcObjectData.Lookup(anKey,rpobj);
}

long tcDatabase::AddOrUpdateObject(std::shared_ptr<tcDatabaseObject>rpobj)
{

    if (ObjectExists(rpobj->GetName()))
    {
        fprintf(stdout, "Updating database class: %s\n", rpobj->GetName());
        std::shared_ptr<tcDatabaseObject> oldObj = GetObject(rpobj->GetName());
        assert(oldObj != 0);
        DeleteObject(oldObj->mnKey);
    }
    long  key;
    // std::string className = rpobj->mzClass.c_str();
    // if(className=="57mm/70 Mks 2-3 Store")
    // {
    //     int a=0;
    // }
    mcObjectData.AddElement(rpobj, key); // add to database, key gets new key val
    rpobj->mnKey = key; // set key val of object (may not be necessary anymore)
    nameToKey[rpobj->GetName() ] = key;
    return key;
}
long tcDatabase::AddOrUpdateObjectForceKey(std::shared_ptr<tcDatabaseObject> rpobj,long forceKey)
{
    if (ObjectExists(rpobj->GetName()))
    {
        fprintf(stdout, "Updating database class: %s\n", rpobj->GetName());
        std::shared_ptr<tcDatabaseObject> oldObj = GetObject(rpobj->GetName());
        assert(oldObj != 0);
        DeleteObject(oldObj->mnKey);
    }
    mcObjectData.AddElementForceKey(rpobj, forceKey); // add to database, key gets new key val
    rpobj->mnKey = forceKey; // set key val of object (may not be necessary anymore)
    nameToKey[rpobj->GetName() ] = forceKey;

    return forceKey;
}


void tcDatabase::AddOrUpdateSignatureModelData(const tcSignatureModel&data)
{
    signatureModelData[data.mzClass]=data;
}
void tcDatabase::AddOrUpdateAcousticModelData(const tcAcousticModel& data)
{
    acousticModelData[data.databaseClass]=data;
}
void tcDatabase::AddOrUpdateWeaponDamageData(const tcWeaponDamage& data)
{
    weaponDamageData.AddOrUpdate(data);
}
void tcDatabase::AddOrUpdateDamageEffectData(const tcDamageEffect&data)
{
    damageEffectData.AddOrUpdate(data);
}


/**
* @return NULL if not found
*/
std::shared_ptr<tcDatabaseObject> tcDatabase::GetObject(long anKey)
{
    std::shared_ptr<tcDatabaseObject> databaseObject;
    if (mcObjectData.Lookup(anKey, databaseObject))
    {
        return databaseObject;
    }
    else
    {
        return 0;
    }
}

/**
* Lookup and return object database class name by key
* @return empty string reference if not found
*/
const std::string& tcDatabase::GetObjectClassName(long key)
{
    static std::string result;
    result.clear();

    if (std::shared_ptr<tcDatabaseObject> databaseObject = GetObject(key))
    {
        result = databaseObject->mzClass.c_str();
    }

    return result;
}

long tcDatabase::GetKey(const char* s)
{
    std::shared_ptr<tcDatabaseObject> obj = GetObject(std::string(s));
    if (obj != 0)
    {
        return obj->mnKey;
    }
    else
    {
        return -1;
    }
}

/**
* Gets object by class name.
* @return NULL if not found
*/
std::shared_ptr<tcDatabaseObject> tcDatabase::GetObject(const std::string& className)
{
    std::string updatedClassName(className); // local variable that can be updated with cross-ref

    // check nameToKey for already loaded object
    std::map<std::string, long>::iterator mapIter = nameToKey.find(className);
    if (mapIter != nameToKey.end())
    {
        return GetObject(mapIter->second);
    }
    else
    {
        // try crossReference table next
        std::map<std::string, std::string>::const_iterator refIter = crossReference.find(className);
        if (refIter != crossReference.end())
        {
            updatedClassName = refIter->second;
            // try nameToKey again with cross-referenced class name
            mapIter = nameToKey.find(updatedClassName);
            if (mapIter != nameToKey.end())
            {
                return GetObject(mapIter->second);
            }
        }
    }

    if (mapIter == nameToKey.end())
    {
#ifdef _DEBUG
        if (tcSimState::Get()->IsMultiplayerClient())
        {
            assert(false);
        }
#endif \
    // request load from database and try again if useDynamicLoad
        if (useDynamicLoad && LoadRecordSql(updatedClassName.c_str()))
        {
            std::map<std::string, long>::iterator mapIter2 = nameToKey.find(updatedClassName);
            if (mapIter2 != nameToKey.end())
            {
                return GetObject(mapIter2->second);
            }
        }

        std::string missingClass = className.c_str();
        if (missingClass.size() == 0)
        {
            missingClass = "Empty string";
        }

        fprintf(stderr, "Error - tcDatabase::GetObject - not found in nameToKey (%s)\n",
                missingClass.c_str());
        return 0;
    }
    else
    {
        assert(false); // shouldn't hit this
        return GetObject(mapIter->second);
    }


}


bool tcDatabase::ObjectExists(const std::string& className) const
{
    std::map<std::string, long>::const_iterator mapIter = nameToKey.find(className);
    return (mapIter != nameToKey.end());
}

/**
* find key of next object of same mnClassID as anKey
*/
long tcDatabase::GetNextObjectOfSameClass(long anKey) 
{
    long nPoolSize = mcObjectData.GetCount();
    long nCurrentKey;
    std::shared_ptr<tcDatabaseObject >pobj;

    nCurrentKey = anKey;
    if (mcObjectData.Lookup(nCurrentKey,pobj)==false) {return NULL_INDEX;}


    std::string className = pobj->GetClassName();


    for (int i=0;i<nPoolSize;i++)
    {
        nCurrentKey = mcObjectData.GetNextKey(nCurrentKey);
        if (mcObjectData.Lookup(nCurrentKey,pobj)==false) {return NULL_INDEX;} // error
        if (pobj->GetClassName() == className)
        {
            return nCurrentKey;
        }
    }
    return anKey; // not found so return starting key as next
}


std::vector<std::string> tcDatabase::GetPlatformNames(const std::string& className)
{
    std::vector<std::string> result;

    std::string command =
        strutil::format("select Name from platform_names where DatabaseClass=\"%s\";",
                        className.c_str());
    sqlite3_command sqlCmd(*sqlConnection, command);
    sqlite3_reader records = sqlCmd.executereader();
    while (records.read())
    {
        result.push_back(records.getstring(0));
    }

    return result;
}

/**
* @returns platforms in service at <dateYear>
* @param dateYear floating point year, fractional year indicates date within year, e.g. 2000.5 is about June 1
*/
std::vector<std::string> tcDatabase::GetPlatformNamesByDate(const std::string& className, float dateYear)
{
    std::vector<std::string> result;

    std::string command =
        strutil::format("select Name from platform_names where DatabaseClass=\"%s\" and DateInService <= %f and DateOutService >= %f;",
                        className.c_str(), dateYear, dateYear);
    sqlite3_command sqlCmd(*sqlConnection, command);
    sqlite3_reader records = sqlCmd.executereader();
    while (records.read())
    {
        result.push_back(records.getstring(0));
    }

    return result;
}

std::vector<std::string> tcDatabase::GetPlatformHulls(const std::string& className)
{
    std::vector<std::string> result;

    std::string command =
        strutil::format("select HullNumber from platform_names where DatabaseClass=\"%s\";",
                        className.c_str());
    sqlite3_command sqlCmd(*sqlConnection, command);
    sqlite3_reader records = sqlCmd.executereader();
    while (records.read())
    {
        result.push_back(records.getstring(0));
    }

    return result;
}

/**
* Find key of previous object of same mnClassID as anKey
*/
long tcDatabase::GetPrevObjectOfSameClass(long anKey) 
{
    long nPoolSize = mcObjectData.GetCount();
    long nCurrentKey;
    std::shared_ptr<tcDatabaseObject>pobj;

    nCurrentKey = anKey;
    if (mcObjectData.Lookup(nCurrentKey,pobj)==false) {return NULL_INDEX;}

    std::string className = pobj->GetClassName();

    for (int i=0;i<nPoolSize;i++)
    {
        nCurrentKey = mcObjectData.GetPrevKey(nCurrentKey);
        if (mcObjectData.Lookup(nCurrentKey,pobj)==false) {return NULL_INDEX;} // error
        if (pobj->GetClassName() == className)
        {
            return nCurrentKey;
        }
    }
    return anKey; // not found so return starting key as next
}



/** 
* OBSOLETE with RTTI dynamic_cast usage, eliminated 2/19/03
* these methods check mnClassID before downcasting and return NULL
* if not consistent with the requested class or not found

std::shared_ptr<tcDatabaseObject> tcDatabase::GetSafeDBObject(long anKey) {
   std::shared_ptr<tcDatabaseObject> pdbobj;

   if (GetObject(anKey,pdbobj)==0) {return NULL;}
   if (pdbobj->mnClassID != DTYPE_OBJECT) {return NULL;}
   else {return pdbobj;}
}

tcPlatformDBObject* tcDatabase::GetSafeGenericDBObject(long anKey) {
   std::shared_ptr<tcDatabaseObject> pdbobj;

   if (GetObject(anKey,pdbobj)==0) {return NULL;}
   if (pdbobj->mnClassID != DTYPE_GENERIC) {return NULL;}
   else {return (tcPlatformDBObject*)pdbobj;}
}

std::shared_ptr<tcLauncherDBObject> tcDatabase::GetSafeLauncherDBObject(long anKey) {
   std::shared_ptr<tcDatabaseObject> pdbobj;

   if (GetObject(anKey,pdbobj)==0) {return NULL;}
   if (pdbobj->mnClassID != DTYPE_LAUNCHER) {return NULL;}
   else {return (std::shared_ptr<tcLauncherDBObject>)pdbobj;}
}

std::shared_ptr<tcMissileDBObject> tcDatabase::GetSafeMissileDBObject(long anKey) {
   std::shared_ptr<tcDatabaseObject> pdbobj;

   if (GetObject(anKey,pdbobj)==0) {return NULL;}
   if (pdbobj->mnClassID != DTYPE_MISSILE) {return NULL;}
   else {return (std::shared_ptr<tcMissileDBObject>)pdbobj;}
}
*/

// lookup class string associated with key
int tcDatabase::GetObjectClass(long anKey, std::string& rzClass) {
   std::shared_ptr< tcDatabaseObject >pdbobj;
    int bFound = mcObjectData.Lookup(anKey,pdbobj);
    if (bFound) {
        rzClass = pdbobj->mzClass;
    }
    else {
        rzClass = "ERR";
    }
    return bFound;
}

const std::vector<tcDatabase::RecordSummary>& tcDatabase::GetTableSummary(const std::string& tableName) const
{
    static std::vector<RecordSummary> emptyList; //< return for error/not-found case

    std::map<std::string, std::vector<RecordSummary>>::const_iterator iter =
        tableSummary.find(tableName);

    if (iter != tableSummary.end())
    {
        return iter->second;
    }
    else
    {
        assert(false);
        return emptyList;
    }
}

/**
* @returns vector of RecordSummary structures for each db class listed in itemList
* Can be used to filter equipment by year or country without loading everything into the active database
*/
const std::vector<tcDatabase::RecordSummary>& tcDatabase::GetItemSummary(const std::vector<std::string>& itemList) const
{
    static std::vector<RecordSummary> itemRecords;
    itemRecords.clear();

    
    size_t nItems = itemList.size();
    for (size_t n=0; n<nItems; n++)
    {
        std::string item_n(itemList[n].c_str());
        // get table name
        std::map<std::string, RecordSummary>::const_iterator iter =
            classSummary.find(item_n);
        if (iter != classSummary.end())
        {
            itemRecords.push_back(iter->second);
        }
    }

    return itemRecords;
}



/**
* @param filter leave empty to allow all database entries, "loadout" to return only weapons, CM, fuel tanks
* Future goal: Searches full database (not just what's dynamically loaded) and add time parameter
*/
std::vector<std::string> tcDatabase::WildcardSearch(const std::string& expression, const std::string& filter)
{
    std::vector<std::string> result;

    //if (s.Matches(childClassList[k].c_str()))
    int idx1 = expression.find('*');
    int idx2 = expression.find('?');
    int nPrefix = (int)std::min(unsigned(idx1), (unsigned)idx2); // convert to unsigned so that -1 doesn't affect minimum

    if ((idx1 == std::string::npos) && (idx2 == std::string::npos))
    {
        result.push_back(expression);
        return result;
    }

    std::string prefix = expression.substr(0,nPrefix);

    std::map<std::string, long>::const_iterator mapIter = nameToKey.lower_bound(prefix);
    bool searching = (mapIter != nameToKey.end());
    while (searching)
    {
        std::string s(mapIter->first.c_str());
        bool prefixMatches = (prefix == s.substr(0,nPrefix));

        //        std::regex e (expression);
        //        if ( std::regex_match(s, e))
        if(strutil::wildcard_match(s,expression))
        {
            std::shared_ptr<const tcDatabaseObject> data = database::tcDatabase::GetObject(s);
            assert(data != 0);

            if (filter.length() == 0)
            {
                result.push_back(s);
            }
            else if (filter == "loadout")
            {
                switch (data->mnModelType)
                {
                case MTYPE_MISSILE:
                case MTYPE_TORPEDO:
                case MTYPE_BALLISTIC:
                case MTYPE_SONOBUOY:
                case MTYPE_AIRCM:
                case MTYPE_WATERCM:
                case MTYPE_FUELTANK:
                case MTYPE_LASERGUIDEDBOMB:
                case MTYPE_BALLISTICMISSILE:
                    result.push_back(s);
                    break;
                default:
                    break;
                }
                // old code below replaced with switch above 22NOV2009
                //bool isWeapon = (data->mnModelType == MTYPE_MISSILE) || (data->mnModelType == MTYPE_TORPEDO) ||
                //    (data->mnModelType == MTYPE_BALLISTIC);
                //bool otherValidEquipment = (data->mnModelType == MTYPE_CM) || (data->mnModelType == MTYPE_FUELTANK);
                //if (isWeapon || otherValidEquipment)
                //{
                //    result.push_back(s);
                //}
            }
            else
            {
                assert(false);
            }
        }

        ++mapIter;

        searching = (mapIter != nameToKey.end()) && (prefixMatches);
    }

    return result;
}

/**
* @param filter leave empty to allow all database entries, "loadout" to return only weapons, CM, fuel tanks
* Searches only what is currently loaded in active database
*/
std::vector<std::string> tcDatabase::WildcardSearchLoaded(const std::string& expression, const std::string& filter)
{
    std::vector<std::string> result;

    //if (s.Matches(childClassList[k].c_str()))
    int idx1 = expression.find('*');
    int idx2 = expression.find('?');
    int nPrefix = (int)std::min(unsigned(idx1), (unsigned)idx2); // convert to unsigned so that -1 doesn't affect minimum

    if ((idx1 == string::npos) && (idx2 == string::npos))
    {
        result.push_back(expression);
        return result;
    }

    std::string prefix = expression.substr(0,nPrefix);

    std::map<std::string, long>::const_iterator mapIter = nameToKey.lower_bound(prefix);
    bool searching = (mapIter != nameToKey.end());
    while (searching)
    {
        std::string s(mapIter->first.c_str());
        bool prefixMatches = (prefix == s.substr(0,nPrefix));
        //        std::regex e (s);
        //        if ( std::regex_match(s, e))
        if(strutil::wildcard_match(s,expression))
        {
            std::shared_ptr<const tcDatabaseObject> data = database::tcDatabase::GetObject(mapIter->second);
            assert(data != 0);

            if (filter.length() == 0)
            {
                result.push_back(s);
            }
            else if (filter == "loadout")
            {
                switch (data->mnModelType)
                {
                case MTYPE_MISSILE:
                case MTYPE_TORPEDO:
                case MTYPE_BALLISTIC:
                case MTYPE_SONOBUOY:
                case MTYPE_AIRCM:
                case MTYPE_WATERCM:
                case MTYPE_FUELTANK:
                case MTYPE_LASERGUIDEDBOMB:
                case MTYPE_BALLISTICMISSILE:
                    result.push_back(s);
                    break;
                default:
                    break;
                }
                // old code below replaced with switch above 22NOV2009
                //bool isWeapon = (data->mnModelType == MTYPE_MISSILE) || (data->mnModelType == MTYPE_TORPEDO) ||
                //    (data->mnModelType == MTYPE_BALLISTIC);
                //bool otherValidEquipment = (data->mnModelType == MTYPE_CM) || (data->mnModelType == MTYPE_FUELTANK);
                //if (isWeapon || otherValidEquipment)
                //{
                //    result.push_back(s);
                //}
            }
            else
            {
                assert(false);
            }
        }

        ++mapIter;

        searching = (mapIter != nameToKey.end()) && (prefixMatches);
    }

    return result;
}

void tcDatabase::SetProgressReporting( int p1, int p2)
{
    // progressDialog = dlg;
    startProgress = p1;
    finishProgress = p2;
}


void tcDatabase::ReportProgress(const std::string& msg, float fractionalProgess)
{
    int progressVal = startProgress + int(0.5f + fractionalProgess*float(finishProgress-startProgress));
    //     if (progressDialog != 0)
    //     {
    //         int progressVal = startProgress + int(0.5f + fractionalProgess*float(finishProgress-startProgress));
    // //        progressDialog->Update(progressVal, msg);
    //     }
}



tcDatabase::tcDatabase()  :
    mstrCurrentFile("NULL"),
    mnVersion(VERSION_CURRENT),
    sqlConnection(0),
    useDynamicLoad(true)
// progressDialog(0)
{
    tcDatabaseObject::AttachDatabase(this);

    if (tcOptions::Get()->OptionStringExists("CacheFullDatabase"))
    {
        useDynamicLoad = false;
    }

    InitDamageDefaults();
}

tcDatabase::~tcDatabase() 
{
}

}
const std::map<std::string, std::string>& tcDatabase::GetNameToTable()
{
    return nameToTable;
}

const std::map<string, tcSignatureModel>& tcDatabase::GetSignatureModelData()
{
    return signatureModelData;
}

const std::map<string, tcAcousticModel>& tcDatabase::GetAcousticModelData()
{
    return acousticModelData;
}

const database::tcDatabaseTable<database::tcWeaponDamage> &tcDatabase::GetWeaponDamageData()
{
    return weaponDamageData;
}

const tcDatabaseTable<tcDamageEffect>& tcDatabase::GetDamageEffectData()
{
    return damageEffectData;
}
