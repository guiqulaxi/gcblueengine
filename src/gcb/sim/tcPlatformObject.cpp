/** 
**  @file tcPlatformObject.cpp
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

#include "tcAllianceSensorMap.h"
#include "tcCommPlatform.h"
#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcPlatformObject.h"
#include "tcPlatformDBObject.h"
#include "tcLauncherDBObject.h"
#include "tcMissileObject.h"
#include "tcStoresDBObject.h"
#include "tcWeaponDBObject.h"
#include "tcString.h"
#include "tcRadar.h"
#include "tcESMSensor.h"
#include "tcLauncher.h"
//#include "tc3DModel.h"
#include "tcSimState.h"
#include "tcStores.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "ai/Brain.h"
#include "tcScenarioLogger.h"
#include "tcDamageModel.h"
#include "tcScenarioRandomizer.h"
#include "tcDatabase.h"
#include "tcEventManager.h"
#include <Dense>
#include <cassert>
#include "tcGoalTracker.h"
#include "tcSensorMap.h"
using  Eigen::Vector2d;
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using namespace ai;
using namespace scriptinterface ;
/**
* Static method, call once at startup
*/
void tcPlatformObject::InitPlatformObject()
{
    Brain::InitTaskNameLookup();
}


void tcPlatformObject::DesignateDatum(tcPoint p) 
{
    float fRange_km;

    msTargetDatum.mfLon_rad=p.x;
    msTargetDatum.mfLat_rad=p.y;

    fRange_km = mcKin.RangeToKm(&msTargetDatum);
    tcString s;
    s.Format("datum is %3.1f km from platform", fRange_km);
    WTLC(s.GetBuffer());
}

void tcPlatformObject::DesignateLauncherDatum(GeoPoint p, unsigned int anLauncher) 
{
	mcLauncherState.SetLauncherDatum(anLauncher, p.mfLon_rad, p.mfLat_rad, p.mfAlt_m);
}

/**
* @return false if target cannot be designated, out of seeker coverage or no fire
* @return false control support available.
*/
bool tcPlatformObject::DesignateLauncherTarget(long anID, unsigned anLauncher) 
{
    if (std::shared_ptr<tcLauncher> launcher = mcLauncherState.GetLauncher(anLauncher))
    {
        launcher->ActivateFireControl();
    }

    return mcLauncherState.SetLauncherTarget(anLauncher, anID);
}

/**
* set AI target, also set all launcher targets. This
* may have some undesirable side effects !?
*/
void tcPlatformObject::DesignateTarget(long anID)
{
    if (anID == -1)
    {
        brain->SetTarget(-1);
        unsigned nLaunchers = mcLauncherState.GetLauncherCount();
        for (size_t n=0; n<nLaunchers; n++)
        {
            std::shared_ptr<tcLauncher> launcher = mcLauncherState.GetLauncher(n);
            if (launcher->mnCurrent == launcher->mnUncommitted) // don't wipe out previous target info if launch in progress
            {
                mcLauncherState.SetLauncherTarget(n, -1);
                mcLauncherState.SetLauncherDatum(n, 0, 0, 0);
            }
        }
        return;
    }

    tcSensorMapTrack track;
    bool trackFound = simState->GetTrack(anID, GetAlliance(), track);
    if (!trackFound)
    {
        return;
    }

    brain->SetTarget(anID);
    unsigned nLaunchers = mcLauncherState.GetLauncherCount();
    for (size_t n=0; n<nLaunchers; n++)
    {
        std::shared_ptr<tcLauncher> launcher = mcLauncherState.GetLauncher(n);
        if ((launcher->IsEffective(track)) && (!track.IsBearingOnly()))
        {
            mcLauncherState.SetLauncherTarget(n, anID);
            mcLauncherState.SetLauncherDatum(n, track.mfLon_rad, track.mfLat_rad, 0);
        }
        else
        {
            mcLauncherState.SetLauncherTarget(n, -1);
            mcLauncherState.SetLauncherDatum(n, 0, 0, 0);
        }
    }
}

/**
* Call in destructor to clean up formation references
*/
void tcPlatformObject::DestroyFormation()
{
    if (!formation.isActive) return;

    if (formation.IsLeader())
    {
    }
    else
    {
        std::shared_ptr<tcPlatformObject> leader = 
            std::dynamic_pointer_cast<tcPlatformObject>(simState->GetObject(formation.leaderId));
        if ((leader != 0) && (leader->GetAlliance() == GetAlliance()))
        {
            leader->formation.RemoveFollower(mnID);
        }

    }
}

/**
*
*/
void tcPlatformObject::UpdateAI(float t)
{
    assert(brain);

    brain->Update(t);
}

// update guidance to maintain/achieve formation position
void tcPlatformObject::UpdateFormationGuidance() 
{
    formation.Update(std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));
}

/**
* turn by maximum amount toward goal heading
* 这段代码的目标是使一个平台的朝向逐渐接近其目标朝向，
* 同时考虑了转向速率、伤害和时间差的影响。
* 它还提供了一种平滑朝向变化率变化的方法，以确保平台平滑地改变其朝向
*/
void tcPlatformObject::UpdateHeading(float dt_s) 
{
    float dh_rad = mcGS.mfGoalHeading_rad - mcKin.mfHeading_rad;
    radtoplusminuspi(dh_rad); // map dh_deg to [-180,180]
    float absdh_rad = fabsf(dh_rad);//当前朝向与目标朝向差值

    if (absdh_rad < 0.0001f)
    {
        mcKin.mfHeading_rad = mcGS.mfGoalHeading_rad;
        mcKin.mfYaw_rad = mcKin.mfHeading_rad;
        reducedTurnRate_degps = 360.0f; // clear slow turn
        return;
    }


    float effectiveTurnRate_degps = std::min(reducedTurnRate_degps, mpDBObject->mfTurnRate_degps);

    float dh_max = C_PIOVER180*effectiveTurnRate_degps*dt_s;//计算在给定的时间差内，最大允许的朝向变化量
    if (mfDamageLevel > 0.2f)
    {
        dh_max *= 0.5f;
    }
    // linearly reduce turn rate near goal

    const float dh_thresh = 10.0f*C_PIOVER180;
    const float k_dh = 1.0f/dh_thresh;
    if (absdh_rad < dh_thresh)//当前朝向与目标朝向差值如果小于10度
    {
        dh_max *= absdh_rad*k_dh;
    }

    float dh_min = -dh_max;
    if (dh_rad < dh_min) {dh_rad = dh_min;} // restrict to turn rate
    else if (dh_rad > dh_max) {dh_rad = dh_max;}
    
    
    // simple way to smooth heading rate changes when not near goal
    if (absdh_rad > dh_thresh) 
    {
        float ddh_rad = dh_rad - lastHeadingDelta;
        const float ddh_max = 0.0002f;
        if (ddh_rad < -ddh_max) dh_rad = lastHeadingDelta - ddh_max;
        else if (ddh_rad > ddh_max) dh_rad = lastHeadingDelta + ddh_max;
    }

    lastHeadingDelta = dh_rad;

    mcKin.mfHeading_rad += dh_rad;
    if (mcKin.mfHeading_rad >= C_TWOPI) {mcKin.mfHeading_rad -= C_TWOPI;}
    if (mcKin.mfHeading_rad < 0) {mcKin.mfHeading_rad += C_TWOPI;}

	mcKin.mfYaw_rad = mcKin.mfHeading_rad;
}

/**
* Adjust speed to goal speed, limited by max acceleration
* Also updates fuel state (setting fuel capacity to 0 in db gives infinite fuel)
*/
void tcPlatformObject::UpdateSpeed(float dt_s) 
{
    float ds_kts = mcGS.mfGoalSpeed_kts - mcKin.mfSpeed_kts;
    float ds_max = mpDBObject->mfAccel_ktsps*dt_s;
    float ds_min = -ds_max;

    if (ds_kts < ds_min) {ds_kts = ds_min;} // restrict to acceleration
    else if (ds_kts > ds_max) {ds_kts = ds_max;}
    mcKin.mfSpeed_kts += ds_kts;

	if (mcKin.mfSpeed_kts < 0) mcKin.mfSpeed_kts = 0;

	// if a fuel capacity is indicated then update fuel consumption
	if (!mpDBObject->HasInfiniteFuel())
	{
		fuel_kg -= dt_s * mpDBObject->GetFuelConsumptionConstant(mcKin.mfSpeed_kts) * mcKin.mfSpeed_kts;
		if (fuel_kg < 0) fuel_kg = 0;

		if (fuel_kg == 0)
		{
			if (mcKin.mfSpeed_kts > 0) mcKin.mfSpeed_kts -= 2*ds_max;
			if (mcKin.mfAlt_m > 0) mcKin.mfAlt_m -= dt_s * 10;
		}
	}
}

/**
* apply movement restrictions (based on terrain height and altitude normally)
*/
void tcPlatformObject::ApplyRestrictions() 
{
}

void tcPlatformObject::Move(float dt_s) 
{
    float fHeading_rad = mcKin.mfHeading_rad;
    float fGroundSpeed_kts = cosf(mcKin.mfClimbAngle_rad)*mcKin.mfSpeed_kts;
    double fDistance_rad = fGroundSpeed_kts*dt_s*(float)C_KTSTORADPS;

    mcKin.mfLon_rad += fDistance_rad*(double)(sinf(fHeading_rad)/cosf((float)mcKin.mfLat_rad));
    mcKin.mfLat_rad += (double)cosf(fHeading_rad)*fDistance_rad; 
    mcKin.mfAlt_m += sinf(mcKin.mfClimbAngle_rad)*mcKin.mfSpeed_kts*C_KTSTOMPS*dt_s;

    float wrapLow = float(mcKin.mfLon_rad < -C_PI);
    float wrapHigh = float(mcKin.mfLon_rad >= C_PI);

    mcKin.mfLon_rad += (wrapLow - wrapHigh) * C_TWOPI;

    // check for pole crossing
    if (fabsf(mcKin.mfLat_rad) >= C_PIOVER2)
    {
        if (mcKin.mfLat_rad >= C_PIOVER2)
        {
            mcKin.mfLat_rad = C_PI - mcKin.mfLat_rad;
        }
        else
        {
            mcKin.mfLat_rad = -C_PI - mcKin.mfLat_rad;
        }
        mcKin.mfHeading_rad = C_PI - mcKin.mfHeading_rad;
        mcGS.mfGoalHeading_rad = C_PI - mcGS.mfGoalHeading_rad;
    }

    assert((mcKin.mfLon_rad >= -C_PI) && (mcKin.mfLon_rad < C_PI));
    assert((mcKin.mfLat_rad >= -C_PIOVER2) && (mcKin.mfLat_rad <= C_PIOVER2));
	assert(!_isnan(mcKin.mfRoll_rad));
	assert(!_isnan(mcKin.mfPitch_rad));
}



/**
* update launcher state (reload time) 
*/
void tcPlatformObject::UpdateLauncherState(float dt_s) 
{
    mcLauncherState.Update(dt_s);
}

/** 
* update platform magazines 
*/
void tcPlatformObject::UpdateMagazines(double t)
{
    if (clientMode) return; // no magazine update for client
    size_t nMagazines = magazines.size();
    for (size_t n=0; n<nMagazines; n++)
    {
        std::shared_ptr<tcStores> mag = magazines[n];
        assert(mag);
        mag->Update(t);
    }
}

/** 
* update platform sensors 
*/
void tcPlatformObject::UpdateSensors(double t)
{
    if (clientMode) return; // no sensor update for client
    GetComponent<tcSensorPlatform>()->Update(t);
}
 void tcPlatformObject::UpdateComms(double t)
{
     if (clientMode) return; // no sensor update for client
     GetComponent<tcCommPlatform>()->Update(t);
}

void tcPlatformObject::Update(double afStatusTime) 
{
    float dt_s = (float)(afStatusTime - mfStatusTime);

    //UpdateEffects();

    if (parent != NULL) {return;} // captive, let parent update if applicable
    if (mpDBObject == NULL) {return;}
    

	/* In multiplayer mode, skip command based updates for client objects not controlled
	** by client. This will cause object to jump more but avoids having to broadcast command
	** changes to all alliance clients. The controller of the object will see smoother
	** behavior.
	*/
	if (!IsClientMode() || IsControlled())
	{
        UpdateFormationGuidance(); // formation heading/speed calculation

		UpdateHeading(dt_s);

		UpdateSpeed(dt_s);

		UpdateClimb(dt_s);

		ApplyRestrictions();
	}

    Move(dt_s);

    UpdateLauncherState(dt_s);

    UpdateSensors(afStatusTime);

    UpdateComms(afStatusTime);

    UpdateMagazines(afStatusTime);

    UpdateAI(afStatusTime);

    //Update3D();

    mfStatusTime = afStatusTime;
}

/**
* @return pointer to platform's "brain" (AI)
*/
std::shared_ptr<Brain>  tcPlatformObject::GetBrain()
{
    return brain;
}

long tcPlatformObject::GetFormationLeader() const
{
    return formation.leaderId;
}

/**
* @return fuel capacity in kg including external fuel tanks
*/
float tcPlatformObject::GetFuelCapacity() const
{
	return (mpDBObject->GetInternalFuelCapacity() + externalFuelCapacity_kg);
}

/**
* @return pointer to launcher with index of <idx> or NULL (0) for error
*/
std::shared_ptr<tcLauncher> tcPlatformObject::GetLauncher(unsigned idx)
{
    return mcLauncherState.GetLauncher(idx);
}

std::shared_ptr<const tcLauncher> tcPlatformObject::GetLauncher(unsigned idx) const
{
    return mcLauncherState.GetLauncher(idx);
}

unsigned int tcPlatformObject::GetLauncherCount() const
{
    return mcLauncherState.GetLauncherCount();
}

/**
* @return description of launchers for display
*/
std::string tcPlatformObject::GetLauncherDescription()
{
	static std::string errorString = "Error";
	std::string description;

	unsigned nLaunchers = mcLauncherState.GetLauncherCount();
	for (unsigned n=0; n < nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);

		const char* childClassName = (launcher->mpChildDBObj != 0) ? launcher->mpChildDBObj->mzClass.c_str() :
		                 errorString.c_str();

		description += strutil::format("%s, %d x %s\n",
			launcher->mpLauncherDBObj->mzClass.c_str(),
			launcher->mnCurrent,
			childClassName);
	}

	if (nLaunchers == 0)
	{
		description = "No weapons\n";
	}

	return description;
}


/**
*
*/
int tcPlatformObject::GetLauncherQuantity(unsigned anLauncher) 
{
    return mcLauncherState.GetLauncherQuantity(anLauncher);
}

/**
* Intended to allow scenario edit to save loadout state in compact format
*/
const std::string& tcPlatformObject::GetLoadoutCommand() const
{
    static std::string result;

    std::string s;

    unsigned int nLaunchers = mcLauncherState.GetLauncherCount();
    for (unsigned int n=0; n<nLaunchers; n++)
    {
        std::string item = mcLauncherState.GetLauncherChildClass(n);
        int qty = mcLauncherState.GetLauncherQuantity(n);
        s += strutil::format("%d %s;", qty, item.c_str());
    }

    result = s.c_str();
    
    return result;
}

/**
* This version instantly sets the platform to use the specified
* loadout items and quantities. Should only be used for edit mode,
* loading scenarios, and testing.
*/
void tcPlatformObject::SetLoadoutCommand(const std::string& s)
{
    std::vector<std::string> item;
    std::vector<unsigned int> quantity;
    ParseLoadoutCommand(s, item, quantity);

    unsigned int nLaunchers = mcLauncherState.GetLauncherCount();
    for (unsigned int launcherIdx=0; 
        (launcherIdx<item.size()) && (launcherIdx < nLaunchers); launcherIdx++)
    {
        std::shared_ptr<tcLauncher> launcher = mcLauncherState.GetLauncher(launcherIdx);
        assert(launcher != 0);

        if (quantity[launcherIdx] > 0)
        {
            launcher->SetChildClass(item[launcherIdx].c_str());
            if (launcher->mpChildDBObj != 0)
            {
                launcher->SetChildQuantity(quantity[launcherIdx]);
            }
            else
            {
				fprintf(stderr, "tcPlatformObject::SetLoadoutCommand - bad item (%s)\n", item[launcherIdx].c_str());
                launcher->SetChildQuantity(0);
            }
        }
        else
        {
            launcher->SetChildClass("");
            launcher->SetChildQuantity(0);
        }
    }
}

/**
* This version schedules platform to load specified items from host
* parent. Can be used during normal simulation.
*/
void tcPlatformObject::ScheduleLoadoutCommand(const std::string& s)
{
    std::vector<std::string> item;
    std::vector<unsigned int> quantity;
    ParseLoadoutCommand(s, item, quantity);

    std::shared_ptr<tcPlatformObject> parentPlatform = std::dynamic_pointer_cast<tcPlatformObject>(parent);
    if (parentPlatform == 0)
    {
        fprintf(stderr, "tcPlatformObject::ScheduleLoadoutCommand - no host platform (%s)\n", 
            GetName());
        assert(false);
        return; // not landed or docked, or parent is not tcPlatformObject
    }


    unsigned int nLaunchers = mcLauncherState.GetLauncherCount();
    for (unsigned int launcherIdx=0; 
        (launcherIdx<item.size()) && (launcherIdx < nLaunchers); launcherIdx++)
    {
        std::shared_ptr<tcLauncher> launcher = mcLauncherState.GetLauncher(launcherIdx);
        assert(launcher != 0);

        if (quantity[launcherIdx] > 0)
        {
            size_t nMagazines = parentPlatform->GetMagazineCount();
            for (size_t n=0; n<nMagazines; n++)
            {
                std::shared_ptr<tcStores> mag = parentPlatform->GetMagazine(n);
                bool result = mag->LoadLauncher(launcherIdx, item[launcherIdx], tcGameObject::shared_from_this(), quantity[launcherIdx]);
            }
        }
    }
}


void tcPlatformObject::ParseLoadoutCommand(const std::string& cmd, 
                                           std::vector<std::string>& item, std::vector<unsigned int>& quantity)
{
    item.clear();
    quantity.clear();

    std::string s2(cmd.c_str());

    bool parsing = true;
    unsigned int launcherIdx = 0;
    auto itemtxts=strutil::split(s2,';');
    for(auto itemtxt :itemtxts)
    {
        if(itemtxt.length()==0) continue;
        auto texts=strutil::split(itemtxt,' ');
        std::string qtyText =texts[0];
        std::string itemText =texts[1];
        for(size_t i=2;i<texts.size();i++)
        {
         itemText+=(" "+texts[i]);
        }
        item.push_back(std::string(itemText.c_str()));
        try {
            quantity.push_back(std::stoul(qtyText));
        } catch (...) {

        }


    }

//    while (parsing && (launcherIdx < mcLauncherState.GetLauncherCount()))
//    {
//        std::string loadout = s2.BeforeFirst(';');
//        s2 = s2.AfterFirst(';');

//        std::string qtyText = loadout.BeforeFirst(' ');

//        std::string itemText = loadout.AfterFirst(' ');
//        itemText.Trim(true); // remove spaces at beginning and end
//        itemText.Trim(false);
        
//        unsigned long qty = 0;
//        if (qtyText.ToULong(&qty, 10))
//        {
//            item.push_back(std::string(itemText.c_str()));
//            quantity.push_back((unsigned int)(qty));
//        }

//        parsing = (s2.size() > 0);
//        launcherIdx++;
//    }
}


const std::string& tcPlatformObject::GetLoadoutTag() const
{
	return loadoutTag;
}


void tcPlatformObject::SetLoadoutTag(const std::string& s)
{
	loadoutTag = s;
}

void tcPlatformObject::SetMaxTurnRate(float rate_degps)
{
    reducedTurnRate_degps = rate_degps;
}

/**
* @return true if platform is intercepting (has targeted) track with id
*/
bool tcPlatformObject::IsInterceptingTrack(long id)
{
    assert(id >= 0);

    return brain->GetTarget() == id;
}

/**
* Called when new general damage occurs. 
* @param damage fractional amount of new damage
*/
void tcPlatformObject::ApplyGeneralDamage(float damage, std::shared_ptr<tcGameObject> damager)
{
    float priorDamage = mfDamageLevel;
    mfDamageLevel += damage;
    mfDamageLevel = std::min(mfDamageLevel, 1.0f);

    UpdateScoreForDamage(damager, priorDamage);

    float scaledDamage = (mfDamageLevel <= 0.5f) ? (0.4f * damage) : damage;

    unsigned int nLaunchers = GetLauncherCount();
    for (unsigned int m=0; m<nLaunchers; m++)
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(m);
        assert(launcher);
        
        if ( !launcher->IsDamaged() && (randf() <= scaledDamage))
        {
            launcher->SetDamaged(true);
            launcher->UpdateScoreForDamage(damager);
        }
    }

    // higher probability of sensor damage
    scaledDamage = (mfDamageLevel <= 0.5f) ? (0.6f * damage) : damage;

    unsigned int nSensors = GetComponent<tcSensorPlatform>()->GetSensorCount();
    for (unsigned int n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState> sensor = GetComponent<tcSensorPlatform>()->GetSensorMutable(n);
        assert(sensor);

        if ( !sensor->IsDamaged() && (randf() <= scaledDamage))
        {
            sensor->SetDamaged(true);
        }
    }

    if (damage > 0)
    {
        tcEventManager::Get()->DamageReceived(GetAlliance());
    }
}



/**
* @return damage fraction for new damage, 0 means no new damage
*/
float tcPlatformObject::ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager)
{
    // 初始化各种伤害类型为0
    float impactDamage = 0; // 撞击伤害
    float internalDamage = 0; // 内部伤害
    float blastDamage = 0; // 爆炸伤害
    float waterBlastDamage = 0; // 水下爆炸伤害
    float thermalDamage = 0; // 热辐射伤害
    float fragDamage = 0; // 破片伤害

    // 如果当前对象已经严重损坏（mfDamageLevel >= 1），则不再接受新伤害
    if (mfDamageLevel >= 1) return 0;

    // 记录应用伤害前的损坏程度
    float priorDamage = mfDamageLevel;

    // 从数据库中获取当前对象的伤害效果数据
    const database::tcDamageEffect* damageEffect =
        database->GetDamageEffectData(mpDBObject->damageEffect);

    // 如果没有找到伤害效果数据，输出错误信息并断言失败
    if (damageEffect == 0)
    {
        fprintf(stderr, "tcPlatformObject::ApplyAdvancedDamage -- NULL damageEffect for %s\n",
                mzClass.c_str());
        assert(false);
        return 0;
    }

    // 根据动能计算撞击伤害
    impactDamage = damageEffect->GetFragmentDamageFactor(damage.kinetic_J);
    // 如果伤害类型为穿透且撞击伤害大于一定值或攻击者在水下，则计算内部伤害
    if (damage.isPenetration && ((impactDamage > 0.002f) || damager->mcKin.mfAlt_m < -1.0f))
    {
        internalDamage = damageEffect->GetInternalDamageFactor(damage.explosive_kg);
    }
    // 根据爆炸压力计算爆炸伤害
    blastDamage = damageEffect->GetBlastDamageFactor(damage.blast_psi);
    // 根据水下爆炸压力计算水下爆炸伤害
    waterBlastDamage = damageEffect->GetWaterBlastDamageFactor(damage.waterBlast_psi);
    // 根据热辐射能量计算热辐射伤害
    thermalDamage = damageEffect->GetRadiationDamageFactor(damage.thermal_J_cm2);

    // 如果破片命中数大于0，则根据破片能量计算破片伤害
    if (damage.fragHits > 0)
    {
        float hitsFactor = 1.0f + log10f(float(damage.fragHits)); // 计算命中因子
        fragDamage = hitsFactor * damageEffect->GetFragmentDamageFactor(damage.fragEnergy_J);
    }

    // 计算累计伤害
    float cumulativeDamage = impactDamage + internalDamage + blastDamage + waterBlastDamage + thermalDamage + fragDamage;

    std::string damageDescription; // 用于记录伤害类型的字符串
    float newDamage = 0; // 新增伤害值

    // 如果累计伤害大于0，则进行后续处理
    if (cumulativeDamage > 0)
    {
        // 根据不同的伤害类型，在damageDescription字符串中添加相应的标记
        if (impactDamage > 0) damageDescription.append("K");
        if (internalDamage > 0) damageDescription.append("X");
        if (blastDamage > 0) damageDescription.append("B");
        if (waterBlastDamage > 0) damageDescription.append("U");
        if (thermalDamage > 0) damageDescription.append("T");
        if (fragDamage > 0) damageDescription.append("F");

        // 根据高斯分布生成一个随机数，用于调整实际伤害值
        float rand_val = GaussianRandom::Get()->randn_fast();
        rand_val = 0.642f * fabsf(rand_val) + 0.05f; // 调整随机数的范围和分布
        newDamage = rand_val * cumulativeDamage;

        // 更新当前对象的损坏程度
        mfDamageLevel += newDamage;

        // 确保损坏程度不超过1
        mfDamageLevel = std::min(mfDamageLevel, 1.0f);

        // 根据伤害值更新分数
        UpdateScoreForDamage(damager, priorDamage);

        // 应用伤害对发射器的影响
        ApplyLauncherDamage(newDamage, damager);
    }

    // 检查并处理传感器伤害
    bool sensorDamage = GetComponent<tcSensorPlatform>()->ApplyAdvancedDamage(damage, damager, newDamage);
    if (sensorDamage)
    {
        damageDescription.append("S"); // 在伤害描述中添加传感器伤害标记
        newDamage += 0.0001f; // 确保报告有新的伤害
    }

    // 设置最后的伤害描述
    SetLastDamageDescription(damageDescription);

    // 如果新增伤害大于0，则通知事件管理器对象受到了伤害
    if (newDamage > 0)
    {
        tcEventManager::Get()->DamageReceived(GetAlliance());
    }

    // 返回新增伤害值
    return newDamage;
}

/**
* Checks each launcher for failure when new damage occurs
*/
void tcPlatformObject::ApplyLauncherDamage(float damage, std::shared_ptr<tcGameObject> damager)
{
    float scaledDamage = (mfDamageLevel <= 0.5f) ? (0.4f * damage) : damage;

    unsigned int nLaunchers = GetLauncherCount();
    for (unsigned int m=0; m<nLaunchers; m++)
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(m);
        assert(launcher);
        
        if ( !launcher->IsDamaged() && (randf() <= scaledDamage))
        {
            launcher->SetDamaged(true);
            launcher->UpdateScoreForDamage(damager);
        }
    }
}




/**
* Called when repairs remove damage. Launchers, sensors, etc.
* are tested for fix.
* @param fractional amount of new repairs
*/
void tcPlatformObject::ApplyRepairs(float repair)
{
    mfDamageLevel -= repair;
    if (mfDamageLevel <= 0) mfDamageLevel = 0;

    float scaledRepairs = (mfDamageLevel <= 0.5f) ? repair : (0.5f * repair);

    unsigned int nLaunchers = GetLauncherCount();
    for (unsigned int m=0; m<nLaunchers; m++)
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(m);
        assert(launcher);
        
        if (launcher->IsDamaged() && (randf() <= scaledRepairs))
        {
            launcher->SetDamaged(false);
        }
    }

    unsigned int nSensors = GetComponent<tcSensorPlatform>()->GetSensorCount();
    for (unsigned int n=0; n<nSensors; n++)
    {
        std::shared_ptr<tcSensorState> sensor = GetComponent<tcSensorPlatform>()->GetSensorMutable(n);
        assert(sensor);
        
        if (sensor->IsDamaged() && (randf() <= scaledRepairs))
        {
            sensor->SetDamaged(false);
        }
    }

}

/**
* Automatically configure platform magazine contents and air complement
* If setupName is empty, then use first setup with valid date range
* Clear magazines and aircraft before autoconfiguring if setupName is valid
*/
void tcPlatformObject::AutoConfigurePlatform(const std::string& setupName)
{
    std::vector<database::AirComplement> airComplement;
    std::vector<database::MagazineLoadout> magazineLoadout;
    std::vector<database::LauncherLoadout> launcherLoadout;

    GetAutoConfigurationData(setupName, airComplement, magazineLoadout, launcherLoadout);

    AutoConfigureMagazines(magazineLoadout);
    AutoConfigureLaunchers(launcherLoadout);
}

void tcPlatformObject::AutoConfigureLaunchers(const std::vector<database::LauncherLoadout>& launcherLoadout)
{
    if (launcherLoadout.size() == 0)
    {
        return;
    }

    // clear all launchers
    size_t nLaunchers = (size_t)GetLauncherCount();
    for (size_t n=0; n<nLaunchers; n++)
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
        launcher->SetChildQuantity(0);
    }

    for (size_t k=0; k<launcherLoadout.size(); k++)
    {
        if (std::shared_ptr<tcLauncher> launcher = GetLauncherById(launcherLoadout[k].launcherId))
        {
            launcher->SetChildClass(launcherLoadout[k].item);
            launcher->SetChildQuantity(launcherLoadout[k].quantity);
        }
        else
        {
            assert(false); // invalid launcher id
        }
    }
}


void tcPlatformObject::AutoConfigureMagazines(const std::vector<database::MagazineLoadout>& magazineLoadout)
{
    if (magazineLoadout.size() == 0)
    {
        return;
    }

    // clear all magazines
    size_t nMagazines = GetMagazineCount();
    for (size_t n=0; n<nMagazines; n++)
    {
        std::shared_ptr<tcStores> stores = GetMagazine(n);
        stores->RemoveAllItems();
    }

    for (size_t k=0; k<magazineLoadout.size(); k++)
    {
        if (std::shared_ptr<tcStores> stores = GetMagazineById(magazineLoadout[k].magazineId))
        {
            stores->AddItems(magazineLoadout[k].item, (unsigned long)magazineLoadout[k].quantity);
        }
        else
        {
            assert(false); // invalid magazine id
        }
    }
}

void tcPlatformObject::GetAutoConfigurationData(const std::string& setupName, 
        std::vector<database::AirComplement>& airComplement, std::vector<database::MagazineLoadout>& magazineLoadout,
        std::vector<database::LauncherLoadout>& launcherLoadout)
{
    std::string databaseClass = mpDBObject->mzClass.c_str();

    std::string selectedSetup = setupName;
    if (selectedSetup.size() == 0)
    {
        tcDateTime current = simState->GetDateTime();
        float currentYear = float(current.GetYear()) + (1.0f/12.0f)*(float(current.GetMonth()) - 0.5f);

        std::vector<std::string> platformSetups;
        bool valid = database->FindPlatformSetups(databaseClass, currentYear, platformSetups);
        if (valid && (platformSetups.size() > 0))
        {
            selectedSetup = platformSetups[0];
        }
        if (!valid) return;
    }
    
    database->GetPlatformSetupData(databaseClass, selectedSetup, airComplement, magazineLoadout, launcherLoadout);
}


void tcPlatformObject::Clear()  
{  
    tcGameObject::Clear();
    
    formation.Clear();

//    mcAI.ClearOrders();
    fuel_kg = 0;
    lastHeadingDelta = 0;

    reducedTurnRate_degps = 360.0f;
}

/**
*
*/
unsigned int tcPlatformObject::GetMagazineCount() const
{
    return (unsigned int)magazines.size();
}

/**
*
*/
std::shared_ptr<tcStores> tcPlatformObject::GetMagazine(unsigned int idx)
{
    if (idx >= magazines.size()) return 0;
    else return magazines[idx];
}

const std::shared_ptr<tcStores> tcPlatformObject::GetMagazineConst(unsigned int idx) const
{
    if (idx >= magazines.size()) return 0;
    else return magazines[idx];
}

std::shared_ptr<tcStores> tcPlatformObject::GetMagazineById(unsigned int id)
{
    if (magazines.size() != mpDBObject->magazineId.size())
    {
        assert(false); // had an invalid magazine reference in db?
        return 0;
    }

    for (size_t n=0; n<mpDBObject->magazineId.size(); n++)
    {
        if (mpDBObject->magazineId[n] == id)
        {
            return magazines[n];
        }
    }

    return 0;
}

std::shared_ptr<tcLauncher> tcPlatformObject::GetLauncherById(unsigned int id)
{
    if (mcLauncherState.mnCount != mpDBObject->launcherId.size())
    {
        assert(false); // had an invalid launcher reference in db?
        return 0;
    }

    for (size_t n=0; n<mpDBObject->launcherId.size(); n++)
    {
        if (mpDBObject->launcherId[n] == id)
        {
            return mcLauncherState.GetLauncher(n);
        }
    }

    return 0;
}


/**
* @return quantity of item available in all magazines on platform
*/
unsigned int tcPlatformObject::GetMagazineQuantity(const std::string& item)
{
    std::string s;
    unsigned int quantity = 0;
    size_t nMagazines = magazines.size();
    for (size_t n=0; n<nMagazines; n++)
    {
        quantity += magazines[n]->CurrentItemQuantity(item, s);
    }

    return quantity;
}

float tcPlatformObject::GetMaxTurnRate() const
{
    return reducedTurnRate_degps;
}

/**
* @return true if either currently equipped for target type or
* parent magazines have compatible weapons in stock for target type
*/
bool tcPlatformObject::IsCapableVsTargetType(int targetFlag)
{
	if (IsEquippedForTargetType(targetFlag)) return true;

	std::shared_ptr<tcPlatformObject> parentPlatform = std::dynamic_pointer_cast<tcPlatformObject>(parent);
	if (parentPlatform == 0) return false; // not landed or docked, or parent is not tcPlatformObject

	size_t nMagazines = parentPlatform->GetMagazineCount();
	for (size_t n=0; n<nMagazines; n++)
	{
        std::shared_ptr<tcStores> mag = parentPlatform->GetMagazine(n);
        int magFlags = mag->GetAvailableTargetFlags(tcGameObject::shared_from_this());
		if ((magFlags & targetFlag) != 0) return true;
	}

	return false;
}

void tcPlatformObject::AdjustExternalFuelCapacity(float change_kg)
{
	externalFuelCapacity_kg += change_kg;
	
	if (externalFuelCapacity_kg < 0)
	{
		assert(externalFuelCapacity_kg >= -0.1f); // allow for some rounding error here
		externalFuelCapacity_kg = 0;
	}

	float adjustedCapacity_kg = GetFuelCapacity();
	if (fuel_kg > adjustedCapacity_kg) fuel_kg = adjustedCapacity_kg;
	
}


/**
* @return true if all launchers empty and not loading
*/
bool tcPlatformObject::AllLaunchersEmpty()
{
	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		if ((launcher->IsLoading()) || (launcher->mnCurrent > 0)) return false;
	}

	return true;
}

/**
* @return true if all launchers full and not loading
*/
bool tcPlatformObject::AllLaunchersFull()
{
	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		//if ((launcher->IsLoading()) || (launcher->mnCurrent < launcher->capacity)) return false;
        if ((launcher->IsLoading()) || (launcher->mnCurrent == 0)) return false;
	}

	return true;
}

/**
* @return true if all launchers not loading
*/
bool tcPlatformObject::AllLaunchersReady()
{
	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		//if ((launcher->IsLoading()) || (launcher->mnCurrent < launcher->capacity)) return false;
        if (launcher->IsLoading()) return false;
	}

	return true;
}


/**
* @return true if fully equipped, done loading, and at least one 
* launcher is effective vs. target type
*/
bool tcPlatformObject::IsEquippedForTargetType(int targetFlag)
{
	if (targetFlag == 0) return false; // don't call this to check empty

    if ((targetFlag & AEW_TARGET) != 0)
    {
        size_t nSensors = (size_t)GetComponent<tcSensorPlatform>()->GetSensorCount();

        for (size_t n=0; n<nSensors; n++)
        {
            std::shared_ptr<const tcRadar> radar =  std::dynamic_pointer_cast<const tcRadar>(GetComponent<tcSensorPlatform>()->GetSensor(n));
            if ((radar != 0) && 
                (radar->mpDBObj->isSurveillance) && 
                (radar->mpDBObj->mfFieldOfView_deg >= 360))
            {
                return true;
            }
        }
        return false;
    }

	bool anyEffective = false;

	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		if (launcher->IsLoading() || (launcher->mnCurrent == 0)) // 30MAY2011 changed to allow undercapacity, no particular reason, just seems too restrictive with weight limits
        {
            return false;
        }
		anyEffective = anyEffective || ((launcher->mnTargetFlags & targetFlag) != 0);
	}

	return anyEffective;
}

/**
* @return true if fully equipped, done loading, and at least one launcher is effective vs. target type
*/
bool tcPlatformObject::RatingForTargetType(int targetFlag, float& weaponWeight_kg, float& maxRange_km)
{
	if (targetFlag == 0) return false; // don't call this to check empty

    if ((targetFlag & AEW_TARGET) != 0)
    {
        return RatingForTargetTypeAEW(weaponWeight_kg, maxRange_km);
    }

	bool anyEffective = false;
	bool stillLoading = false;
	weaponWeight_kg = 0;
	maxRange_km = 0;

	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		stillLoading = stillLoading || launcher->IsLoading();
		
		if (((launcher->mnTargetFlags & targetFlag) != 0) && (launcher->mnCurrent > 0))
		{
			anyEffective = true;
			weaponWeight_kg += float(launcher->mnCurrent) * launcher->GetItemWeight();
            std::shared_ptr<tcWeaponDBObject> weaponData =  std::dynamic_pointer_cast<tcWeaponDBObject>(launcher->GetChildDatabaseObject());
			if (weaponData != 0)
			{
				maxRange_km = std::max(weaponData->maxRange_km, maxRange_km);
			}
			else
			{
				assert(false);
			}
		}

		
	}

	return anyEffective && !stillLoading;
}

/**
* Version "work-around" to support AEW missions
* @maxRange_km max ref range of search radar
* @return true if fully equipped, done loading, and at least one launcher is effective vs. target type
*/
bool tcPlatformObject::RatingForTargetTypeAEW(float& weaponWeight_kg, float& maxRange_km)
{
	bool anyEffective = false;
	weaponWeight_kg = 0;
	maxRange_km = 0;
    const float minRefRange_km = 25.0f;
    const float minMaxRange_km = 100.0f;

    size_t nSensors = (size_t)GetComponent<tcSensorPlatform>()->GetSensorCount();

	for (size_t n=0; n<nSensors; n++)
	{
        std::shared_ptr<const tcRadar> radar =  std::dynamic_pointer_cast<const tcRadar>(GetComponent<tcSensorPlatform>()->GetSensor(n));
        if ((radar != 0) && (!radar->IsDamaged()) && 
            (radar->mpDBObj->mfFieldOfView_deg >= 360) &&
            (radar->mpDBObj->isSurveillance) &&
            (radar->mpDBObj->mfRefRange_km >= minRefRange_km) && 
            (radar->mpDBObj->mfMaxRange_km >= minMaxRange_km))
        {
            anyEffective = true;
            maxRange_km = std::max(maxRange_km, radar->mpDBObj->mfRefRange_km);
        }
	}

	return anyEffective;
}


/**
* @return true if fully equipped, done loading, and at least one 
* launcher is effective vs. target type and has at least one nuclear weapon
*/
bool tcPlatformObject::IsEquippedWithNuclear(int targetFlag)
{
	if (targetFlag == 0) return false; // don't call this to check empty

	bool anyEffective = false;

	size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);
		if (launcher->IsLoading() || (launcher->mnCurrent == 0) || 
            (launcher->capacity > launcher->mnCurrent))
        {
            return false;
        }

		anyEffective = anyEffective || 
            (launcher->IsLoadedNuclear() && ((launcher->mnTargetFlags & targetFlag) != 0));
	}

	return anyEffective;
}


/**
* @return true if any launchers are loading or unloading
*/
bool tcPlatformObject::IsLoading() const
{
    size_t nLaunchers = GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<const tcLauncher> launcher = GetLauncher(n);
		if (launcher->IsLoading()) return true;
	}

    return false;
}



void tcPlatformObject::UnloadAllLaunchers()
{
	std::shared_ptr<tcPlatformObject> parentPlatform = std::dynamic_pointer_cast<tcPlatformObject>(parent);
	if (parentPlatform == 0)
	{
		fprintf(stderr, "tcPlatformObject::UnloadAllLaunchers - no host platform (%s)\n", 
			GetName());
		assert(false);
		return; // not landed or docked, or parent is not tcPlatformObject
	}
    
    // check if anything loaded
	size_t nLaunchers = GetLauncherCount();
    bool anyLoaded = false;
	for (size_t n=0; (n<nLaunchers)&&(!anyLoaded); n++)
	{
		std::shared_ptr<tcLauncher> launcher = GetLauncher(n);    
		assert(launcher);

        anyLoaded = anyLoaded || (launcher->mnCurrent > 0);
    }
    if (!anyLoaded)
    {
        SetLoadoutTag("");
        return; // already empty
    }

	size_t nMagazines = parentPlatform->GetMagazineCount();
	for (size_t n=0; n<nMagazines; n++)
	{
        std::shared_ptr<tcStores> mag = parentPlatform->GetMagazine(n);
        if (mag->CanUnloadThisObject(tcGameObject::shared_from_this()))
		{
            mag->AddAutomationOp("Empty", tcGameObject::shared_from_this()); // all equip for platform has to be in one magazine
			return;
		}
	}

	fprintf(stderr, "tcPlatformObject::EquipForTargetType('empty') - no mags available (%s)\n", 
		GetName());
	assert(false);
}

/**
* @param targetType "Empty" "AAW" "ASuW" "ASW" "Strike"
*/
void tcPlatformObject::EquipForTargetType(const std::string& targetType)
{
	if (targetType == "Empty")
	{
		UnloadAllLaunchers();
		return;
	}

	std::shared_ptr<tcPlatformObject> parentPlatform = std::dynamic_pointer_cast<tcPlatformObject>(parent);
	if (parentPlatform == 0)
	{
		fprintf(stderr, "tcPlatformObject::EquipForTargetType - no host platform (%s)\n", 
			GetName());
		assert(false);
		return; // not landed or docked, or parent is not tcPlatformObject
	}

    bool useNuclear = false;

	int targetFlag = 0;
	if (targetType == "AAW") targetFlag = AIR_TARGET;
	else if (targetType == "ASuW") targetFlag = SURFACE_TARGET;
	else if (targetType == "ASW") targetFlag = SUBSURFACE_TARGET;
	else if (targetType == "Strike") targetFlag = LAND_TARGET;
    else if (targetType == "Nuclear")
    {
        targetFlag = AIR_TARGET | SURFACE_TARGET | LAND_TARGET;
        useNuclear = true;
    }
	else 
	{
		fprintf(stderr, "tcPlatformObject::EquipForTargetType - targetType not found (%s)\n", 
			GetName());
		assert(false);
		return;
	}

	size_t nMagazines = parentPlatform->GetMagazineCount();
	for (size_t n=0; n<nMagazines; n++)
	{
        std::shared_ptr<tcStores> mag = parentPlatform->GetMagazine(n);
        int magFlags = mag->GetAvailableTargetFlags(tcGameObject::shared_from_this(), useNuclear);
		if ((magFlags & targetFlag) != 0)
		{
            mag->AddAutomationOp(targetType, tcGameObject::shared_from_this());
			return;
		}
	}

	fprintf(stdout, "tcPlatformObject::EquipForTargetType - no compatible equipment found (%s)\n", 
		GetName());
}

/**
* Schedule automatic loadout op for target type. Platform must be
* landed and have access to appropriate stores
*/
void tcPlatformObject::EquipForTargetType(int targetFlag)
{
	if ((targetFlag != 0) && (IsEquippedForTargetType(targetFlag))) return; // already equipped

	std::string loadoutType;
	if (targetFlag == 0)
	{
		loadoutType = "Empty";
	}
	else if ((targetFlag & AIR_TARGET) != 0)
	{
		loadoutType = "AAW";
	}
	else if ((targetFlag & SURFACE_TARGET) != 0)
	{
		loadoutType = "ASuW";
	}	
	else if ((targetFlag & SUBSURFACE_TARGET) != 0)
	{
		loadoutType = "ASW";
	}	
	else if ((targetFlag & LAND_TARGET) != 0)
	{
		loadoutType = "Strike";
	}
	else
	{
		fprintf(stderr, "tcPlatformObject::EquipForTargetType - bad target flag (%s)\n", 
			GetName());
		assert(false); // bad targetFlag
		return;
	}

	EquipForTargetType(loadoutType);
}


/**
* To avoid dynamic_cast for testing if tcPlatformObject
*/
bool tcPlatformObject::IsPlatformObject() const
{
    return true;
}

bool tcPlatformObject::IsRefueling() const
{
	return isRefueling;
}

/**
* @return key of object to launch, otherwise NULL_INDEX
*/
void tcPlatformObject::Launch(long& rnKey, unsigned& rnLauncher) 
{
    mcLauncherState.Launch(rnKey, rnLauncher);
}

/**
* Sets goal altitude in guidance
*/
void tcPlatformObject::SetAltitude(float new_altitude_m) 
{
    mcGS.SetAltitude(new_altitude_m);
    commandObj.SetNewCommand(ALT_CMD);

	if (IsEditMode())
	{
		mcKin.mfAlt_m = new_altitude_m;
	}
}

/**
* Sets goal heading in guidance
*/
void tcPlatformObject::SetHeading(float afNewHeading) 
{
    mcGS.SetHeading(afNewHeading);
    commandObj.SetNewCommand(HEADING_CMD);

	if (IsEditMode())
	{
		mcKin.mfHeading_rad = afNewHeading;
		if (mcKin.mfHeading_rad < 0) mcKin.mfHeading_rad += C_TWOPI;
	}
}

void tcPlatformObject::SetRefueling(bool state)
{
	isRefueling = state;
}

/**
* Set goal speed to afNewSpeed. If goal speed
* is greater than max speed then set goal to
* max speed.
*/
void tcPlatformObject::SetSpeed(float newSpeed) 
{
    mcGS.SetSpeed(newSpeed);
    commandObj.SetNewCommand(SPEED_CMD);

	if (IsEditMode())
	{
		mcKin.mfSpeed_kts = newSpeed;
	}
}

/**
* If launcher is ready, increment pending of anLauncher by anQuantity.
* This method does not support targeting multiple targets.
* @return tcLauncherState::teLauncherStatus error code, LAUNCHER_READY = 0 for success
*/
int tcPlatformObject::SetLaunch(int anLauncher, int anQuantity) 
{
    return mcLauncherState.SetLaunch(anLauncher, anQuantity);
}



void tcPlatformObject::RandInitNear(float afLon_deg, float afLat_deg) 
{
    //  tcGameObject::RandInitNear(afLon,afLat);
    if (mpDBObject == NULL) {return;}
    mzClass = mpDBObject->mzClass;
    mzUnit = "PL_";
    mzUnit=strutil::AssignRandomSuffix(mzUnit);

    mfStatusTime = 0;        
    mcKin.mfLon_rad = C_PIOVER180*(afLon_deg + randfc(1.1f));      
    mcKin.mfLat_rad = C_PIOVER180*(afLat_deg + randfc(1.1f));
    mcKin.mfAlt_m = (mpDBObject->mnType == PTYPE_FIXEDWING) ? 5000.0f : 0.0f;               
    mcKin.mfHeading_rad = C_TWOPI*randf();           
    mcKin.mfSpeed_kts = 0.80f*mpDBObject->mfMaxSpeed_kts;
    mcKin.mfPitch_rad = 0;
    mcKin.mfRoll_rad = 0;
    mfDamageLevel = 0;  
    SetHeading(mcKin.mfHeading_rad);
    SetSpeed(mcKin.mfSpeed_kts);   
    SetAltitude(mcKin.mfAlt_m);
	fuel_kg = mpDBObject->GetInternalFuelCapacity();
    lastHeadingDelta = 0;
}
void tcPlatformObject::SetLongitude(float aflon_deg )
{
    mcKin.mfLon_rad = C_PIOVER180*(aflon_deg);
}
void tcPlatformObject::SetLatitude(float aflat_deg)
{
    mcKin.mfLat_rad = C_PIOVER180*(aflat_deg);
}

void tcPlatformObject::PrintToFile(tcFile& file) 
{
    tcString s;

    tcGameObject::PrintToFile(file);
    int nLaunchers = mcLauncherState.mnCount;

    if (nLaunchers > tcPlatformDBObject::MAXLAUNCHERS) 
    {
        file.WriteString("Error - launcher count overflow");
        mcLauncherState.mnCount = 0;
        nLaunchers = 0;
    }

    for(int i=0;i<nLaunchers;i++) 
    {
        s.Format("   LAU%d: %s x %d\n",i, 
            mcLauncherState.GetLauncherChildClass(i).c_str(),
            mcLauncherState.GetLauncherQuantity(i));
        file.WriteString(s.GetBuffer());
    }
    
    GetComponent<tcSensorPlatform>()->PrintToFile(file);
    
}

void tcPlatformObject::SaveToFile(tcFile& file) 
{
    assert(false);

    tcGameObject::SaveToFile(file); 

    file.Write(&fuel_kg,sizeof(fuel_kg));
    
    GetComponent<tcSensorPlatform>()->SaveToFile(file);
    
    // other data
    mcLauncherState.Serialize(file, false);
    mcGS.Serialize(file, false);
}

/**
*
*/
void tcPlatformObject::LoadFromFile(tcFile& file) 
{
    tcGameObject::LoadFromFile(file);

    file.Read(&fuel_kg,sizeof(fuel_kg));
    
    GetComponent<tcSensorPlatform>()->LoadFromFile(file);

    // other data
    mcLauncherState.Serialize(file, true);
    mcGS.Serialize(file, true);
}


/**
*
*/
void tcPlatformObject::Serialize(tcFile& file, bool mbLoad) 
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

void tcPlatformObject::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{
    tcScenarioRandomizer* randomizer = tcScenarioRandomizer::Get();

	std::string s;

    float terrainHeight_m = mapData->GetTerrainHeight(C_180OVERPI*mcKin.mfLon_rad, C_180OVERPI*mcKin.mfLat_rad, 0);
    if (terrainHeight_m < 0) terrainHeight_m = 0;

	logger.AddScenarioText("unit = SM.GetDefaultUnit()");
    
	s=strutil::format("unit.className = '%s'", mzClass.c_str());
	logger.AddScenarioText(s);

	s=strutil::format("unit.unitName = \"%s\"", mzUnit.c_str());
	logger.AddScenarioText(s);

	assert((mcKin.mfLon_rad >= -C_PI) && (mcKin.mfLon_rad < C_PI));
	assert((mcKin.mfLat_rad >= -C_PIOVER2) && (mcKin.mfLat_rad <= C_PIOVER2));

    if (!formation.IsFollower())
    {
        std::vector<tcRect> randomBoxes = randomizer->GetRandomBoxes(mzUnit.c_str());
        if (randomBoxes.size() == 0)
        {
            s=strutil::format("unit.SetPosition(%f, %f, %.1f)", C_180OVERPI*mcKin.mfLon_rad,
                C_180OVERPI*mcKin.mfLat_rad, mcKin.mfAlt_m - terrainHeight_m);
            logger.AddScenarioText(s);
        }
        else
        {
            s = "boxes = [";
            for (size_t k=0; k<randomBoxes.size(); k++)
            {
                if (k > 0) s += ",";
                s += strutil::format("[%.4f, %.4f, %.4f, %.4f]",
                    C_180OVERPI*randomBoxes[k].left, C_180OVERPI*randomBoxes[k].right, 
                    C_180OVERPI*randomBoxes[k].bottom, C_180OVERPI*randomBoxes[k].top);
            }
            s += "]";
            logger.AddScenarioText(s);

            s=strutil::format("box = boxes[int(%d*random())]", randomBoxes.size());
            logger.AddScenarioText(s);

            logger.AddScenarioText("lon_deg = random()*(box[1]-box[0]) + box[0]");
            logger.AddScenarioText("lat_deg = random()*(box[3]-box[2]) + box[2]");

            s=strutil::format("unit.SetPosition(lon_deg, lat_deg, %.1f)", mcKin.mfAlt_m - terrainHeight_m);
            logger.AddScenarioText(s);
        }
    }
    else
    {
        SaveFormationPositionToPython(logger);
    }

	s=strutil::format("unit.heading = %.2f", C_180OVERPI*mcKin.mfHeading_rad);
    logger.AddScenarioText(s);

	s=strutil::format("unit.speed = %.1f", mcKin.mfSpeed_kts);
	logger.AddScenarioText(s);

    if (GetCost() >= 0)
    {
        s=strutil::format("unit.cost = %.1f", GetCost());
        logger.AddScenarioText(s);
    }

	s=strutil::format("SM.AddUnitToAlliance(unit, %d)", GetAlliance());
	logger.AddScenarioText(s);

    size_t nLaunchers = GetLauncherCount();
    for (size_t k=0; k<nLaunchers; k++)
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(k);
        if (launcher->mnCurrent > 0)
        {
            s=strutil::format("SM.SetUnitLauncherItem(unit.unitName, %d, '%s', %d)", k,
                launcher->GetChildClassName().c_str(), launcher->mnCurrent);
        }
        else
        {
            s=strutil::format("SM.SetUnitLauncherItem(unit.unitName, %d, '', 0)", k);
        }
        logger.AddScenarioText(s);
    }    
    
    if (simState->mcSensorMap.GetAlwaysVisibleState(tcGameObject::shared_from_this()))
    {
        logger.AddScenarioText("SM.SetUnitAlwaysVisibleState(unit.unitName, 1)");
    }

    logger.AddScenarioText("UI = SM.GetUnitInterface(unit.unitName)");

	for (size_t k=0; k<magazines.size(); k++)
	{
		magazines[k]->SaveToPython(logger);
	}

    GetComponent<tcSensorPlatform>()->SaveToPython(logger);

	brain->SaveToPython(logger);

    formation.SaveToPython(logger);
}

void tcPlatformObject::SaveFormationPositionToPython(scriptinterface::tcScenarioLogger& logger)
{
    std::string s;
    std::shared_ptr<const tcPlatformObject> leader = std::dynamic_pointer_cast<tcPlatformObject>(simState->GetObject(formation.leaderId));
    if (leader == 0)
    {
        s=strutil::format("unit.SetPosition(%f, %f, %.1f)", C_180OVERPI*mcKin.mfLon_rad,
                C_180OVERPI*mcKin.mfLat_rad, mcKin.mfAlt_m);
        logger.AddScenarioText(s);
        assert(false); // follower without leader, shouldn't happen
        return;
    }

    float dlon_deg = C_180OVERPI * (mcKin.mfLon_rad - leader->mcKin.mfLon_rad);
    float dlat_deg = C_180OVERPI * (mcKin.mfLat_rad - leader->mcKin.mfLat_rad);

    s=strutil::format("UI = SM.GetUnitInterface('%s')", leader->mzUnit.c_str());
    logger.AddScenarioText(s);

    s=strutil::format("leader_track = UI.GetTrackById(UI.GetPlatformId())");
    logger.AddScenarioText(s);

    s=strutil::format("lon_deg = 57.296*leader_track.Lon + %.4f", dlon_deg);
    logger.AddScenarioText(s);

    s=strutil::format("lat_deg = 57.296*leader_track.Lat + %.4f", dlat_deg);
    logger.AddScenarioText(s);

    s=strutil::format("unit.SetPosition(lon_deg, lat_deg, %.1f)", mcKin.mfAlt_m);
    logger.AddScenarioText(s);
}


/**
* Loads state from command stream
*/
tcCommandStream& tcPlatformObject::operator<<(tcCommandStream& stream)
{
    tcGameObject::operator<<(stream);

	ClearNewCommand();

    unsigned short updateMask;
    stream >> updateMask;

    if (updateMask & UPDATE_GUIDANCE)
    {
		stream >> mcGS.mfGoalHeading_rad;
		stream >> mcGS.mfGoalSpeed_kts;
		stream >> mcGS.mfGoalAltitude_m;
	}

    if (updateMask & UPDATE_LAUNCHERS)
    {
        mcLauncherState << stream;
    }

    if (updateMask & UPDATE_SENSORS)
    {
        GetComponent<tcSensorPlatform>()->operator<<(stream);
    }

	if (updateMask & UPDATE_AI)
	{
		brain->operator<<(stream);
	}
	
    if (updateMask & UPDATE_STORES)
    {
        for (size_t n=0; n<magazines.size(); n++)
	    {
            unsigned char updateMag;
            stream >> updateMag;
            if (updateMag != 0)
            {   
                magazines[n]->operator<<(stream);
            }
        }
    }

    if (updateMask & UPDATE_FORMATION)
    {
        formation.operator<<(stream);
    }


    return stream;
}

/**
* Saves state to command stream
*/
tcCommandStream& tcPlatformObject::operator>>(tcCommandStream& stream)
{
    tcGameObject::operator>>(stream);

    // form update mask
    unsigned short updateMask = 0;
    updateMask = UPDATE_GUIDANCE; // always update guidance for now

	if (mcLauncherState.HasNewCommand())
    {
        updateMask |= UPDATE_LAUNCHERS;
    }
    if (GetComponent<tcSensorPlatform>()->HasNewCommand())
    {
        updateMask |= UPDATE_SENSORS;
    }
	if (brain->HasNewCommand())
	{
		updateMask |= UPDATE_AI;
	}
	
	for (size_t n=0; n<magazines.size(); n++)
	{
        if (magazines[n]->HasNewCommand())
        {
            updateMask |= UPDATE_STORES;
        }
    }

    if (formation.HasNewCommand())
    {
        updateMask |= UPDATE_FORMATION;
    }
    
	if (stream.GetDetailLevel() == tcStream::WRITE_ALL) updateMask = 0xFF;

	//if (IsClientMode()) updateMask &= (~UPDATE_AI); // don't do ai updates at client

    stream << updateMask;


    if (updateMask & UPDATE_GUIDANCE)
    {
        stream << mcGS.mfGoalHeading_rad;
        stream << mcGS.mfGoalSpeed_kts;
        stream << mcGS.mfGoalAltitude_m;
    }
    
    if (updateMask & UPDATE_LAUNCHERS)
    {
        mcLauncherState >> stream;
    }

    if (updateMask & UPDATE_SENSORS)
    {
        GetComponent<tcSensorPlatform>()->operator>>(stream);
    }

	if (updateMask & UPDATE_AI)
	{
		brain->operator>>(stream);
	}

    if (updateMask & UPDATE_STORES)
    {
        for (size_t n=0; n<magazines.size(); n++)
	    {
            if (magazines[n]->HasNewCommand())
            {   
                unsigned char updateMag = 1;
                stream << updateMag;
                magazines[n]->operator>>(stream);
            }
            else
            {
                unsigned char updateMag = 0;
                stream << updateMag;
            }
        }
    }

    if (updateMask & UPDATE_FORMATION)
    {
        formation.operator>>(stream);
    }

    return stream;
}

/**
* Loads state from create stream
*/
tcCreateStream& tcPlatformObject::operator<<(tcCreateStream& stream)
{
    tcGameObject::operator<<(stream);

    GetComponent<tcSensorPlatform>()->operator<<(stream);

    return stream;
}

/**
* Saves state to create stream
*/
tcCreateStream& tcPlatformObject::operator>>(tcCreateStream& stream)
{
    tcGameObject::operator>>(stream);
    
    GetComponent<tcSensorPlatform>()->operator>>(stream);

    return stream;
}


/**
* Loads state from update stream
*/
tcUpdateStream& tcPlatformObject::operator<<(tcUpdateStream& stream)
{
    tcGameObject::operator<<(stream);

    mcLauncherState.operator<<(stream);

    GetComponent<tcSensorPlatform>()->operator<<(stream);

	unsigned char nMagazines;
	stream >> nMagazines;
	if (magazines.size() != nMagazines)
	{
		fprintf(stderr, "tcPlatformObject::operator<< - bad platform update\n");
		assert(false);
		return stream;
	}

	for (unsigned char n=0; n<nMagazines; n++)
	{
		magazines[n]->operator<<(stream);
	}

    return stream;
}

/**
* Saves state to update stream
*/
tcUpdateStream& tcPlatformObject::operator>>(tcUpdateStream& stream)
{
    tcGameObject::operator>>(stream);

    mcLauncherState.operator>>(stream);

    GetComponent<tcSensorPlatform>()->operator>>(stream);

	unsigned char nMagazines = (unsigned char)magazines.size();
	stream << nMagazines;
	for (unsigned char n=0; n<nMagazines; n++)
	{
		magazines[n]->operator>>(stream);
	}

    return stream;
}


/**
* Loads state from game stream
*/
tcGameStream& tcPlatformObject::operator<<(tcGameStream& stream)
{
    tcGameObject::operator<<(stream);

    mcLauncherState.operator<<(stream);

    GetComponent<tcSensorPlatform>()->operator<<(stream);

	unsigned char nMagazines;
	stream >> nMagazines;
	if (magazines.size() != nMagazines)
	{
		fprintf(stderr, "tcPlatformObject::operator<<(tcGameStream) -- corrupt stream\n");
		assert(false);
		return stream;
	}
	for (unsigned char n=0; n<nMagazines; n++)
	{
		magazines[n]->operator<<(stream);
	}

    stream >> fuel_kg;
	stream >> externalFuelCapacity_kg;
    stream >> lastHeadingDelta;
	stream >> isRefueling;
	stream >> loadoutTag;
    stream >> reducedTurnRate_degps;
    mcGS << stream;

    *brain << stream;

    stream >> mcLaunchRequest.mnLauncher;
    stream >> mcLaunchRequest.mnQuantity;
    msTargetDatum << stream;

	if (stream.GetVersionId() >= 10) formation.operator<<(stream);

    commandObj << stream;

    missilePreplan.clear();
    unsigned char nPreplan;
    stream >> nPreplan;
    for (unsigned char n=0; n<nPreplan; n++)
    {
        GeoPoint p;
        p << stream;
        missilePreplan.push_back(p);
    }

    stream.ReadCheckValue(143);

    return stream;
}

/**
* Saves state to game stream
*/
tcGameStream& tcPlatformObject::operator>>(tcGameStream& stream)
{
    tcGameObject::operator>>(stream);

    mcLauncherState.operator>>(stream);

    GetComponent<tcSensorPlatform>()->operator>>(stream);

	unsigned char nMagazines = magazines.size();
	stream << nMagazines;
	for (unsigned char n=0; n<nMagazines; n++)
	{
		magazines[n]->operator>>(stream);
	}

    stream << fuel_kg;
	stream << externalFuelCapacity_kg;
    stream << lastHeadingDelta;
	stream << isRefueling;
	stream << loadoutTag;
    stream << reducedTurnRate_degps;
    mcGS >> stream;

    *brain >> stream;

    stream << mcLaunchRequest.mnLauncher;
    stream << mcLaunchRequest.mnQuantity;
    msTargetDatum >> stream;

	if (stream.GetVersionId() >= 10) formation.operator>>(stream);

    commandObj >> stream;

    assert(missilePreplan.size() < 256);
    unsigned char nPreplan = (unsigned char)missilePreplan.size();
    stream << nPreplan;
    for (unsigned char n=0; n<nPreplan; n++)
    {
        missilePreplan[n] >> stream;
    }

    stream.WriteCheckValue(143);

    return stream;
}


void tcPlatformObject::ClearNewCommand()
{
    commandObj.ClearNewCommand();
    mcLauncherState.ClearNewCommand();
    GetComponent<tcSensorPlatform>()->ClearNewCommand();
	brain->ClearNewCommand();
    formation.ClearNewCommand();
	
	for (size_t n=0; n<magazines.size(); n++)
	{
        magazines[n]->ClearNewCommand();
    }
}

bool tcPlatformObject::HasNewCommand() const
{
	bool newBrainCommand = brain->HasNewCommand();
	
	if (newBrainCommand) return true;

	for (size_t n=0; n<magazines.size(); n++)
	{
		if (magazines[n]->HasNewCommand()) return true;
    }

    return commandObj.HasNewCommand() || mcLauncherState.HasNewCommand() ||
        GetComponent<tcSensorPlatform>()->HasNewCommand() || formation.HasNewCommand();
}

bool tcPlatformObject::IsCommunicable() const
{
    if(std::shared_ptr<tcCommPlatform> comm= GetComponent<tcCommPlatform>())
    {
       return  comm->HasActivatedComm();
    }
    return true;
}

void tcPlatformObject::SetController(const std::string& username)
{
	// set controller for all children
	size_t nChildren = children.size();
	for (size_t n=0; n<nChildren; n++)
	{
		children[n]->SetController(username);
	}

	tcControllableObject::SetController(username);
}

bool tcPlatformObject::IsAir() const
{
    UINT32 nModelType = mnModelType;
    return (nModelType == MTYPE_FIXEDWING)||(nModelType == MTYPE_FIXEDWINGX)
           ||(nModelType == MTYPE_AIR)||(nModelType == MTYPE_HELO);
}
bool tcPlatformObject::IsGroundVehicle() const
{

    return (mnModelType == MTYPE_GROUNDVEHICLE);
}

/// returns true if platform is a helo
bool tcPlatformObject::IsHelo() const
{

    return (mnModelType == MTYPE_HELO);
}

bool tcPlatformObject::IsFixed() const
{
    return (mnModelType == MTYPE_FIXED) ||
           (mnModelType == MTYPE_AIRFIELD);
}

/// returns true if platform is a submarine
bool tcPlatformObject::IsSub() const
{
    return (mnModelType == MTYPE_SUBMARINE);
}
void tcPlatformObject::LoadOther(const std::string& item, unsigned long quantity)
{
    if (!IsControlled()) return;

    std::string exactItem;
    size_t nMagazines = GetMagazineCount();
    for (size_t n=0; n<nMagazines; n++)
    {
        std::shared_ptr<tcStores> mag = GetMagazine(n);
        if (mag->CurrentItemQuantity(item, exactItem))
        {
            mag->LoadOther(exactItem, quantity, tcGameObject::shared_from_this());
            return;
        }
    }
    if (std::shared_ptr<tcPlatformObject> parent = std::dynamic_pointer_cast<tcPlatformObject>(parent))
    {
        size_t nMagazines = parent->GetMagazineCount();
        for (size_t n=0; n<nMagazines; n++)
        {
            std::shared_ptr<tcStores> mag = parent->GetMagazine(n);
            if (mag->CurrentItemQuantity(item, exactItem))
            {
                mag->LoadOther(exactItem, quantity, tcGameObject::shared_from_this());
                return;
            }
        }
    }
}

std::vector<tcSensorMapTrack> tcPlatformObject::GetTrackListValidROE(int anClassMask,
                                                      float afMaxRange_km)
{
    std::vector<tcSensorMapTrack> trackList;

    double t = simState->GetTime();

    std::shared_ptr<tcSensorMapTrack>pTrack;
    tcGoalTracker* goalTracker = tcGoalTracker::Get();



    tcAllianceSensorMap  *sensorMap =
        simState->mcSensorMap.GetOrCreateMap(GetAlliance());
     assert(sensorMap != 0);
    int nCount = sensorMap->GetTrackCount();
    if (nCount==0)
    {
        return trackList;
    }

    long nPos = sensorMap->GetStartTrackPosition();
    for(int n=0;n<nCount;n++)
    {
        sensorMap->GetNextTrack(nPos, pTrack);

        bool classificationMatch = pTrack->MatchesMask(anClassMask);

        bool bearingOnlyValid = !pTrack->IsBearingOnly() || (pTrack->errorPoly.size() > 0);

        bool valid = classificationMatch && bearingOnlyValid &&
                     !pTrack->IsDestroyed() && !pTrack->IsStale();

        if (valid && (goalTracker->IsTargetLegal(tcGameObject::shared_from_this(), *pTrack)))
        {
            GeoPoint p;
            p.mfAlt_m = 0;
            p.mfLat_rad = pTrack->mfLat_rad;
            p.mfLon_rad = pTrack->mfLon_rad;
            float fRange_km = mcKin.RangeToKm(&p);
            if (fRange_km <= afMaxRange_km)
            {
                tcSensorMapTrack predictedTrack(*pTrack);
                pTrack->GetPrediction(predictedTrack, t);
                trackList.push_back(predictedTrack);
            }
        }
    }

    return trackList;
}


float tcPlatformObject::GetHeadingToDatum(float afLon_rad, float afLat_rad)
{
    GeoPoint p;
    p.mfAlt_m = 0;
    p.mfLon_rad = afLon_rad;
    p.mfLat_rad = afLat_rad;
    float heading_rad = mcKin.HeadingToGeoRad(&p);
    assert(fabsf(heading_rad) <= C_TWOPI);

    return heading_rad*C_180OVERPI;
}

float tcPlatformObject::GetRangeToDatum(float afLon_rad, float afLat_rad)
{
    GeoPoint p;
    p.mfAlt_m = 0;
    p.mfLon_rad = afLon_rad;
    p.mfLat_rad = afLat_rad;
    float range_km = mcKin.RangeToKm(&p);
    return range_km;
}
/**
* Set fire control sensors for launchers. If launcher
* has a non-null fire control sensor, then find and set
* it.
*/
void tcPlatformObject::SetFireControlSensors()
{
    size_t nSensors = GetComponent<tcSensorPlatform>()->GetSensorCount();
    
	size_t nLaunchers = mcLauncherState.GetLauncherCount();
 
    assert(mpDBObject->launcherFireControl.size() == nLaunchers);

    for (size_t nLauncher=0; nLauncher<nLaunchers; nLauncher++) 
    {
        std::shared_ptr<tcLauncher> launcher = GetLauncher(nLauncher);
        launcher->UpdateFireControlSensor();
    }
}

void tcPlatformObject::SetFormationAltitudeOffset(float dh_m)
{
    formation.SetAltitudeOffset(dh_m);
}

void tcPlatformObject::SetFormationLeader(long id)
{
    formation.SetPlatformId(mnID);

    if (id < 0)
    {
        formation.LeaveFormation();
        return;
    }

    std::shared_ptr<tcPlatformObject> leader = std::dynamic_pointer_cast<tcPlatformObject>(simState->GetObject(id));

    // allow formation with non-friendly if within 1.0 km range 
    if (leader == 0) return;
    
    bool hostileFormation = (leader->GetAlliance() != GetAlliance());
    const float hostileFormationRange_km = 1.5f;
    if (hostileFormation && (leader->RangeTo(*this) > hostileFormationRange_km))
    {
        return;
    }

    // for hostile formations, there is no leader participation

    // check that leader is not part of a formation as a follower
    if (leader->formation.isActive && (!hostileFormation) && (leader->formation.leaderId != -1)) return;

    // check that current leader != id
    if (formation.isActive && (formation.leaderId == id)) return;

    // if already part of formation, remove from old formation
    if (formation.isActive && (formation.leaderId != -1))
    {
        std::shared_ptr<tcPlatformObject> oldLeader = 
            std::dynamic_pointer_cast<tcPlatformObject>(simState->GetObject(formation.leaderId));
        if ((oldLeader != 0) && (oldLeader->GetAlliance() == GetAlliance()))
        {
            oldLeader->formation.RemoveFollower(mnID);
        }
    }

    if (!hostileFormation)
    {
        leader->formation.isActive = true;
        leader->formation.leaderId = -1;
        leader->formation.AddFollower(mnID);
    }


    formation.isActive = true;
    formation.leaderId = id;
    formation.useNorthBearing = false;
    formation.range_center_km = 2.0f;
    formation.range_span_km = 0.5f;
    formation.bearing_center_rad = 0.2f;
    formation.bearing_span_rad = 0.2f;

	SetFormationMode(tcFormation::SPRINTDRIFT);
}

void tcPlatformObject::SetFormationMode(int mode)
{
	formation.SetFormationMode(mode);

    MarkFormationUpdated();
}

void tcPlatformObject::SetFormationPosition(float range_km, float span_km, float bearing_rad, float span_rad)
{
    formation.SetFormationPosition(range_km, span_km, bearing_rad, span_rad);
}

void tcPlatformObject::MarkFormationUpdated()
{
    formation.SetNewCommand();
}


/**
*
*/
tcPlatformObject::tcPlatformObject()
: mpDBObject(0),
  loadoutTag(""),
  reducedTurnRate_degps(0)
{
    assert(false);
    Clear();
    brain = std::make_shared<Brain>();
    mcLauncherState.mnCount = 0;
    mnModelType = MTYPE_PLATFORM;
    AddComponent(std::make_shared<tcSensorPlatform>());
}


tcPlatformObject::tcPlatformObject(std::shared_ptr<tcPlatformDBObject>obj)
: tcGameObject(obj),
    //tcSensorPlatform(),
  externalFuelCapacity_kg(0),
  isRefueling(false),
  loadoutTag(""),
  reducedTurnRate_degps(360.0f)
{
    using namespace database;
    // tcSensorPlatform::Init(obj, std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));

    // brain = new Brain(std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));
    brain=std::make_shared<Brain>();
    mpDBObject = obj;
    mnModelType = MTYPE_PLATFORM;
    AddComponent(std::make_shared<tcSensorPlatform>());


//    mcAI.ClearOrders();


}


/**
*
*/
tcPlatformObject::tcPlatformObject(tcPlatformObject& o) : 
    tcGameObject(o),
    //tcSensorPlatform(o),
    externalFuelCapacity_kg(o.externalFuelCapacity_kg),
    formation(o.formation),
    commandObj(o.commandObj),
    isRefueling(o.isRefueling),
    loadoutTag(o.loadoutTag),
    reducedTurnRate_degps(o.reducedTurnRate_degps)
{
    brain = std::make_shared<Brain>();

    fuel_kg = o.fuel_kg;
//    mcAI = o.mcAI;
    mcGS = o.mcGS;
    mcLauncherState = o.mcLauncherState;
    mcLaunchRequest = o.mcLaunchRequest;
    mpDBObject = o.mpDBObject;
    msTargetDatum = o.msTargetDatum;

    assert(magazines.size() == 0);
    int nMagazines = (int)o.magazines.size();
    for (int n=0; n<nMagazines; n++) 
    {
        assert(false); // need to write this code
    }

    formation.SetPlatformId(mnID);

}
/**
*
*/
tcPlatformObject::~tcPlatformObject()
{
    DestroyFormation();

    // if (brain) delete brain;

    for (size_t n=0; n<magazines.size(); n++)
    {
        //delete magazines[n];
    }

}

void tcPlatformObject::Construct()
{

    GetComponent<tcSensorPlatform>()->Init(mpDBObject->GetComponent<tcSensorPlatformDBObject>(),
                           std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));
    mcLauncherState.SetParent(std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));

    brain->SetPlatformObject( std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));

    fuel_kg = mpDBObject->GetInternalFuelCapacity(); // max internal fuel


    // add magazines
    if (mpDBObject->mnNumMagazines > tcPlatformDBObject::MAXMAGAZINES)
    {
        mpDBObject->mnNumMagazines = tcPlatformDBObject::MAXMAGAZINES;
        fprintf(stderr, "tcPlatformObject::tcPlatformObject - Warning - "
                        "DB magazine count exceeded limit\n");
    }

    magazines.clear();
    for (int i=0; i<mpDBObject->mnNumMagazines; i++)
    {
        std::shared_ptr<tcDatabaseObject> pDBObj = database->GetObject(mpDBObject->maMagazineClass[i].c_str());

        if (std::shared_ptr<tcStoresDBObject> storesDBObj = std::dynamic_pointer_cast<tcStoresDBObject>(pDBObj))
        {
            std::shared_ptr<tcStores> mag = std::make_shared<tcStores>(storesDBObj);
            mag->SetParent(std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));
            magazines.push_back(mag);
        }
        else
        {
            fprintf(stderr, "Error - tcPlatformObject::tcPlatformObject(std::shared_ptr<tcPlatformDBObject>obj)"
                            " - Stores obj not found\n");
        }

    }

    // add launchers
    mcLauncherState.SetParent(std::dynamic_pointer_cast<tcPlatformObject>(tcGameObject::shared_from_this()));
    mcLauncherState.mnCount = 0;

    for (int nLauncher=0; nLauncher<mpDBObject->mnNumLaunchers; nLauncher++)
    {
        long nLauncherKey = database->GetKey(mpDBObject->maLauncherClass[nLauncher].c_str());
        if (nLauncherKey != -1)
        {
            Vector2d attitude = mpDBObject->GetLauncherAttitude(nLauncher);
            float FOV_deg = mpDBObject->GetLauncherFOV_deg(nLauncher);
            bool isReloadable = mpDBObject->launcherIsReloadable[nLauncher];

            mcLauncherState.AddFullLauncher(nLauncherKey, C_PIOVER180*attitude.x(),
                                            C_PIOVER180*attitude.y(), FOV_deg, mpDBObject->launcherName[nLauncher], isReloadable);
        }
        else
        {
            assert(false);
            fprintf(stderr, "tcPlatformObject::tcPlatformObject - Launcher not in database (%s)\n",
                    mpDBObject->maLauncherClass[nLauncher].c_str());
        }
    }

    SetFireControlSensors();

    //model->SetupAnimation(this);

    lastHeadingDelta = 0;

}


