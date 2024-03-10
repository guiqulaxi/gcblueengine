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
#ifndef _DATABASEMANAGER_H_
#define _DATABASEMANAGER_H_

#include "sqlite/sqlite3x.hpp"
//#include "wx/string.h"
#include "wx/arrstr.h"
//#include "wx/datetime.h"

#include <map>
#include <vector>

using sqlite3x::sqlite3_connection;

class tcDatabaseManager
{
public:

    bool Open(const std::string& inFile);
    bool Close();
    void Commit(bool beginAgain);
    bool IsOpen() const;
    bool AreChangesPending() const;

    sqlite3_connection& GetConnection();

    const std::vector<std::string>& ReadDatabaseObjectFields(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList);
    void UpdateDatabaseObject(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList, const std::vector<std::string>& valueList);

	const std::vector<std::string>& GetGeneralList(const std::string& table, const std::string& field, const std::string& constraint="");
    const std::vector<std::string>& GetPlatformList(const std::string& platformTable, const std::string& constraint="");
	const std::vector<std::string>& GetPlatformListAnnotated(const std::string& platformTable, const std::string& constraint="");
    const std::vector<std::vector<std::string>>& GetPlatformTableData(const std::string& table, const std::string& databaseClass, 
        const std::vector<std::string>& fieldList, const std::string additionalConstraint="");
    void UpdatePlatformTableData(const std::string& table, const std::string& databaseClass, const std::vector<std::string>& fieldList,
         const std::vector<std::vector<std::string>>& tableData, const std::string& additionalConstraint="");
    const std::vector<std::string>& GetReferences(const std::string& table, const std::string& field, const std::string& value);
    const std::vector<int> GetIdList(const std::string& table, const std::string& databaseClass, const std::string& field);
    const std::vector<std::string>& ExecuteQuery(const std::string& query);

    bool PlatformExistsInTable(const std::string& platformTable, const std::string& platformName);
    bool PlatformExistsInTableList(const std::vector<std::string>& platformTableList, const std::string& platformName, std::string& matchingTable);
    bool RenameRecord(const std::string& table, const std::string& originalName, const std::string& newName);
    bool DeleteRecord(const std::string& table, const std::string& databaseClass, const std::string& additionalConstraint="");
    bool DuplicateRecord(const std::string& table, const std::string& databaseClass, const std::string& copyName);

	const std::string& GetCountry(const std::string& databaseClass);
	bool IsWithinDateRange(const std::string& s, const const std::chrono::system_clock::time_point& startFilterDate, const const std::chrono::system_clock::time_point& endFilterDate);
	double DateTimeToFloatYear(const const std::chrono::system_clock::time_point& dt) const;

    bool CreateIndices();

    bool CheckForErrors(const std::string& logFile);
    bool CheckAllSetups();
    bool CheckSetupData(const std::string& databaseClass, std::vector<std::string>& errorMessages);
    bool CheckLauncherSetup(const std::string& databaseClass, const std::string& setupName, std::vector<std::string>& errorMessages);
	bool CheckMagazineSetup(const std::string& databaseClass, const std::string& setupName, std::vector<std::string>& errorMessages);
    static tcDatabaseManager* Get();

private:
    enum {
        PLATFORM_TABLE = 1, 
        SENSOR_TABLE = 2, 
        LAUNCHER_EQUIPMENT_TABLE = 3, 
        STORES_TABLE = 4,
        DEFAULT_TABLE = 5
        };

    sqlite3_connection sqlConnection;
    bool isOpen;
    bool changesArePending;

    std::map<std::string, int> tableRenameTypes;
    std::vector<std::string> aircraftTables;
	std::vector<std::string> platformTables;

    std::vector<std::string> launcherEquipmentTables;
	std::vector<std::string> magazineEquipmentTables;
    std::vector<std::string> setupFields;
    std::vector<std::string> launcherFields;
	std::vector<std::string> magazineLoadoutFields;
	std::vector<std::string> aircraftFields;
	std::vector<std::string> itemFields;
	std::vector<std::string> fueltankFields;

    void Init();
    void BackupFile(const std::string& fileName);

	void TestTemporaryLoad();

    tcDatabaseManager();
    virtual ~tcDatabaseManager();


};


#endif