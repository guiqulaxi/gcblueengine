/**
**  @file tcSensorPlatformDBObject.h
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

#ifndef _SENSORPLATFORMDBOBJECT_H_
#define _SENSORPLATFORMDBOBJECT_H_

#//include "tcDBString.h"
#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include <vector>
#include <string>
#include <memory>
#include "tcComponentDBObject.h"
class tcFile;

namespace database
{
    class tcDatabase;
	class tcSqlReader;
    class CsvTranslator;

    /**
    * Sensor info for platform
    */
    class tcSensorPlatformDBObject : public tcComponentDBObject
    {
    public:
        enum 
        { 
            MAXSENSORS = 16   ///< number of sensor entries supported in database
        };

        std::vector<std::string> sensorClass;

        
		std::vector<long> sensorId; ///< database id's of sensors
        std::vector<float> sensorAz; ///< pointing angles of sensors in degrees


        virtual const char* GetClassName() const {return "Generic";} ///< returns class name of database object
       
		bool HasAllEmitters(std::vector<long>& emitters);
        
        void PrintToFile(tcFile& file);
      
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;
        void WritePythonValue(const std::string &mzClass, std::string& valueString) const;
        void WritePython(const std::string&mzClass, std::string& valueString) const;

        static void AddSqlColumns(std::string& columnString);

        tcSensorPlatformDBObject();
        tcSensorPlatformDBObject(const tcSensorPlatformDBObject& obj); ///< copy constructor
        virtual ~tcSensorPlatformDBObject();
        void UpdateSensorList();

	private:
        

    };

}

#endif

