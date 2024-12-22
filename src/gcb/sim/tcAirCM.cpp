/**
** @file tcAirCM.cpp 
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
//#include "stdwx.h" // precompiled header file

#include "tcAirCM.h"
#include "tcCounterMeasureDBObject.h"
#include "tcPlatformDBObject.h"
#include "tcSensorMap.h"
#include "tcSimState.h"
#include "tc3DPoint.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "tcDamageModel.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

/**
* Load state from game stream
*/
tcGameStream& tcAirCM::operator<<(tcGameStream& stream)
{
	tcGameObject::operator<<(stream);

    stream >> typeCode;
    stream >> timeRemaining_s;
    stream >> vg_mps;
    stream >> vup_mps;


	return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcAirCM::operator>>(tcGameStream& stream)
{
	tcGameObject::operator>>(stream);

    stream << typeCode;
    stream << timeRemaining_s;
    stream << vg_mps;
    stream << vup_mps;

	return stream;
}


/**
* Load state from update stream
*/
tcUpdateStream& tcAirCM::operator<<(tcUpdateStream& stream)
{
    tcGameObject::operator<<(stream);

    return stream;
}

/**
* Save state to update stream
*/
tcUpdateStream& tcAirCM::operator>>(tcUpdateStream& stream)
{
    tcGameObject::operator>>(stream);

    return stream;
}

/**
* @return damage fraction for new damage, 0 means no new damage
*/
float tcAirCM::ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager)
{
    bool kill = (damage.blast_psi > 1.0f) || (damage.fragHits > 0) || (damage.kinetic_J > 0) || (damage.thermal_J_cm2 > 50.0f);

    if (kill)
    {
        ApplyGeneralDamage(1.0f, damager);
        return 1.0f;
    }
    else
    {
        return 0;
    }
}

/**
* apply movement restrictions (based on terrain height and altitude normally)
*/
void tcAirCM::ApplyRestrictions() 
{
	if (typeCode == CM_WATERFLARE)
	{
		mcKin.mfAlt_m = std::max(mcKin.mfAlt_m, 1.0f); // sit "on" water surface
	}

    // destroy on impact with ground or water, or when operational time runs out
    if ((mcKin.mfAlt_m <= 0)||(mcTerrain.mfHeight_m >= mcKin.mfAlt_m)||(timeRemaining_s <= 0)) 
    {
        mfDamageLevel = 1.0f;
    }    
}


bool tcAirCM::IsChaff() const
{
    return typeCode == CM_CHAFF;
}

bool tcAirCM::IsFlare() const
{
    return (typeCode == CM_FLARE) || (typeCode == CM_WATERFLARE);
}


/**
* Initializes state for launch from game object.
* Adds self to simulation
*
* @param obj launching game object
* @param launcher index of launcher
*/
void tcAirCM::LaunchFrom(std::shared_ptr<tcGameObject> obj, unsigned nLauncher)
{
    if (std::shared_ptr<tcPlatformObject> platObj = std::dynamic_pointer_cast<tcPlatformObject>(obj))
	{
		tc3DPoint launcherPos = platObj->mpDBObject->GetLauncherPosition(nLauncher);
		GeoPoint pos = obj->RelPosToLatLonAlt(launcherPos.x, launcherPos.y,
			launcherPos.z);
		mcKin.mfLon_rad = pos.mfLon_rad;
		mcKin.mfLat_rad = pos.mfLat_rad;
		mcKin.mfAlt_m = pos.mfAlt_m;
	}
	else
	{
		mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
		mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
		mcKin.mfAlt_m = obj->mcKin.mfAlt_m;
	}
	
    mcKin.mfPitch_rad = obj->mcKin.mfClimbAngle_rad;
	mcKin.mfClimbAngle_rad = obj->mcKin.mfClimbAngle_rad;
	mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
	mcKin.mfHeading_rad = obj->mcKin.mfHeading_rad;
    mfStatusTime = obj->mfStatusTime;
	
    timeRemaining_s = mpDBObject->lifeSpan_s;

	if (mcKin.mfAlt_m < 30.0f) mcKin.mfAlt_m = 30.0f;
    
    
    std::string s;
    if (IsChaff())
    {
        s = strutil::format("Chaff %d-%d", obj->mnID, launchedCounter++);
    }
    else if (IsFlare())
    {
        s = strutil::format("Flare %d-%d", obj->mnID, launchedCounter++);
    }
    mzUnit = s.c_str();      

	SetAlliance(obj->GetAlliance());     

    tcSimState* simState = tcSimState::Get();
    simState->AddPlatform(tcGameObject::shared_from_this());
     
}

void tcAirCM::Move(float dt_s)
{
    float heading_rad = mcKin.mfHeading_rad;

    double distance_xy_rad = C_MTORAD * vg_mps * dt_s;
    float distance_z_m = vup_mps * dt_s;

    mcKin.mfLon_rad += distance_xy_rad*(double)(sinf(heading_rad)/cosf((float)mcKin.mfLat_rad));
    mcKin.mfLat_rad += distance_xy_rad*(double)cosf(heading_rad); 
    mcKin.mfAlt_m += distance_z_m;    // use constant downward (slow) velocity for now
}

void tcAirCM::Update(double t)
{
    float dt_s = (float)(t - mfStatusTime);
    
    UpdateSpeed(dt_s);
    
    Move(dt_s);

    timeRemaining_s -= dt_s;
    
    ApplyRestrictions();

//    Update3D();
    
    mfStatusTime = t;    
}


void tcAirCM::UpdateSpeed(float dt_s)
{   
    float speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts;
    //获取与给定高度相关的相对空气密度
    float relativeAirDensity = Aero::GetRelativeAirDensity(mcKin.mfAlt_m);

    // don't apply drag for short time after launch
    //检查物体的剩余时间是否小于其生命周期减去0.5秒。这可能是为了在物体刚刚发射后的短时间内不应用阻力。
    if (timeRemaining_s < mpDBObject->lifeSpan_s - 0.5f)
    {
        //计算阻力因子，它基于相对空气密度和从数据库对象中获取的空气阻力系数
        float dragFactor = relativeAirDensity * mpDBObject->GetAirDragFactor();
        //计算由阻力产生的加速度
        float drag_accel = dragFactor * dt_s * speed_mps * speed_mps;
        drag_accel = std::min(drag_accel, 0.5f * speed_mps);
        speed_mps -= drag_accel;
    }
    
    //根据爬升角度将速度分解为水平和垂直分量
    vg_mps = cosf(mcKin.mfClimbAngle_rad) * speed_mps; // horizontal speed, speed over ground
    vup_mps = sinf(mcKin.mfClimbAngle_rad) * speed_mps;
    //垂直速度减去重力加速度乘以时间差的影响
    vup_mps -= C_G * dt_s;
    //重新计算总速度，将水平和垂直速度的平方和开方后转换为节
    mcKin.mfSpeed_kts = C_MPSTOKTS * sqrtf(vg_mps*vg_mps + vup_mps*vup_mps);
    //计算物体的俯仰角
    mcKin.mfPitch_rad = atan2f(vup_mps, vg_mps);
    //更新爬升角度为当前的俯仰
	mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
}

/**
 *
 */
tcAirCM::tcAirCM() 
  : mpDBObject(0),
    typeCode(0),
    vg_mps(0),
    vup_mps(0)
{

}


tcAirCM::tcAirCM(const tcAirCM& src) 
{
    assert(false); // not supported
}

/**
* Constructor that initializes using info from database entry.
*/
tcAirCM::tcAirCM(std::shared_ptr<tcCounterMeasureDBObject> obj)
 :  tcGameObject(obj), 
    mpDBObject(obj),
    vg_mps(0),
    vup_mps(0)
{
    if (obj->subType == "Chaff")
    {
        typeCode = CM_CHAFF;
    }
    else if (obj->subType == "Flare")
    {
        typeCode = CM_FLARE;
    }
    else if (obj->subType == "WaterFlare")
    {
        typeCode = CM_WATERFLARE;
    }
    else
    {
        typeCode = 0;
        fprintf(stderr, "tcAirCM::tcAirCM - Unrecognized subType (%s)\n",
            obj->subType.c_str());
    }
}

/**
 *
 */
tcAirCM::~tcAirCM() 
{
}

