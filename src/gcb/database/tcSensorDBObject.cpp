/**  
**  @file tcSensorDBObject.cpp
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

#include "strutil.h"
#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif // _MSC_VER > 1000

#include "tcSensorDBObject.h"
//#include "math_constants.h"
//#include "randfn.h"
#include "CsvTranslator.h"
#include "tinyxml2.h"
#include "database/tcSqlReader.h"
#include "tcSensorState.h" // for factory method
#include "tcGameObject.h" // for factory method
#include <sstream>


#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

void tcSensorDBObject::CalculateParams()
{
    tcDatabaseObject::CalculateParams();
    angleError_deg = std::max(angleError_deg, 0.001f);
    elevationError_deg = std::max(elevationError_deg, 0.001f);

    angleError_rad = C_PIOVER180 * angleError_deg;
    elevationError_rad = C_PIOVER180 * elevationError_deg;

	maxElevation_deg = std::min(maxElevation_deg, 90.0f);
	minElevation_deg = std::min(minElevation_deg, -90.0f);

    minElevation_rad = C_PIOVER180 * minElevation_deg;
    maxElevation_rad = C_PIOVER180 * maxElevation_deg;

    averageFrequency_Hz = 0.5f * (minFrequency_Hz + maxFrequency_Hz);

    if (minFrequency_Hz > maxFrequency_Hz)
    {
        float temp = maxFrequency_Hz;
        maxFrequency_Hz = minFrequency_Hz;
        minFrequency_Hz = temp;
        fprintf(stderr, "Error - Sensor DB min freq must not exceed max freq, swapping (%s)\n", mzClass.c_str());
        //assert(false);
    }

    if (idThreshold_dB >= 99.0f)
    {
        idThreshold_dB = 9999.0f;
    }
}

std::shared_ptr<tcSensorState> tcSensorDBObject::CreateSensor(std::shared_ptr<tcGameObject> parent)
{
    return nullptr;
}

/**
* @return short description for database info window or other similar info displays
*/
const char* tcSensorDBObject::GetTypeDescription() const
{
    return "";
}


void tcSensorDBObject::PrintToFile(tcFile& file) 
{
   char zBuff[128];
   
   tcDatabaseObject::PrintToFile(file);
   
   sprintf(zBuff,"   ref range: %3.1f km\n",mfRefRange_km);
   file.WriteString(zBuff);
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcSensorDBObject::AddSqlColumns(std::string& columnString)
{
	tcDatabaseObject::AddSqlColumns(columnString);
    
	columnString += ",";

    columnString += "MaxRange_km number(5),";
    columnString += "RefRange_km number(6),";
    columnString += "FieldOfView_deg number(3),";
    columnString += "MinElevation_deg number(4),";
    columnString += "MaxElevation_deg number(4),";
    columnString += "ScanPeriod_s number(5),";
    columnString += "DamageEffect varchar(30),";
    columnString += "RangeError number(4),";
    columnString += "AngleError_deg number(4),";
    columnString += "ElevationError_deg number(4),";
    columnString += "MinFrequency_Hz number(6),";
    columnString += "MaxFrequency_Hz number(6),";
    columnString += "IdThreshold_dB numeric,";
    columnString += "CounterMeasureFactor number(5),";
    columnString += "IsSurveillance number(1)";
}

void tcSensorDBObject::ReadSql(tcSqlReader& entry)
{
	tcDatabaseObject::ReadSql(entry);

	mfMaxRange_km = entry.GetDouble("MaxRange_km");
	mfRefRange_km = entry.GetDouble("RefRange_km");
	mfFieldOfView_deg = entry.GetDouble("FieldOfView_deg");
    minElevation_deg = entry.GetDouble("MinElevation_deg");
    maxElevation_deg = entry.GetDouble("MaxElevation_deg");
	mfScanPeriod_s = entry.GetDouble("ScanPeriod_s");
    damageEffect = entry.GetString("DamageEffect");
    rangeError = entry.GetDouble("RangeError");
    angleError_deg = entry.GetDouble("AngleError_deg");
    elevationError_deg = entry.GetDouble("ElevationError_deg");
    minFrequency_Hz = entry.GetDouble("MinFrequency_Hz");
    maxFrequency_Hz = entry.GetDouble("MaxFrequency_Hz");
    idThreshold_dB = entry.GetDouble("IdThreshold_dB");
    counterMeasureFactor = entry.GetDouble("CounterMeasureFactor");
    isSurveillance = entry.GetInt("IsSurveillance") != 0;

    //CalculateParams();
}

void tcSensorDBObject::WriteSql(std::string& valueString) const
{
	tcDatabaseObject::WriteSql(valueString);

	std::stringstream s;

	s << ",";

	s << mfMaxRange_km << ",";
	s << mfRefRange_km << ",";
	s << mfFieldOfView_deg << ",";
    s << minElevation_deg << ",";
    s << maxElevation_deg << ",";
	s << mfScanPeriod_s << ",";
    s << "'" << damageEffect.c_str() << "',";
    s << rangeError << ",";
    s << angleError_deg << ",";
    s << elevationError_deg << ",";
    s << minFrequency_Hz << ",";
    s << maxFrequency_Hz << ",";
    s << idThreshold_dB << ",";
    s << counterMeasureFactor << ",";
    s << isSurveillance;

	valueString += s.str();
}

void tcSensorDBObject::WritePythonValue(std::string &valueString) const
{
    tcDatabaseObject::WritePythonValue(valueString);
    valueString+="    dbObj.mfMaxRange_km="+strutil::to_python_value(mfMaxRange_km)+"\n";
    valueString+="    dbObj.mfRefRange_km="+strutil::to_python_value(mfRefRange_km)+"\n";
    valueString+="    dbObj.mfFieldOfView_deg="+strutil::to_python_value(mfFieldOfView_deg)+"\n";
    valueString+="    dbObj.minElevation_deg="+strutil::to_python_value(minElevation_deg)+"\n";
    valueString+="    dbObj.maxElevation_deg="+strutil::to_python_value(maxElevation_deg)+"\n";
    valueString+="    dbObj.mfScanPeriod_s="+strutil::to_python_value(mfScanPeriod_s)+"\n";
    valueString+="    dbObj.damageEffect="+strutil::to_python_value(damageEffect)+"\n";
    valueString+="    dbObj.rangeError="+strutil::to_python_value(rangeError)+"\n";
    valueString+="    dbObj.angleError_deg="+strutil::to_python_value(angleError_deg)+"\n";
    valueString+="    dbObj.elevationError_deg="+strutil::to_python_value(elevationError_deg)+"\n";
    valueString+="    dbObj.minFrequency_Hz="+strutil::to_python_value(minFrequency_Hz)+"\n";
    valueString+="    dbObj.maxFrequency_Hz="+strutil::to_python_value(maxFrequency_Hz)+"\n";
    valueString+="    dbObj.idThreshold_dB="+strutil::to_python_value(idThreshold_dB)+"\n";
    valueString+="    dbObj.counterMeasureFactor="+strutil::to_python_value(counterMeasureFactor)+"\n";
    valueString+="    dbObj.isSurveillance="+strutil::to_python_value(isSurveillance)+"\n";

}

void tcSensorDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcSensorDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";;
}


tcSensorDBObject::tcSensorDBObject() : tcDatabaseObject(),
    mfMaxRange_km(100.0f),
    mfRefRange_km(80.0f),
    mfFieldOfView_deg(360.0f),
    minElevation_deg(-90.0f),
    maxElevation_deg(90.0f),
    minElevation_rad(-1.7f),
    maxElevation_rad(1.7f),
    mfScanPeriod_s(4.0f),
    damageEffect(""),
    isSurveillance(true)
{
   mzClass = "Default Sensor";
}

tcSensorDBObject::tcSensorDBObject(const tcSensorDBObject& obj) 
:   tcDatabaseObject(obj),
    mfMaxRange_km(obj.mfMaxRange_km),
    mfRefRange_km(obj.mfRefRange_km),
    mfFieldOfView_deg(obj.mfFieldOfView_deg),
    minElevation_deg(obj.minElevation_deg),
    maxElevation_deg(obj.maxElevation_deg),
    mfScanPeriod_s(obj.mfScanPeriod_s),
    damageEffect(obj.damageEffect),
    rangeError(obj.rangeError),
    angleError_deg(obj.angleError_deg),
    elevationError_deg(obj.elevationError_deg),
    minFrequency_Hz(obj.minFrequency_Hz),
    maxFrequency_Hz(obj.maxFrequency_Hz),
    idThreshold_dB(obj.idThreshold_dB),
    isSurveillance(obj.isSurveillance),
    angleError_rad(obj.angleError_rad),
    elevationError_rad(obj.elevationError_rad),
    minElevation_rad(obj.minElevation_rad),
    maxElevation_rad(obj.maxElevation_rad),
    counterMeasureFactor(obj.counterMeasureFactor)
{

}

tcSensorDBObject::~tcSensorDBObject() 
{
}


}
// #include <pybind11-global/pybind11/pybind11.h>
// #include <pybind11-global/pybind11/eval.h>
// #include <pybind11-global/pybind11/embed.h>

// using namespace scriptinterface ;
// namespace py = pybind11;
// using namespace py;
// void init_file1_bindings(py::module &m) {

//     // 绑定 file1.cpp 中的函数和类
//     py::class_<tcSensorDBObject,tcDatabaseObject>(m,"tcSensorDBObject")
//         .def_readwrite("mfMaxRange_km",&tcSensorDBObject::mfMaxRange_km);
// }


