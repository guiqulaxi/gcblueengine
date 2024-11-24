/**   
**  @file tcStoresDBObject.cpp
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
#endif // _MSC_VER > 1000



#include "tcStoresDBObject.h"
#include "CsvTranslator.h"
#include "tinyxml2.h"
#include "database/tcSqlReader.h"
#include <sstream>
#include "strutil.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{


	void tcStoresDBObject::PrintToFile(tcFile& file) 
	{
		tcString s;

		tcDatabaseObject::PrintToFile(file);

        s.Format("   display name:%s, capacity:%d, move time:%f \n", 
            displayName.c_str(), capacity, moveTime);
        file.WriteString(s.GetBuffer());
        for (size_t n=0; n<compatibleItems.size(); n++)
        {
            s.Format("       %d: %s\n", n, compatibleItems[n].c_str());
        }
		
	}

	/**
	* Adds sql column definitions to columnString. This is used for
	* SQL create table command
	*/
	void tcStoresDBObject::AddSqlColumns(std::string& columnString)
	{
		tcDatabaseObject::AddSqlColumns(columnString);

		columnString += ",";

        columnString += "DisplayName varchar(30),";
		columnString += "Capacity number(4),";
        columnString += "MaxVolume_m3 number(5),";
        columnString += "MaxWeight_kg number(5),";
		columnString += "MoveTime_s number(5),";

		for(unsigned i=0; i<MAX_STORES; i++) 
		{
			tcString s;
			s.Format("Class%d varchar(30)",i+1);
			columnString += s.GetBuffer();

			if (i < MAX_STORES - 1) columnString += ",";
		}
	}

	void tcStoresDBObject::ReadSql(tcSqlReader& entry)
	{
		tcDatabaseObject::ReadSql(entry);

        displayName = entry.GetString("DisplayName");
		capacity = entry.GetLong("Capacity");
        maxVolume_m3 = entry.GetDouble("MaxVolume_m3");
        maxWeight_kg = entry.GetDouble("MaxWeight_kg");
		moveTime = entry.GetDouble("MoveTime_s");

		for (unsigned i=0; i<MAX_STORES; i++) 
		{
			tcString s;

			s.Format("Class%d", i+1);
            std::string item =  entry.GetString(s.GetBuffer());
            if(item!="")
            {
                // 25 JUL 2009, modified this to allow semicolon delimited list of items
                std::string itemsToParse(item.c_str());
                auto items=strutil::split(itemsToParse,';');
                for(auto s:items)
                {
                    compatibleItems.push_back(s);
                }
            }

//            while (!itemsToParse.IsEmpty())
//            {
//                std::string item2 = itemsToParse.BeforeFirst(';');
//                item2.Trim(true);
//                item2.Trim(false);
//                if (item2.length() > 2)
//                {
//                    compatibleItems.push_back(item2);
//                }
//                itemsToParse = itemsToParse.AfterFirst(';');
//            }

            //if (item.length() > 2)
            //{
            //    compatibleItems.push_back(item);
            //}
		}
	}

    void tcStoresDBObject::WriteSql(std::string& valueString) const
	{
		tcDatabaseObject::WriteSql(valueString);

		std::stringstream s;

		s << ",";
		s << "'" << displayName.c_str() << "',";
		s << capacity << ",";
        s << maxVolume_m3 << ",";
        s << maxWeight_kg << ",";
		s << moveTime << ",";


		for(unsigned i=0; i<MAX_STORES; i++)
		{
            if (i < compatibleItems.size())
			{
				s << "'" << compatibleItems[i].c_str() << "'";
			}
			else
			{
				s << "''";
			}

			if (i < MAX_STORES - 1) s << ",";
		}

		valueString += s.str();
	}

    void tcStoresDBObject::WritePythonValue(std::string &valueString) const
    {
        tcDatabaseObject::WritePythonValue(valueString);
        valueString+="    dbObj.displayName="+strutil::to_python_value(displayName.c_str())+"\n";
        valueString+="    dbObj.capacity="+strutil::to_python_value(capacity)+"\n";
        valueString+="    dbObj.maxVolume_m3="+strutil::to_python_value(maxVolume_m3)+"\n";
        valueString+="    dbObj.maxWeight_kg="+strutil::to_python_value(maxWeight_kg)+"\n";
        valueString+="    dbObj.moveTime="+strutil::to_python_value(moveTime)+"\n";
        valueString+="    dbObj.compatibleItems="+strutil::to_python_value(compatibleItems)+"\n";
        valueString+="    dbObj.CalculateParams()\n";

    }

    void tcStoresDBObject::WritePython(std::string &valueString) const
    {
        valueString+="import pygcb\n";
        valueString+="def CreateDBObject():\n";
        valueString+="    dbObj=pygcb.tcStoresDBObject()\n";
        WritePythonValue(valueString);
        valueString+="    return dbObj\n";
    }


	tcStoresDBObject::tcStoresDBObject() : tcDatabaseObject(),
        displayName(""),
        capacity(0),
		moveTime(0)
	{
		mzClass = "Default Stores";

        compatibleItems.clear();
	}

	tcStoresDBObject::tcStoresDBObject(tcStoresDBObject& obj) 
		: tcDatabaseObject(obj) 
	{
        displayName = obj.displayName;
        capacity = obj.capacity;
		moveTime = obj.moveTime;
		
        compatibleItems.clear();
        for(unsigned i=0; i<obj.compatibleItems.size(); i++) 
		{
            compatibleItems.push_back(obj.compatibleItems[i]);
		}

	}


	tcStoresDBObject::~tcStoresDBObject() 
	{
	}


}
