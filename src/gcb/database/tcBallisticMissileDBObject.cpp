/*  
**  @file tcBallisticMissileDBObject.cpp
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


#include "tcBallisticMissileDBObject.h"
#include "database/tcSqlReader.h"
#include "strutil.h"
#include "tcAirDetectionDBObject.h"

#include <sstream>
#include "tcBallisticMissile.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

    void tcBallisticMissileDBObject::CalculateParams()
    {
        tcWeaponDBObject::CalculateParams();
        const float minBC = 0.001f;
        bcStage1 = std::max(bcStage1, minBC);
        bcStage2 = std::max(bcStage2, minBC);
        bcStage3 = std::max(bcStage3, minBC);
        bcStage4 = std::max(bcStage4, minBC);

        inv_bcStage1 = 1.0f / bcStage1;
        inv_bcStage2 = 1.0f / bcStage2;
        inv_bcStage3 = 1.0f / bcStage3;
        inv_bcStage4 = 1.0f / bcStage4;

        float t1 = timeStage1_s;
        float t2 = t1 + timeStage2_s;
        float t3 = t2 + timeStage3_s;
        float t4 = t3 + timeStage4_s;

        if (accelStage4_mps2 > 0)
        {
            thrustShutoffTime_s = t4;
        }
        else if (accelStage3_mps2 > 0)
        {
            thrustShutoffTime_s = t3;
        }
        else if (accelStage2_mps2 > 0)
        {
            thrustShutoffTime_s = t2;
        }
        else
        {
            thrustShutoffTime_s = t1;
        }
    }


    /**
    * Adds sql column definitions to columnString. This is used for
    * SQL create table command
    */
    void tcBallisticMissileDBObject::AddSqlColumns(std::string& columnString)
    {
        tcWeaponDBObject::AddSqlColumns(columnString);

        tcAirDetectionDBObject::AddSqlColumns(columnString);

        columnString += ",";

        columnString += "Gmax numeric,";

        columnString += "TimeStage1_s,";
        columnString += "AccelStage1_mps2,";
        columnString += "BCStage1,";

        columnString += "TimeStage2_s,";
        columnString += "AccelStage2_mps2,";
        columnString += "BCStage2,";

        columnString += "TimeStage3_s,";
        columnString += "AccelStage3_mps2,";
        columnString += "BCStage3,";

        columnString += "TimeStage4_s,";
        columnString += "AccelStage4_mps2,";
        columnString += "BCStage4";
    }

    teWeaponLaunchMode tcBallisticMissileDBObject::GetLaunchMode() const
    {
        return DATUM_ONLY;
    }

    void tcBallisticMissileDBObject::ReadSql(tcSqlReader& entry)
    {
        tcWeaponDBObject::ReadSql(entry);
        auto airDetectionDBObject =std::make_shared<tcAirDetectionDBObject>();
        airDetectionDBObject->ReadSql(entry);
        components.push_back(airDetectionDBObject);
        gmax = entry.GetDouble("Gmax");

        timeStage1_s = entry.GetDouble("TimeStage1_s");
        accelStage1_mps2 = entry.GetDouble("AccelStage1_mps2");
        bcStage1 = entry.GetDouble("BCStage1");

        timeStage2_s = entry.GetDouble("TimeStage2_s");
        accelStage2_mps2 = entry.GetDouble("AccelStage2_mps2");
        bcStage2 = entry.GetDouble("BCStage2");

        timeStage3_s = entry.GetDouble("TimeStage3_s");
        accelStage3_mps2 = entry.GetDouble("AccelStage3_mps2");
        bcStage3 = entry.GetDouble("BCStage3");

        timeStage4_s = entry.GetDouble("TimeStage4_s");
        accelStage4_mps2 = entry.GetDouble("AccelStage4_mps2");
        bcStage4 = entry.GetDouble("BCStage4");

        //CalculateParams();
    }

    void tcBallisticMissileDBObject::WriteSql(std::string& valueString)
    {
        tcWeaponDBObject::WriteSql(valueString);
        GetComponent<tcAirDetectionDBObject>()->WriteSql(valueString);

        std::stringstream s;

        s << ",";

        s << gmax << ",";

        s << timeStage1_s << ",";
        s << accelStage1_mps2 << ",";
        s << bcStage1 << ",";

        s << timeStage2_s << ",";
        s << accelStage2_mps2 << ",";
        s << bcStage2 << ",";

        s << timeStage3_s << ",";
        s << accelStage3_mps2 << ",";
        s << bcStage3 << ",";

        s << timeStage4_s << ",";
        s << accelStage4_mps2 << ",";
        s << bcStage4;

        valueString += s.str();
    }

    void tcBallisticMissileDBObject::WritePythonValue(std::string &valueString) const
    {
        tcWeaponDBObject::WritePythonValue(valueString);

        GetComponent<tcAirDetectionDBObject>()->WritePythonValue(mzClass,valueString);

        valueString+="    dbObj.gmax="+strutil::to_python_value(gmax)+"\n";
        valueString+="    dbObj.timeStage1_s="+strutil::to_python_value(timeStage1_s)+"\n";
        valueString+="    dbObj.accelStage1_mps2="+strutil::to_python_value(accelStage1_mps2)+"\n";
        valueString+="    dbObj.bcStage1="+strutil::to_python_value(bcStage1)+"\n";
        valueString+="    dbObj.timeStage2_s="+strutil::to_python_value(timeStage2_s)+"\n";
        valueString+="    dbObj.accelStage2_mps2="+strutil::to_python_value(accelStage2_mps2)+"\n";
        valueString+="    dbObj.bcStage2="+strutil::to_python_value(bcStage2)+"\n";
        valueString+="    dbObj.timeStage3_s="+strutil::to_python_value(timeStage3_s)+"\n";
        valueString+="    dbObj.accelStage3_mps2="+strutil::to_python_value(accelStage3_mps2)+"\n";
        valueString+="    dbObj.bcStage3="+strutil::to_python_value(bcStage3)+"\n";
        valueString+="    dbObj.timeStage4_s="+strutil::to_python_value(timeStage4_s)+"\n";
        valueString+="    dbObj.accelStage4_mps2="+strutil::to_python_value(accelStage4_mps2)+"\n";
        valueString+="    dbObj.bcStage4="+strutil::to_python_value(bcStage4)+"\n";
    }

    void tcBallisticMissileDBObject::WritePython(std::string &valueString) const
    {
        valueString+="import pygcb\n";
        valueString+="def CreateDBObject():\n";
        valueString+="    dbObj=pygcb.tcBallisticMissileDBObject()\n";
        WritePythonValue(valueString);
        valueString+="    dbObj.CalculateParams()\n";
        valueString+="    return dbObj\n";
    }


    tcBallisticMissileDBObject::tcBallisticMissileDBObject(const tcBallisticMissileDBObject& obj) 
        : tcWeaponDBObject(obj),

        gmax(obj.gmax),
        timeStage1_s(obj.timeStage1_s),
        accelStage1_mps2(obj.accelStage1_mps2),
        bcStage1(obj.bcStage1),
        timeStage2_s(obj.timeStage2_s),
        accelStage2_mps2(obj.accelStage2_mps2),
        bcStage2(obj.bcStage2),
        timeStage3_s(obj.timeStage3_s),
        accelStage3_mps2(obj.accelStage3_mps2),
        bcStage3(obj.bcStage3),
        timeStage4_s(obj.timeStage4_s),
        accelStage4_mps2(obj.accelStage4_mps2),
        bcStage4(obj.bcStage4)
    {
        mnModelType = MTYPE_BALLISTICMISSILE;

        CalculateParams();
    }

    tcBallisticMissileDBObject::tcBallisticMissileDBObject() : tcWeaponDBObject(),
        gmax(0),
        timeStage1_s(0),
        accelStage1_mps2(0),
        bcStage1(0),
        timeStage2_s(0),
        accelStage2_mps2(0),
        bcStage2(0),
        timeStage3_s(0),
        accelStage3_mps2(0),
        bcStage3(0),
        timeStage4_s(0),
        accelStage4_mps2(0),
        bcStage4(0)
    {
        mnModelType = MTYPE_BALLISTICMISSILE;
        mnType = PTYPE_MISSILE;
    }

    tcBallisticMissileDBObject::~tcBallisticMissileDBObject() 
    {
    }

    std::shared_ptr<tcGameObject>tcBallisticMissileDBObject::CreateGameObject()
    {
        auto obj= std::make_shared<tcBallisticMissile>(dynamic_pointer_cast<tcBallisticMissileDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }

} // namespace database

