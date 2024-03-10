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

#include "DatabaseExport.h"
#include "DatabaseManager.h"

#include "wx/dir.h"
#include "wx/file.h"
#include "wx/filefn.h"
#include "wx/msgdlg.h"
#include "wx/textfile.h"
//#include "wx/wx.h"
#include <string>
#include <vector>

//#ifdef _DEBUG
//#define new DEBUG_NEW
//#endif

using sqlite3x::sqlite3_connection;
using sqlite3x::sqlite3_reader;


bool tcDatabaseTranslator::ExportDatabaseToCSV(sqlite3_connection& sqlConnection, const std::string& outDir)
{
    std::string command("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;");
    sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader tableData = sqlCmd.executereader(); 
    unsigned int nRead = 0;
    while (tableData.read())
    {
        std::string tableName = tableData.getstring(0);
        if (!ExportTableToCSV(sqlConnection, tableName, outDir))
        {
            return false;
        }
        nRead++;
    }

    if (nRead > 0)
    {
        return true;
    }
    else
    {
        std::string msg("Database file is invalid or empty");
        //wxMessageBox(msg, "Database Error", wxICON_ERROR | wxOK);
        return false;
    }
}

bool tcDatabaseTranslator::ExportTableToCSV(sqlite3_connection& sqlConnection, const std::string& tableName, const std::string& outDir)
{

    if (!wxDir::Exists(outDir))
    {
        wxMkdir(outDir);
    }

    std::string fileName;
    fileName.Printf("%s\\%s.csv", outDir.c_str(), tableName.c_str());
    wxTextFile out_file(fileName);
    bool success = false;
    if (out_file.Exists())
    {
        success = out_file.Open();
        out_file.Clear();
    }
    else
    {
        success = out_file.Create();
    }

    if (!success)
    {
        //wxMessageBox("Error opening csv file");
        return false;
    }

    std::vector<std::string> fieldNames;
    std::vector<std::string> fieldTypes;
    std::vector<bool> isPrimaryKey;

    std::string command;
    command=strutil::format("PRAGMA table_info(%s);", tableName.c_str());
    sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader fieldData = sqlCmd.executereader();
    while (fieldData.read())
    {
        std::string field_name = fieldData.getstring(1);
        std::string field_type = fieldData.getstring(2);
        bool pk = fieldData.getint(5) != 0;

        fieldNames.push_back(field_name);
        fieldTypes.push_back(field_type);
        isPrimaryKey.push_back(pk);
    }

    // type affinities
    //* TEXT
    //* NUMERIC
    //* INTEGER
    //* REAL
    //* NONE
    assert(fieldTypes.size() == fieldNames.size());

    // write header row
    std::string line;
    for (size_t n=0; n<fieldNames.size(); n++)
    {
        line += strutil::format("%s %s", fieldNames[n].c_str(), fieldTypes[n].c_str());
        if (isPrimaryKey[n]) line += " primary key";

        if (n < (fieldNames.size()-1)) 
        {
            line += ",";
        }
        else
        {
            //line += "\n";
        }
    }
    out_file.AddLine(line, wxTextFileType_Dos);

    // write data for table
    {
        command=strutil::format("select * from %s;", tableName.c_str());
        sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
        sqlite3_reader data = sqlCmd.executereader();
        while (data.read())
        {
            std::string line;
            for (size_t n=0; n<fieldNames.size(); n++)
            {
                std::string fieldText = data.getstring(n).c_str();
                FieldExportCleaner(fieldText);

                std::string sn("\"");
                sn += fieldText;
                sn += "\"";

                line += sn;
                if (n < (fieldNames.size()-1)) 
                {
                    line += ",";
                }
                else
                {
                    //line += "\n";
                }
            }
            out_file.AddLine(line, wxTextFileType_Dos);
        }
    }

    out_file.Write(wxTextFileType_Dos);

    return true;
}

const std::vector<std::string>& tcDatabaseTranslator::GetTableList(sqlite3_connection& sqlConnection)
{
	static std::vector<std::string> tableList;
	tableList.clear();

	std::string command("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;");
    sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader tableData = sqlCmd.executereader(); 
    while (tableData.read())
    {
        std::string tableName = tableData.getstring(0);
		tableList.push_back(tableName);
    }

	return tableList;
}

bool tcDatabaseTranslator::ImportDatabaseFromCSV(sqlite3_connection& sqlConnection, const std::string& inDir)
{
    std::string command("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;");
    sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
    sqlite3_reader tableData = sqlCmd.executereader(); 
    unsigned int nTables = 0;
    while (tableData.read())
    {
        nTables++;
    }

    if (nTables > 0)
    {
        std::string msg(strutil::format("Overwrite tables in database?"));
            wxMessageDialog* confirm = new wxMessageDialog(NULL, msg, "Confirm Overwrite", wxYES_NO | wxNO_DEFAULT | wxICON_QUESTION);
        if (confirm->ShowModal() != wxID_YES)
        {
            return false;
        }
    }

    if (!wxDir::Exists(inDir))
    {
        std::string msg;
        msg.Printf("Import directory not found (%s)", inDir.c_str());
        //wxMessageBox(msg, "Import Error", wxICON_ERROR | wxOK);
        return false;
    }

    wxDir dir(inDir);
    if (!dir.HasFiles("*.csv"))
    {
        std::string msg;
        msg.Printf("No CSV files found in %s", inDir.c_str());
        //wxMessageBox(msg, "Import Error", wxICON_ERROR | wxOK);
        return false;
    }

    std::vector<std::string> fileArray;
    dir.GetAllFiles(inDir, &fileArray, "*.csv",  wxDIR_FILES);
    size_t nFiles = fileArray.size();
    for (size_t n=0; n<nFiles; n++)
    {
        if (!ImportTableFromCSV(sqlConnection, fileArray[n]))
        {
            return false;
        }
    }


    return true;
}

bool tcDatabaseTranslator::ImportTableFromCSV(sqlite3_connection& sqlConnection, const std::string& inFile)
{
    if (!tcDatabaseManager::Get()->IsOpen()) return false;

    std::string tableName = inFile.AfterLast('\\').BeforeFirst('.');

    wxTextFile csvFile;
    csvFile.Open(inFile.c_str());
    if (!csvFile.IsOpened())
    {
        std::string msg;
        msg.Printf("Failed to open CSV file %s", inFile.c_str());
        //wxMessageBox(msg, "Import Error", wxICON_ERROR | wxOK);
        return false;
    }

    std::vector<std::string> csvData;

    size_t nLines = csvFile.GetLineCount();
    if (nLines == 0)
    {
        std::string msg;
        msg.Printf("Empty CSV file %s", inFile.c_str());
        //wxMessageBox(msg, "Import Error", wxICON_ERROR | wxOK);
        return false; // empty file
    }

    tcDatabaseManager::Get()->Commit(true);

    std::string command;

    if (dropTable)
    {
        try
        {
            command=strutil::format("DROP TABLE %s;", tableName.c_str());
            sqlite3x::sqlite3_command sqlCmd(sqlConnection, command);
            sqlCmd.executenonquery();
        }
        catch (...)
        {
            // probably table doesnt exist, empty database??
        }
    }

    std::string headerLine = csvFile.GetFirstLine();
    size_t nReplace = headerLine.Replace("\"", ""); // remove all quotes from header line, so field affinity is read correctly
    command=strutil::format("CREATE TABLE %s (%s);", tableName.c_str(), headerLine.c_str());
    sqlite3x::sqlite3_command sqlCmdCreate(sqlConnection, command);
    sqlCmdCreate.executenonquery();

    statusRows.push_back(strutil::format("Importing %s...", tableName.c_str()));
    unsigned int errorCount = 0;

    //command = "BEGIN;";
    //sqlite3x::sqlite3_command sqlCmdBegin(sqlConnection, command.c_str());
    //sqlCmdBegin.executenonquery();

    size_t csv_line = 1; // line in CSV file
    std::string line = csvFile.GetNextLine();

    while (!csvFile.Eof())
    {
        size_t nCurrent = csvFile.GetCurrentLine();
        wxTextFileType lineType = csvFile.GetLineType(csvFile.GetCurrentLine());

        while ((lineType != wxTextFileType_Dos) && (!csvFile.Eof()))
        {
            line += csvFile.GetNextLine(); // keep reading until we get to a DOS /n/r record ending used by CSV format
            if (!csvFile.Eof())
            {
                lineType = csvFile.GetLineType(csvFile.GetCurrentLine());
            }
        }

        LineCleaner(line);

        try
        {
            command=strutil::format("INSERT OR REPLACE INTO %s VALUES (%s);", tableName.c_str(), line.c_str());
            sqlite3x::sqlite3_command sqlCmdCreate(sqlConnection, command);
            sqlCmdCreate.executenonquery();
        }
		catch (sqlite3x::database_error err)
		{
			// likely a bad pattern of quotes or commas, remove quotes within quotes
            if (errorCount == 0) statusRows.push_back("\n"); // first error
            std::string errorLine;
			errorLine.Printf("ERROR (%s) %s line %d: %s\n", err.what(), tableName.c_str(), csv_line+1, line.c_str());
            statusRows.push_back(errorLine);
            errorCount++;
		}
        catch (...)
        { 
			// likely a bad pattern of quotes or commas, remove quotes within quotes
            if (errorCount == 0) statusRows.push_back("\n"); // first error
            std::string errorLine;
            errorLine.Printf("ERROR %s line %d: %s\n", tableName.c_str(), csv_line+1, line.c_str());
            statusRows.push_back(errorLine);
            errorCount++;
        }

        if (!csvFile.Eof()) line = csvFile.GetNextLine();
        csv_line++;
    }

    tcDatabaseManager::Get()->Commit(true);
    //command = "COMMIT;";
    //sqlite3x::sqlite3_command sqlCmdCommit(sqlConnection, command.c_str());
    //sqlCmdCommit.executenonquery();

    if (errorCount == 0)
    {
        statusRows.push_back("no errors\n");
    }
    else
    {
        statusRows.push_back("\n");
    }
    return true;
}

/**
* Attempt to fix quotes within text fields and other errors that cause import problems
*/
void tcDatabaseTranslator::LineCleaner(std::string& line)
{
    std::string cleanLine;

    // if a " is encountered, the next character must be a " ("" escape) or a comma do end the record
    for (size_t n=0; n<line.size(); n++)
    {
        wxChar cn = line.GetChar(n);
        wxChar cnm1 = (n > 0) ? line.GetChar(n-1) : '*';
        wxChar cnp1 = ((n+1) < line.size()) ? line.GetChar(n+1) : 0;

        if ((cn != '"') && (cn != ','))
        {
            cleanLine += cn;
        }
        else if (cn == '"')
        {
            if ((n == 0) || (cnp1 == ',') || (cnp1 == '"') || (cnm1 == '"') || (cnm1 == ',') || (cnp1 == 0))
            {
                cleanLine += cn;
            }
            else // add double quote
            {
                cleanLine += cn;
                cleanLine += '"';
            }
        }
        else if (cn == ',')
        {
            if ((cnp1 == ',') || (cnp1 == 0))
            {
                cleanLine += cn;
                cleanLine += "\"\"";
            }
            else
            {
                cleanLine += cn;
            }
        }
    }

    line = cleanLine;
}

/**
* Changes all single instances of " in field to "" 
*/
void tcDatabaseTranslator::FieldExportCleaner(std::string& fieldText)
{
    std::string cleanField;

    for (size_t n=0; n<fieldText.size(); n++)
    {
        wxChar cn = fieldText.GetChar(n);
        wxChar cnm1 = (n > 0) ? fieldText.GetChar(n-1) : 0;
        wxChar cnp1 = ((n+1) < fieldText.size()) ? fieldText.GetChar(n+1) : 0;

        if ((cn != '"') || (cnp1 == '"') || (cnm1 == '"'))
        {
            cleanField += cn;
        }
        else // add double quote
        {
            cleanField += cn;
            cleanField += '"';
        }
    }

    fieldText = cleanField;
}


void tcDatabaseTranslator::Test()
{
    //sqlite3x::sqlite3_connection sqlConnection;

    //sqlConnection.open("mytest.db");

    //sqlConnection.executenonquery("CREATE TABLE test_table (Field1 TEXT, Field2 TEXT, Field3)");


    //sqlConnection.close();
    
}

tcDatabaseTranslator::tcDatabaseTranslator()
: dropTable(true)
{
}

tcDatabaseTranslator::~tcDatabaseTranslator()
{
}