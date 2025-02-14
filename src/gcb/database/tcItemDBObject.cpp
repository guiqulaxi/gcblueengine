/**   
**  @file tcItemDBObject.cpp
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



#include "tcItemDBObject.h"
#include "CsvTranslator.h"
#include "tinyxml2.h"
#include "database/tcSqlReader.h"
#include <sstream>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{


	void tcItemDBObject::PrintToFile(tcFile& file) 
	{
		tcDatabaseObject::PrintToFile(file);
	}

	/**
	* Adds sql column definitions to columnString. This is used for
	* SQL create table command
	*/
	void tcItemDBObject::AddSqlColumns(std::string& columnString)
	{
		tcDatabaseObject::AddSqlColumns(columnString);
	}

	void tcItemDBObject::ReadSql(tcSqlReader& entry)
	{
		tcDatabaseObject::ReadSql(entry);
	}

    void tcItemDBObject::WriteSql(std::string& valueString) const
	{
		tcDatabaseObject::WriteSql(valueString);
	}

    void tcItemDBObject::WritePythonValue(std::string &valueString) const
    {
        tcDatabaseObject::WritePythonValue(valueString);
    }

    void tcItemDBObject::WritePython(std::string &valueString) const
    {
        valueString+="import pygcb\n";
        valueString+="def CreateDBObject():\n";
        valueString+="    dbObj=pygcb.tcItemDBObject()\n";
        WritePythonValue(valueString);
        valueString+="    dbObj.CalculateParams()\n";
        valueString+="    return dbObj\n";;
    }


	tcItemDBObject::tcItemDBObject()
	{
		mzClass = "Default Item";
	}

	tcItemDBObject::tcItemDBObject(const tcItemDBObject& obj) 
		: tcDatabaseObject(obj) 
	{
	}


	tcItemDBObject::~tcItemDBObject() 
	{
	}


}
