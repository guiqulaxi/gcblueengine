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
void tcTorpedoObject::LaunchFrom(tcGameObject* obj, unsigned nLauncher)
{
    isWireActive = false;
    autoWireUpdates = true;

    tcLauncher virtualLauncher; // for missile deployment
    tcLauncher* pLauncher = &virtualLauncher;

    if (tcPlatformObject* platObj = dynamic_cast<tcPlatformObject*>(obj))
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
            tcSonarDBObject* sonar = mpDBObject->GetSeekerDBObj();
            
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
    else if (tcMissileObject* missile = dynamic_cast<tcMissileObject*>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        virtualLauncher.pointingAngle = 0;
        virtualLauncher.pointingElevation = 0;
        virtualLauncher.firingArc_deg = 0;
        virtualLauncher.runToEnable_m = 0;
        virtualLauncher.msDatum = missile->msWaypoint;
        virtualLauncher.runDepth_m = 0;
        virtualLauncher.preEnableSpeed_kts = 35.0f;
        virtualLauncher.ceiling_m = 0;
        virtualLauncher.floor_m = 0;
        virtualLauncher.usePassive = false;
        virtualLauncher.mnTargetID = missile->GetIntendedTarget();

        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
        searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
    }
    else if (tcTorpedoObject* torpedo = dynamic_cast<tcTorpedoObject*>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        virtualLauncher.pointingAngle = 0;
        virtualLauncher.pointingElevation = 0;
        virtualLauncher.runToEnable_m = 1.0; // start enabled
        virtualLauncher.msDatum = torpedo->waypoint;
        virtualLauncher.runDepth_m = torpedo->goalDepth_m;
        virtualLauncher.preEnableSpeed_kts = 35.0f;
        virtualLauncher.ceiling_m = 0;
        virtualLauncher.floor_m = 0;
        virtualLauncher.usePassive = false;
        virtualLauncher.mnTargetID = torpedo->GetIntendedTarget();

        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts + C_MPSTOKTS * mpDBObject->launchSpeed_mps;
        searchMode = randbool() ? SEARCH_LEFTCIRCLE : SEARCH_RIGHTCIRCLE;
    }
    else if (tcBallisticWeapon* ballistic = dynamic_cast<tcBallisticWeapon*>(obj))
    {
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;
        mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts + C_MPSTOKTS * mpDBObject->launchSpeed_mps;

        virtualLauncher.pointingAngle = 0;
        virtualLauncher.pointingElevation = 0;
        virtualLauncher.runToEnable_m = 1.0; // start enabled
        virtualLauncher.msDatum.Set(mcKin.mfLon_rad, mcKin.mfLat_rad, 0);
        virtualLauncher.runDepth_m = 0;
        virtualLauncher.preEnableSpeed_kts = 35.0f;
        virtualLauncher.ceiling_m = 0;
        virtualLauncher.floor_m = 0;
        virtualLauncher.usePassive = false;
        virtualLauncher.mnTargetID = ballistic->GetIntendedTarget();

        if (ballistic->mpDBObject->payloadQuantity > 1) // assume this is a RBU type
        {
            virtualLauncher.pointingAngle += randfc(1.0f);
            virtualLauncher.pointingElevation += randfc(0.1f);
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

    simState->AddPlatform(static_cast<tcGameObject*>(this));

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
tcSonar* tcTorpedoObject::GetSensorState() 
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

    // air launched torpedoes drop into water first
    bool outOfWater = (mcKin.mfAlt_m > 0.0f);
    if (outOfWater)
    {
        UpdateDrop(dt_s);
        return;
    }

    switch (mpDBObject->weaponType)
    {
    case tcTorpedoDBObject::DEPTH_CHARGE:
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
    // if we're this close to the detonation point then detonate, otherwise defer to future time step
    const float tminDet_s = 0.05f; 

    float detRange_m = mpDBObject->detonationRange_m;

    tcGeoRect region;
    float checkDistance_rad = (100.0f + detRange_m) * C_MTORAD;

    region.Set(mcKin.mfLon_rad-checkDistance_rad, mcKin.mfLon_rad+checkDistance_rad,
               mcKin.mfLat_rad-checkDistance_rad, mcKin.mfLat_rad+checkDistance_rad);

    tcGameObjIterator iter(region);

    for (iter.First();iter.NotDone();iter.Next())
    {
        tcGameObject *target = iter.Get();
        if ((target != this) && (target->mpDBObject != mpDBObject)) // no self detection, and cheat and ignore other depth charges
        {
            float dx, dy, dz, dt;
            Vector3d collisionPoint;
            float collisionRange_m;

            // first check for impact
            if (target->CalculateCollisionPoint(this, collisionPoint, dt, collisionRange_m))
            {
                // if this isn't a direct hit weapon, check if we're close enough despite impending collision
                if (detRange_m > 0)
                {
                    float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m));
                    if (dt_det_s > tminDet_s) return;

                    Detonate(dt_det_s);
                    SetDirectHitTargetId(-1);
                    return;
                }

                if (dt <= tminDet_s)
                {
                    collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
                    dx = collisionPoint.x();
                    dy = collisionPoint.y();
                    dz = collisionPoint.z();

                    Detonate(dt);
                    SetDirectHitTargetId(target->mnID);
                    SetImpactPoint(Vector3d(dx, dy, dz));
                    return;
                }
            }

            // check for proximity detonation if this isn't a direct hit weapon
            if (detRange_m > 0)
            {
                // check for future closest point of approach
                dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

                if (dt <= tminDet_s)
                {
                    float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz); // start with range to model origin

                    // check if "up" ray is closer
                    if (target->CalculateCollisionPointDir(this, Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
                    {
                        damageRange_m = std::min(collisionRange_m, damageRange_m);
                    }

                    if (damageRange_m <= 2*detRange_m)
                    {
                        Detonate(dt);
                        SetDirectHitTargetId(-1);
                        return;
                    }
                }
            }

        }
    }
}


void tcTorpedoObject::UpdateDetonation()
{
    // if we're this close to the detonation point then detonate, otherwise defer to future time step
    const float tminDet_s = 0.05f; 
    

    tcSensorState* sensor = GetSensorMutable(0);
    if (sensor == 0)
    {
        UpdateDetonationUnguided();
        return;
    }

    assert(sensor != 0);
    if (sensor->mnMode != SSMODE_SEEKERTRACK) return; 

    if ((interceptTime > 3.0f) || (sensor->mcTrack.mnID == -1)) return;

    tcGameObject* target = simState->GetObject(sensor->mcTrack.mnID);

    if (target != 0)
    {
        SetIntendedTarget(sensor->mcTrack.mnID); // in case it doesn't match
    }
    else
    {
        SetIntendedTarget(-1);
        sensor->mcTrack.mnID = -1;
        return;
    }

    float dx, dy, dz, dt;
    Vector3d collisionPoint;
    float collisionRange_m;

    float detRange_m = mpDBObject->detonationRange_m;

    // first check for impact
    if (target->CalculateCollisionPoint(this, collisionPoint, dt, collisionRange_m))
    {
        // if this isn't a direct hit weapon, check if we're close enough despite impending collision
        if (detRange_m > 0)
        {
            float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m));
            if (dt_det_s > tminDet_s) return;

            Detonate(dt_det_s);
            SetDirectHitTargetId(-1);
            return;
        }

        /*fprintf(stdout, "Collision detect: dt: %f, x: %.1f, y:%.1f, z:%.1f\n",
            dt, collisionPoint.x, collisionPoint.y, collisionPoint.z);*/
        if (dt > tminDet_s) return; // defer until future time step

        collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
        dx = collisionPoint.x();
        dy = collisionPoint.y();
        dz = collisionPoint.z();

        Detonate(dt);
        SetDirectHitTargetId(target->mnID);
        SetImpactPoint(Vector3d(dx, dy, dz));
        return;
    }

    // if this is a direct hit weapon (detonation range == 0) then return
    if (detRange_m == 0) return;

    //// check for sufficient proximity to target now
    //float currentRange_m = 1000.0f * target->mcKin.RangeToKmAlt(mcKin);

    //if (currentRange_m <= detRange_m)
    //{
    //    Detonate(0);
    //    SetDamageRange(0);
    //    SetDirectHitTargetId(-1);
    //    return;
    //}

    // check for future closest point of approach
    dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

    //float keelDepth_m = target->GetZmin();

    if (dt > tminDet_s) return; // defer until future time step

    float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz); // start with range to model origin

    // check if "up" ray is closer
    if (target->CalculateCollisionPointDir(this, Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
    {
        damageRange_m = std::min(collisionRange_m, damageRange_m);
    }

    if (damageRange_m <= 2*detRange_m)
    {
        Detonate(dt);
        SetDirectHitTargetId(-1);
    }


}

// expensive since does collision testing on all objects that are close to this torpedo every update
void tcTorpedoObject::UpdateDetonationUnguided()
{
    if (runToEnable_m > 0) return;

    tcGeoRect region;
    const float dlat = C_MTORAD * 200.0f;
    float dlon = dlat / cosf(mcKin.mfLat_rad);

    region.Set(mcKin.mfLon_rad - dlon, mcKin.mfLon_rad + dlon,
               mcKin.mfLat_rad - dlat, mcKin.mfLat_rad + dlat);

    tcGameObjIterator iter(region);

    for (iter.First(); iter.NotDone(); iter.Next())
    {
        tcGameObject* target = iter.Get();

        if ((target != this) && (target != 0))
        {
            // if we're this close to the detonation point then detonate, otherwise defer to future time step
            const float tminDet_s = 0.05f;

            float dx, dy, dz, dt;
            Vector3d collisionPoint;
            float collisionRange_m;

            float detRange_m = mpDBObject->detonationRange_m;

            // first check for impact
            if (target->CalculateCollisionPoint(this, collisionPoint, dt, collisionRange_m))
            {
                // if this isn't a direct hit weapon, check if we're close enough despite impending collision
                if (detRange_m > 0)
                {
                    float dt_det_s = dt * (1.0 - (detRange_m / collisionRange_m));
                    if (dt_det_s > tminDet_s) return;

                    Detonate(dt_det_s);
                    SetDirectHitTargetId(-1);
                    return;
                }

                /*fprintf(stdout, "Collision detect: dt: %f, x: %.1f, y:%.1f, z:%.1f\n",
				dt, collisionPoint.x, collisionPoint.y, collisionPoint.z);*/
                if (dt > tminDet_s) return; // defer until future time step

                collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
                dx = collisionPoint.x();
                dy = collisionPoint.y();
                dz = collisionPoint.z();

                Detonate(dt);
                SetDirectHitTargetId(target->mnID);
                SetImpactPoint(Vector3d(dx, dy, dz));
                return;
            }

            // if this is a direct hit weapon (detonation range == 0) then return
            if (detRange_m == 0) return;

            // check for future closest point of approach
            dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

            if (dt > tminDet_s) return; // defer until future time step

            float damageRange_m = sqrtf(dx*dx + dy*dy + dz*dz); // start with range to model origin

            // check if "up" ray is closer
            if (target->CalculateCollisionPointDir(this, Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
            {
                damageRange_m = std::min(collisionRange_m, damageRange_m);
            }

            if (damageRange_m <= 2*detRange_m)
            {
                Detonate(dt);
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


void tcTorpedoObject::UpdateBottomMine(float dt_s)
{
    if ((mcKin.mfSpeed_kts == 0) && (mcKin.mfAlt_m < 0))
    { 
        UpdateBottomMineTrigger(mfStatusTime);
    }
    else
    {
        // sink to bottom
        const float sinkSpeed_kts = 8.0f;
        float alpha = 0.1f * dt_s;
        mcKin.mfClimbAngle_rad = (1.0f-alpha)*mcKin.mfClimbAngle_rad - alpha*1.55f; // slowly change to -89 deg
        mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;

        goalSpeed_kts = sinkSpeed_kts;
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
        guidanceUpdateInterval = 30.0;

        if (mcKin.mfAlt_m < -mpDBObject->maxDepth_m)
        {
            ApplyGeneralDamage(1.0f, 0);
        }

        if (mcKin.mfAlt_m <= mcTerrain.mfHeight_m)
        {   
            // deploy mine
            mcKin.mfSpeed_kts = 0;
            mcKin.mfAlt_m = std::max(std::min(-goalDepth_m, -10.0f), mcTerrain.mfHeight_m);
            mcKin.mfPitch_rad = 1.55f;
            mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
            lastGuidanceUpdate = mfStatusTime + 60.0; // delay arming
        }
    }

    //UpdateEffects();

    //Update3D();


}

void tcTorpedoObject::UpdateBottomMineTrigger(double t)
{
    float dt_s = t - lastGuidanceUpdate;
    if ((dt_s < guidanceUpdateInterval) || (clientMode)) return;
    lastGuidanceUpdate = t;

    switch (mpDBObject->weaponType)
    {
    case  tcTorpedoDBObject::BOTTOM_MINE:
    {
        // find all objects within +/- 1 km
        float rangeY_rad = C_KMTORAD*1.0f;
        float rangeX_rad = rangeY_rad/cosf(mcKin.mfLat_rad);
        tcGeoRect region;
        region.left = mcKin.mfLon_rad - rangeX_rad;
        region.right = mcKin.mfLon_rad + rangeX_rad;
        region.bottom = mcKin.mfLat_rad - rangeY_rad;
        region.top = mcKin.mfLat_rad + rangeY_rad;

        tcGameObjIterator iter(region);
        float closestRange_km = 999.0f;
        tcGameObject* closestTarget = 0;
        for (iter.First();iter.NotDone();iter.Next())
        {
            tcGameObject* target = iter.Get();

            bool isEligible = ((target->mpDBObject->mnType & PTYPE_SURFACE) != 0) ||
                              (target->mpDBObject->mnType == PTYPE_SUBMARINE);
            isEligible = isEligible && (target != this); // no self detection
            if (isEligible)
            {
                float range_km = this->mcKin.RangeToKmAlt(target->mcKin);
                if (range_km < closestRange_km)
                {
                    closestTarget = target;
                    closestRange_km = range_km;
                }
            }
        }

        float detonationRange_km = 0.001f*mpDBObject->detonationRange_m;

        if (closestRange_km <= detonationRange_km)
        {
            tcKinematics targetKin = closestTarget->mcKin;
            targetKin.Extrapolate(0.25f);
            float futureRange_km = targetKin.RangeToKmAlt(this->mcKin);
            if (futureRange_km < closestRange_km)
            {
                guidanceUpdateInterval = 0.25f;
            }
            else
            {
                Detonate(0);
            }
        }
        else if (closestRange_km < 1.0f)
        {
            guidanceUpdateInterval = 1.0f + 10.0f*closestRange_km;
        }
        else
        {
            guidanceUpdateInterval = 30.0f;
        }
    }
    break;
    case tcTorpedoDBObject::BOTTOM_MINE_CAPTOR:
    {
        if (seeker == 0)
        {
            assert(false);
            return;
        }

        if (!seeker->IsActive())
        {
            seeker->SetActive(true);
            seeker->mnMode = SSMODE_SEEKERSEARCH;
        }
        tcSensorPlatform::Update(mfStatusTime);
        if (seeker->mnMode == SSMODE_SEEKERTRACK)
        {
            if (!payloadDeployed) DeployPayload();
            else SelfDestruct();
        }
    }
    break;
    default:
        assert(false);
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
    mzUnit.AssignRandomStringB();

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
tcTorpedoObject::tcTorpedoObject(tcTorpedoDBObject* obj)
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

    tcSensorPlatform::Init(obj->sonarClass.c_str(), this); // to avoid using this in initializer

    seeker = dynamic_cast<tcSonar*>(GetSensorMutable(0));
}

/**
*
*/
tcTorpedoObject::~tcTorpedoObject() 
{
}


