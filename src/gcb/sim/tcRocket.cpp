/** 
**  @file tcRocket.cpp
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

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcRocket.h"
#include "tcBallisticDBObject.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "database/tcPlatformDBObject.h"
//#include "tc3DModel.h"
#include "tcLauncher.h"
#include "tcSimState.h"
#include "tc3DPoint.h"
#include "tcGameObjIterator.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



/**
* Load state from game stream
*/
tcGameStream& tcRocket::operator<<(tcGameStream& stream)
{
	tcBallisticWeapon::operator<<(stream);

	return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcRocket::operator>>(tcGameStream& stream)
{
	tcBallisticWeapon::operator>>(stream);

	return stream;
}



/**
* Initializes ballistic weapon state for launch from game object.
* Adds self to simulation
*
* @param obj launching game object
* @param launcher index of launcher
*/
void tcRocket::LaunchFrom(tcGameObject* obj, unsigned nLauncher)
{
    // 获取指定发射器的指针
    const tcLauncher* pLauncher = obj->GetLauncher(nLauncher);

    // 检查发射对象是否是平台对象（可能是飞机、舰船等）
    if (tcPlatformObject* platObj = dynamic_cast<tcPlatformObject*>(obj))
    {
        // 获取发射器在平台对象中的位置
        tc3DPoint launcherPos = platObj->mpDBObject->GetLauncherPosition(nLauncher);
        // 将位置转换为地理坐标（经度、纬度、高度）
        GeoPoint pos = obj->RelPosToLatLonAlt(launcherPos.x, launcherPos.y, launcherPos.z);
        // 设置运动学状态中的经度、纬度和高度
        mcKin.mfLon_rad = pos.mfLon_rad;
        mcKin.mfLat_rad = pos.mfLat_rad;
        mcKin.mfAlt_m = pos.mfAlt_m;
    }
    else
    {
        // 如果不是平台对象，则直接使用发射对象的运动学状态中的位置信息
        mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
        mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
        mcKin.mfAlt_m = obj->mcKin.mfAlt_m;
    }

    // 复制发射对象的运动学状态中的速度、航向和俯仰角
    mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
    mcKin.mfHeading_rad = obj->mcKin.mfHeading_rad;
    mcKin.mfPitch_rad = obj->mcKin.mfPitch_rad;

    // 加上发射器的指向仰角和方位角
    mcKin.mfPitch_rad += pLauncher->pointingElevation;
    mcKin.mfHeading_rad += pLauncher->pointingAngle;

    // 添加角度误差以模拟轨迹的不准确性
    mcKin.mfHeading_rad += 0.707 * GaussianRandom::Get()->randn_fast() * mpDBObject->angleError_rad;
    mcKin.mfPitch_rad += 0.707 * GaussianRandom::Get()->randn_fast() * mpDBObject->angleError_rad;

    // 设置爬升角为俯仰角
    mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
    // 设置状态时间为发射对象的状态时间
    mfStatusTime = obj->mfStatusTime;


    // 如果发射器是自动指向模式
    if (pLauncher->IsAutoPoint()) // normally should be AutoPoint for rockets to make targeting easier
    {
        // 设置速度为发射速度（转换为节）
        mcKin.mfSpeed_kts = C_MPSTOKTS * mpDBObject->launchSpeed_mps;

        // 获取拦截目标的方位角和仰角等信息
        tcTrack targetTrack;
        float launchAz_rad = 0;
        float launchEl_rad = 0;
        float tti_s;
        float range_km;
        if (simState->GetTruthTrack(pLauncher->mnTargetID, targetTrack))
        {
            // 如果有目标，则计算拦截数据
            mcKin.GetInterceptData3D(targetTrack, launchAz_rad, launchEl_rad, tti_s, range_km);
        }
        else if (!pLauncher->msDatum.IsZero())
        {
            // 如果没有目标但有数据点，则使用数据点作为目标
            targetTrack.mfLon_rad = pLauncher->msDatum.mfLon_rad;
            targetTrack.mfLat_rad = pLauncher->msDatum.mfLat_rad;
            targetTrack.mfAlt_m = pLauncher->msDatum.mfAlt_m;
            targetTrack.mfSpeed_kts = 0;
            mcKin.GetInterceptData3D(targetTrack, launchAz_rad, launchEl_rad, tti_s, range_km);
        }
        else
        {
            return; // 没有目标ID或数据点，则不进行发射
        }

        // 设置航向角和俯仰角为计算出的拦截角度
        mcKin.mfHeading_rad = launchAz_rad;
        mcKin.mfPitch_rad = launchEl_rad;
    }
    else // 假设发射器是固定在前向位置
    {
        // 在当前速度上加上发射速度
        mcKin.mfSpeed_kts += C_MPSTOKTS * mpDBObject->launchSpeed_mps;
    }

    // 再次添加角度误差（这部分可能是冗余的，因为在上面已经加过一次）
    mcKin.mfHeading_rad += GaussianRandom::Get()->randn_fast() * mpDBObject->angleError_rad;
    mcKin.mfPitch_rad += GaussianRandom::Get()->randn_fast() * mpDBObject->angleError_rad;
    mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;


    // 记录发射平台ID
    launchingPlatform = obj->mnID;

    // 初始化发射距离为0
    distFromLaunch_m = 0;

    // 根据弹药的类型设置目标位置
    switch (mpDBObject->ballisticType)
    {
    case tcBallisticDBObject::ROCKET:
    {
        // 对于火箭，目标位置为发射器的数据点
        targetPos = pLauncher->msDatum;
    }
    break;
    default:
        assert(false);
        return; // 错误，未知的弹药类型
    }

    // 确保发射模式是仅数据点模式
    assert(pLauncher->meLaunchMode == DATUM_ONLY);


    // 设置单位名称（格式为"RKT 平台ID-计数器"）
    std::string s = strutil::format("RKT %d-%d", obj->mnID, launchedCounter++);
    mzUnit = s.c_str();

    // 设置联盟（与发射对象相同）
    SetAlliance(obj->GetAlliance());

    // 将自己添加到模拟中
    simState->AddPlatform(static_cast<tcGameObject*>(this));

    // 设置预定目标（必须在设置联盟和ID之后进行）
    // 这是tcWeaponObject的方法
    SetIntendedTarget(pLauncher->mnTargetID);
}


/**
*
*/
void tcRocket::Update(double afStatusTime)
{
    float dt_s = (float)(afStatusTime - mfStatusTime);

	mfStatusTime = afStatusTime;

	assert(mpDBObject);

    if (dt_s <= 0) return;


	// initialize local kinematic state variables if vxy_mps == 0
	if (vxy_mps == 0)
	{
		float v = C_KTSTOMPS * mcKin.mfSpeed_kts;
		vz_mps = v * sinf(mcKin.mfPitch_rad);
		float cospitch = cosf(mcKin.mfPitch_rad);
		vxy_mps = v * cospitch;
	}

    float distxy_m = dt_s * vxy_mps;
	float dist = C_MTORAD * distxy_m;
    float dlon = dist * sinf(mcKin.mfHeading_rad) / cosf(mcKin.mfLat_rad);
    float dlat = dist * cosf(mcKin.mfHeading_rad);
	

    float distxyz_m = dt_s * C_KTSTOMPS * mcKin.mfSpeed_kts;
    distFromLaunch_m += distxyz_m;
   

	mcKin.mfLon_rad += dlon;
	mcKin.mfLat_rad += dlat;
	mcKin.mfAlt_m += vz_mps * dt_s;

	// pitch, climb angle, and speed are constant--no need to update

    HandlePoleWrap();

    //Update3D();

	if (clientMode) return;

    if ((mpDBObject->maxRange_km > 0) && 
        (distFromLaunch_m > 1000.0f * mpDBObject->maxRange_km))
    {
        if ((mpDBObject->payloadClass.size() == 0) || payloadDeployed)
        {
            SelfDestruct();
        }
        else
        {
            DeployPayload();
        }
    }

    if (mcKin.mfAlt_m < -1.0f)
    {
        SelfDestruct();
    }

    /*** check for impact detonation with ground ***/
	if (distFromLaunch_m < 150.0f) return;

    float terrainHeight_m = mcTerrain.mfHeight_m;
    if (terrainHeight_m < 0) terrainHeight_m = 0;
    // interpret detonation range as altitude of detonation for ground detonation
    float detAlt_m = mpDBObject->detonationRange_m;

    float dz =  terrainHeight_m + detAlt_m - mcKin.mfAlt_m; // height above ground or sea level

    float t_impact = dz / vz_mps;

	if ((t_impact <= 0.03f) && (vz_mps < 0))
	{
		Detonate(0);
		return;
	}

	/*** check for detonation with nearby targets ***/
	tcBallisticWeapon::CheckGravityBombImpact();
}




/**
*
*/
tcRocket::tcRocket() 
: tcBallisticWeapon()
{
	mnModelType = MTYPE_ROCKET;
    mpDBObject = 0;
}

/**
* Copy constructor.
*/
tcRocket::tcRocket(const tcRocket& obj) 
: tcBallisticWeapon(obj)
{
	mnModelType = MTYPE_ROCKET;

    mpDBObject = obj.mpDBObject;
}

/**
* Constructor that initializes using info from database entry.
*/
tcRocket::tcRocket(tcBallisticDBObject* obj)
: tcBallisticWeapon(obj)
{
	mnModelType = MTYPE_ROCKET;

    mpDBObject = obj;
}

/**
*
*/
tcRocket::~tcRocket() 
{
}

