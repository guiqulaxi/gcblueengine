/*  
**  @file tcMissileDBObject.cpp
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


#include "tcMissileDBObject.h"
#include "math_constants.h"
#include "tcDatabase.h"
#include "database/tcSqlReader.h"
#include "tcAirDetectionDBObject.h"
#include "tcSensorDBObject.h"
#include "tcRadarDBObject.h"
#include "tcESMSensor.h"
#include "tcAero.h"
#include <sstream>
#include <cassert>
#include "tcMissileObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace std;

namespace database
{

bool tcMissileDBObject::AcceptsWaypoints() const
{
    return acceptsWaypoints;
}

void tcMissileDBObject::CalculateParams()
{
    aczConstant_kts = C_KTSTOMPS * (50.0f / std::min(mfGmax, 20.0f)); // % smaller is more responsive

    invMass_kg = 1.0f / weight_kg;
}



/**
* @return estimate of missile speed to use for adjusting future target position
*/
float tcMissileDBObject::EstimateSpeed_mps() const
{
    float cruiseAltitude_m = 100.0f;
    if (mnNumSegments > 0)
    {
        cruiseAltitude_m = maFlightProfile[0].mfAltitude_m;
    }


    float rho = Aero::GetAirDensity(cruiseAltitude_m);

    float vsound_mps = Aero::GetSoundSpeed(cruiseAltitude_m);

    float speedSuper_mps = sqrtf(mfSustThrust_N / (mfCdpsup*rho));

    if (speedSuper_mps >= (vsound_mps*mfMsupm))
    {
        return speedSuper_mps;
    }
    else
    {
        float speedSub_mps = sqrtf(mfSustThrust_N / (mfCdpsub*rho));
        return speedSub_mps;
    }
}

teWeaponLaunchMode tcMissileDBObject::GetLaunchMode() const
{
    if (mnNumSegments==0) {return AUTO;}

    const tsMissileFlightSegment *firstSegment = &maFlightProfile[0];

    if (firstSegment->meGuidanceMode == GM_NAV)
    {
        return DATUM_ONLY;
    }
    else if (firstSegment->meGuidanceMode == GM_COMMAND)
    {
        return needsFireControl ? FC_TRACK : TARGET_ONLY;
    }
    else
    {
        return SEEKER_TRACK;
    }
}

long tcMissileDBObject::GetSensorKey()
{
    assert(database);
    if (sensorKey != NULL_INDEX) return sensorKey;
    sensorKey = database->GetKey(maSensorClass.c_str());

    // do not report error for missiles with no sensor (e.g. some AGMs)
    if ((sensorKey == NULL_INDEX) && (maSensorClass.size() > 0))
    {
        fprintf(stderr, "tcMissileDBObject::GetSensorKey -- not found "
                        "(%s)\n", maSensorClass.c_str());
    }
    return sensorKey;
}

/**
* @return seeker field of view in radians
*/
float tcMissileDBObject::GetSeekerFOV()
{
    if (seekerFOV_rad >= 0) return seekerFOV_rad;

    long seekerKey = GetSensorKey();
    tcDatabaseObject* obj = database->GetObject(seekerKey);
    if (tcSensorDBObject* sensor = dynamic_cast<tcSensorDBObject*>(obj))
    {
        seekerFOV_rad = C_PIOVER180 * sensor->mfFieldOfView_deg;
    }
    else
    {
        if ((targetFlags != 4) && (payloadClass.length() == 0))
        {
            fprintf(stderr, "tcMissileDBObject::GetSeekerFOV - (%s) no seeker or payload and has non-land target\n",
                    mzClass.c_str());
            assert(false);
        }
        seekerFOV_rad = C_TWOPI;
    }

    return seekerFOV_rad;
}

/**
* This checks that the database object has all of the emitters in the 
* emitters vector. Somewhat expensive, nEmitters * nSensors
* comparisons for positive result, fewer for negative result.
* Modified tcPlatformDBObject method
* @see tcPlatformDBObject::HasAllEmitters
* @return true if this database object has all of the emitters
*/
bool tcMissileDBObject::HasAllEmitters(std::vector<long>& emitters)
{
    size_t nEmitters = emitters.size();

    long seekerKey = GetSensorKey();

    for (size_t k=0; k<nEmitters; k++)
    {
        long emitterId = emitters[k];

        if (seekerKey != emitterId) return false;
    }
    return true;
}

/**
* @return true if missile has ESM seeker
*/
bool tcMissileDBObject::IsARM()
{
    if (isARM == -1)
    {
        tcDatabaseObject* obj = database->GetObject(GetSensorKey());
        if (tcESMDBObject* esm = dynamic_cast<tcESMDBObject*>(obj))
        {
            isARM = 1;
        }
        else 
        {
            isARM = 0;
        }
    }

    return (isARM != 0);
}

/**
* @return true if first segment is GM_COMMAND command guidance
*/
bool tcMissileDBObject::IsCommandLaunched() const
{
    return (mnNumSegments > 0) && (maFlightProfile[0].meGuidanceMode == GM_COMMAND);
}

/**
* @return true if missile is fire and forget
*/
bool tcMissileDBObject::IsFireAndForget()
{
    if (fireAndForget == -1)
    {
        teWeaponLaunchMode launchMode = GetLaunchMode();
        if ((launchMode == DATUM_ONLY) || (launchMode == AUTO))
        {
            fireAndForget = 1;
        }
        else if (launchMode == FC_TRACK)
        {
            fireAndForget = 0;
        }
        else // launchMode == SEEKER_TRACK
        {
            assert(launchMode == SEEKER_TRACK);
            tcDatabaseObject* obj = database->GetObject(GetSensorKey());
            if (tcRadarDBObject* radar = dynamic_cast<tcRadarDBObject*>(obj))
            {
                fireAndForget = (IsCommandLaunched() || radar->isSemiactive) ? 0 : 1;
            }
            else
            {
                fireAndForget = 1;
            }
        }

    }

    return (fireAndForget != 0);
}

/**
* @return true if this missile relies on a fire control sensor from the parent platform for any of its guidance
*/
bool tcMissileDBObject::NeedsFireControl() const
{
    return needsFireControl;
}


void tcMissileDBObject::PrintToFile(tcFile& file) 
{
    tcString s;

    tcWeaponDBObject::PrintToFile(file);

    s.Format("   ");
    file.WriteString(s.GetBuffer());
}


/**
* Adds sql column definitions to columnString. This is used for
* SQL create table command
*/
void tcMissileDBObject::AddSqlColumns(std::string& columnString)
{
    tcWeaponDBObject::AddSqlColumns(columnString);

    tcAirDetectionDBObject::AddSqlColumns(columnString);

    columnString += ",";

    columnString += "DragArea_sm number(8),";
    columnString += "Gmax number(8),";
    columnString += "MaxTurnRate_degps number(4),";
    columnString += "Cdpsub number(8),";
    columnString += "Cdptran number(8),";
    columnString += "Cdpsup number(8),";
    columnString += "Mcm number(8),";
    columnString += "Msupm number(8),";
    columnString += "BoostThrust_N number(8),";
    columnString += "BoostTime_s number(8),";
    columnString += "SustThrust_N number(8),";
    columnString += "SustTime_s number(8),";
    columnString += "Range_km number(5),";
    columnString += "ShutdownSpeed_mps number(5),";
    columnString += "SensorClass varchar(30),";
    columnString += "NeedsFireControl number(1),";
    columnString += "AcceptsWaypoints numeric,";

    for(unsigned i=0;i<MAX_MISSILE_FLIGHT_SEGMENTS;i++)
    {
        tcString s;

        s.Format("Rng%d_km number(5),",i+1);
        columnString += s.GetBuffer();

        s.Format("Alt%d_m number(5),",i+1);
        columnString += s.GetBuffer();

        s.Format("AltMode%d number(2),",i+1);
        columnString += s.GetBuffer();

        s.Format("GuidMode%d number(2)",i+1);
        columnString += s.GetBuffer();

        if (i < MAX_MISSILE_FLIGHT_SEGMENTS-1)
        {
            columnString += ",";
        }
    }
}

void tcMissileDBObject::ReadSql(tcSqlReader& entry)
{
    tcWeaponDBObject::ReadSql(entry);
    tcAirDetectionDBObject::ReadSql(entry);

    mfDragArea_sm = entry.GetDouble("DragArea_sm");
    mfGmax = entry.GetDouble("Gmax");
    mfMaxTurnRate_degps = entry.GetDouble("MaxTurnRate_degps");
    mfCdpsub = entry.GetDouble("Cdpsub");
    mfCdptran = entry.GetDouble("Cdptran");
    mfCdpsup = entry.GetDouble("Cdpsup");
    mfMcm = entry.GetDouble("Mcm");
    mfMsupm = entry.GetDouble("Msupm");
    mfBoostThrust_N = entry.GetDouble("BoostThrust_N");
    mfBoostTime_s = entry.GetDouble("BoostTime_s");
    mfSustThrust_N = entry.GetDouble("SustThrust_N");
    mfSustTime_s = entry.GetDouble("SustTime_s");
    mfShutdownSpeed_mps = entry.GetDouble("ShutdownSpeed_mps");
    maSensorClass = entry.GetString("SensorClass").c_str();
    needsFireControl = entry.GetInt("NeedsFireControl") != 0;
    acceptsWaypoints = entry.GetInt("AcceptsWaypoints") != 0;

    mfMcm = std::min(mfMcm, mfMsupm - 0.01f); // avoid divide by zero in missile kstate calc


    mnNumSegments = 0;
    maFlightProfile.clear();
    for (unsigned i=0;i<MAX_MISSILE_FLIGHT_SEGMENTS;i++)
    {
        float range, alt;
        int altMode, guidanceMode;

        range = entry.GetDouble("Rng%d_km", i+1);
        alt = entry.GetDouble("Alt%d_m", i+1);
        altMode = entry.GetInt("AltMode%d", i+1);
        guidanceMode = entry.GetInt("GuidMode%d", i+1);

        if ((range > 0)||(alt > 0))
        {
            tsMissileFlightSegment missileFlightSegment;
            missileFlightSegment.mfRange_km=range;
            missileFlightSegment.mfAltitude_m=alt;
            missileFlightSegment.meAltitudeMode=(teAltitudeMode)altMode;
            missileFlightSegment.meGuidanceMode=(teGuidanceMode)guidanceMode;
            maFlightProfile.push_back(missileFlightSegment);
            mnNumSegments++;
            // maFlightProfile[mnNumSegments].mfRange_km = range;
            // maFlightProfile[mnNumSegments].mfAltitude_m = alt;
            // maFlightProfile[mnNumSegments].meAltitudeMode = (teAltitudeMode)altMode;
            // maFlightProfile[mnNumSegments++].meGuidanceMode = (teGuidanceMode)guidanceMode;
        }

    }

    // set other params that do not come from database file
    sensorKey = NULL_INDEX;
    fireAndForget = -1;
    isARM = -1;

    if (GetLaunchMode() == FC_TRACK) // force needsFireControl for this case, why need database input for needs FC?
    {
        needsFireControl = true;
    }

    CalculateParams();

}

void tcMissileDBObject::WriteSql(std::string& valueString) const
{
    tcWeaponDBObject::WriteSql(valueString);
    tcAirDetectionDBObject::WriteSql(valueString);

    std::stringstream s;

    s << ",";

    s << mfDragArea_sm << ",";
    s << mfGmax << ",";
    s << mfMaxTurnRate_degps << ",";
    s << mfCdpsub << ",";
    s << mfCdptran << ",";
    s << mfCdpsup << ",";
    s << mfMcm << ",";
    s << mfMsupm << ",";
    s << mfBoostThrust_N << ",";
    s << mfBoostTime_s << ",";
    s << mfSustThrust_N << ",";
    s << mfSustTime_s << ",";
    s << mfShutdownSpeed_mps << ",";
    s << "'" << std::string(maSensorClass.c_str()) << "',";
    s << needsFireControl << ",";
    s << acceptsWaypoints << ",";

    for(unsigned i=0;i<maFlightProfile.size();i++)
    {
        if (i<mnNumSegments)
        {
            s << maFlightProfile[i].mfRange_km << ",";
            s << maFlightProfile[i].mfAltitude_m << ",";
            s << (long)maFlightProfile[i].meAltitudeMode << ",";
            s << (long)maFlightProfile[i].meGuidanceMode;
        }
        else
        {
            s << "0,";
            s << "0,";
            s << "0,";
            s << "0";
        }

        if (i < maFlightProfile.size()-1)
        {
            s << ",";
        }

    }

    valueString += s.str();

}

void tcMissileDBObject::WritePythonValue(std::string &valueString) const
{
    tcWeaponDBObject::WritePythonValue(valueString);
    tcAirDetectionDBObject::WritePythonValue(mzClass,valueString);
    valueString+="    dbObj.mfDragArea_sm="+strutil::to_python_value(mfDragArea_sm)+"\n";
    valueString+="    dbObj.mfGmax="+strutil::to_python_value(mfGmax)+"\n";
    valueString+="    dbObj.mfMaxTurnRate_degps="+strutil::to_python_value(mfMaxTurnRate_degps)+"\n";
    valueString+="    dbObj.mfCdpsub="+strutil::to_python_value(mfCdpsub)+"\n";
    valueString+="    dbObj.mfCdptran="+strutil::to_python_value(mfCdptran)+"\n";
    valueString+="    dbObj.mfCdpsup="+strutil::to_python_value(mfCdpsup)+"\n";
    valueString+="    dbObj.mfMcm="+strutil::to_python_value(mfMcm)+"\n";
    valueString+="    dbObj.mfMsupm="+strutil::to_python_value(mfMsupm)+"\n";
    valueString+="    dbObj.mfBoostThrust_N="+strutil::to_python_value(mfBoostThrust_N)+"\n";
    valueString+="    dbObj.mfBoostTime_s="+strutil::to_python_value(mfBoostTime_s)+"\n";
    valueString+="    dbObj.mfSustThrust_N="+strutil::to_python_value(mfSustThrust_N)+"\n";
    valueString+="    dbObj.mfSustTime_s="+strutil::to_python_value(mfSustTime_s)+"\n";
    valueString+="    dbObj.mfShutdownSpeed_mps="+strutil::to_python_value(mfShutdownSpeed_mps)+"\n";
    valueString+="    dbObj.maSensorClass="+strutil::to_python_value(maSensorClass.c_str())+"\n";
    valueString+="    dbObj.needsFireControl="+strutil::to_python_value(needsFireControl)+"\n";
    valueString+="    dbObj.acceptsWaypoints="+strutil::to_python_value(acceptsWaypoints)+"\n";
    valueString+="    dbObj.fireAndForget="+strutil::to_python_value(fireAndForget)+"\n";
    valueString+="    dbObj.isARM="+strutil::to_python_value(isARM)+"\n";
    valueString+="    dbObj.seekerFOV_rad="+strutil::to_python_value(seekerFOV_rad)+"\n";
    valueString+="    dbObj.aczConstant_kts="+strutil::to_python_value(aczConstant_kts)+"\n";
    valueString+="    dbObj.invMass_kg="+strutil::to_python_value(invMass_kg)+"\n";
    valueString+="    dbObj.mnNumSegments="+strutil::to_python_value(mnNumSegments)+"\n";
    valueString+="    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*"+std::to_string(maFlightProfile.size())+"\n";
    for (size_t i=0 ; i < mnNumSegments; ++i) {
        valueString+="    dbObj.maFlightProfile["+std::to_string(i)+"].meAltitudeMode=pygcb.teAltitudeMode."+teAltitudeModeToString(maFlightProfile[i].meAltitudeMode)+"\n";
        valueString+="    dbObj.maFlightProfile["+std::to_string(i)+"].meGuidanceMode=pygcb.teGuidanceMode."+teGuidanceModeToString(maFlightProfile[i].meGuidanceMode)+"\n";
        valueString+="    dbObj.maFlightProfile["+std::to_string(i)+"].mfAltitude_m="+strutil::to_python_value(maFlightProfile[i].mfAltitude_m)+"\n";
        valueString+="    dbObj.maFlightProfile["+std::to_string(i)+"].mfRange_km="+strutil::to_python_value(maFlightProfile[i].mfRange_km)+"\n";

    }

}

void tcMissileDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcMissileDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";

    valueString+="    return dbObj\n";;

}


tcMissileDBObject::tcMissileDBObject(const tcMissileDBObject& obj) 
    : tcWeaponDBObject(obj),
    tcAirDetectionDBObject(obj),
    seekerFOV_rad(obj.seekerFOV_rad),
    fireAndForget(obj.fireAndForget),
    isARM(obj.isARM),
    mfDragArea_sm(obj.mfDragArea_sm),
    mfGmax(obj.mfGmax),
    mfMaxTurnRate_degps(obj.mfMaxTurnRate_degps),
    mfCdpsub(obj.mfCdpsub),
    mfCdptran(obj.mfCdptran),
    mfCdpsup(obj.mfCdpsup),
    mfMcm(obj.mfMcm),
    mfMsupm(obj.mfMsupm),
    mfBoostThrust_N(obj.mfBoostThrust_N),
    mfBoostTime_s(obj.mfBoostTime_s),
    mfSustThrust_N(obj.mfSustThrust_N),
    mfSustTime_s(obj.mfSustTime_s),
    mfShutdownSpeed_mps(obj.mfShutdownSpeed_mps),
    maSensorClass(obj.maSensorClass),
    needsFireControl(obj.needsFireControl),
    acceptsWaypoints(obj.acceptsWaypoints),
    mnNumSegments(obj.mnNumSegments)
{
    mnModelType = MTYPE_MISSILE;

    maFlightProfile.clear();
    for(int i=0;i<obj.maFlightProfile.size();i++)
    {
        //maFlightProfile[i] = obj.maFlightProfile[i];
        maFlightProfile.push_back(obj.maFlightProfile[i]);
    }
    sensorKey = NULL_INDEX;

    CalculateParams();
}

tcMissileDBObject::tcMissileDBObject() : tcWeaponDBObject(), tcAirDetectionDBObject(),
    seekerFOV_rad(-1.0f),
    fireAndForget(-1),
    isARM(-1),
    mfDragArea_sm(1.0f),
    mfGmax(20.0f),
    mfMaxTurnRate_degps(15.0f),
    mfCdpsub(0.2f),
    mfCdptran(0.4f),
    mfCdpsup(0.3f),
    mfMcm(0.9f),
    mfMsupm(1.1f),
    mfBoostThrust_N(4000.0f),
    mfBoostTime_s(20.0f),
    mfSustThrust_N(400.0f),
    mfSustTime_s(60.0f),
    needsFireControl(false),
    acceptsWaypoints(false),
    aczConstant_kts(4.0f)
{
    mnModelType = MTYPE_MISSILE;
    mnType = PTYPE_MISSILE;

    // flight profile, array of flight segment info
    mnNumSegments = 1;
    tsMissileFlightSegment missileFlightSegment;
    missileFlightSegment.mfRange_km=0.0f;
    missileFlightSegment.mfAltitude_m= 10000.0f;
    missileFlightSegment.meAltitudeMode=AM_ASL;
    missileFlightSegment.meGuidanceMode=GM_COMMAND;
    maFlightProfile.push_back(missileFlightSegment);
    // maFlightProfile[0].mfRange_km = 0.0f;
    // maFlightProfile[0].mfAltitude_m = 10000.0f;
    // maFlightProfile[0].meAltitudeMode = AM_ASL;
    // maFlightProfile[0].meGuidanceMode = GM_COMMAND;
    sensorKey = NULL_INDEX;
}

tcMissileDBObject::~tcMissileDBObject() 
{
}

tcGameObject *tcMissileDBObject::CreateGameObject()
{
    return new tcMissileObject(this);
}

std::string tcMissileDBObject::teAltitudeModeToString(teAltitudeMode data)const
{
    switch (data) {
    case AM_ASL:
        return "AM_ASL";
        break;
    case AM_AGL:
        return "AM_AGL";
        break;
    case AM_INTERCEPT:
        return "AM_INTERCEPT";
        break;
    case AM_DATUM:
        return "AM_DATUM";
        break;
    case AM_INTERCEPT_HIGH:
        return "AM_INTERCEPT_HIGH";
        break;
    case AM_ASL_LOFT:
        return "AM_ASL_LOFT";
        break;
    default:
        break;
    }
    return "";
}
std::string tcMissileDBObject::teGuidanceModeToString(teGuidanceMode data) const
{
    switch (data) {
    case GM_COMMAND:
        return "GM_COMMAND";
        break;
    case GM_NAV:
        return "GM_NAV";
        break;
    case GM_SENSOR1:
        return "GM_SENSOR1";
        break;
    case GM_DEPLOY:
        return "GM_DEPLOY";
        break;
    }
    return "";
}


} // namespace database

