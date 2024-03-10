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

#include "DatabaseManager.h"

//#include "wx/string.h"
#include "wx/dir.h"
#include "wx/file.h"
#include "wx/filefn.h"
#include "wx/msgdlg.h"
#include "wx/textfile.h"
#include "wx/xml/xml.h"
#include "wx/progdlg.h"

#include "tcDBObjSerializerSql.h"
#include "tcPool.h"
#include "tcSonarDBObject.h"
#include "tcPlatformDBObject.h"

#include <vector>


//#ifdef _DEBUG
//#define new DEBUG_NEW
//#endif

using sqlite3x::sqlite3_connection;
using sqlite3x::sqlite3_reader;
using sqlite3x::sqlite3_command;
using namespace database;

tcDatabaseManager* tcDatabaseManager::Get()
{
    static tcDatabaseManager instance;

    return &instance;
}

bool tcDatabaseManager::AreChangesPending() const
{
    return changesArePending;
}

/**
* Save copy of fileName in backup directory with timetag appended to name
*/
void tcDatabaseManager::BackupFile(const std::string& fileName)
{
    if (!wxDir::Exists("backup"))
    {
        wxMkdir("backup");
    }

    std::string databaseFile = fileName.AfterLast('\\').BeforeFirst('.');

    const std::chrono::system_clock::time_point current = std::chrono::system_clock::now();
    std::string timeStamp = strutil::format("-%04d%02d%02d-%02d%02d%02d.db", current.GetYear(), 1+current.GetMonth(), current.GetDay(),
        current.GetHour(), current.GetMinute(), current.GetSecond());
    std::string backupFile = std::string("backup\\") + databaseFile + timeStamp;

    wxCopyFile(fileName, backupFile, true);
}

/**
* If database is open, close it
*/
bool tcDatabaseManager::Close()
{
    try
    {
        if (isOpen)
        {
            sqlConnection.close();
            return true;
        }
        else
        {
            return false;
        }
    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "Close Error");
        return false;
    }
}

bool tcDatabaseManager::CheckAllSetups()
{
    std::vector<std::string> platformList;
    for (size_t n=0; n<platformTables.size(); n++)
    {
        WX_APPEND_ARRAY(platformList, GetPlatformList(platformTables[n].c_str(), ""));
    }

    wxProgressDialog* progressDialog = new wxProgressDialog("Checking platform setups", "", 100, NULL, wxPD_SMOOTH);
	progressDialog->SetSize(300, 115);

    bool allOK = true;
    std::vector<std::string> errorMessages;
    for (size_t n=0; n<platformList.size(); n++)
    {
        int progressValue = int(100.0f * float(n) / float(platformList.size()));
        progressDialog->Update(progressValue, platformList[n]);
        bool platformOK = CheckSetupData(platformList[n], errorMessages);
        allOK = allOK && platformOK;
    }

    progressDialog->Destroy();


	wxTextFile log("database_setup_errors.txt");
	if (!log.Exists())
	{
		log.Create();
	}
	else
	{
		log.Open();
	}
	log.Clear();


    if (allOK)
    {
        //wxMessageBox("All aircraft setups meet weight, all magazine setups have valid references", "Setup Check Results");
		log.AddLine("No errors in setups found");
    }
    else
    {
		for (size_t n=0; n<errorMessages.size(); n++)
        {
			log.AddLine(errorMessages[n]);
		}


        std::string combinedErrors("Errors detected in setups:\n");
        size_t maxLines = 30;
        for (size_t n=0; (n<errorMessages.size())&&(n<maxLines); n++)
        {
            combinedErrors += errorMessages[n];
            combinedErrors += "\n";
        }
        if (errorMessages.size() >= maxLines)
        {
            combinedErrors += strutil::format("... more errors, only showing first %d, see database_setup_errors.txt\n", maxLines);
        }
        wxMessageDialog dialog(0, combinedErrors, "Setup Check Results", wxICON_ERROR);
        dialog.ShowModal();
    }

	log.Write();
	log.Close();

    return allOK;
}

bool tcDatabaseManager::CheckForErrors(const std::string& logFile)
{
    return tcDatabase::Get()->CheckForErrors(logFile);
}

bool tcDatabaseManager::CheckSetupData(const std::string& databaseClass, std::vector<std::string>& errorMessages)
{
    std::vector<std::vector<std::string>> setupData =
        GetPlatformTableData("platform_setup", databaseClass, setupFields);

    bool allOK = true;
    for (size_t n=0; n<setupData.size(); n++)
    {
        std::string setupName = setupData[n][0].c_str();
		std::string magazineLoadoutName = setupData[n][4].c_str();
        std::string launcherLoadoutName = setupData[n][5].c_str();

        bool setupOK = CheckLauncherSetup(databaseClass, launcherLoadoutName, errorMessages);
        allOK = allOK && setupOK;

		setupOK = CheckMagazineSetup(databaseClass, magazineLoadoutName, errorMessages);
        allOK = allOK && setupOK;
    }

    return allOK;
}

bool tcDatabaseManager::CheckLauncherSetup(const std::string& databaseClass, const std::string& setupName, 
                                           std::vector<std::string>& errorMessages)
{
	unsigned int nErrors = 0;

    std::vector<std::vector<std::string>> data = GetPlatformTableData("launcher_loadout", setupName, launcherFields);


	std::string matchingTable;
	double fuel_kg = 0;
	double maxTakeoffWeight_kg = 0;
	double weight_kg = 0;
	double dryWeight_kg = 0;

	bool checkAircraftWeight = false;

	if (PlatformExistsInTableList(aircraftTables, databaseClass, matchingTable))
	{
		std::vector<std::vector<std::string>> aircraftData = GetPlatformTableData(matchingTable, databaseClass, aircraftFields);
		if (aircraftData.size() > 0)
		{
			aircraftData[0][0].ToDouble(&fuel_kg);
			aircraftData[0][1].ToDouble(&maxTakeoffWeight_kg);
			aircraftData[0][2].ToDouble(&dryWeight_kg);

			checkAircraftWeight = true;
		}
		else
		{
			assert(false);
		}
	}
	else
	{
		// don't check aircraft weight, but check for valid references
	}

	weight_kg = dryWeight_kg;



	// iterate through each item in data and update quantity, volume, and weight
	for (size_t n=0; n<data.size(); n++)
	{
		std::string item = data[n][0];
		long quantity_n = 0;
		data[n][1].ToLong(&quantity_n);

		std::string matchingTable;
		if (PlatformExistsInTableList(launcherEquipmentTables, item, matchingTable))
		{
			if (checkAircraftWeight)
			{
				std::vector<std::vector<std::string>> itemData = GetPlatformTableData(matchingTable, item, itemFields);
				if (itemData.size() > 0)
				{
					double itemWeight_kg = 0;
					itemData[0][0].ToDouble(&itemWeight_kg);

					weight_kg += double(quantity_n) * itemWeight_kg;
				}
				if (matchingTable == "fueltank")
				{
					std::vector<std::vector<std::string>> tankData = GetPlatformTableData(matchingTable, item, fueltankFields);
					if (tankData.size() > 0)
					{
						double fueltankFuel_kg = 0;
						tankData[0][0].ToDouble(&fueltankFuel_kg);
						weight_kg += double(quantity_n) * fueltankFuel_kg;
					}
				}
			}
		}
		else if (item.size() > 0) // non-blank item not found, bad reference
		{
			nErrors++;
			errorMessages.push_back(strutil::format("%s setup %s item not found: %s",
				databaseClass.c_str(), setupName.c_str(), item.c_str()));
		}
	}


	if (checkAircraftWeight)
	{
		float totalWeight_kg = weight_kg + fuel_kg;
		if (totalWeight_kg > maxTakeoffWeight_kg)
		{
			nErrors++;
			errorMessages.push_back(strutil::format("%s aircraft setup %s is overweight (%.1f/%.1f)",
				databaseClass.c_str(), setupName.c_str(), totalWeight_kg, maxTakeoffWeight_kg));
		}
	}


	return (nErrors == 0);
}


bool tcDatabaseManager::CheckMagazineSetup(const std::string& databaseClass, const std::string& setupName, 
                                           std::vector<std::string>& errorMessages)
{
    std::vector<std::vector<std::string>> data = GetPlatformTableData("magazine_loadout", setupName, magazineLoadoutFields);

	// just check that all items exist for now, TODO need to add weight/quantity check
	std::string matchingTable;
	
	size_t nRows = data.size();
	unsigned int nErrors = 0;
	for (size_t n=0; n<nRows; n++)
	{
		std::string itemName = data[n][0].c_str();
		if (PlatformExistsInTableList(magazineEquipmentTables, itemName, matchingTable))
		{
		}
		else
		{
			nErrors++;
			errorMessages.push_back(strutil::format("%s setup %s. Item not found: %s",
				databaseClass.c_str(), setupName.c_str(), itemName.c_str()));
		}
	}
	
	return (nErrors == 0);
}


/**
* @param beginAgain true to begin another transaction, set false if application is closing
*/
void tcDatabaseManager::Commit(bool beginAgain)
{
    try
    {
        sqlite3x::sqlite3_command sqlCmd(sqlConnection, "COMMIT;");
        sqlCmd.executenonquery();
        changesArePending = false;

        if (beginAgain)
        {
            sqlite3x::sqlite3_command sqlCmdBegin(sqlConnection, "BEGIN IMMEDIATE;");
            sqlCmdBegin.executenonquery();
			
			tcDatabase::Get()->Clear();
			tcDatabase::Get()->ReadWriteSql(&sqlConnection, true);
        }

    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "Commit Error");
    }
}

bool tcDatabaseManager::CreateIndices()
{
    try
    {
        if (!IsOpen()) return false;

        wxXmlDocument doc;
        std::string xmlPath("config/table_index.xml");
        if (!doc.Load(xmlPath))
        {
            std::string msg = strutil::format("tcDatabaseManager::CreateIndices - file not found or corrupt (%s)", xmlPath.c_str());
            //wxMessageBox(msg, "Error");
            return false;
        }

        wxXmlNode* root = doc.GetRoot();
        if (root == 0) return false;
        
        wxXmlNode* node = root->GetChildren();
        while (node != 0)
        {
            if (node->GetName() == "table")
            {
                std::string tableName = node->GetPropVal("name", "");
                std::string fieldName = node->GetPropVal("field", "");

                if ((tableName.size() > 0) && (fieldName.size() > 0))
                {
                    changesArePending = true;

                    try
                    {
                        std::string cmdText;
                        cmdText.Printf("DROP INDEX \"%s_autoidx\"", tableName.c_str());
                        sqlite3x::sqlite3_command dropCmd(sqlConnection, cmdText);
                        std::string msg = dropCmd.executestring();
                    }
                    catch (...)
                    {
                        // do nothing
                        std::string s = "Doing nothing";
                    }

                    std::string cmdText;
                    cmdText.Printf("CREATE INDEX %s_autoidx ON %s(%s ASC)",
                        tableName.c_str(), tableName.c_str(), fieldName.c_str());
                    sqlite3x::sqlite3_command sqlCmd(sqlConnection, cmdText);
                    sqlCmd.executenonquery();

                    
                }
            }

            node = node->GetNext();
        }



        return true;


    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "Error creating indices");
        return false;
    }
}

bool tcDatabaseManager::DeleteRecord(const std::string& table, const std::string& databaseClass, const std::string& additionalConstraint)
{
    std::map<std::string, int>::const_iterator iter = 
        tableRenameTypes.find(table);

    int tableType = DEFAULT_TABLE;   
    
    if (iter != tableRenameTypes.end())
    {
        tableType = iter->second;
    }

    std::vector<std::string> tableList;

    switch (tableType)
    {
    case PLATFORM_TABLE:
        tableList.push_back(table);
        tableList.push_back("platform_launcher");
        tableList.push_back("platform_magazine");
        tableList.push_back("platform_sensor");
        tableList.push_back("platform_names");
        tableList.push_back("platform_setup");
        break;
    default:
        tableList.push_back(table);
        break;
    }

    for (size_t n=0; n<tableList.size(); n++)
    {
        std::string command = strutil::format("delete from %s where DatabaseClass=\"%s\"", tableList[n].c_str(), databaseClass.c_str());
        if (additionalConstraint.size() > 0)
        {
            command += " and ";
            command += additionalConstraint;
        }
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlCmd.executenonquery();
        
        changesArePending = true;
    }

    return true;
}


bool tcDatabaseManager::DuplicateRecord(const std::string& table, const std::string& databaseClass, const std::string& copyName)
{
    std::map<std::string, int>::const_iterator iter = 
        tableRenameTypes.find(table);

    int tableType = DEFAULT_TABLE;

    if (iter != tableRenameTypes.end())
    {
        tableType = iter->second;
    }

	bool duplicateSetups = false;

    std::vector<std::string> tableList;

    switch (tableType)
    {
    case PLATFORM_TABLE:
        tableList.push_back(table);
        tableList.push_back("platform_launcher");
        tableList.push_back("platform_magazine");
        tableList.push_back("platform_sensor");
        tableList.push_back("platform_names");
		duplicateSetups = true;
        break;
    default:
        tableList.push_back(table);
        break;
    }

    for (size_t n=0; n<tableList.size(); n++)
    {
        std::string command = strutil::format("select * from %s where DatabaseClass=\"%s\";", tableList[n].c_str(), databaseClass.c_str());
        sqlite3_command selectCommand(sqlConnection, command);
        sqlite3_reader results = selectCommand.executereader();

        std::string s;

        std::vector<std::string> valuesArray;

        while (results.read())
        {
            int nCols = results.GetNumberCols();
            std::string valuesString = std::string("\"") + copyName + std::string("\"");
            for (int m=1;m<nCols;m++)
            {
                valuesString += ",\"";
                valuesString += std::string(results.getstring(m).c_str());
                valuesString += "\"";
            }
            valuesArray.push_back(valuesString);
        }

        for (size_t k=0; k<valuesArray.size(); k++)
        {
            command = strutil::format("insert into %s values (%s);", tableList[n].c_str(), valuesArray[k].c_str());
            sqlite3_command insertCommand(sqlConnection, command);
            try
            {
                insertCommand.executenonquery();
                changesArePending = true;
            }
            catch (sqlite3x::database_error err)
            {
                //wxMessageBox(err.what(), "Database Error");
            }
        }

    }

	if (duplicateSetups)
	{
		std::string command = strutil::format("select * from platform_setup where DatabaseClass=\"%s\";", databaseClass.c_str());
        sqlite3_command selectCommand(sqlConnection, command);
        sqlite3_reader results = selectCommand.executereader();

		int setupNumber = 1;
        std::vector<std::string> valuesArray;
        while (results.read())
        {
            int nCols = results.GetNumberCols();
			assert(nCols == 7);
			
			std::string setupName(results.getstring(1).c_str());
			std::string initialYear(results.getstring(2).c_str());
			std::string finalYear(results.getstring(3).c_str());
			std::string airComplement(results.getstring(4).c_str());
			std::string magazineLoadout(results.getstring(5).c_str());
			std::string launcherLoadout(results.getstring(6).c_str());


            std::string valuesString;
			valuesString.Printf("\"%s\",\"%s-%d\",\"%s\",\"%s\",\"%s-%d-A\",\"%s-%d-M\",\"%s-%d-L\"", copyName.c_str(), copyName.c_str(), setupNumber,
				initialYear.c_str(), finalYear.c_str(),
				copyName.c_str(), setupNumber,
				copyName.c_str(), setupNumber,
				copyName.c_str(), setupNumber);

            valuesArray.push_back(valuesString);

			DuplicateRecord("air_complement", airComplement, strutil::format("%s-%d-A", copyName.c_str(), setupNumber));
			DuplicateRecord("magazine_loadout", magazineLoadout, strutil::format("%s-%d-M", copyName.c_str(), setupNumber));
			DuplicateRecord("launcher_loadout", launcherLoadout, strutil::format("%s-%d-L", copyName.c_str(), setupNumber));

			setupNumber++;
        }

		for (size_t k=0; k<valuesArray.size(); k++)
        {
            command = strutil::format("insert into platform_setup values (%s);", valuesArray[k].c_str());
            sqlite3_command insertCommand(sqlConnection, command);
            try
            {
                insertCommand.executenonquery();
                changesArePending = true;
            }
            catch (sqlite3x::database_error err)
            {
                //wxMessageBox(err.what(), "Database Error");
            }
        }

	}

    return true;
}

const std::vector<std::string>& tcDatabaseManager::ExecuteQuery(const std::string& query)
{
    static std::vector<std::string> result;
    result.clear();

    if (!IsOpen()) return result;

    try
    {
        sqlite3_command sqlCmd(sqlConnection, query);
        sqlite3_reader results = sqlCmd.executereader();

        std::string s;

        while (results.read())
        {
            std::string s(results.getstring(0).c_str());
            result.push_back(s);
        }

        return result;
    }
    catch (...)
    {
        return result;
    }

}

sqlite3_connection& tcDatabaseManager::GetConnection()
{
    return sqlConnection;
}

/**
* @return vector of distinct values that occur in specified field, database class and table
*/
const std::vector<int> tcDatabaseManager::GetIdList(const std::string& table, const std::string& databaseClass, const std::string& field)
{
    static std::vector<int> idList;

    idList.clear();

    if (!IsOpen()) return idList;

    std::string command = strutil::format("select distinct %s from %s where DatabaseClass=\"%s\";", field.c_str(), table.c_str(), databaseClass.c_str());
    try
    {
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlite3_reader results = sqlCmd.executereader();

        std::string s;

        while (results.read())
        {
            std::string val(results.getstring(0).c_str());
            long nval = -1;
            if (val.ToLong(&nval))
            {
                idList.push_back(int(nval));
            }
        }

        return idList;
    }
    catch (...)
    {
        return idList;
    }
}

const std::string& tcDatabaseManager::GetCountry(const std::string& databaseClass)
{
	static std::string countryName;
	countryName.clear();

	tcDatabaseObject* data = tcDatabase::Get()->GetObject(databaseClass);
	if (tcPlatformDBObject* platformData = dynamic_cast<tcPlatformDBObject*>(data))
	{
		countryName = platformData->country.c_str();
	}

	return countryName;
}

/**
* Generalized version of GetPlatformList that returns unique list of records in table
*/
const std::vector<std::string>& tcDatabaseManager::GetGeneralList(const std::string& table, const std::string& field, const std::string& constraint)
{
	static std::vector<std::string> recordNames;

    recordNames.clear();

    if (!isOpen) return recordNames;


    std::string command;
    if (constraint.size() == 0)
    {
        command=strutil::format("select distinct %s from %s;", field.c_str(), table.c_str());
    }
    else
    {
        command=strutil::format("select distinct %s from %s %s;", field.c_str(), table.c_str(), constraint.c_str());
    }

    sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader results = sqlCmd.executereader();

    std::string s;

    while (results.read())
    {
        recordNames.push_back(std::string(results.getstring(0).c_str()));
    }

    recordNames.Sort();

    return recordNames;
}

const std::vector<std::string>& tcDatabaseManager::GetPlatformList(const std::string& platformTable, const std::string& constraint)
{
    static std::vector<std::string> platforms;

    platforms.clear();

    if (!isOpen) return platforms;

    std::string field("DatabaseClass");

    std::string command;
    if (constraint.size() == 0)
    {
        command=strutil::format("select distinct %s from %s;", field.c_str(), platformTable.c_str());
    }
    else
    {
        command=strutil::format("select distinct %s from %s %s;", field.c_str(), platformTable.c_str(), constraint.c_str());
    }

    sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader results = sqlCmd.executereader();

    std::string s;

    while (results.read())
    {
        platforms.push_back(std::string(results.getstring(0).c_str()));
    }

    platforms.Sort();

    return platforms;
}

/**
* Add date range to each name entry, if available
*/
const std::vector<std::string>& tcDatabaseManager::GetPlatformListAnnotated(const std::string& platformTable, const std::string& constraint)
{
	static std::vector<std::string> platformList;
	platformList.clear();

	int tableType = DEFAULT_TABLE;

    std::map<std::string, int>::const_iterator iter = 
        tableRenameTypes.find(platformTable);

    if (iter != tableRenameTypes.end())
    {
        tableType = iter->second;
    }

	platformList = GetPlatformList(platformTable, constraint);

	if ((platformTable == "sonobuoy") || ((tableType != PLATFORM_TABLE) && (tableType != LAUNCHER_EQUIPMENT_TABLE)))
	{
		return platformList;
	}

	// add InitialYear FinalYear info to each line
	for (size_t n=0; n<platformList.size(); n++)
	{

		std::string command;

		command=strutil::format("select DatabaseClass,InitialYear,FinalYear from %s where DatabaseClass=%s;", 
			platformTable.c_str(), platformList[n].c_str());

		sqlite3_command sqlCmd(sqlConnection, command);
		sqlite3_reader results = sqlCmd.executereader();

		std::string s;

		if (results.read())
		{
			platformList[n] = strutil::format("%s (%s-%s)", 
				platformList[n].c_str(), results.getstring(1).c_str(), results.getstring(2).c_str());
		}
	}


	return platformList;
}


const std::vector<std::vector<std::string>>& tcDatabaseManager::GetPlatformTableData(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList,
                                                                          const std::string additionalConstraint)
{
    static std::vector<std::vector<std::string>> tableData;
    tableData.clear();

    if (!isOpen) return tableData;

    std::string fields;
    for (size_t n=0; n<fieldList.size(); n++)
    {
        fields += fieldList[n];
        if ((n+1)<fieldList.size()) fields += ",";
    }

    std::string field("DatabaseClass");
    std::string command = strutil::format("select %s from %s where DatabaseClass=\"%s\"", fields.c_str(), table.c_str(), databaseClass.c_str());
    if (additionalConstraint.size() > 0)
    {
        command += " and ";
        command += additionalConstraint;
    }
    

    try
    {
		sqlite3_command sqlCmd(sqlConnection, command);
        sqlite3_reader results = sqlCmd.executereader();

        while (results.read())
        {
            std::vector<std::string> row;
            for (size_t n=0; n<fieldList.size(); n++)
            {
                row.push_back(results.getstring(int(n)).c_str());
            }
            tableData.push_back(row);
        }
    }
    catch (sqlite3x::database_error err)
    {
		std::string errorDescription;
		errorDescription.Printf("Error (%s) with command:%s", err.what(), command.c_str());
        //wxMessageBox(errorDescription, "Database Error");
    }

    return tableData;
}



/**
* @return list of DatabaseClass values for cases where field matches value
*/
const std::vector<std::string>& tcDatabaseManager::GetReferences(const std::string& table, const std::string& field, const std::string& value)
{
    static std::vector<std::string> references;

    references.clear();

    std::string command = strutil::format("select DatabaseClass from %s where %s = \"%s\"", table.c_str(), field.c_str(), value.c_str());
    sqlite3_command sqlCmd(sqlConnection, command);

    try
    {
        sqlite3_reader results = sqlCmd.executereader();

        while (results.read())
        {
            references.push_back(results.getstring(0).c_str());
        }
    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "Database Error");
    }


    return references;
}


void tcDatabaseManager::Init()
{
    //enum {
    //    PLATFORM_TABLE = 1, 
    //    SENSOR_TABLE = 2, 
    //    LAUNCHER_EQUIPMENT_TABLE = 3, 
    //    STORES_TABLE = 4, 
    //    };

    tableRenameTypes["air"] = PLATFORM_TABLE;
    tableRenameTypes["ground"] = PLATFORM_TABLE;
    tableRenameTypes["ship"] = PLATFORM_TABLE;
    tableRenameTypes["simpleair"] = PLATFORM_TABLE;
    tableRenameTypes["sonobuoy"] = PLATFORM_TABLE;
    tableRenameTypes["sub"] = PLATFORM_TABLE;


    tableRenameTypes["ecm"] = SENSOR_TABLE;
    tableRenameTypes["esm"] = SENSOR_TABLE;
    tableRenameTypes["optical"] = SENSOR_TABLE;
    tableRenameTypes["radar"] = SENSOR_TABLE;
    tableRenameTypes["sonar"] = SENSOR_TABLE;

    tableRenameTypes["ballistic"] = LAUNCHER_EQUIPMENT_TABLE;
    tableRenameTypes["torpedo"] = LAUNCHER_EQUIPMENT_TABLE;
    tableRenameTypes["missile"] = LAUNCHER_EQUIPMENT_TABLE;
	tableRenameTypes["ballistic_missile"] = LAUNCHER_EQUIPMENT_TABLE;

    tableRenameTypes["stores"] = DEFAULT_TABLE;



    aircraftTables.push_back("air");
    aircraftTables.push_back("simpleair");

	platformTables.push_back("air");
	platformTables.push_back("simpleair");
	platformTables.push_back("ship");
	platformTables.push_back("sub");
	platformTables.push_back("ground");

    launcherEquipmentTables.push_back("ballistic");
    launcherEquipmentTables.push_back("ballistic_missile");
    launcherEquipmentTables.push_back("torpedo");
    launcherEquipmentTables.push_back("missile");
    launcherEquipmentTables.push_back("cm");
    launcherEquipmentTables.push_back("sonobuoy");
    launcherEquipmentTables.push_back("fueltank");

	magazineEquipmentTables = launcherEquipmentTables;
	magazineEquipmentTables.push_back("item");

    setupFields.push_back("SetupName");
    setupFields.push_back("InitialYear");
    setupFields.push_back("FinalYear");
    setupFields.push_back("AirComplement");
    setupFields.push_back("MagazineLoadout");
    setupFields.push_back("LauncherLoadout");

    launcherFields.push_back("Item");
    launcherFields.push_back("Quantity");
    launcherFields.push_back("LauncherId");

    magazineLoadoutFields.push_back("Item");
    magazineLoadoutFields.push_back("Quantity");
    magazineLoadoutFields.push_back("MagazineId");


	aircraftFields.push_back("FuelCapacity_kg");
	aircraftFields.push_back("MaxTakeoffWeight_kg");
	aircraftFields.push_back("Weight_kg");

	itemFields.push_back("Weight_kg");

	fueltankFields.push_back("FuelCapacity_kg");

}

double tcDatabaseManager::DateTimeToFloatYear(const const std::chrono::system_clock::time_point& dt) const
{
	double result = 0;

	// convert back to floating point year
	result = double(dt.GetYear());
	if (const std::chrono::system_clock::time_point::IsLeapYear(dt.GetYear()))
	{
		result += (double(dt.GetDayOfYear()) - 0.5) / 366.0;
	}
	else
	{
		result += (double(dt.GetDayOfYear()) - 0.5) / 365.0;
	}

	return result;
}


bool tcDatabaseManager::IsOpen() const
{
    return isOpen;
}

bool tcDatabaseManager::IsWithinDateRange(const std::string& s, const const std::chrono::system_clock::time_point& startFilterDate, const const std::chrono::system_clock::time_point& endFilterDate)
{
	static unsigned long errorCount = 0;

	double startDate = DateTimeToFloatYear(startFilterDate);
	double endDate = DateTimeToFloatYear(endFilterDate);

	tcDatabase* database = tcDatabase::Get();
	bool dynamicLoad = database->IsUsingDynamicLoad();

	tcDatabaseObject* data = database->GetObject(s);
	if (data != 0)
	{
		return (data->initialYear <= endDate) && (data->finalYear >= startDate);
	}
	else
	{
		return true; // changed this 15DEC2013 to keep non tcDatabaseObject tables from disappearing
		//if (errorCount++ <= 1)
		//{
		//	assert(false);
		//}
		//return false;
	}
}

bool tcDatabaseManager::Open(const std::string& inFile)
{
    try
    {
        if (isOpen)
        {
            sqlConnection.close();
        }

        BackupFile(inFile);

        sqlConnection.open(inFile.c_str());

        sqlite3x::sqlite3_command sqlCmdBegin(sqlConnection, "BEGIN IMMEDIATE;");
        sqlCmdBegin.executenonquery();

        isOpen = true;
        changesArePending = false;

		tcDatabase::Get()->ReadWriteSql(&sqlConnection, true);

        return true;
    }
    catch (...)
    {
        isOpen = false;
        changesArePending = false;
        return false;
    }
}

bool tcDatabaseManager::PlatformExistsInTable(const std::string& platformTable, const std::string& platformName)
{
    if (!isOpen) return false;

    std::string field("DatabaseClass");
    std::string command = strutil::format("select * from %s where DatabaseClass=\"%s\";", platformTable.c_str(), platformName.c_str());
    sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader results = sqlCmd.executereader();

    std::string s;

    if (results.read())
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool tcDatabaseManager::PlatformExistsInTableList(const std::vector<std::string>& platformTableList, const std::string& platformName, std::string& matchingTable)
{
    for (size_t n=0; n<platformTableList.size(); n++)
    {
        std::string table = platformTableList[n];
        if (PlatformExistsInTable(table, platformName))
        {
            matchingTable = table;
            return true;
        }
    }

    matchingTable.clear();

    return false;
}

/**
* Reads fields for objects derived from tcDatabaseClass or that have a DatabaseClass column as text primary key
*/
const std::vector<std::string>& tcDatabaseManager::ReadDatabaseObjectFields(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList)
{
    static std::vector<std::string> fields;
    fields.clear();

    if ((!isOpen) || (fieldList.size() == 0)) return fields;

    std::string columnDefinition;
    for (size_t k=0; k<fieldList.size(); k++)
    {
        columnDefinition += fieldList[k];
        if ((k+1) < fieldList.size()) columnDefinition += ",";
    }

	if (databaseClass.size() == 0)
	{
		return fields; // to keep "not an error" from being thrown below
	}

    std::string command = strutil::format("select %s from %s where DatabaseClass=\"%s\";", 
        columnDefinition.c_str(), table.c_str(), databaseClass.c_str());

    try
    {   
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlite3_reader results = sqlCmd.executereader();

        if (results.read())
        {
            for (size_t k=0; k<fieldList.size(); k++)
            {
                fields.push_back(results.getstring(k).c_str());
            }
        }

        assert(!results.read()); // should only be one result for unique DatabaseClass
    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "ReadDatabaseObjectFields Error");
        throw std::exception("ReadDatabaseObjectFields Error");
    }

    return fields;
}

/**
* @return true if rename successful
*/
bool tcDatabaseManager::RenameRecord(const std::string& table, const std::string& originalName, const std::string& newName)
{
    std::map<std::string, int>::const_iterator iter = 
        tableRenameTypes.find(table);

    int tableType = DEFAULT_TABLE;

    if (iter != tableRenameTypes.end())
    {
        tableType = iter->second;
    }

    std::vector<std::string> tableList;

    switch (tableType)
    {
    case PLATFORM_TABLE:
        tableList.push_back(table);
        tableList.push_back("platform_launcher");
        tableList.push_back("platform_magazine");
        tableList.push_back("platform_sensor");
        tableList.push_back("platform_names");
        tableList.push_back("platform_setup");
        break;
    default:
        tableList.push_back(table);
        break;
    }

    for (size_t n=0; n<tableList.size(); n++)
    {
        std::string command = strutil::format("update %s set DatabaseClass=\"%s\" where DatabaseClass=\"%s\";", tableList[n].c_str(), newName.c_str(), originalName.c_str());
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlCmd.executenonquery();
        changesArePending = true;
    }

    return true;
}

void tcDatabaseManager::TestTemporaryLoad()
{
	if (!isOpen) return;

	/*tcDatabase* database = tcDatabase::Get();
	tcDBObjSerializerSql<tcSonarDBObject> serializer(database, sqlConnection, "sonar");

	tcSonarDBObject* sonar = serializer.LoadRecordTemporary("AQS-13B");
	delete sonar;*/

}

void tcDatabaseManager::UpdateDatabaseObject(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList, const std::vector<std::string>& valueList)
{
    assert(fieldList.size() == valueList.size());
    std::string setExpression;

    for (size_t n=0; n<fieldList.size(); n++)
    {
        setExpression += strutil::format("%s=\"%s\"", fieldList[n].c_str(), valueList[n].c_str());
        if ((n+1)<fieldList.size()) setExpression += ",";
    }

    try
    {
        std::string command = strutil::format("update %s set %s where DatabaseClass=\"%s\";", 
            table.c_str(), setExpression.c_str(), databaseClass.c_str());
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlCmd.executenonquery();
        changesArePending = true;

		tcDatabase::Get()->ReloadRecord(databaseClass.c_str());
    }
    catch (sqlite3x::database_error err)
    {
        std::string caption = strutil::format("Update of %s failed", databaseClass.c_str());
        //wxMessageBox(err.what(), caption);
    }

}

/**
* Updates platform tables like platform_launcher, platform_sensor, platform_magazine
* Deletes existing entries and then inserts updated data
*/
void tcDatabaseManager::UpdatePlatformTableData(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList,
         const std::vector<std::vector<std::string>>& tableData, const std::string& additionalConstraint)
{
    if (!isOpen) return;

    try
    {
        std::string command = strutil::format("delete from %s where DatabaseClass=\"%s\"", table.c_str(), databaseClass.c_str());
        if (additionalConstraint.size() > 0)
        {
            command += " and ";
            command += additionalConstraint;
        }
        sqlite3_command sqlCmd(sqlConnection, command);
        sqlCmd.executenonquery();
        changesArePending = true;

        std::string fields("DatabaseClass,");
        for (size_t n=0; n<fieldList.size(); n++)
        {
            fields += fieldList[n];
            if ((n+1)<fieldList.size()) fields += ",";
        }

        size_t nColumns = fieldList.size();
        for (size_t row=0; row<tableData.size(); row++)
        {
            assert(tableData[row].size() == nColumns);

            std::string values = std::string("\"") + databaseClass + std::string("\",");
            for (size_t n=0; n<nColumns; n++)
            {
                std::string value_n = std::string("\"") + tableData[row][n] + std::string("\"");
                values += value_n;
                if ((n+1) < nColumns) values += ",";
            }

            std::string command2 = strutil::format("insert into %s (%s) values (%s)", table.c_str(), fields.c_str(), values.c_str());
            sqlite3_command sqlCmd2(sqlConnection, command2);
            sqlCmd2.executenonquery();
        }

		tcDatabase::Get()->ReloadRecord(databaseClass.c_str());

    }
    catch (sqlite3x::database_error err)
    {
        //wxMessageBox(err.what(), "Database Error");
    }


}


tcDatabaseManager::tcDatabaseManager()
: isOpen(false),
  changesArePending(false)
{
    Init();
}

tcDatabaseManager::~tcDatabaseManager()
{
    Close();
}
