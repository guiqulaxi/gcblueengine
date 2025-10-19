/** 
**  @file tcBallisticWeapon.cpp
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

#include "tcBallisticWeapon.h"
#include "tcBallisticDBObject.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "database/tcPlatformDBObject.h"
//#include "tc3DModel.h"
//#include "tcParticleEffect.h"
#include "tcLauncher.h"
#include "tcSimState.h"
#include "tc3DPoint.h"
#include "tcBallisticMissile.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

/**
* Load state from update stream
*/
tcUpdateStream& tcBallisticWeapon::operator<<(tcUpdateStream& stream)
{
	tcWeaponObject::operator<<(stream);

	stream >> vxy_mps;
	stream >> vz_mps;

	return stream;
}

/**
* Save state to update stream
*/
tcUpdateStream& tcBallisticWeapon::operator>>(tcUpdateStream& stream)
{
	tcWeaponObject::operator>>(stream);

	stream << vxy_mps;
	stream << vz_mps;

	return stream;
}

/**
* Load state from game stream
*/
tcGameStream& tcBallisticWeapon::operator<<(tcGameStream& stream)
{
	tcWeaponObject::operator<<(stream);

	stream >> vz_mps;
	stream >> vxy_mps;
    stream >> distFromLaunch_m;
    targetPos << stream;

	return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcBallisticWeapon::operator>>(tcGameStream& stream)
{
	tcWeaponObject::operator>>(stream);

	stream << vz_mps;
	stream << vxy_mps;
    stream << distFromLaunch_m;
    targetPos >> stream;

	return stream;
}

/**
* @return targeting solution or (0,0,0) if targetId not valid
*/
const GeoPoint& tcBallisticWeapon::CalculateGunSolution(int targetId)
{
    static GeoPoint targetDatum;
    tcTrack targetTrack;
    tcTrack interceptTrack;

    // if the launcher has a target, set launch az based on projected position
    // cheat with truth track
    if (simState->GetTruthTrack(targetId, targetTrack))
    {
        float range_m = 1000.0f * mcKin.RangeToKm(targetTrack);
        float dz_m = targetTrack.mfAlt_m - mcKin.mfAlt_m;
        float tti_s;
        mpDBObject->GetGunneryElevation(range_m, dz_m, tti_s);
        interceptTrack = targetTrack.PredictAhead(tti_s);

        if (targetTrack.mfSpeed_kts > 0)
        {
            // second iteration
            range_m = 1000.0f * mcKin.RangeToKm(interceptTrack);
            dz_m = interceptTrack.mfAlt_m - mcKin.mfAlt_m;
            mpDBObject->GetGunneryElevation(range_m, dz_m, tti_s);
            interceptTrack = targetTrack.PredictAhead(tti_s);

            // third iteration
            range_m = 1000.0f * mcKin.RangeToKm(interceptTrack);
            dz_m = interceptTrack.mfAlt_m - mcKin.mfAlt_m;
            mpDBObject->GetGunneryElevation(range_m, dz_m, tti_s);
            interceptTrack = targetTrack.PredictAhead(tti_s);

            range_m = 1000.0f * mcKin.RangeToKm(interceptTrack);
            dz_m = interceptTrack.mfAlt_m - mcKin.mfAlt_m;
            mpDBObject->GetGunneryElevation(range_m, dz_m, tti_s);
            interceptTrack = targetTrack.PredictAhead(tti_s);
        }

        targetDatum.mfLon_rad = interceptTrack.mfLon_rad;
        targetDatum.mfLat_rad = interceptTrack.mfLat_rad;
        targetDatum.mfAlt_m = interceptTrack.mfAlt_m;
    }
    else
    {
        targetDatum.Set(0, 0, 0);
    }

    return targetDatum;
}

/**
* Initializes ballistic weapon state for launch from game object.
* Adds self to simulation
*
* @param obj launching game object
* @param launcher index of launcher
*/
void tcBallisticWeapon::LaunchFrom(std::shared_ptr<tcGameObject> obj, unsigned nLauncher)
{
    std::shared_ptr<tcLauncher> pLauncher =std::make_shared<tcLauncher>();
    pLauncher->mnTargetID = -1;
    pLauncher->pointingAngle = 0;
    pLauncher->pointingElevation = 0;
    pLauncher->firingArc_deg = 0;
    pLauncher->mfTimeToReady = 0;



    if (std::shared_ptr<tcPlatformObject> platObj = std::dynamic_pointer_cast<tcPlatformObject>(obj))
	{
		tc3DPoint launcherPos = platObj->mpDBObject->GetLauncherPosition(nLauncher);
		GeoPoint pos = obj->RelPosToLatLonAlt(launcherPos.x, launcherPos.y,
			launcherPos.z);
		mcKin.mfLon_rad = pos.mfLon_rad;
		mcKin.mfLat_rad = pos.mfLat_rad;
		mcKin.mfAlt_m = pos.mfAlt_m;
        
        pLauncher = obj->GetLauncher(nLauncher);
	}
    else if (std::shared_ptr<tcBallisticMissile> bmissile = std::dynamic_pointer_cast<tcBallisticMissile>(obj))
	{
		mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
		mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
		mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        pLauncher->msDatum = bmissile->GetTargetDatum();
        pLauncher->mnTargetID = bmissile->GetIntendedTarget();
        pLauncher->pointingAngle = 0;
        pLauncher->pointingElevation = 0;
	}
    else if (std::shared_ptr<tcBallisticWeapon> ballistic = std::dynamic_pointer_cast<tcBallisticWeapon>(obj))
	{
		mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
		mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
		mcKin.mfAlt_m = obj->mcKin.mfAlt_m;

        pLauncher->msDatum = targetPos;
        pLauncher->mnTargetID = ballistic->GetIntendedTarget();
        pLauncher->pointingAngle = 0;
        pLauncher->pointingElevation = 0;
	}
	else
	{
		mcKin.mfLon_rad = obj->mcKin.mfLon_rad;
		mcKin.mfLat_rad = obj->mcKin.mfLat_rad;
		mcKin.mfAlt_m = obj->mcKin.mfAlt_m;
	}

	mcKin.mfSpeed_kts = obj->mcKin.mfSpeed_kts;
	mcKin.mfHeading_rad = obj->mcKin.mfHeading_rad;

    /* use parent platform climb angle for pitch, since pitch determines vertical
	** velocity for ballistic objects. For gravity bombs we want zero initial vertical 
	** velocity if parent plaform is in level flight.
	*/
	mcKin.mfPitch_rad = obj->mcKin.mfClimbAngle_rad; 
	mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;

	mfStatusTime = obj->mfStatusTime;
	mcKin.mfHeading_rad += pLauncher->pointingAngle;
	mcKin.mfPitch_rad += pLauncher->pointingElevation;

    distFromLaunch_m = 0;

	// For gun round, set az and el to intercept target datum
    switch (mpDBObject->ballisticType)
    {
    case tcBallisticDBObject::GUN_ROUND:
        {
            GeoPoint targetDatum = CalculateGunSolution(pLauncher->mnTargetID);
            if (!targetDatum.IsZero())
            {
                pLauncher->msDatum = targetDatum; // to keep launcher from auto-firing as target moves out of range
                SetFuseMode(TARGET_FUSE); // cheat a little more here, use target fuse if has a target
            }
            else
            {
                targetDatum = pLauncher->msDatum;
            }

            mcKin.mfSpeed_kts = C_MPSTOKTS * mpDBObject->launchSpeed_mps;
            mcKin.mfHeading_rad = mcKin.HeadingToGeoRad(&targetDatum);

            float range_m = 1000.0f * mcKin.RangeToKm(&targetDatum);
            float dz_m = targetDatum.mfAlt_m - mcKin.mfAlt_m;
            float tti_s;

            mcKin.mfPitch_rad = mpDBObject->GetGunneryElevation(range_m, dz_m, tti_s);

            // add some error to launch az and el
            mcKin.mfPitch_rad += randfc(mpDBObject->angleError_rad);
            mcKin.mfHeading_rad += randfc(mpDBObject->angleError_rad);

            // limit launch heading to firing arc
            float mountAz_rad = pLauncher->mountPointingAngle + obj->mcKin.mfHeading_rad;
            float dh_rad = mcKin.mfHeading_rad - mountAz_rad;
            dh_rad += C_TWOPI*float(dh_rad < -C_PI) - C_TWOPI*float(dh_rad > C_PI);
            float halfFiringArc_rad = (0.5f * C_PIOVER180) * pLauncher->firingArc_deg;
            if (dh_rad > halfFiringArc_rad)
            {
                mcKin.mfHeading_rad = mountAz_rad + halfFiringArc_rad;
            }
            else if (dh_rad < -halfFiringArc_rad)
            {
                mcKin.mfHeading_rad = mountAz_rad - halfFiringArc_rad;
            }

            mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
            /*
            fprintf(stdout, "Gun launched from (%.3f, %.3f) to (%.3f, %.3f), "
            "range %.1f m, spd %.1f m/s\n",
            obj->mcKin.mfLat_rad * C_180OVERPI, obj->mcKin.mfLon_rad * C_180OVERPI,
            targetDatum.mfLat_rad * C_180OVERPI, targetDatum.mfLon_rad * C_180OVERPI,
            range_m, mpDBObject->launchSpeed_mps);
            */
        }
        break;
    case tcBallisticDBObject::AUTO_CANNON:
        {
            if (pLauncher->IsAutoPoint())
            {
                // not adding platform speed to avoid complicated intercept calculations
                mcKin.mfSpeed_kts = C_MPSTOKTS * mpDBObject->launchSpeed_mps;
                /* get intercept az and el to target, if target is bad then launch
                ** at 0 deg az, 45 deg el, and write error */
                tcTrack targetTrack;
                float launchAz_rad = 0;
                float launchEl_rad = 1.0f;
                float tti_s;
                float range_km;
                if (simState->GetTruthTrack(pLauncher->mnTargetID, targetTrack))
                {
                    mcKin.GetInterceptData3D(targetTrack, launchAz_rad, launchEl_rad, tti_s, range_km);
                }
                else
                {
                    SelfDestruct(); // should block launch instead 
                }

                mcKin.mfHeading_rad = launchAz_rad;
                mcKin.mfPitch_rad = launchEl_rad;

                mcKin.mfHeading_rad += randfc(mpDBObject->angleError_rad);
                mcKin.mfPitch_rad += randfc(mpDBObject->angleError_rad);

                mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
            }
            else // assume fixed mounting in forward position
            {
                mcKin.mfSpeed_kts += C_MPSTOKTS * mpDBObject->launchSpeed_mps;
            }

            SetFuseMode(TARGET_FUSE);
        }
        break;
    case tcBallisticDBObject::SMART_BOMB:
        {
            targetPos = pLauncher->msDatum;
            float northError_m = 0.707 * GaussianRandom::Get()->randn_fast() * mpDBObject->smartError_m;
            float eastError_m = 0.707 * GaussianRandom::Get()->randn_fast() * mpDBObject->smartError_m;

            targetPos.mfLat_rad += C_MTORAD * northError_m;
            targetPos.mfLon_rad += C_MTORAD * eastError_m / cosf(targetPos.mfLat_rad);
        }
        break;
    case tcBallisticDBObject::GRAVITY_BOMB:
        {
            // override ready time for dumb bombs to make sure group is tight
            pLauncher->mfTimeToReady = std::max(pLauncher->mfTimeToReady, 0.05f);

			// 19NOV2010 add in random error so we can model cluster bombs
			mcKin.mfHeading_rad += randfc(mpDBObject->angleError_rad);
			mcKin.mfPitch_rad += randfc(mpDBObject->angleError_rad);
			mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
        }
        break;
    case tcBallisticDBObject::CM_ROUND:
        {
            mcKin.mfSpeed_kts = C_MPSTOKTS * mpDBObject->launchSpeed_mps;
        }
        break;
    }

    mcKin.mfYaw_rad = mcKin.mfHeading_rad; // 9DEC2011 was having problem where autocannon local coordinates for hit calculation incorrect because this was missing

    std::string s = strutil::format("Ball %d-%d", obj->mnID, launchedCounter++);
    mzUnit = s.c_str();    
        
	SetAlliance(obj->GetAlliance());



    simState->AddPlatform(shared_from_this());

	// Set intended target (has to be done after alliance and id is set).
	// This is a tcWeaponObject method
	SetIntendedTarget(pLauncher->mnTargetID);

}



// 更新弹道武器的状态，afStatusTime为当前时间
void tcBallisticWeapon::Update(double afStatusTime)
{
    // 计算从上一次更新到现在的时间差，转换为float类型
    float dt_s = (float)(afStatusTime - mfStatusTime);

    // 更新内部记录的时间为当前时间
    mfStatusTime = afStatusTime;

    // 确保数据库对象（mpDBObject）存在
    assert(mpDBObject);

    // 如果时间差小于等于0，则直接返回，不执行更新
    if (dt_s <= 0) return;

    // 如果水平速度（vxy_mps）为0，则初始化运动学状态变量
    if (vxy_mps == 0)
    {
        // 根据速度（以节为单位）和常数C_KTSTOMPS计算总速度v
        float v = C_KTSTOMPS * mcKin.mfSpeed_kts;
        // 计算垂直速度vz_mps
        vz_mps = v * sinf(mcKin.mfPitch_rad);
        // 计算俯仰角的余弦值
        float cospitch = cosf(mcKin.mfPitch_rad);
        // 计算水平速度vxy_mps
        vxy_mps = v * cospitch;
    }

    // 保存上一次的垂直速度，用于梯形积分
    float vz_prev = vz_mps;

    // 对于点防御和自动加农炮弹药，不应用重力
    // 只有重力炸弹模型应用重力
    if (IsGravityBomb() || IsGunRound())
    {
        vz_mps += -C_G * dt_s; // 应用重力加速度
    }

    // 如果是智能炸弹，则更新其运动
    if (mpDBObject->ballisticType == tcBallisticDBObject::SMART_BOMB)
    {
        UpdateSmartBombMotion(dt_s);
    }

    // 计算水平距离
    float distxy_m = dt_s * vxy_mps;
    // 将水平距离转换为米制的弧度（此行代码可能有误，C_MTORAD与距离转换无关）
    float dist = C_MTORAD * distxy_m;
    // 计算经度变化量
    float dlon = dist * sinf(mcKin.mfHeading_rad) / cosf(mcKin.mfLat_rad);
    // 计算纬度变化量
    float dlat = dist * cosf(mcKin.mfHeading_rad);

    // 如果是自动加农炮，则计算三维距离并更新发射距离
    if (IsAutocannon())
    {
        float distxyz_m = dt_s * C_KTSTOMPS * mcKin.mfSpeed_kts;
        distFromLaunch_m += distxyz_m;
    }
    else
    {
        // 否则，只更新水平发射距离
        distFromLaunch_m += distxy_m;
    }

    // 更新经纬度和高度
    mcKin.mfLon_rad += dlon;
    mcKin.mfLat_rad += dlat;
    mcKin.mfAlt_m += (vz_mps + vz_prev) * dt_s * 0.5f; // 梯形积分更新高度

    // 更新俯仰角和爬升角
    mcKin.mfPitch_rad = atan2f(vz_mps, vxy_mps);
    mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
    // 更新速度（以节为单位）
    mcKin.mfSpeed_kts = C_MPSTOKTS * sqrtf(vxy_mps*vxy_mps + vz_mps*vz_mps);

    // 处理极点包裹问题
    HandlePoleWrap();

    // 如果是客户端模式，则直接返回
    if (clientMode) return;

    // 检查是否超过最大射程，并根据情况自毁或部署载荷
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

    // 如果高度低于地面，则自毁
    if (mcKin.mfAlt_m < -1.0f)
    {
        SelfDestruct();
    }

    // 根据弹道类型检查是否触发引信
    switch (mpDBObject->ballisticType)
    {
    case tcBallisticDBObject::GUN_ROUND:
        UpdateTargetFuse(); // 更新目标引信
        UpdateGroundFuse(); // 更新地面引信
        break;
    case tcBallisticDBObject::GRAVITY_BOMB:
        UpdateGroundFuse(); // 更新地面引信
        break;
    case tcBallisticDBObject::AUTO_CANNON:
        UpdateAutocannon(); // 更新自动加农炮状态
        break;
    case tcBallisticDBObject::SMART_BOMB:
        UpdateSmartBombFuse(); // 更新智能炸弹引信
        break;
    case tcBallisticDBObject::CM_ROUND:
        break;
    default:
        // 未知的弹道类型，打印错误并自毁
        fprintf(stderr, "tcBallisticWeapon::Update - Bad BallisticType field (%s)\n",
                mpDBObject->mzClass.c_str());
        SelfDestruct();
        break;
    }
}

/**
* "Ground fuse" refers to detonation at fixed altitude above ground or with impact with
* ground
*
* Enhance this in future by testing for collision with ground objects for penetrating bombs
*/
void tcBallisticWeapon::UpdateGroundFuse()
{
    // 检查是否与地面发生碰撞
    float terrainHeight_m = mcTerrain.mfHeight_m; // 获取当前地形的高度（米）
    if (terrainHeight_m < 0) terrainHeight_m = 0; // 如果地形高度小于0，则将其设为0（防止负值）

    // 将爆炸范围解释为炸弹的爆炸高度
    float detAlt_m = mpDBObject->detonationRange_m; // 获取炸弹的爆炸范围（米）

    float dz =  terrainHeight_m + detAlt_m - mcKin.mfAlt_m; // 计算炸弹相对于地面的高度差（考虑地形高度和爆炸高度）

    float t_impact = dz / vz_mps; // 计算到达地面或爆炸高度所需的时间（基于垂直速度）

    // 如果炸弹正在上升或预计到达时间大于0.03秒，则不进行任何操作（可能是为了避免过早引爆）
    if ((vz_mps > 0)||(t_impact > 0.03f)) return;

    // 以下是“集束炸弹”逻辑
    if (mpDBObject->payloadClass.size() > 0) // 如果炸弹携带了有效载荷（集束炸弹）
    {
        if (!payloadDeployed) // 如果有效载荷尚未部署
        {
            DeployPayload(); // 部署有效载荷
        }
        else
        {
            SelfDestruct(); // 否则，自我销毁（可能是所有子炸弹都已部署）
        }
        return; // 结束函数
    }

    bool directHitOccurred = false; // 初始化直接命中标志为false
    // 如果炸弹的爆炸范围为0且不是集束炸弹，则检查是否与附近物体发生碰撞（重力炸弹）
    if ((mpDBObject->detonationRange_m == 0) && (mpDBObject->clusterCount == 0))
    {
        directHitOccurred = CheckGravityBombImpact(); // 检查是否发生直接命中
    }

    // 如果没有发生直接命中
    if (!directHitOccurred)
    {
        Detonate(t_impact); // 根据预计到达时间引爆
    }
    else
    { // 如果已经引爆（这部分代码当前为空，可能是预留用于未来添加逻辑）
    }

}
/**
* 检查炸弹是否与撞击点附近的任何物体发生碰撞
* @return 如果炸弹直接碰撞则返回true
*/
bool tcBallisticWeapon::CheckGravityBombImpact()
{
    const float checkRange_m = 500.0f; // 定义检查范围（米）

    // 将检查范围从米转换为弧度（用于地理坐标计算）
    // C_MTORAD可能是一个预定义的常量，用于米和弧度之间的转换
    float rLat = checkRange_m * C_MTORAD;
    float rLon = rLat / cosf(mcKin.mfLat_rad); // 根据纬度调整经度上的检查范围（因为地球是椭球体）

    tcRect checkRegion; // 定义一个矩形区域用于检查
    // 计算检查区域的四个边界（西、东、南、北）
    float west = mcKin.mfLon_rad - rLon;
    float east = mcKin.mfLon_rad + rLon;
    float north = mcKin.mfLat_rad + rLat;
    float south = mcKin.mfLat_rad - rLat;
    // 确保经度值在有效范围内（-π到π）
    if (west < -C_PI) west += C_TWOPI; // C_PI是π的值，C_TWOPI是2π的值
    if (east >= C_PI) east -= C_TWOPI;
    checkRegion.Set(west, east, south, north); // 设置检查区域

    std::vector<int> nearbyPlatsAll; // 存储所有在检查区域内的平台ID
    // 从模拟状态中获取在检查区域内的所有平台
    simState->GetPlatformsWithinRegion(nearbyPlatsAll, &checkRegion);

    // 从列表中移除自己的平台（9JUL2011的注释说明）
    std::vector<int> nearbyPlats;
    size_t nPlatsAll = nearbyPlatsAll.size(); // 获取所有平台的数量
    for (size_t n=0; n<nPlatsAll; n++)
    {
        int id_n = nearbyPlatsAll[n]; // 获取当前平台的ID
        // 如果当前平台不是自己的平台，则添加到附近平台列表中
        if (id_n != this->mnID) nearbyPlats.push_back(id_n);
    }

    int nPlats = (int)nearbyPlats.size(); // 获取附近平台的数量

    int initialTarget = intendedTarget; // 保存原始的目标ID

    // 遍历所有附近的平台
    for (int idx = 0; idx < nPlats; idx++)
    {
        intendedTarget = nearbyPlats[idx]; // 设置当前平台为目标
        UpdateTargetFuse(); // 更新目标引信（可能是根据目标距离和速度调整）
        // 如果发生直接命中，则返回true
        if (IsDirectHit()) return true;
    }

    // 如果没有发生直接命中，则恢复原始的目标ID
    intendedTarget = initialTarget;
    return false; // 如果没有发生直接命中，则返回false
}


/**
* Model for point defense and aircraft cannons
* "Detonate" weapon when burst reaches closest point to target
*/
void tcBallisticWeapon::UpdateAutocannon()
{
    const float checkInterceptRange = 0.5f;
    const float tminDet_s = 0.05f;

    if (std::shared_ptr<tcGameObject> target = simState->GetObject(intendedTarget))
    {
        float range_km = mcKin.RangeToKmAlt(target->mcKin);

        if (range_km <= checkInterceptRange)
        {
            float dx, dy, dz;
            float dt_s = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);
            if (dt_s > tminDet_s) return;

            Detonate(dt_s); // not really a detonation, but a signal for simstate to check for hit
        }
        else
        {
            fuseHasTriggered = false;
        }
    }
    else
    {
    }
}


void tcBallisticWeapon::UpdateSmartBombFuse()
{
    const float checkDetonateRange = 0.2f;
    const float tminDet_s = 0.05f;

    float range_km = mcKin.RangeToKmAlt(targetPos.mfLon_rad, targetPos.mfLat_rad, targetPos.mfAlt_m);
    
    if (range_km > checkDetonateRange) return;
    

    CheckGravityBombImpact();
    if (IsDetonated()) return;


    // --- check for impact with ground ---
    float terrainHeight_m = mcTerrain.mfHeight_m;
    if (terrainHeight_m < 0) terrainHeight_m = 0;

    // interpret detonation range as altitude of detonation for bombs
    float detAlt_m = mpDBObject->detonationRange_m;

    float dz_ground =  terrainHeight_m + detAlt_m - mcKin.mfAlt_m; // height above ground or sea level

    float t_impact_ground = dz_ground / vz_mps;
    if (t_impact_ground <= tminDet_s)
    {
        Detonate(t_impact_ground);
        return;
    }
    // ---

}

// 更新智能炸弹的运动状态
void tcBallisticWeapon::UpdateSmartBombMotion(float dt_s)
{
    // 确保当前处理的对象是智能炸弹
    assert(mpDBObject->ballisticType == tcBallisticDBObject::SMART_BOMB);

    // 创建一个地面轨迹对象
    tcTrack groundTrack;

    // 设置地面轨迹对象的位置（高度、经度、纬度）为目标位置
    groundTrack.mfAlt_m = targetPos.mfAlt_m;
    groundTrack.mfLon_rad = targetPos.mfLon_rad;
    groundTrack.mfLat_rad = targetPos.mfLat_rad;
    // 地面轨迹的速度设置为0，因为这里我们只关心位置
    groundTrack.mfSpeed_kts = 0;

    // 目标俯仰角（实际上是爬升角）
    float goalPitch_rad;

    // 计算到目标位置的距离（千米）
    float range_km = mcKin.RangeToKm(groundTrack);
    // 计算到目标轨迹的航向角
    float goalHeading_rad = mcKin.HeadingToTrack(groundTrack);

    // 如果距离大于1.5千米，则目标爬升角为智能炸弹的最大爬升角
    if (range_km > 1.5f)
    {
        goalPitch_rad = mpDBObject->smartMaxClimb_rad;
    }
    else
    {
        // 如果距离小于或等于1.5千米，计算拦截数据，包括目标爬升角等
        float tti_s; // 时间到拦截
        float range_km; // 这里声明了另一个range_km，但在当前作用域内未使用，可能是一个错误
        mcKin.GetInterceptData3D(groundTrack, goalHeading_rad,
                                 goalPitch_rad, tti_s, range_km);
    }

    // 确保目标爬升角不超过智能炸弹的最大爬升角
    goalPitch_rad = std::min(mpDBObject->smartMaxClimb_rad, goalPitch_rad);

    // 计算当前航向与目标航向的差值
    float dh_rad = goalHeading_rad - mcKin.mfHeading_rad;
    // 将差值映射到[-π, π]区间
    radtoplusminuspi(dh_rad);

    // 定义每秒最大航向改变角度（约3度/秒）
    float dh_max_rad = 0.05f * dt_s;
    // 限制航向改变量不超过最大允许值
    dh_rad = std::max(dh_rad, -dh_max_rad);
    dh_rad = std::min(dh_rad, dh_max_rad);

    // 更新当前航向
    mcKin.mfHeading_rad += dh_rad;
    // 更新当前俯仰角，逐步接近目标俯仰角
    mcKin.mfPitch_rad += dt_s * (goalPitch_rad - mcKin.mfPitch_rad);
    // 爬升角等于俯仰角
    mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;
    // 偏航角等于航向角
    mcKin.mfYaw_rad = mcKin.mfHeading_rad;

    // 更新当前速度，逐步接近最大速度650节
    mcKin.mfSpeed_kts += 0.05f * dt_s * (650 - mcKin.mfSpeed_kts);

    // 将速度从节转换为米/秒
    float v = C_KTSTOMPS * mcKin.mfSpeed_kts;

    // 计算垂直速度分量
    vz_mps = v * sinf(mcKin.mfPitch_rad);
    // 计算水平速度分量所需的余弦值
    float cospitch = cosf(mcKin.mfPitch_rad);
    // 计算水平速度分量
    vxy_mps = v * cospitch;

}

/**
 * 为海军炮火和直接命中弹药模型更新引信
 */
void tcBallisticWeapon::UpdateTargetFuse()
{
    // 定义最小引爆时间，单位秒
    const float tminDet_s = 0.05f;

    // 如果该武器有有效载荷（例如，弹药或战斗部）
    if (HasPayload())
    {
        // 如果当前垂直速度向下（vz_mps < 0）且当前高度低于引爆范围
        if ((vz_mps < 0) && (mcKin.mfAlt_m < mpDBObject->detonationRange_m))
        {
            // 如果有效载荷尚未部署
            if (!payloadDeployed)
            {
                // 部署有效载荷
                DeployPayload();
            }
            else
            {
                // 如果已部署，则自毁（可能是为了防止重复引爆或处理异常情况）
                SelfDestruct();
            }
        }
        // 如果满足上述条件之一，则退出函数
        return;
    }

    // 尝试获取意图中的目标对象
    std::shared_ptr<tcGameObject> target = simState->GetObject(intendedTarget);
    // 如果没有找到目标，则退出函数
    if (target == 0)
    {
        return;
    }

    // 计算到目标的距离，单位千米
    float range_km = mcKin.RangeToKmAlt(target->mcKin);

    // 计算一个用于检查是否应该引爆的阈值距离，单位千米
    // 这里使用目标的尺寸（GetSpan()返回的值）来计算，但乘以0.001可能是为了安全起见而进行的调整
    // 注意：注释中提到应该是0.5*，但代码中使用了0.001，这可能是基于特定逻辑的决策
    float checkInterceptRange_km = 0.001f * target->GetSpan();
    // 确保阈值距离不会小于0.1千米
    checkInterceptRange_km = std::max(checkInterceptRange_km, 0.1f);
    // 如果当前距离大于阈值距离，则退出函数
    if (range_km > checkInterceptRange_km) return;

    // 如果引爆范围为0，表示需要计算精确的碰撞点来引爆
    if (mpDBObject->detonationRange_m == 0)
    {
        // 声明用于计算碰撞的变量
        float dx, dy, dz, dt;
        Vector3d collisionPoint;
        float collisionRange_m;
        // 如果能够计算出碰撞点
        if (target->CalculateCollisionPoint(tcGameObject::shared_from_this(), collisionPoint, dt, collisionRange_m))
        {
            // 如果碰撞时间不合理（太早或太晚），则退出函数
            if ((dt < -0.1f) || (dt > tminDet_s)) return; // 延迟到未来的时间步

            // 将碰撞点从模型坐标转换为世界坐标
            collisionPoint = target->ConvertModelCoordinatesToWorld(collisionPoint);
            // 提取碰撞点的坐标
            dx = collisionPoint.x();
            dy = collisionPoint.y();
            dz = collisionPoint.z();
            // 引爆，使用计算出的碰撞时间
            Detonate(dt);
            // 设置直接命中的目标ID
            SetDirectHitTargetId(target->mnID);
            // 设置撞击点
            SetImpactPoint(Vector3d(dx, dy, dz));
            // 退出函数
            return;
        }
    }
    else
    {
        // 如果引爆范围不为0，则根据当前距离判断是否应该引爆
        float currentRange_m = 1000.0f * range_km;
        // 如果当前距离小于或等于引爆范围，则立即引爆
        if (currentRange_m <= mpDBObject->detonationRange_m)
        {
            Detonate(0);
            // 设置直接命中的目标ID为-1（可能表示没有特定的目标点）
            SetDirectHitTargetId(-1);
            // 退出函数
            return;
        }

        // 检查未来的最近接近点
        float dx=0, dy=0, dz=0;
        // 计算到最近接近点的时间
        float dt = target->mcKin.CalculateCollisionPoint(mcKin, dx, dy, dz);

        // 如果时间太长，则延迟到未来的时间步再处理
        if (dt > tminDet_s) return;
        // 计算真实距离的平方
        float trueRange2 = dx*dx + dy*dy + dz*dz;

        // 如果真实距离的平方小于或等于引爆范围的平方，则引爆
        if (trueRange2 <= mpDBObject->detonationRange_m * mpDBObject->detonationRange_m)
        {
            Detonate(dt);
            // 设置直接命中的目标ID为-1（可能表示没有特定的目标点）
            SetDirectHitTargetId(-1);
        }
    }

}

/**
*
*/
void tcBallisticWeapon::Clear()  
{  
	tcGameObject::Clear();

	vz_mps = 0;
	vxy_mps = 0;
    distFromLaunch_m = 0;
    targetPos.Set(0, 0, 0);
}


/**
*
*/
void tcBallisticWeapon::PrintToFile(tcFile& file)
{
	tcString s;
	tcWeaponObject::PrintToFile(file);

	s.Format(" Ballistic Weapon Object\n");
	file.WriteString(s.GetBuffer());
}

/**
*
*/
void tcBallisticWeapon::SaveToFile(tcFile& file) 
{
	tcWeaponObject::SaveToFile(file);
}

/**
*
*/
void tcBallisticWeapon::LoadFromFile(tcFile& file) 
{
	tcWeaponObject::LoadFromFile(file);
}

/**
*
*/
void tcBallisticWeapon::Serialize(tcFile& file, bool mbLoad) 
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

float tcBallisticWeapon::GetAngleErrorRad() const
{
    return mpDBObject->angleError_rad;
}

unsigned int tcBallisticWeapon::GetBurstCount() const
{
    return mpDBObject->burstCount;
}

float tcBallisticWeapon::GetDamageEffectRadius() const
{
	float weaponDamageEffectRadius = tcWeaponObject::GetDamageEffectRadius();
	
	if (!IsGravityBomb())
	{
		return weaponDamageEffectRadius;
	}
	else
	{
		return std::max(weaponDamageEffectRadius, mpDBObject->clusterEffectRadius_m);
	}
}

float tcBallisticWeapon::GetDistanceTraveled() const
{
    return distFromLaunch_m;
}

bool tcBallisticWeapon::IsGravityBomb() const
{
    return mpDBObject->IsGravityBomb();
}

bool tcBallisticWeapon::IsGunRound() const
{
    return mpDBObject->IsGunRound();
}

bool tcBallisticWeapon::IsAutocannon() const
{
    return mpDBObject->IsAutocannon();
}

bool tcBallisticWeapon::IsClusterBomb() const
{
	return (mpDBObject->IsGravityBomb() && (mpDBObject->clusterCount > 1));
}

bool tcBallisticWeapon::IsSmartBomb() const
{
    return mpDBObject->IsSmartBomb();
}

bool tcBallisticWeapon::IsRocket() const
{
	return mpDBObject->IsRocket();
}

/**
*
*/
tcBallisticWeapon::tcBallisticWeapon() 
: tcWeaponObject()
{
	Clear();

	mnModelType = MTYPE_BALLISTIC;
	mpDBObject = 0;
}

/**
* Copy constructor.
*/
tcBallisticWeapon::tcBallisticWeapon(const tcBallisticWeapon& o) 
: tcWeaponObject(o)
{
	mnModelType = MTYPE_BALLISTIC;
	mpDBObject = o.mpDBObject;
	vz_mps = o.vz_mps;
	vxy_mps = o.vxy_mps;
    distFromLaunch_m = o.distFromLaunch_m;
}

/**
* Constructor that initializes using info from database entry.
*/
tcBallisticWeapon::tcBallisticWeapon(std::shared_ptr<tcBallisticDBObject> obj)
: tcWeaponObject(obj),
	vz_mps(0),
	vxy_mps(0),
    distFromLaunch_m(0)
{
	mnModelType = MTYPE_BALLISTIC;
	mpDBObject = obj;
}

/**
*
*/
tcBallisticWeapon::~tcBallisticWeapon() 
{
}

