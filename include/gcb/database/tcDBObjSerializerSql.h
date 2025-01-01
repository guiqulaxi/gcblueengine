/**
**  @file tcDBObjSerializerSql.h
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

#ifndef _DBOBJSERIALIZERSQL_H_
#define _DBOBJSERIALIZERSQL_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabase.h"
#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include "sqlite/sqlite3x.hpp"
#include "database/tcSqlReader.h"

//#include <wx/wx.h>
#ifdef WIN32
//#include <wx/msw/private.h> // for MS Windows specific definitions
#endif

using sqlite3x::sqlite3_reader;
using sqlite3x::sqlite3_command;
using sqlite3x::sqlite3_connection;
using std::string;
using std::exception;

/** 
* Saves/loads objects of class T from database. 
* Class T is any class derived from tcDatabaseObject.
* Class T should be a leaf class for this to work properly.
*
* SQL version of serializer to work with sqlite3 and sqlite3_plus
* C++ wrapper
*/
namespace database
{

	template <class T> 
	class tcDBObjSerializerSql
	{
	public:
		tcDBObjSerializerSql(tcDatabase* db, sqlite3x::sqlite3_connection& con, std::string s)
			: database(db), sqlConn(con), tableName(s) {}

		bool Load();
        long LoadRecord(const char* databaseClass);
        long LoadRecordForceKey(const char* databaseClass, long key);
		T* LoadRecordTemporary(const char* databaseClass);
		bool Save();
	private:
		tcDatabase* database;
		std::string tableName;
		sqlite3x::sqlite3_connection& sqlConn;

	};


	template <class T>
		bool tcDBObjSerializerSql<T>::Load()
	{ 

		try
		{
			// check if the table exists, abort if it doesn't
			std::string command = strutil::format("select count(*) from sqlite_master where name='%s';",
				tableName.c_str());
            string countStr = sqlConn.executestring(command);

			if (countStr == "0")
			{
				std::string message = strutil::format(
					"tcDBObjSerializerSql<T>::Load() table (%s) not found\n",
					tableName.c_str());

                //wxMessageBox(message.GetData(), "Error", wxICON_ERROR);
				return false;
			}

        }
        catch (exception& ex)
		{
            //wxMessageBox(ex.what(), "Error", wxICON_ERROR);
			return false;
		}



		try
		{
			std::string command = strutil::format("pragma table_info(%s);", tableName.c_str());
			sqlite3_command sqlCmd(sqlConn, command);

			sqlite3_reader tableInfo = sqlCmd.executereader();

			command = strutil::format("select * from %s;", tableName.c_str());

			sqlite3_command sqlCmd2(sqlConn, command);
			sqlite3_reader tableData = sqlCmd2.executereader();

			tcSqlReader sqlReader(tableInfo, tableData);

			while (sqlReader.Read())
			{
				long key;
                std::shared_ptr<T> obj = std::make_shared< T>();
                // T* obj = new T;
				obj->ReadSql(sqlReader);

                obj->CalculateParams();
                // if the obj already exists, delete the old and add the new (update)
                // (doesn't work for duplicates within database since BuildDictionaries needs to be called)
                // if (database->ObjectExists(obj->GetName()))
                // {
                //     fprintf(stdout, "Updating database class: %s\n", obj->GetName());
                //     std::shared_ptr<tcDatabaseObject>oldObj = database->GetObject(obj->GetName());
                //     // assert(oldObj != nullptr);
                    
                //     database->DeleteObject(oldObj->mnKey);
                // }
                // std::string className = obj->mzClass.c_str();
                // if(className=="57mm/70 Mks 2-3 Store")
                // {
                //     int a=0;
                // }
                // database->mcObjectData.AddElement(obj, key); // add to database, key gets new key val
                // obj->mnKey = key; // set key val of object (may not be necessary anymore)
                key=database->AddOrUpdateObject(obj);
            }

			tableInfo.close();
			tableData.close();

        }
        catch (exception& ex)
		{
            //wxMessageBox(ex.what(), "Error", wxICON_ERROR);
			return false;
		}

		return true;
	}

    template <class T>
        long tcDBObjSerializerSql<T>::LoadRecordForceKey(const char* databaseClass, long key)
    {
        long recordKey = -1;

		try
		{
			std::string command = strutil::format("pragma table_info(%s);", tableName.c_str());
			sqlite3_command sqlCmd(sqlConn, command);

			sqlite3_reader tableInfo = sqlCmd.executereader();

			command = strutil::format("select * from %s where DatabaseClass=\"%s\";", 
                tableName.c_str(), databaseClass);

			sqlite3_command sqlCmd2(sqlConn, command);
			sqlite3_reader tableData = sqlCmd2.executereader();

			tcSqlReader sqlReader(tableInfo, tableData);
            
			if (sqlReader.Read())
			{
                std::shared_ptr<T> obj = std::make_shared<T>();
                obj->ReadSql(sqlReader);
                
                // if the obj already exists, delete the old and add the new (update)
                // (doesn't work for duplicates within database since BuildDictionaries needs to be called)
    //             if (database->ObjectExists(obj->GetName()))
    //             {
    //                 fprintf(stdout, "Updating database class: %s\n", obj->GetName());
    //                 std::shared_ptr<tcDatabaseObject> oldObj = database->GetObject(obj->GetName());
    //                 assert(oldObj != 0);
                    
    //                 database->DeleteObject(oldObj->mnKey);
    //             }
    //             std::string className = obj->mzClass.c_str();
    //             if(className=="57mm/70 Mks 2-3 Store")
    //             {
    //                 int a=0;
    //             }
    //             database->mcObjectData.AddElementForceKey(obj, key);
                // obj->mnKey = key; // set key val of object (may not be necessary anymore)
                database->AddOrUpdateObjectForceKey(obj, key);
                recordKey = key;
			}

			tableInfo.close();
			tableData.close();
		}
		catch (exception& ex)
		{
            //wxMessageBox(ex.what(), "Error", wxICON_ERROR);
			return false;
		}

		return recordKey;
    }

    /**
    * Searches for and loads 1 record matching DatabaseClass.
    * @return new key if found, -1 otherwise
    */
	template <class T>
		long tcDBObjSerializerSql<T>::LoadRecord(const char* databaseClass)
	{ 
        long recordKey = -1;

		try
		{
			std::string command = strutil::format("pragma table_info(%s);", tableName.c_str());
			sqlite3_command sqlCmd(sqlConn, command);

			sqlite3_reader tableInfo = sqlCmd.executereader();

			command = strutil::format("select * from %s where DatabaseClass=\"%s\";", 
                tableName.c_str(), databaseClass);

			sqlite3_command sqlCmd2(sqlConn, command);
			sqlite3_reader tableData = sqlCmd2.executereader();

			tcSqlReader sqlReader(tableInfo, tableData);
            
			if (sqlReader.Read())
			{
				long key;
                std::shared_ptr<T> obj = std::make_shared<T>();
				obj->ReadSql(sqlReader);
                
                // if the obj already exists, delete the old and add the new (update)
                // (doesn't work for duplicates within database since BuildDictionaries needs to be called)
                // if (database->ObjectExists(obj->GetName()))
                // {
                //     fprintf(stdout, "Updating database class: %s\n", obj->GetName());
                //     std::shared_ptr<tcDatabaseObject> oldObj = database->GetObject(obj->GetName());
                //     assert(oldObj != 0);
                    
                //     database->DeleteObject(oldObj->mnKey);
                // }
                // std::string className = obj->mzClass.c_str();
                // if(className=="57mm/70 Mks 2-3 Store")
                // {
                //     int a=0;
                // }
                // database->mcObjectData.AddElement(obj, key); // add to database, key gets new key val
                // obj->mnKey = key; // set key val of object (may not be necessary anymore)
                recordKey =  database->AddOrUpdateObject(obj);;
			}

			tableInfo.close();
			tableData.close();
		}
		catch (exception& ex)
		{
            //wxMessageBox(ex.what(), "Error", wxICON_ERROR);
			return false;
		}

		return recordKey;
	}


	/**
    * Searches for and loads 1 record matching DatabaseClass.
    * @return ponter to new T if found, 0 otherwise
    */
	template <class T>
		T* tcDBObjSerializerSql<T>::LoadRecordTemporary(const char* databaseClass)
	{ 
        long recordKey = -1;

		try
		{
			std::string command = strutil::format("pragma table_info(%s);", tableName.c_str());
			sqlite3_command sqlCmd(sqlConn, command.c_str());

			sqlite3_reader tableInfo = sqlCmd.executereader();

			command = strutil::format("select * from %s where DatabaseClass=\"%s\";", 
                tableName.c_str(), databaseClass);

			sqlite3_command sqlCmd2(sqlConn, command.c_str());
			sqlite3_reader tableData = sqlCmd2.executereader();

			tcSqlReader sqlReader(tableInfo, tableData);
            
			T* obj = 0;
			if (sqlReader.Read())
			{
				obj = new T;
				obj->ReadSql(sqlReader);
			}

			tableInfo.close();
			tableData.close();

			return obj;
		}
		catch (std::exception& ex)
		{
            //wxMessageBox(ex.what(), "Error", wxICON_ERROR);
			return 0;
		}

		return 0;
	}



	/**
	* This version starts from a clean slate, first erasing the table
	* in the database if it exists.
	*/
	template <class T>
		bool tcDBObjSerializerSql<T>::Save()
	{

		try
		{
			// delete table if it exists
			std::string command = strutil::format("select count(*) from sqlite_master where name='%s';", 
				tableName.c_str());
			string countStr = sqlConn.executestring(command);


			if (countStr != "0")
			{
				command = strutil::format("drop table %s;", tableName.c_str());
				sqlConn.executenonquery(command);
			}




			std::string columnString;
			T::AddSqlColumns(columnString);

#ifdef _DEBUG
			fprintf(stdout, "column str: (%s)\n", columnString.c_str());
#endif
			command = strutil::format("create table %s (%s);", 
				tableName.c_str(), columnString.c_str());
			sqlConn.executenonquery(command);
		}
		catch(exception &ex) 
		{
			std::string message = strutil::format("Database error in table %s: %s",
				tableName.c_str(), ex.what());
            //wxMessageBox(message.GetData(), "Error", wxICON_ERROR);
		}

		long key;
		long nEntries = database->mcObjectData.GetCount();
		long pos = database->mcObjectData.GetStartPosition();
        std::shared_ptr<tcDatabaseObject> dbObj;

		for (long n=0;n<nEntries;n++) 
		{
			database->mcObjectData.GetNextAssoc(pos, key, dbObj);
            std::shared_ptr<T> obj = std::dynamic_pointer_cast<T>(dbObj);
			if (obj != 0)
			{
				try
				{
					std::string valueString;
					obj->WriteSql(valueString);

#ifdef _DEBUG
					fprintf(stdout, "value str: (%s)\n", valueString.c_str());
#endif
					std::string command = strutil::format("insert into %s values (%s);",
						tableName.c_str(), valueString.c_str());
					sqlConn.executenonquery(command);
				}
				catch(exception &ex) 
				{
					std::string message = strutil::format(
						"Error in table: %s, entry: %s, %s",
						tableName.c_str(), dbObj->mzClass.c_str(), ex.what());
                    //wxMessageBox(message.GetData(), "Database Error", wxICON_ERROR);
				}

			}

		}


		return true;

	}

} // namespace database

#endif

