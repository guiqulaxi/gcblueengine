/**
**  @file tcTorpedoObject.cpp
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

#include "tcTorpedoObject.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "database/tcPlatformDBObject.h"
#include "database/tcSonarDBObject.h"
#include "database/tcTorpedoDBObject.h"
#include "database/tcBallisticDBObject.h"
//#include "tc3DModel.h"
//#include "tcParticleEffect.h"
#include "tcLauncher.h"
#include "tcMissileObject.h"
#include "tcBallisticWeapon.h"
#include "tcSimState.h"
#include "tc3DPoint.h"
#include "tcGameObjIterator.h"
#include <cassert>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

/**
* Load state from update stream
*/
tcUpdateStream& tcTorpedoObject::operator<<(tcUpdateStream& stream)
{
    tcWeaponObject::operator<<(stream);

    stream >> goalHeading_rad;
    stream >> goalPitch_rad;
    stream >> goalSpeed_kts;
    stream >> interceptTime;
    stream >> lastGuidanceUpdate;
    stream >> guidanceUpdateInterval;
    waypoint << stream;
    seeker->operator<<(stream);

    return stream;
}

/**
* Save state to update stream
*/
tcUpdateStream& tcTorpedoObject::operator>>(tcUpdateStream& stream)
{
    tcWeaponObject::operator>>(stream);

    stream << goalHeading_rad;
    stream << goalPitch_rad;
    stream << goalSpeed_kts;
    stream << interceptTime;
    stream << lastGuidanceUpdate;
    stream << guidanceUpdateInterval;
    waypoint >> stream;
    seeker->operator>>(stream);

    return stream;
}

/**
* Load state from game stream
*/
tcGameStream& tcTorpedoObject::operator<<(tcGameStream& stream)
{
    int version = stream.GetVersionId();

    tcWeaponObject::operator<<(stream);
    tcSensorPlatform::operator<<(stream);

    stream >> goalDepth_m;
    stream >> goalHeading_rad;
    stream >> goalPitch_rad;
    stream >> goalSpeed_kts; 
    stream >> interceptTime;
    stream >> runTime;
    if (version > 8) {stream >> searchStartTime;}
    stream >> lastGuidanceUpdate;
    stream >> guidanceUpdateInterval;

    waypoint << stream;

    stream >> runToEnable_m;   
    stream >> ceiling_m;
    stream >> floor_m;
    stream >> isWireActive;
    stream >> autoWireUpdates;
    stream >> battery_kJ;
    stream >> searchHeading_rad;
    stream >> searchMode;

    stream.ReadCheckValue(263);

    return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcTorpedoObject::operator>>(tcGameStream& stream)
{
    int version = stream.GetVersionId();

    tcWeaponObject::operator>>(stream);
    tcSensorPlatform::operator>>(stream);

    stream << goalDepth_m;
    stream << goalHeading_rad;
    stream << goalPitch_rad;
    stream << goalSpeed_kts; 
    stream << interceptTime;
    stream << runTime;
    if (version > 8) {stream << searchStartTime;}
    stream << lastGuidanceUpdate;
    stream << guidanceUpdateInterval;

    waypoint >> stream;

    stream << runToEnable_m;   
    stream << ceiling_m;
    stream << floor_m;
    stream << isWireActive;
    stream << autoWireUpdates;
    stream << battery_kJ;
    stream << searchHeading_rad;
    stream << searchMode;

    stream.WriteCheckValue(263);

    return stream;
}



/**
* Initializes missile state for launch from game object.
* Adds self to simulation
*
* @param obj launching game object
* @param launcher index of launcher
*/
void tcTorpedoObject::LaunchFrom(std::shared_ptr<tcGameObject> obj, unsigned nLauncher)
{
    isWireActive = false;
    autoWireUpdates = true;

    // tcLauncher virtualLauncher; // for missile deployment
    // std::shared_ptr<tcLauncher> pLauncher = &virtualLauncher;
    std::shared_ptr<tcLauncher> pLauncher = std::make_shared<tcLauncher>();
    if (std::shared_ptr<tcPlatformObject> platObj = std::dynamic_pointer_cast<tcPlatformObject>(obj))
    {
        tc3DPoint launcherPos = platObj->mpDBObject->GetLauncherPosition(nLauncher);
        GeoPoint pos = obj->RelPosToLatLonAlt(launcherPos.x, launcherPos.y,
                                              launcherPos.z);
        mcKin.mfLon_rad = pos.mfLon_rad;
        mcKin.mfLat_rad = pos.mfLat_rad;
        mcKin.mfAlt_m = pos.mfAlt_m;

        pLauncher = obj->GetLauncher(nLauncher);

        if (mcKin.mfAlt_m <= 0)
        {
             std::shared_ptr<tcSonarDBObject> sonar = mpDBObject->GetSeekerDBObj();
            
            mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts + C_MPSTOKTS * mpDBObject->launchSpeed_mps;

            if ((sonar != 0) && ((sonar->isWakeHoming) || (sonar->mfMaxRange_km <= 0.1f)))
            {
                searchMode = SEARCH_STRAIGHT;
            }
            else
            {
                searchMode = SEARCH_SNAKE;
            }
            isWireActive = mpDBObject->wireGuidance;
        }
        else // air launched
        {
            mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
            searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
        }
    }
    else if (std::shared_ptr<tcMissileObject> missile =  std::dynamic_pointer_cast<tcMissileObject>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        pLauncher->pointingAngle = 0;
        pLauncher->pointingElevation = 0;
        pLauncher->firingArc_deg = 0;
        pLauncher->runToEnable_m = 0;
        pLauncher->msDatum = missile->msWaypoint;
        pLauncher->runDepth_m = 0;
        pLauncher->preEnableSpeed_kts = 35.0f;
        pLauncher->ceiling_m = 0;
        pLauncher->floor_m = 0;
        pLauncher->usePassive = false;
        pLauncher->mnTargetID = missile->GetIntendedTarget();

        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
        searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
    }
    else if (std::shared_ptr<tcTorpedoObject> torpedo = std::dynamic_pointer_cast<tcTorpedoObject>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        pLauncher->pointingAngle = 0;
        pLauncher->pointingElevation = 0;
        pLauncher->runToEnable_m = 1.0; // start enabled
        pLauncher->msDatum = torpedo->waypoint;
        pLauncher->runDepth_m = torpedo->goalDepth_m;
        pLauncher->preEnableSpeed_kts = 35.0f;
        pLauncher->ceiling_m = 0;
        pLauncher->floor_m = 0;
        pLauncher->usePassive = false;
        pLauncher->mnTargetID = torpedo->GetIntendedTarget();

        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts + C_MPSTOKTS * mpDBObject->launchSpeed_mps;
        searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
    }
    else if (std::shared_ptr<tcBallisticWeapon> ballistic =  std::dynamic_pointer_cast<tcBallisticWeapon>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;
        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts + C_MPSTOKTS * mpDBObject->launchSpeed_mps;

        pLauncher->pointingAngle = 0;
        pLauncher->pointingElevation = 0;
        pLauncher->runToEnable_m = 1.0; // start enabled
        pLauncher->msDatum.Set(mcKin.mfLon_rad, mcKin.mfLat_rad, 0);
        pLauncher->runDepth_m = 0;
        pLauncher->preEnableSpeed_kts = 35.0f;
        pLauncher->ceiling_m = 0;
        pLauncher->floor_m = 0;
        pLauncher->usePassive = false;
        pLauncher->mnTargetID = ballistic->GetIntendedTarget();

        if (ballistic->mpDBObject->payloadQuantity > 1) // assume this is a RBU type
        {
            pLauncher->pointingAngle += randfc(1.0f);
            pLauncher->pointingElevation += randfc(0.1f);
        }
    }
    else
    {
        assert(false);
        fprintf(stderr, "tcTorpedoObject::LaunchFrom - Launched from invalid platform (%s)\n",
                obj->GetName());
        return;
    }

    // added this for unguided torpedo modeling, 11 APR 2011
    if (seeker == 0) // straight run if no seeker
    {
        searchMode = SEARCH_STRAIGHT;
    }



    mcKin.mfHeading_rad = obj->mcKin.mfHeading_rad + pLauncher->pointingAngle;
    mcKin.mfPitch_rad = obj->mcKin.mfPitch_rad + pLauncher->pointingElevation;
    mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;

    waypoint = pLauncher->msDatum;

    goalHeading_rad = mcKin.HeadingToGeoRad(&waypoint);
    if (pLauncher->runToEnable_m > 0)
    {
        runToEnable_m = pLauncher->runToEnable_m;
    }
    else if (mpDBObject->payloadClass.size() == 0)
    {
        runToEnable_m = 500.0f * mcKin.RangeToKm(&waypoint); // enable halfway to waypoint
    }
    else // has payload
    {
        runToEnable_m = 1000.0f * mcKin.RangeToKm(&waypoint); // set run to enable to deploy payload at waypoint
    }

    if (pLauncher->runDepth_m > 0)
    {
        goalDepth_m = pLauncher->runDepth_m;
    }
    else if (mpDBObject->weaponType == tcTorpedoDBObject::TORPEDO)  // run depth not specified
    {
        // set run depth based on target classification
        tcTrack track;
        bool found = simState->mcSensorMap.GetTrack(pLauncher->mnTargetID, track, obj->GetAlliance());
        if (found && (track.mnClassification != 0))
        {
            if (track.IsSurface())
            {
                goalDepth_m = 5.0f;
            }
            else if (track.IsSub())
            {
                if ((track.mnFlags & TRACK_ALT_VALID) != 0)
                {
                    goalDepth_m = -track.mfAlt_m;
                }
                else
                {
                    float terrain_m = tcMapData::Get()->GetTerrainHeight(
                        C_180OVERPI*obj->mcKin.mfLon_rad, C_180OVERPI*obj->mcKin.mfLat_rad, obj->mfStatusTime);
                    float maxDepth_m = std::min(-terrain_m - 15.0f, mpDBObject->maxDepth_m);
                    maxDepth_m = std::max(maxDepth_m, 10.0f);
                    goalDepth_m = ((maxDepth_m - 10.0f) * randf()) + 10.0f; // randomly pick a depth
                }
            }
        }
        else
        {
            bool subValid = (mpDBObject->targetFlags & SUBSURFACE_TARGET) != 0;
            bool surfaceValid = (mpDBObject->targetFlags & SURFACE_TARGET) != 0;

            if (surfaceValid && !subValid)
            {
                goalDepth_m = 5.0f;
            }
            else
            {
                float terrain_m = tcMapData::Get()->GetTerrainHeight(
                    C_180OVERPI*obj->mcKin.mfLon_rad, C_180OVERPI*obj->mcKin.mfLat_rad, obj->mfStatusTime);
                float maxDepth_m = std::min(-terrain_m - 15.0f, mpDBObject->maxDepth_m);
                maxDepth_m = std::max(maxDepth_m, 10.0f);
                goalDepth_m = ((maxDepth_m - 10.0f) * randf()) + 10.0f; // randomly pick a depth
            }
        }
    }
    else // mine or depth charge
    {
        float terrain_m = tcMapData::Get()->GetTerrainHeight(
            C_180OVERPI*obj->mcKin.mfLon_rad, C_180OVERPI*obj->mcKin.mfLat_rad, obj->mfStatusTime);
        float maxDepth_m = std::min(-terrain_m - 50.0f, mpDBObject->maxDepth_m);
        maxDepth_m = std::max(maxDepth_m, 100.0f);
        goalDepth_m = ((maxDepth_m - 100.0f) * randf()) + 100.0f; // randomly pick a depth
    }

    // keep off bottom and surface
    float bottom_m = -obj->mcTerrain.mfHeight_m;
    goalDepth_m = std::max(std::min(goalDepth_m, bottom_m - 15.0f), 5.0f);

    // limit speed to 10 - max_speed
    goalSpeed_kts = std::max(std::min(pLauncher->preEnableSpeed_kts, mpDBObject->maxSpeed_kts), 10.0f);

    ceiling_m = pLauncher->ceiling_m;
    
    if (floor_m > 0)
    {
        floor_m = pLauncher->floor_m;
    }
    else
    {
        floor_m = 8096.0f;
    }


    if (mpDBObject->weaponType == tcTorpedoDBObject::BOTTOM_MINE_CAPTOR)
    {
        if (mpDBObject->payloadClass.size() == 0)
        {
            fprintf(stderr, "tcTorpedoObject::LaunchFrom - CAPTOR has no payload (%s)\n",
                    mpDBObject->mzClass.c_str());
            return;
        }
    }


    mfStatusTime = obj->mfStatusTime;

    battery_kJ = mpDBObject->battery_kJ; // start with full battery charge

    if (seeker != 0)
    {
        if (pLauncher->usePassive)
        {
            seeker->SetPassiveSonar();
        }
        else
        {
            seeker->SetActiveSonar();
        }

        seeker->mnMode = SSMODE_SEEKERSEARCH;
        seeker->SetActive(false); // override default for passive to always be active
    }

    std::string s = strutil::format("Torp %d-%d", obj->mnID, launchedCounter++);
    mzUnit = s.c_str();      

    SetAlliance(obj->GetAlliance());

    simState->AddPlatform(shared_from_this());

    // Set intended target (has to be done after alliance and id is set).
    // This is a tcWeaponObject method
    SetIntendedTarget(pLauncher->mnTargetID);

}

/**
* @return time remaining in seconds based on current fuel consumption
*/
float tcTorpedoObject::RuntimeRemaining()
{
    return 0; // not implemented yet
}

/**
* For wire guidance updates
*/
void tcTorpedoObject::SetAltitude(float alt_m)
{
    goalDepth_m = -alt_m;
    autoWireUpdates = false;

    if (IsEditMode())
    {
        mcKin.mfAlt_m = alt_m;
    }
}

/**
*
*/
void tcTorpedoObject::SetHeading(float newHeading) 
{
    goalHeading_rad = newHeading;
    searchHeading_rad = goalHeading_rad;
    if (seeker != 0) seeker->mnMode = SSMODE_SEEKERSEARCH;
    autoWireUpdates = false; // don't do auto updates once manual update has occurred

    if (IsEditMode())
    {
        mcKin.mfHeading_rad = goalHeading_rad;
    }
}

/**
*
*/
void tcTorpedoObject::SetSpeed(float newSpeed) 
{
    goalSpeed_kts = newSpeed;
}

/**
*
*/
std::shared_ptr<tcSonar> tcTorpedoObject::GetSensorState()
{
    return seeker;
}



/**
* @returns sonar source level of object or, if object has active sonar on, maximum of source level of 
* target and max active sonar source level.
*/
float tcTorpedoObject::GetSonarSourceLevel(float az_deg) const
{
    float SLp = mpDBObject->GetSourceLevel(C_KTSTOMPS*goalSpeed_kts, -mcKin.mfAlt_m, az_deg);
    if (!IsEnsonifying()) return SLp;

    if (seeker->mpDBObj->SL > SLp)
    {
        return seeker->mpDBObj->SL;
    }
    else
    {
        return SLp;
    }
}

/**
*
*/
void tcTorpedoObject::Update(double afStatusTime)
{
    float dt_s = (float)(afStatusTime - mfStatusTime);
    mfStatusTime = afStatusTime;

    assert(mpDBObject);

    // air launched torpedoes drop into water first 在空中显示
    bool outOfWater = (mcKin.mfAlt_m > 0.0f);
    if (outOfWater)
    {
        UpdateDrop(dt_s);
        return;
    }

    switch (mpDBObject->weaponType)
    {
    case tcTorpedoDBObject::DEPTH_CHARGE: ///深水炸弹
        UpdateDepthCharge(dt_s);
        return;
    case tcTorpedoDBObject::BOTTOM_MINE:
    case tcTorpedoDBObject::BOTTOM_MINE_CAPTOR:
        UpdateBottomMine(dt_s);
        return;
    default:
        // continue
        break;
    }


    UpdateSpeedSimple(dt_s);

    float speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts;
    float disp_m = speed_mps * dt_s; // distance moved this update
    float disp_rad = C_MTORAD * disp_m; // distance in equator radians
    runToEnable_m -= disp_m;

    float disp_xy_rad = disp_rad * cosf(mcKin.mfClimbAngle_rad);
    float disp_z_m = disp_m * sinf(mcKin.mfClimbAngle_rad);
    float heading_rad = mcKin.mfHeading_rad;

    mcKin.mfLon_rad += disp_xy_rad * (double)(sinf(heading_rad) / cosf((float)mcKin.mfLat_rad));
    mcKin.mfLat_rad += (double)cosf(heading_rad) * disp_xy_rad; 
    mcKin.mfAlt_m += disp_z_m;



    if (!clientMode)
    {
        UpdateGuidance(afStatusTime);
    }

    

    if (runTime > 5.0f)  // swim level for first few seconds
    {
        /*** heading calculation ***/
        float dh_rad, dh_min, dh_max;
        dh_rad = goalHeading_rad - mcKin.mfHeading_rad;
        radtoplusminuspi(dh_rad); // map dh_deg to [-pi,pi)
        dh_max = mpDBObject->maxTurnRate_radps * dt_s; 
        dh_min = -dh_max;
        if (dh_rad < dh_min) {dh_rad = dh_min;} // restrict to turn rate
        else if (dh_rad > dh_max) {dh_rad = dh_max;}
        mcKin.mfHeading_rad += dh_rad;
        if (mcKin.mfHeading_rad >= C_TWOPI) {mcKin.mfHeading_rad -= C_TWOPI;}
        if (mcKin.mfHeading_rad < 0) {mcKin.mfHeading_rad += C_TWOPI;}

        /*** pitch calculation ***/
        float dp_rad, dp_min, dp_max;
        dp_rad = goalPitch_rad - mcKin.mfPitch_rad;
        dp_max = 2 * mpDBObject->maxTurnRate_radps * dt_s;
        dp_min = -dp_max;
        if (dp_rad < dp_min) {dp_rad = dp_min;} 
        else if (dp_rad > dp_max) {dp_rad = dp_max;}
        mcKin.mfPitch_rad += dp_rad;
        mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
    }

    HandlePoleWrap();

    //UpdateEffects();

    //Update3D();

    runTime += dt_s;

    if (clientMode) return;

    UpdateDetonation();

    //    float priorDamage = mfDamageLevel;

    /*** check for crash ***/

    if (mcTerrain.mfHeight_m >= mcKin.mfAlt_m)
    {
        ApplyGeneralDamage(1.0f, 0);
        tcString s;
        s.Format("Torpedo %s hit bottom at time %.1f lon %.3f, lat %.3f",
                 mzUnit.c_str(), afStatusTime, mcKin.mfLon_rad*C_180OVERPI, mcKin.mfLat_rad*C_180OVERPI);
        WTL(s.GetBuffer());
    }

    // update battery

    battery_kJ -= dt_s * mpDBObject->batteryRate_kWpkt * mcKin.mfSpeed_kts;

    if (battery_kJ <= 0)
    {
        ApplyGeneralDamage(1.0f, 0); // self-destruct
#ifdef _DEBUG
        tcString s;
        s.Format("Torpedo %s shut down at time %.1f lon %.3f, lat %.3f",
                 mzUnit.c_str(), afStatusTime, mcKin.mfLon_rad*C_180OVERPI, mcKin.mfLat_rad*C_180OVERPI);
        WTL(s.GetBuffer());
#endif
    }

    // post-launch malfunction check
    if (!tcWeaponObject::malfunctionChecked && (runTime > 60.0f))
    {
        MalfunctionCheck();
    }

    tcSensorPlatform::Update(afStatusTime);

}

/**
* If intended target is set, automatically update guidance based on latest sensor map track
*/
void tcTorpedoObject::UpdateAutoWireGuidance()
{
    if (!(isWireActive && autoWireUpdates && (intendedTarget != -1))) return;

    tcSensorMapTrack track;
    if (tcSimState::Get()->GetTrack(intendedTarget, GetAlliance(), track))
    {
        if (!track.IsBearingOnly())
        {
            goalHeading_rad = mcKin.HeadingToTrack(track);
        }
    }
}


/**
* Depth charge just sinks at max speed
*/
void tcTorpedoObject::UpdateDepthCharge(float dt_s)
{
    float alpha = 0.1f * dt_s;
    mcKin.mfClimbAngle_rad = (1.0f-alpha)*mcKin.mfClimbAngle_rad - alpha*1.55f; // slowly change to -89 deg
    mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;

    goalSpeed_kts = mpDBObject->maxSpeed_kts;
    UpdateSpeedSimple(dt_s);

    float speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts;
    float disp_m = speed_mps * dt_s; // distance moved this update

    float disp_z_m = disp_m * sinf(mcKin.mfClimbAngle_rad);
    mcKin.mfAlt_m += disp_z_m;

    if (mcKin.mfClimbAngle_rad > -1.50f)
    {
        float disp_rad = C_MTORAD * disp_m; // distance in equator radians
        float heading_rad = mcKin.mfHeading_rad;
        float disp_xy_rad = disp_rad * cosf(mcKin.mfClimbAngle_rad);
        mcKin.mfLon_rad += disp_xy_rad * (double)(sinf(heading_rad) / cosf((float)mcKin.mfLat_rad));
        mcKin.mfLat_rad += (double)cosf(heading_rad) * disp_xy_rad;
        
        HandlePoleWrap();
    }

    //	UpdateEffects();

    //    Update3D();

    if (clientMode) return;

    if (mcKin.mfAlt_m < -10.0f)
    {
        UpdateDepthChargeDetonation();
    }

    if (mcKin.mfAlt_m <= mcTerrain.mfHeight_m)
    {
        SelfDestruct();
    }

}

/**
* Assumes that all depth charges have either contact or proximity fuse
* 假设所有的深水炸弹都装有接触引信或近炸引信
*/
void tcTorpedoObject::UpdateDepthChargeDetonation()
{
    // 如果我们距离引爆点非常近，则引爆，否则推迟到未来的时间步
    const float tminDet_s = 0.05f; // 最小引爆时间，单位秒

    // 从数据库对象中获取引爆范围
    float detRange_m = mpDBObject->detonationRange_m;

    // 定义一个地理矩形区域用于搜索潜在目标
    tcGeoRect region;
    // 将引爆范围和额外安全距离（100米）转换为弧度，并设置为搜索区域的边界
    float checkDistance_rad = (100.0f + detRange_m) * C_MTORAD; // C_MTORAD可能是米到弧度的转换常数

    // 根据当前位置和搜索距离设置地理矩形区域
    region.Set(mcKin.mfLon_rad-checkDistance_rad, mcKin.mfLon_rad+checkDistance_rad,
               mcKin.mfLat_rad-checkDistance_rad, mcKin.mfLat_rad+checkDistance_rad);

    // 创建一个游戏对象迭代器，用于遍历搜索区域内的所有对象
    tcGameObjIterator iter(region);

    // 遍历搜索区域内的所有对象
    for (iter.First();iter.NotDone();iter.Next())
    {
        std::shared_ptr<tcGameObject>target = iter.Get(); // 获取当前遍历到的对象
        // 忽略自己和其他同类型的深度炸弹
        if ((target != shared_from_this()) && (target->mpDBObject != mpDBObject))
        {
            // 用于存储碰撞点的坐标和时间差的变量
            float dx, dy, dz, dt;
            Vector3d collisionPoint; // 碰撞点的三维坐标
            float collisionRange_m; // 碰撞时的实际距离

            // 首先检查是否会发生碰撞
            if (target->CalculateCollisionPoint(shared_from_this(), collisionPoint, dt, collisionRange_m))
            {
                // 如果这不是一个直接命中的武器，检查尽管即将发生碰撞，但我们是否足够接近引爆点
                if (detRange_m > 0)
                {
                    // 根据碰撞距离和引爆范围计算引爆时间差
                    float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m));
                    // 如果引爆时间差大于最小引爆时间，则推迟引爆
                    if (dt_det_s > tminDet_s) return;

                    // 引爆深度炸弹
                    Detonate(dt_det_s);
                    // 设置直接命中的目标ID为-1（表示没有直接命中特定目标）
                    SetDirectHitTargetId(-1);
                    // 提前返回，因为已经引爆
                    return;
                }

                // 如果是直接命中的情况，并且碰撞时间小于最小引爆时间
                if (dt <= tminDet_s)
                {
                    // 将碰撞点从模型坐标转换为世界坐标
                    collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
                    // 获取碰撞点的三维坐标
                    dx = collisionPoint.x();
                    dy = collisionPoint.y();
                    dz = collisionPoint.z();

                    // 引爆深度炸弹
                    Detonate(dt);
                    // 设置直接命中的目标ID
                    SetDirectHitTargetId(target->mnID);
                    // 设置碰撞点的三维坐标
                    SetImpactPoint(Vector3d(dx, dy, dz));
                    // 提前返回，因为已经引爆
                    return;
                }
            }

            // 如果这不是一个直接命中的武器，检查近距离引爆条件
            if (detRange_m > 0)
            {
                // 检查未来最近的接近点
                dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

                // 如果接近点的时间小于最小引爆时间
                if (dt <= tminDet_s)
                {
                    // 计算到模型原点的距离作为初始损伤范围
                    float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz);

                    // 检查向上的射线是否更接近
                    if (target->CalculateCollisionPointDir(shared_from_this(), Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
                    {
                        // 更新损伤范围为射线碰撞范围和初始损伤范围中的较小值
                        damageRange_m = std::min(collisionRange_m, damageRange_m);
                    }

                    // 如果损伤范围在两倍引爆范围内，则引爆
                    if (damageRange_m <= 2*detRange_m)
                    {
                        Detonate(dt);
                        // 设置直接命中的目标ID为-1（表示没有直接命中特定目标）
                        SetDirectHitTargetId(-1);
                        // 提前返回，因为已经引爆
                        return;
                    }
                }
            }
        }
    }
}


void tcTorpedoObject::UpdateDetonation()
{
    // 如果我们距离爆炸点这么近，则爆炸，否则延迟到未来的时间步
    const float tminDet_s = 0.05f; // 最小爆炸延迟时间，单位秒

    std::shared_ptr<tcSensorState> sensor = GetSensorMutable(0); // 获取第一个可变传感器状态
    if (sensor == 0)
    {
        UpdateDetonationUnguided(); // 如果没有传感器，则更新非制导爆炸逻辑
        return;
    }

    assert(sensor != 0); // 断言确保传感器不为空
    if (sensor->mnMode != SSMODE_SEEKERTRACK) return; // 如果传感器不是追踪模式，则返回

    if ((interceptTime > 3.0f) || (sensor->mcTrack.mnID == -1)) return; // 如果拦截时间超过3秒或追踪目标ID为-1，则返回

    std::shared_ptr<tcGameObject> target = simState->GetObject(sensor->mcTrack.mnID); // 从模拟状态中获取追踪的目标对象

    if (target != 0)
    {
        SetIntendedTarget(sensor->mcTrack.mnID); // 如果目标存在，则设置意图目标ID
    }
    else
    {
        SetIntendedTarget(-1); // 如果目标不存在，则清除意图目标ID
        sensor->mcTrack.mnID = -1; // 清除追踪目标ID
        return;
    }

    float dx, dy, dz, dt; // 定义变量dx, dy, dz用于存储碰撞点的坐标，dt用于存储碰撞时间
    Vector3d collisionPoint; // 定义碰撞点向量
    float collisionRange_m; // 定义碰撞范围，单位米

    float detRange_m = mpDBObject->detonationRange_m; // 获取爆炸范围，单位米

    // 首先检查是否碰撞
    if (target->CalculateCollisionPoint(shared_from_this(), collisionPoint, dt, collisionRange_m))
    {
        // 如果这不是直接命中武器，检查是否尽管即将碰撞但仍足够接近
        if (detRange_m > 0)
        {
            float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m)); // 计算实际爆炸时间
            if (dt_det_s > tminDet_s) return; // 如果实际爆炸时间大于最小爆炸延迟时间，则返回

            Detonate(dt_det_s); // 爆炸
            SetDirectHitTargetId(-1); // 清除直接命中目标ID
            return;
        }

        // 直接命中武器，检查是否延迟到未来时间步
        if (dt > tminDet_s) return; // 如果碰撞时间大于最小爆炸延迟时间，则返回

        collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint); // 将碰撞点从模型坐标转换为世界坐标
        dx = collisionPoint.x(); // 获取碰撞点x坐标
        dy = collisionPoint.y(); // 获取碰撞点y坐标
        dz = collisionPoint.z(); // 获取碰撞点z坐标

        Detonate(dt); // 爆炸
        SetDirectHitTargetId(target->mnID); // 设置直接命中目标ID
        SetImpactPoint(Vector3d(dx, dy, dz)); // 设置爆炸点
        return;
    }

    // 如果是直接命中武器（爆炸范围==0），则返回
    if (detRange_m == 0) return;

    // 检查当前是否足够接近目标
    //float currentRange_m = 1000.0f * target->mcKin.RangeToKmAlt(mcKin);
    // 此部分代码已被注释，可能是因为它在当前逻辑中不是必需的

    // 检查未来的最近接近点
    dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz); // 计算与目标的最近接近点

    if (dt > tminDet_s) return; // 如果最近接近时间大于最小爆炸延迟时间，则返回

    float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz); // 计算到模型原点的距离作为初始损伤范围

    // 检查“向上”射线是否更近
    if (target->CalculateCollisionPointDir(shared_from_this(), Vector3d(0, 0, 1), collisionPoint, collisionRange_m))
    {
        damageRange_m = std::min(collisionRange_m, damageRange_m); // 更新损伤范围为最小碰撞范围
    }

    if (damageRange_m <= 2*detRange_m)
    {
        Detonate(dt); // 爆炸
        SetDirectHitTargetId(-1); // 清除直接命中目标ID
    }
}

// expensive since does collision testing on all objects that are close to this torpedo every update
// 更新无制导鱼雷的爆炸逻辑
void tcTorpedoObject::UpdateDetonationUnguided()
{
    // 如果还有剩余的运行时间到启用点，则直接返回，不执行爆炸逻辑
    if (runToEnable_m > 0) return;

    // 定义一个地理矩形区域，用于搜索潜在的目标
    tcGeoRect region;
    // 将200米转换为弧度（纬度变化量）
    const float dlat = C_MTORAD * 200.0f;
    // 根据当前纬度计算经度变化量，以形成一个正方形的搜索区域
    float dlon = dlat / cosf(mcKin.mfLat_rad);

    // 设置搜索区域，以当前鱼雷的经纬度为中心
    region.Set(mcKin.mfLon_rad - dlon, mcKin.mfLon_rad + dlon,
               mcKin.mfLat_rad - dlat, mcKin.mfLat_rad + dlat);

    // 创建一个迭代器，用于遍历搜索区域内的所有游戏对象
    tcGameObjIterator iter(region);

    // 遍历搜索区域内的所有游戏对象
    for (iter.First(); iter.NotDone(); iter.Next())
    {
        std::shared_ptr<tcGameObject> target = iter.Get(); // 获取当前遍历到的游戏对象

        // 如果当前对象不是鱼雷本身且不是空指针
        if ((target != shared_from_this()) && (target != 0))
        {
            // 定义最小爆炸延迟时间，用于避免过于频繁的爆炸计算
            const float tminDet_s = 0.05f;

            // 定义用于碰撞计算的变量
            float dx, dy, dz, dt;
            Vector3d collisionPoint; // 碰撞点
            float collisionRange_m; // 碰撞范围

            // 获取鱼雷的爆炸范围
            float detRange_m = mpDBObject->detonationRange_m;

            // 首先检查是否与目标发生碰撞
            if (target->CalculateCollisionPoint(shared_from_this(), collisionPoint, dt, collisionRange_m))
            {
                // 如果这不是直接命中的武器，检查尽管即将发生碰撞，但我们是否足够接近
                if (detRange_m > 0)
                {
                    // 计算基于碰撞范围和爆炸范围的延迟时间
                    float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m));
                    // 如果延迟时间大于最小爆炸延迟时间，则推迟到未来的时间步执行
                    if (dt_det_s > tminDet_s) return;

                    // 执行爆炸逻辑
                    Detonate(dt_det_s);
                    // 设置直接命中的目标ID为-1（可能表示无特定目标）
                    SetDirectHitTargetId(-1);
                    // 退出函数
                    return;
                }

                // 如果是直接命中（爆炸范围等于0），但碰撞时间大于最小爆炸延迟时间，则推迟执行
                if (dt > tminDet_s) return;

                // 将碰撞点从模型坐标转换为世界坐标
                collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
                // 获取碰撞点的坐标
                dx = collisionPoint.x();
                dy = collisionPoint.y();
                dz = collisionPoint.z();

                // 执行爆炸逻辑
                Detonate(dt);
                // 设置直接命中的目标ID为目标对象的ID
                SetDirectHitTargetId(target->mnID);
                // 设置爆炸影响点
                SetImpactPoint(Vector3d(dx, dy, dz));
                // 退出函数
                return;
            }

            // 如果这是直接命中的武器（爆炸范围等于0），则直接返回，不进行后续计算
            if (detRange_m == 0) return;

            // 检查未来最接近的接近点
            dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

            // 如果计算出的时间大于最小爆炸延迟时间，则推迟到未来的时间步执行
            if (dt > tminDet_s) return;

            // 计算到目标模型原点的距离作为初始损伤范围
            float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz);

            // 检查向上的射线是否更近
            if (target->CalculateCollisionPointDir(shared_from_this(), Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
            {
                // 更新损伤范围为向上射线碰撞范围和当前损伤范围中的较小值
                damageRange_m = std::min(collisionRange_m, damageRange_m);
            }

            // 如果损伤范围在两倍爆炸范围内，则执行爆炸逻辑
            if (damageRange_m <= 2*detRange_m)
            {
                Detonate(dt);
                // 设置直接命中的目标ID为-1（可能表示非特定目标爆炸）
                SetDirectHitTargetId(-1);
            }

        }
    }
}

/**
*
*/
void tcTorpedoObject::UpdateDrop(float dt_s)
{
    float heading_rad = mcKin.mfHeading_rad;
    float fGroundSpeed_kts = cosf(mcKin.mfClimbAngle_rad) * mcKin.mfSpeed_kts;
    float vz_mps = C_KTSTOMPS * sinf(mcKin.mfClimbAngle_rad) * mcKin.mfSpeed_kts;
    float vxy_mps = C_KTSTOMPS * fGroundSpeed_kts;
    //float z = mcKin.mfAlt_m;

    float dvz = C_G * dt_s;

    if (vz_mps < -30)
    {
        dvz = 0;
    }
    else if (vz_mps < -20)
    {
        dvz = 0.1f * (vz_mps + 30) * dvz; // gradually limit acceleration
    }

    vz_mps = vz_mps - dvz;


    if (vxy_mps > 0)
    {
        vxy_mps = vxy_mps - dt_s * 0.02f * vxy_mps * vxy_mps; // air drag
    }
    if (vxy_mps < 0)
    {
        vxy_mps = 0;
    }

    double fDistance_rad = fGroundSpeed_kts*dt_s*(float)C_KTSTORADPS;

    mcKin.mfLon_rad += fDistance_rad*(double)(sinf(heading_rad)/cosf((float)mcKin.mfLat_rad));
    mcKin.mfLat_rad += (double)cosf(heading_rad)*fDistance_rad; 
    mcKin.mfAlt_m += vz_mps*dt_s;

    mcKin.mfClimbAngle_rad = atan2(vz_mps, vxy_mps);
    mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;
    mcKin.mfSpeed_kts = C_MPSTOKTS * sqrtf(vz_mps*vz_mps + vxy_mps*vxy_mps);
    
    if (mcKin.mfAlt_m <= 0)
    {
        mcKin.mfSpeed_kts *= 0.1f; // lose speed after hitting water
        if (mcKin.mfSpeed_kts < 5.0) mcKin.mfSpeed_kts = 5.0f;

        mcKin.mfClimbAngle_rad *= 0.125f;
        mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;
    }

    //Update3D();

}

/**
*
*/
//void tcTorpedoObject::UpdateEffects()
//{
//    if (model)
//    {
//        if ((mcKin.mfAlt_m < -5) && (mcKin.mfSpeed_kts > 15))
//        {
//			model->SetSmokeMode(tc3DModel::BUBBLES);
//        }
//        else
//        {
//			model->SetSmokeMode(tc3DModel::OFF);
//        }

//        model->UpdateEffects();
//    }
//}




/**
*
*/
void tcTorpedoObject::UpdateGuidance(double t)
{
    // 定义鱼雷加速度常数和它的倒数
    const float torpedo_acz = 50.0f; // 鱼雷加速度（米/秒²）
    const float one_over_torpedo_acz = 1.0f / 50.0f; // 鱼雷加速度的倒数

    // 计算从上一次更新到现在的时间差
    float dt_s = t - lastGuidanceUpdate;
    // 如果时间差小于更新间隔，则直接返回
    if (dt_s < guidanceUpdateInterval) return;
    // 更新上一次更新时间为当前时间
    lastGuidanceUpdate = t;

    //************ 引导模式更新 **************
    // 初始化是否使用截击俯仰角的标志
    bool useInterceptPitch = false;
    // 初始化截击俯仰角为0
    float interceptPitch_rad = 0;

    // 如果鱼雷已经运行到启动距离以内
    if (runToEnable_m <= 0)
    {
        // 如果搜索器存在且当前不活跃
        if ((seeker != nullptr) && (!seeker->IsActive()))
        {
            // 更新自动线缆引导
            UpdateAutoWireGuidance();
            // 激活搜索器
            seeker->SetActive(true);
            // 设置搜索器模式为搜索模式
            seeker->mnMode = SSMODE_SEEKERSEARCH;
            // 设置搜索航向为目标航向
            searchHeading_rad = goalHeading_rad;
            // 设置鱼雷速度为数据库中的最大速度
            goalSpeed_kts = mpDBObject->maxSpeed_kts;
            // 记录搜索开始时的已用时间
            searchStartTime = runTime;
        }

        // 设置引导更新间隔为0.5秒
        guidanceUpdateInterval = 0.5f;

        // 获取搜索器当前模式，如果搜索器不存在则默认为空模式
        short int seekerMode = (seeker != nullptr) ? seeker->mnMode : SSMODE_NULL;

        // 根据搜索器模式执行不同的操作
        switch (seekerMode)
        {
        case SSMODE_NULL:
            // 空模式，不执行任何操作
            break;
        case SSMODE_SEEKERTRACK:
        {
            // 定义一个预测轨迹变量
            tcTrack predictedtrack;
            // 定义时间到截击、距离等变量
            float tti_s;
            float range_km;

            // 设置目标深度为搜索器跟踪目标的深度（取负值）
            goalDepth_m = -seeker->mcTrack.mfAlt_m;
            // 获取预测轨迹
            seeker->mcTrack.GetPrediction(predictedtrack, t);

            // 如果目标是水面目标，则设置深度为在船底下方一定深度处引爆
            if (seeker->mcTrack.mfAlt_m >= -5.0f)
            {
                goalDepth_m = 10.0f; // 设置为10米深度
                predictedtrack.mfAlt_m = -10.0f; // 预测轨迹深度也设置为10米下方
            }

            // 如果只有方位信息，没有距离信息
            if (seeker->mcTrack.mnFlags & TRACK_BEARING_ONLY)
            {
                // 设置目标航向为预测轨迹的方位（此时为方位角）
                goalHeading_rad = predictedtrack.mfHeading_rad;

                // 尝试提前对准目标（临时截击航向）
                if (predictedtrack.mnFlags & TRACK_BEARINGRATE_VALID)
                {
                    // 根据方位变化率调整目标航向
                    goalHeading_rad += 0.5f * predictedtrack.bearingRate_radps;
                }
            }
            else
            {
                // 使用三维截击数据计算目标航向、俯仰角、时间到截击和距离
                mcKin.GetInterceptData3D(predictedtrack, goalHeading_rad,
                                         interceptPitch_rad, tti_s, range_km);

                // 设置使用截击俯仰角的标志为真
                useInterceptPitch = true;
                // 设置截击时间为计算得到的时间
                interceptTime = tti_s;

                // 如果截击时间小于100秒，则随机选择左圆或右圆搜索模式以防丢失目标时能够重新搜索
                if (interceptTime < 100)
                {
                    searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
                }
            }
        }
        break;
        case SSMODE_SEEKERSEARCH:
        {
            // 根据搜索模式计算目标航向
            //
            // 蛇形搜索模式（SEARCH_SNAKE）：
            //     在蛇形搜索模式下，目标航向会根据时间的变化而正弦波动。
            //     searchHeading_rad是搜索开始时的初始航向。
            //     0.4f * sinf(0.2f * (runTime - searchStartTime))是一个正弦函数，其中runTime是当前时间，searchStartTime是搜索开始的时间。这个正弦函数会根据时间的推移而波动，其频率由0.2f决定，振幅由0.4f决定。
            //     因此，goalHeading_rad会在searchHeading_rad的基础上加上这个正弦波动值，从而模拟蛇形搜索的航向变化。
            // 左圆搜索模式（SEARCH_LEFTCIRCLE）：
            //     在左圆搜索模式下，目标航向会随着时间的推移而线性减少，模拟左转的效果。
            //     减少的速率是0.209f弧度/秒（这相当于大约12度/秒，因为π/180 ≈ 0.0175弧度/度，所以0.209f / (π/180) ≈ 12度/秒）。
            //     goalHeading_rad会在searchHeading_rad的基础上减去这个线性减少的值。
            //     为了确保goalHeading_rad保持在0到2π（即360度）的范围内，使用了fmodf函数对结果进行模运算。然后，通过加上π（即180度）来调整方向，这可能是为了将航向从数学上的[0, 2π)范围映射到某个特定的搜索方向范围。
            // 右圆搜索模式（SEARCH_RIGHTCIRCLE）：
            //     在右圆搜索模式下，目标航向会随着时间的推移而线性增加，模拟右转的效果。
            //     增加的速率同样是0.209f弧度/秒。
            //     goalHeading_rad会在searchHeading_rad的基础上加上这个线性增加的值。
            //     同样，为了确保goalHeading_rad保持在0到2π的范围内，使用了fmodf函数。但是，这次是通过减去π来调整方向，这可能是为了与左圆搜索模式保持某种对称性或一致性。


            switch (searchMode)
            {
            case SEARCH_SNAKE:
                // 蛇形搜索模式，根据时间变化正弦函数调整目标航向
                goalHeading_rad = searchHeading_rad + 0.4f * sinf(0.2f * (runTime - searchStartTime));
                break;
            case SEARCH_LEFTCIRCLE:
                // 左圆搜索模式，根据时间线性减少目标航向（模拟左转）
                goalHeading_rad = searchHeading_rad - 0.209f * (runTime - searchStartTime); // 12度/秒
                // 将目标航向限制在0到2π之间，并加上π以调整方向
                goalHeading_rad = fmodf(goalHeading_rad, C_TWOPI) + C_PI;
                break;
            case SEARCH_RIGHTCIRCLE:
                // 右圆搜索模式，根据时间线性增加目标航向（模拟右转）
                goalHeading_rad = searchHeading_rad + 0.209f * (runTime - searchStartTime);
                // 将目标航向限制在0到2π之间，并减去π以调整方向
                goalHeading_rad = fmodf(goalHeading_rad, C_TWOPI) - C_PI;
                break;
            default:
                // 默认不执行任何操作
                break;
            }
        }
        break;
        case SSMODE_SEEKERACQUIRE:
        {
            // 在捕获模式下保持当前航向
            goalHeading_rad = mcKin.mfHeading_rad;
        }
        break;
        default:
        {
            // 默认情况下断言失败（表示不应该到达这里），并将搜索器模式重置为搜索模式
            assert(false);
            seeker->mnMode = SSMODE_SEEKERSEARCH;
        }
        break;
        }
    } // if (runToEnable_m <= 0) 结束
    else
    {
        // 如果数据库对象中存在有效载荷信息
        if (mpDBObject->payloadClass.size() > 0)
        {
            // 如果有效载荷尚未部署
            if (!payloadDeployed)
            {
                // 设置启动距离为到达导航点到部署有效载荷的距离
                runToEnable_m = 1000.0f * mcKin.RangeToKm(&waypoint);
                // 如果启动距离小于等于引爆距离，则部署有效载荷
                if (runToEnable_m <= mpDBObject->detonationRange_m)
                {
                    DeployPayload();
                }
                // 设置目标航向为导航点到鱼雷当前位置的航向
                goalHeading_rad = mcKin.HeadingToGeoRad(waypoint.mfLon_rad, waypoint.mfLat_rad);
            }
            else
            {
                // 有效载荷已部署，执行自毁操作
                SelfDestruct();
            }
        }
    }

    // 不超过最大深度，也不离底部太近（这里有点作弊，因为知道了底部高度，或者鱼雷上有深度探测器）
    // 计算最大深度，取数据库中的最大深度减去10米和地形高度减去10米中的较小值
    float maxDepth_m = std::min(mpDBObject->maxDepth_m - 10.0f, -(mcTerrain.mfHeight_m + 10.0f));

    // 获取当前深度
    float depth_m = -mcKin.mfAlt_m;
    // 如果当前深度大于最大深度，则调整目标深度并设置俯仰角为0（这里应该是为了上浮或保持安全深度）
    if (depth_m > maxDepth_m)
    {
        goalDepth_m = maxDepth_m - 5.0f; // 目标深度设置为最大深度再减去5米
        interceptPitch_rad = 0.1f; // 这里设置俯仰角似乎是为了微调深度，但在此上下文中可能不起作用
    }

    // 根据截击时间更新引导更新率和搜索器扫描率 越靠近更新越频繁
    if (interceptTime <= 2.0)
    {
        // 如果截击时间小于等于2秒，则设置更新间隔和扫描周期为0.
        guidanceUpdateInterval = 0.1f;
        seeker->mfCurrentScanPeriod_s = 0.1f;
    }
    else if (interceptTime <= 5.0)
    {
        guidanceUpdateInterval = 0.2f;
        seeker->mfCurrentScanPeriod_s = 0.2f;
    }

    // depth control
    if (useInterceptPitch)
    {
        assert(!_isnan(interceptPitch_rad));
        goalPitch_rad = interceptPitch_rad;
    }
    else
    {

        //     如果当前深度depth_m大于目标深度goalDepth_m加上torpedo_acz，则意味着潜水物体太深了，需要向上调整。
        // *因此，将goalPitch_rad设置为正数（0.7f），表示应该减小俯仰角（向上抬头）。
        //     如果当前深度depth_m小于目标深度goalDepth_m减去torpedo_acz，则意味着潜水物体太浅了，需要向下调整
        // 。因此，将goalPitch_rad设置为负数（-0.7f），表示应该增加俯仰角（向下低头）。
        //    如果当前深度depth_m在目标深度goalDepth_m的torpedo_acz范围内，
        // 则根据当前深度与目标深度的差值，以及one_over_torpedo_acz（torpedo_acz的倒数，
        // 可能用于归一化或比例调整）来计算一个介于-0.7f和0.7f之间的goalPitch_rad值。
        // 这个计算可能是为了更精细地控制潜水物体在接近目标深度时的俯仰角，以保持或微调其深度。

        if (depth_m > goalDepth_m + torpedo_acz)
        {
            goalPitch_rad = 0.7f;
        }
        else if (depth_m < goalDepth_m - torpedo_acz)
        {
            goalPitch_rad = -0.7f;
        }
        else
        {
            goalPitch_rad = 0.7f * (depth_m - goalDepth_m) * one_over_torpedo_acz;
        }
    }


}


void tcTorpedoObject::UpdateBottomMine(float dt_s) // 更新底部水雷的方法，dt_s为时间间隔（秒）
{
    if ((mcKin.mfSpeed_kts == 0) && (mcKin.mfAlt_m < 0)) // 如果速度为零且高度为负（即在水下）
    {
        UpdateBottomMineTrigger(mfStatusTime); // 更新底部水雷触发条件
    }
    else
    {
        // sink to bottom // 沉到水底
        const float sinkSpeed_kts = 8.0f; // 下沉速度，单位：节
        float alpha = 0.1f * dt_s; // 用于平滑过渡的系数
        mcKin.mfClimbAngle_rad = (1.0f-alpha)*mcKin.mfClimbAngle_rad - alpha*1.55f; // 缓慢改变爬升角到-89度（向下）
        mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad; // 将俯仰角设置为爬升角

        goalSpeed_kts = sinkSpeed_kts; // 目标速度设为下沉速度
        UpdateSpeedSimple(dt_s); // 更新速度

        float speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts; // 将速度从节转换为米/秒
        float disp_m = speed_mps * dt_s; // 在此次更新中移动的距离

        float disp_z_m = disp_m * sinf(mcKin.mfClimbAngle_rad); // 在垂直方向上移动的距离
        mcKin.mfAlt_m += disp_z_m; // 更新高度

        if (mcKin.mfClimbAngle_rad > -1.50f) // 如果爬升角大于-1.5弧度（即未完全向下）
        {
            float disp_rad = C_MTORAD * disp_m; // 将距离转换为赤道弧度
            float heading_rad = mcKin.mfHeading_rad; // 当前朝向
            float disp_xy_rad = disp_rad * cosf(mcKin.mfClimbAngle_rad); // 在水平面上移动的距离
            mcKin.mfLon_rad += disp_xy_rad * (double)(sinf(heading_rad) / cosf((float)mcKin.mfLat_rad)); // 更新经度
            mcKin.mfLat_rad += (double)cosf(heading_rad) * disp_xy_rad; // 更新纬度

            HandlePoleWrap(); // 处理极地环绕问题
        }
        guidanceUpdateInterval = 30.0; // 设定制导更新间隔

        if (mcKin.mfAlt_m < -mpDBObject->maxDepth_m) // 如果当前高度低于最大深度
        {
            ApplyGeneralDamage(1.0f, 0); // 应用一般伤害
        }

        if (mcKin.mfAlt_m <= mcTerrain.mfHeight_m) // 如果当前高度小于或等于地形高度
        {
            // deploy mine // 部署水雷
            mcKin.mfSpeed_kts = 0; // 速度设为零
            mcKin.mfAlt_m = std::max(std::min(-goalDepth_m, -10.0f), mcTerrain.mfHeight_m); // 将高度设置为目标深度（不低于-10米，不高于地形高度）
            mcKin.mfPitch_rad = 1.55f; // 俯仰角设为-89度（向下）
            mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad; // 爬升角设为俯仰角
            lastGuidanceUpdate = mfStatusTime + 60.0; // 延迟制导更新
        }
    }

    //UpdateEffects(); // 更新效果（已注释）

    //Update3D(); // 更新3D模型（已注释）
}

void tcTorpedoObject::UpdateBottomMineTrigger(double t) // 更新底部水雷触发条件的方法，t为当前时间
{
    float dt_s = t - lastGuidanceUpdate; // 计算从上次制导更新到现在的时间间隔
    if ((dt_s < guidanceUpdateInterval) || (clientMode)) return; // 如果时间间隔小于更新间隔或处于客户端模式，则直接返回
    lastGuidanceUpdate = t; // 更新上次制导更新的时间

    // 根据武器类型执行不同的逻辑
    switch (mpDBObject->weaponType)
    {
    case tcTorpedoDBObject::BOTTOM_MINE: // 如果是底部水雷
    {
        // 在以当前位置为中心，半径为1公里的范围内查找所有对象
        float rangeY_rad = C_KMTORAD * 1.0f; // 将1公里转换为弧度
        float rangeX_rad = rangeY_rad / cosf(mcKin.mfLat_rad); // 根据纬度计算经度上的范围
        tcGeoRect region; // 定义一个地理矩形区域
        region.left = mcKin.mfLon_rad - rangeX_rad; // 设置区域的左边界
        region.right = mcKin.mfLon_rad + rangeX_rad; // 设置区域的右边界
        region.bottom = mcKin.mfLat_rad - rangeY_rad; // 设置区域的下边界
        region.top = mcKin.mfLat_rad + rangeY_rad; // 设置区域的上边界

        tcGameObjIterator iter(region); // 创建一个迭代器来遍历区域内的对象
        float closestRange_km = 999.0f; // 初始化最近距离为一个很大的值
        std::shared_ptr<tcGameObject> closestTarget = 0; // 初始化最近目标为nullptr
        for (iter.First(); iter.NotDone(); iter.Next()) // 遍历区域内的所有对象
        {
            std::shared_ptr<tcGameObject> target = iter.Get(); // 获取当前对象

            // 检查对象是否为水面或潜艇类型，并且不是自身
            bool isEligible = ((target->mpDBObject->mnType & PTYPE_SURFACE) != 0) ||
                              (target->mpDBObject->mnType == PTYPE_SUBMARINE);
            isEligible = isEligible && (target != shared_from_this()); // 排除自身检测
            if (isEligible) // 如果对象符合条件
            {
                float range_km = this->mcKin.RangeToKmAlt(target->mcKin); // 计算与当前对象的距离
                if (range_km < closestRange_km) // 如果当前对象距离更近
                {
                    closestTarget = target; // 更新最近目标
                    closestRange_km = range_km; // 更新最近距离
                }
            }
        }

        float detonationRange_km = 0.001f * mpDBObject->detonationRange_m; // 将水雷的爆炸范围从米转换为公里

        // 如果最近距离小于或等于爆炸范围
        if (closestRange_km <= detonationRange_km)
        {
            tcKinematics targetKin = closestTarget->mcKin; // 获取最近目标的运动学状态
            targetKin.Extrapolate(0.25f); // 对目标的位置进行外推，预测0.25秒后的位置
            float futureRange_km = targetKin.RangeToKmAlt(this->mcKin); // 计算预测位置与当前对象的距离
            if (futureRange_km < closestRange_km) // 如果预测的距离更近
            {
                guidanceUpdateInterval = 0.25f; // 设置制导更新间隔为0.25秒
            }
            else
            {
                Detonate(0); // 触发爆炸
            }
        }
        else if (closestRange_km < 1.0f) // 如果最近距离在1公里以内但大于爆炸范围
        {
            guidanceUpdateInterval = 1.0f + 10.0f * closestRange_km; // 根据最近距离动态设置制导更新间隔
        }
        else
        {
            guidanceUpdateInterval = 30.0f; // 设置默认的制导更新间隔为30秒
        }
    }
    break;
    case tcTorpedoDBObject::BOTTOM_MINE_CAPTOR: // 如果是捕获型底部水雷
    {
        if (seeker == 0) // 如果没有导引头
        {
            assert(false); // 断言失败，表示不应该执行到这里
            return; // 直接返回
        }

        if (!seeker->IsActive()) // 如果导引头未激活
        {
            seeker->SetActive(true); // 激活导引头
            seeker->mnMode = SSMODE_SEEKERSEARCH; // 设置导引头为搜索模式
        }
        tcSensorPlatform::Update(mfStatusTime); // 更新传感器平台的状态
        if (seeker->mnMode == SSMODE_SEEKERTRACK) // 如果导引头处于跟踪模式
        {
            if (!payloadDeployed) DeployPayload(); // 如果未部署有效载荷，则部署
            else SelfDestruct(); // 如果已部署，则自毁
        }
    }
    break;
    default: // 如果武器类型不匹配
        assert(false); // 断言失败，表示不应该执行到这里
        break;
    }
}

/**
* Simple model for speed update
* Flat max acceleration
*/
void tcTorpedoObject::UpdateSpeedSimple(float dt_s)
{
    float ds_kts = goalSpeed_kts - mcKin.mfSpeed_kts;
    float ds_max = mpDBObject->acceleration_ktsps * dt_s;
    float ds_min = -ds_max;

    if (ds_kts < ds_min) {ds_kts = ds_min;} // restrict to acceleration
    else if (ds_kts > ds_max) {ds_kts = ds_max;}

    mcKin.mfSpeed_kts += ds_kts;

    if (mcKin.mfSpeed_kts < 0) mcKin.mfSpeed_kts = 0;
}

/**
*
*/
void tcTorpedoObject::Clear()  
{  
    tcGameObject::Clear();
}

/**
*
*/
void tcTorpedoObject::DesignateTarget(long anID) 
{
    seeker->mcTrack.mnID = anID;

    // needs to SSMODE_SEEKERACQUIRE so track is updated before guidance update
    seeker->mnMode = SSMODE_SEEKERACQUIRE;
}

/**
*
*/
void tcTorpedoObject::RandInitNear(float afLon, float afLat) 
{

    //strcpy(mzClass.mz,mpDBObject->mzClass.mz);
    mzUnit=strutil::AssignRandomStringB(mzUnit);

    mfStatusTime = 0;
    mcKin.mfLon_rad = afLon + randfc(1.1f);
    mcKin.mfLat_rad = afLat + randfc(1.1f);

    mcKin.mfHeading_rad = 360*randf();
    mcKin.mfSpeed_kts = 100;
    mfDamageLevel = 0;

    //tcGameObject::RandInitNear(afLon,afLat);
    mcKin.mfAlt_m = -100.0f;
    SetHeading(mcKin.mfHeading_rad);
    SetSpeed(mcKin.mfSpeed_kts);

    mcKin.SetRelativeGeo(waypoint, mcKin.mfHeading_rad*(float)C_PIOVER180, 100.0f);
}

/**
* If missile is targeting a land datum, gp.mnTargetID will be
* set to -1. Otherwise gp.mnTargetID is set to the intended 
* target of the missile.
*
* @return 1 if missile is in terminal phase
*/
int tcTorpedoObject::GetGuidanceParameters(tsGuidanceParameters& gp) 
{
    if (seeker->mnMode == SSMODE_SEEKERTRACK)
    {
        gp.mnTargetID = seeker->mcTrack.mnID;

        if (seeker->IsPassive())
        {
            gp.mfInterceptTime = 0;
        }
        else
        {
            gp.mfInterceptTime = interceptTime;
        }
        return 1;
    }
    else
    {
        return 0;
    }
}

/**
*
*/
void tcTorpedoObject::PrintToFile(tcFile& file)
{
    tcString s;
    tcGameObject::PrintToFile(file);
    s.Format(" Missile Object\n");
    file.WriteString(s.GetBuffer());
}

/**
*
*/
void tcTorpedoObject::SaveToFile(tcFile& file) 
{
    tcGameObject::SaveToFile(file);

    assert(false);
}

/**
*
*/
void tcTorpedoObject::LoadFromFile(tcFile& file) 
{
    tcGameObject::LoadFromFile(file);

    assert(false);
}

/**
*
*/
void tcTorpedoObject::Serialize(tcFile& file, bool mbLoad) 
{
    if (mbLoad)
    {
        LoadFromFile(file);
    }
    else
    {
        SaveToFile(file);
    }
}

/**
*
*/
tcTorpedoObject::tcTorpedoObject() 
    : tcWeaponObject(),
    guidanceUpdateInterval(1.0f),
    lastGuidanceUpdate(0.0f),
    interceptTime(9999.0f),
    runTime(0),
    searchStartTime(0),
    goalPitch_rad(0),
    goalSpeed_kts(35),
    searchHeading_rad(0),
    searchMode(SEARCH_SNAKE),
    mpDBObject(0)
{
    Clear();

    seeker->mnMode = SSMODE_SEEKERSEARCH;
    mnModelType = MTYPE_TORPEDO;
}

/**
* Copy constructor.
*/
tcTorpedoObject::tcTorpedoObject(tcTorpedoObject& o) 
    : tcWeaponObject(o)
{
    mnModelType = MTYPE_TORPEDO;
    goalHeading_rad = o.goalHeading_rad;
    goalPitch_rad = o.goalPitch_rad;
    goalSpeed_kts = o.goalSpeed_kts;
    interceptTime = o.interceptTime;
    runTime = o.runTime;
    searchStartTime = o.searchStartTime;

    lastGuidanceUpdate = o.lastGuidanceUpdate;
    guidanceUpdateInterval = o.guidanceUpdateInterval;
    waypoint = o.waypoint;
    seeker = o.seeker;
    mpDBObject = o.mpDBObject;
}
/**
* Constructor that initializes using info from database entry.
*/
tcTorpedoObject::tcTorpedoObject(std::shared_ptr<tcTorpedoDBObject> obj)
    : tcWeaponObject(obj),
    guidanceUpdateInterval(1.0f),
    lastGuidanceUpdate(0.0f),
    interceptTime(9999.0f),
    runTime(0),
    searchStartTime(0),
    goalPitch_rad(0),
    goalSpeed_kts(35),
    searchHeading_rad(0),
    searchMode(SEARCH_SNAKE),
    mpDBObject(obj)
{
    mnModelType = MTYPE_TORPEDO;

    tcSensorPlatform::Init(obj->sonarClass.c_str(), shared_from_this()); // to avoid using this in initializer

    seeker = std::dynamic_pointer_cast<tcSonar>(GetSensorMutable(0));
}

/**
*
*/
tcTorpedoObject::~tcTorpedoObject() 
{
}


