/** 
**  @file tcFormation.cpp
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

#include "tcFormation.h"
#include "tcGameObject.h"
#include "tcPlatformObject.h"
#include "tcAeroAirObject.h"
#include "tcAirObject.h"
#include "tcPlatformDBObject.h"
#include "tcJetDBObject.h"
#include "tcSimState.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "tcScenarioLogger.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif



/**
* Load from stream
*/
tcCommandStream& tcFormation::operator<<(tcCommandStream& stream)
{
    char nFormationMode;
    stream >> nFormationMode;
    formationMode = (FormationMode)nFormationMode;

    stream >> isActive;
    stream >> useNorthBearing;
    stream >> leaderId;
    stream >> range_center_km;
    stream >> range_span_km;
    stream >> bearing_center_rad;
    stream >> bearing_span_rad;
	stream >> altitudeOffset_m;

    followers.clear();
    unsigned char nFollowers;
    stream >> nFollowers;

    for (unsigned char k=0; k<nFollowers; k++)
    {
        long id;
        stream >> id;
        followers.push_back(id);
    }

    return stream;
}

/**
* Save to stream
*/
tcCommandStream& tcFormation::operator>>(tcCommandStream& stream)
{
    char nFormationMode = (char)formationMode;
    stream << nFormationMode;

    stream << isActive;
    stream << useNorthBearing;
    stream << leaderId;
    stream << range_center_km;
    stream << range_span_km;
    stream << bearing_center_rad;
    stream << bearing_span_rad;
	stream << altitudeOffset_m;

    assert(followers.size() < 256);
    unsigned char nFollowers = (unsigned char)followers.size();
    stream << nFollowers;

    for (unsigned char k=0; k<nFollowers; k++)
    {
        stream << followers[k];
    }

    return stream;
}


/**
* Load from stream
*/
tcGameStream& tcFormation::operator<<(tcGameStream& stream)
{
    char nFormationMode;
    stream >> nFormationMode;
    formationMode = (FormationMode)nFormationMode;

    stream >> isActive;
    stream >> useNorthBearing;
    stream >> leaderId;
    stream >> range_center_km;
    stream >> range_span_km;
    stream >> bearing_center_rad;
    stream >> bearing_span_rad;
	stream >> altitudeOffset_m;

    followers.clear();
    unsigned char nFollowers;
    stream >> nFollowers;

    for (unsigned char k=0; k<nFollowers; k++)
    {
        long id;
        stream >> id;
        followers.push_back(id);
    }

    return stream;
}

/**
* Save to stream
*/
tcGameStream& tcFormation::operator>>(tcGameStream& stream)
{
    char nFormationMode = (char)formationMode;
    stream << nFormationMode;

    stream << isActive;
    stream << useNorthBearing;
    stream << leaderId;
    stream << range_center_km;
    stream << range_span_km;
    stream << bearing_center_rad;
    stream << bearing_span_rad;
	stream << altitudeOffset_m;

    assert(followers.size() < 256);
    unsigned char nFollowers = (unsigned char)followers.size();
    stream << nFollowers;

    for (unsigned char k=0; k<nFollowers; k++)
    {
        stream << followers[k];
    }

    return stream;
}



void tcFormation::AddFollower(long id)
{
    assert(IsLeader());

    followers.push_back(id);

    SetNewCommand();
}

void tcFormation::Clear()
{
    isActive = false; ///< true if formation is active
    useNorthBearing = false;
    leaderId = -1;
    range_center_km = 2.0f;
    range_span_km = 1.5f;
    bearing_center_rad = 0.2f;
    bearing_span_rad = 0.4f;
    lastUpdateTime = 0;
    repositioning = false;
	formationMode = FOLLOW;
    followers.clear();
    hasNewCommand = false;
}


void tcFormation::ClearNewCommand()
{
    hasNewCommand = false;
}

/**
 * 计算并返回拦截目标的航向（以弧度为单位）。
 *
 * @param tgt_east_m 目标相对于自身的东向位置（米）
 * @param tgt_north_m 目标相对于自身的北向位置（米）
 * @param tgt_heading_rad 目标的当前航向（弧度）
 * @param tgt_speed_mps 目标的速度（米/秒）
 * @param own_speed_mps 自身速度（米/秒）
 * @param valid 输出参数，指示计算结果是否有效（能否拦截）
 * @return 拦截目标的航向（弧度）
 */
float tcFormation::GetInterceptHeading(float tgt_east_m, float tgt_north_m, float tgt_heading_rad,
                                       float tgt_speed_mps, float own_speed_mps, bool& valid)
{
    valid = false; // 初始化有效标志为假

    // 计算目标与自身之间的直线距离
    float range_m = sqrtf(tgt_east_m*tgt_east_m + tgt_north_m*tgt_north_m);
    // 计算距离的倒数，用于后续计算
    float inv_range_m = 1.0 / range_m;

    // 计算目标相对于自身的单位向量的东向分量
    float ke = tgt_east_m * inv_range_m;
    // 计算目标相对于自身的单位向量的北向分量
    float kn = tgt_north_m * inv_range_m;

    // 计算目标在其当前航向上的东向速度分量
    float ve = sinf(tgt_heading_rad) * tgt_speed_mps;
    // 计算目标在其当前航向上的北向速度分量
    float vn = cosf(tgt_heading_rad) * tgt_speed_mps;

    // 计算二次方程的系数a（与目标速度无关，仅与位置关系有关）
    float a = ke*ke + kn*kn;
    // 计算二次方程的系数b（与目标速度和位置关系都有关）
    float b = 2.0f*ke*ve + 2.0f*kn*vn;
    // 计算二次方程的系数c（与双方速度有关）
    float c = ve*ve + vn*vn - own_speed_mps*own_speed_mps;

    // 计算二次方程的判别式
    float det_arg = b*b - 4.0f*a*c;
    // 如果判别式大于等于0，表示有解
    if (det_arg >= 0)
    {
        // 计算判别式的平方根
        float det = sqrtf(det_arg);
        // 根据a的正负选择公式计算alpha
        float alpha = (a > 0) ? (det - b) / (2.0f*a) : (-det - b) / (2.0f*a);
        // 计算拦截时的东向速度分量
        float ve_int = ve + alpha*ke;
        // 计算拦截时的北向速度分量
        float vn_int = vn + alpha*kn;

        // 如果alpha大于0，表示可以在未来某时刻拦截目标
        valid = (alpha > 0);

        // 使用atan2函数计算拦截航向（注意这里ve_int, vn_int可能接近0，但atan2能处理这种情况）
        return atan2f(ve_int, vn_int);
    }
    else
    {   // 如果没有解，即不存在拦截路径，则直接返回指向目标的航向
        return atan2f(tgt_east_m, tgt_north_m);
    }
}

/**
* @param tgt_east_m east position of target - east pos of self
* @param tgt_north_m north pos of target - north pos of self
* @return intercept heading in rad
*/
float tcFormation::GetLazyInterceptHeading(float tgt_east_m, float tgt_north_m, float tgt_heading_rad, 
        float tgt_speed_mps, float& own_speed_mps, bool& valid)
{
    valid = false;

    float range_m = sqrtf(tgt_east_m*tgt_east_m + tgt_north_m*tgt_north_m);
    float inv_range_m = 1.0 / range_m;
    
    float ke = tgt_east_m * inv_range_m;
    float kn = tgt_north_m * inv_range_m;

    float ve = sinf(tgt_heading_rad) * tgt_speed_mps;
    float vn = cosf(tgt_heading_rad) * tgt_speed_mps;

    float b = ke*ve + kn*vn;

    if (b < 0)
    {
        float alpha = -b;
        float ve_int = ve + alpha*ke;
        float vn_int = vn + alpha*kn;

        valid = (alpha > 0.5f);

        own_speed_mps = sqrtf(ve_int*ve_int + vn_int*vn_int);

        return atan2f(ve_int, vn_int);
    }
    else
    {
        return 0;
    }
}

/**
* Version that solves for given speed instead of minimizing speed
*
* @param tgt_east_m east position of target - east pos of self
* @param tgt_north_m north pos of target - north pos of self
* @return intercept heading in rad
*/
float tcFormation::GetLazyInterceptHeadingFixedSpeed(float tgt_east_m, float tgt_north_m, float tgt_heading_rad, 
        float tgt_speed_mps, float own_speed_mps, bool& valid)
{
    valid = false;

    float range_m = sqrtf(tgt_east_m*tgt_east_m + tgt_north_m*tgt_north_m);
    float inv_range_m = 1.0 / range_m;
    
    float ke = tgt_east_m * inv_range_m;
    float kn = tgt_north_m * inv_range_m;

    float ve = sinf(tgt_heading_rad) * tgt_speed_mps;
    float vn = cosf(tgt_heading_rad) * tgt_speed_mps;

    float b = ke*ve + kn*vn;

    if (b > 0) return 0;

    float det = b*b - (tgt_speed_mps*tgt_speed_mps - own_speed_mps*own_speed_mps);
    if (det > 0)
    {
        float alpha = -b - sqrtf(det);
        float ve_int = ve + alpha*ke;
        float vn_int = vn + alpha*kn;

        return atan2f(ve_int, vn_int);
    }
    else
    {
        return 0;
    }
}


/**
* 版本用于解决拦截时的接近速度问题
*
* @param tgt_east_m 目标相对于自身的东向位置差
* @param tgt_north_m 目标相对于自身的北向位置差
* @param tgt_heading_rad 目标的航向（弧度）
* @param tgt_speed_mps 目标的速度（米/秒）
* @param own_speed_mps [out] 自身应达到的速度（米/秒），通过计算得出
* @param closingSpeed_mps 接近速度（即两物体相互接近的速度，米/秒）
* @param valid [out] 布尔值，表示计算是否有效
* @return 拦截航向（弧度）
*/
float tcFormation::GetLazyInterceptHeadingClosingSpeed(float tgt_east_m, float tgt_north_m, float tgt_heading_rad,
                                                       float tgt_speed_mps, float& own_speed_mps, float closingSpeed_mps, bool& valid)
{
    valid = true; // 初始化有效标志为true

    // 计算目标与自身之间的直线距离（米）
    float range_m = sqrtf(tgt_east_m*tgt_east_m + tgt_north_m*tgt_north_m);
    // 计算距离的倒数，用于后续计算方向分量
    float inv_range_m = 1.0 / range_m;

    // 计算目标相对于自身的东向单位向量分量
    float ke = tgt_east_m * inv_range_m;
    // 计算目标相对于自身的北向单位向量分量
    float kn = tgt_north_m * inv_range_m;

    // 计算目标在自身坐标系下的东向速度分量
    float ve = sinf(tgt_heading_rad) * tgt_speed_mps;
    // 计算目标在自身坐标系下的北向速度分量
    float vn = cosf(tgt_heading_rad) * tgt_speed_mps;

    // 计算拦截时自身应达到的东向速度分量，考虑接近速度
    float ve_int = ve + closingSpeed_mps*ke;
    // 计算拦截时自身应达到的北向速度分量，考虑接近速度
    float vn_int = vn + closingSpeed_mps*kn;

    // 计算自身为了达到拦截点所需的速度（米/秒）
    own_speed_mps = sqrtf(ve_int*ve_int + vn_int*vn_int);

    // 返回拦截航向（弧度），即自身应达到的航向
    return atan2f(ve_int, vn_int);
}


const tcPlatformObject* tcFormation::GetLeader(const tcPlatformObject* platform) const
{
    assert(platform != 0);

    if (platform != 0)
    {
        return dynamic_cast<const tcPlatformObject*>(platform->simState->GetObject(leaderId));
    }
    else
    {
        return 0;
    }
}

// tcFormation类的成员函数，用于计算当前平台与领队之间的位置误差
void tcFormation::GetPositionError(tcPlatformObject* platform,
                                   float& drange_km, float& dbearing_rad, float& deast_km, float& dnorth_km,
                                   tcKinematics& leaderKin)
{
    // 通过领队ID从模拟状态中获取领队对象
    tcGameObject* leader = platform->simState->GetObject(leaderId);
    // 如果领队对象不存在，则断言失败（这里假设leaderId是有效的）
    if (leader == 0)
    {
        assert(false); // 断言失败，表明存在逻辑错误或配置错误
        return; // 提前退出函数
    }

    // 获取领队的运动学状态，并赋值给leaderKin
    leaderKin = leader->mcKin;

    // 计算当前平台与领队之间的实际距离（千米）
    float range_km = leaderKin.RangeToKm(platform->mcKin);
    // 计算当前平台相对于领队的地理方位角（弧度）
    float bearing_rad = leaderKin.HeadingToGeoRad(platform->mcKin.mfLon_rad, platform->mcKin.mfLat_rad);

    // 计算距离误差（当前距离与期望中心距离之差）
    float range_error_km = range_km - range_center_km;

    // 计算有效方位角（考虑是否直接使用北向或相对于领队朝向的方位角）
    float effectiveBearing = useNorthBearing ? bearing_center_rad : bearing_center_rad + leaderKin.mfHeading_rad;
    // 确保有效方位角在[-π, π)范围内
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    // 计算方位角误差（当前方位角与有效方位角之差）
    float bearing_error_rad = bearing_rad - effectiveBearing;
    // 确保方位角误差在[-π, π)范围内
    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;

    // 计算当前平台相对于领队的北向和东向距离（千米）
    float north_km = cosf(bearing_rad)*range_km;
    float east_km = sinf(bearing_rad)*range_km;

    // 计算领队与期望位置（即目标位置）之间的北向和东向距离（千米）
    float goal_north_km = cosf(effectiveBearing) * range_center_km;
    float goal_east_km = sinf(effectiveBearing) * range_center_km;

    // 设置输出参数：距离误差、方位角误差、东向距离误差、北向距离误差
    drange_km = range_error_km;
    dbearing_rad = bearing_error_rad;
    deast_km = goal_east_km - east_km;
    dnorth_km = goal_north_km - north_km;
}


bool tcFormation::HasNewCommand() const
{
    return hasNewCommand;
}

/**
* @return true if this formation is active as a follower
*/
bool tcFormation::IsFollower() const
{
    return (isActive && (leaderId != -1));
}


bool tcFormation::IsInPosition(tcPlatformObject* platform, float bearing_rad, float range_km) const
{
    const tcPlatformObject* leader = GetLeader(platform);
    assert(leader != 0);
    if (leader == 0) return false;

    float range_error_km = range_km - range_center_km;

    float effectiveBearing = 
        useNorthBearing ? bearing_center_rad : bearing_center_rad + leader->mcKin.mfHeading_rad;
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    float bearing_error_rad = bearing_rad - effectiveBearing;

    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;

    bool inPosition = (fabsf(range_error_km) < 0.5*range_span_km) && (fabsf(bearing_error_rad) < 0.5*bearing_span_rad);

    return inPosition;
}

/**
* Version to allow a little slop for mouse clicking
*/
bool tcFormation::IsInPositionLoose(tcPlatformObject* platform, float bearing_rad, float range_km) const
{
    const tcPlatformObject* leader = GetLeader(platform);
    assert(leader != 0);
    if (leader == 0) return false;

    float range_error_km = range_km - range_center_km;

    float effectiveBearing = 
        useNorthBearing ? bearing_center_rad : bearing_center_rad + leader->mcKin.mfHeading_rad;
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    float bearing_error_rad = bearing_rad - effectiveBearing;

    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;

    bool inPosition = (fabsf(range_error_km) < (0.55*range_span_km + 0.25)) && (fabsf(bearing_error_rad) < 0.5*(bearing_span_rad + 0.1));

    return inPosition;
}

/**
* Version to allow a little slop for mouse clicking
* On triggers near edges
*/
bool tcFormation::IsInPositionLoose2(tcPlatformObject* platform, float bearing_rad, float range_km, 
                                     float& deltaBearing_rad, float& deltaRange_km) const
{
    deltaBearing_rad = 0;
    deltaRange_km = 0;

    const tcPlatformObject* leader = GetLeader(platform);
    assert(leader != 0);
    if (leader == 0) return false;

    float range_error_km = range_km - range_center_km;

    float effectiveBearing = 
        useNorthBearing ? bearing_center_rad : bearing_center_rad + leader->mcKin.mfHeading_rad;
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    float bearing_error_rad = bearing_rad - effectiveBearing;
    deltaBearing_rad = bearing_error_rad;
    deltaRange_km = range_error_km;

    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;

    bool nearRangeEdge =   ((range_error_km > -0.58f*range_span_km) && (range_error_km < -0.42f*range_span_km))
                        || ((range_error_km > 0.42f*range_span_km) && (range_error_km < 0.58f*range_span_km));

    bool nearBearingEdge = ((bearing_error_rad > -0.58f*bearing_span_rad) && (bearing_error_rad < -0.42f*bearing_span_rad))
                        || ((bearing_error_rad > 0.42f*bearing_span_rad) && (bearing_error_rad < 0.58f*bearing_span_rad));

    return nearRangeEdge || nearBearingEdge;
}



bool tcFormation::IsLeader() const
{
    return (isActive && (leaderId == -1));
}


void tcFormation::LeaveFormation()
{
    if (!isActive) return;

    if (IsLeader())
    {
        RemoveAllFollowers();
        Clear();
    }
    else
    {
        assert(platformId != -1);

        tcSimState* simState = tcSimState::Get();
        if (tcPlatformObject* leader = dynamic_cast<tcPlatformObject*>(simState->GetObject(leaderId)))
        {
            leader->formation.RemoveFollower(platformId);
        }

        Clear();
    }

    SetNewCommand();
}

/**
* Normally called when formation leader is destroyed
*/
void tcFormation::RemoveAllFollowers()
{
    assert(IsLeader());

    tcSimState* simState = tcSimState::Get();

    for (size_t k=0;k<followers.size();k++)
    {
        tcPlatformObject* follower = 
            dynamic_cast<tcPlatformObject*>(simState->GetObject(followers[k]));
        if (follower != 0)
        {
            follower->formation.Clear();
        }
        else
        {
            assert(false); // follower not found or not platformobj
        }
    }

    isActive = false;
    followers.clear();
}


void tcFormation::RemoveFollower(long id)
{
    if (followers.size() == 0)
    {
        isActive = false;
        SetNewCommand();
        return;
    }

#ifdef _DEBUG
    tcSimState* simState = tcSimState::Get();
    tcPlatformObject* follower = dynamic_cast<tcPlatformObject*>(simState->GetObject(id));
    tcPlatformObject* platform = dynamic_cast<tcPlatformObject*>(simState->GetObject(platformId));
    // in "hostile formation" for intercept, leader doesn't have information about followers
    if ((follower != 0) && (platform != 0) && (follower->GetAlliance() == platform->GetAlliance()))
    {
        assert(IsLeader());
    }
#endif

    std::vector<long> updatedFollowers;
    for (size_t k=0;k<followers.size();k++)
    {
        if (followers[k] != id) updatedFollowers.push_back(followers[k]);
    }

    assert(followers.size() == updatedFollowers.size() + 1);
    followers = updatedFollowers;

    // if no more followers, then de-activate this formation
    if (followers.size() == 0)
    {
        isActive = false;
    }

    SetNewCommand();
}

void tcFormation::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{
    if (!IsFollower()) return;

    tcSimState* simState = tcSimState::Get();
    tcPlatformObject* leader = dynamic_cast<tcPlatformObject*>(simState->GetObject(leaderId));

    if (leader == 0) return;

    std::string s;

    s=strutil::format("leader_id = UI.LookupFriendlyId('%s')", leader->mzUnit.c_str());
    logger.AddScenarioText(s);

    s=strutil::format("UI.SetFormationLeader(leader_id)");
	logger.AddScenarioText(s);

    s=strutil::format("UI.SetFormationMode(%d)", int(formationMode));
	logger.AddScenarioText(s);

    s=strutil::format("UI.SetFormationPosition(%.3f, %.3f, %.3f, %.3f)", 
        range_center_km, range_span_km, bearing_center_rad, bearing_span_rad);
    logger.AddScenarioText(s);

    s=strutil::format("UI.SetFormationAltitudeOffset(%.1f)", altitudeOffset_m);
    logger.AddScenarioText(s);

    s=strutil::format("UI.SetFormationUseNorthBearing(%d)", int(useNorthBearing));
    logger.AddScenarioText(s);
}

void tcFormation::SetAltitudeOffset(float dh_m)
{
    altitudeOffset_m = dh_m;
}


void tcFormation::SetFormationMode(int mode)
{
	if (!isActive || IsLeader()) return;

	switch (mode)
	{
	case FOLLOW:
		break;
	case SPRINTDRIFT:
		maneuverType = DRIFT;
		break;
	default:
		assert(false);
		return;
	}

	formationMode = tcFormation::FormationMode(mode);
}

void tcFormation::SetFormationPosition(float range_km, float span_km, float bearing_rad, float span_rad)
{
    range_center_km = range_km;
    range_span_km = span_km;
    bearing_center_rad = bearing_rad;
    bearing_span_rad = span_rad;
}

void tcFormation::SetUseNorthBearing(bool state)
{
    useNorthBearing = state;
}


void tcFormation::SetNewCommand()
{
    hasNewCommand = true;
}

void tcFormation::SetPlatformId(long id)
{
    platformId = id;
}



void tcFormation::Update(tcPlatformObject* platform)
{
    if (!isActive || IsLeader()) 
    {
        return;
    }

    if (platform->mfStatusTime - lastUpdateTime < 0.5) return;
    lastUpdateTime = platform->mfStatusTime;

	tcGameObject* leader = platform->simState->GetObject(leaderId);
    if ((leader == 0) || (leader->GetDamageLevel() >= 1.0f))
    {
        LeaveFormation();
        return;
    }


    switch (formationMode)
	{
	case FOLLOW:
		UpdateFollow(platform);
		break;
	case SPRINTDRIFT:
		UpdateSprintDrift(platform);
		break;
	default:
		assert(false);
		break;
	}
    
}

/**
* This version for close formation flying for air-to-air refueling. Should
* work for general air formations too
*/
void tcFormation::Update(tcAirObject* air)
{
    if (!IsFollower()) return;

    if (air->mfStatusTime - lastUpdateTime < 0.5) return;
    lastUpdateTime = air->mfStatusTime;

    tcAirObject* leader = dynamic_cast<tcAirObject*>(air->simState->GetObject(leaderId));
    if ((leader == 0) || (leader->GetDamageLevel() >= 1.0f))
    {
        LeaveFormation();
        return;
    }

    tcAeroAirObject* aero = dynamic_cast<tcAeroAirObject*>(air);

    bool isAeroModel = aero != 0;

    // get range and bearing from leader
    const tcKinematics& leaderKin = leader->mcKin;

    float range_km = leaderKin.RangeToKm(air->mcKin);
    float bearing_rad = leaderKin.HeadingToGeoRad(air->mcKin.mfLon_rad, air->mcKin.mfLat_rad);
    float dAlt_m = leaderKin.mfAlt_m + altitudeOffset_m - air->mcKin.mfAlt_m;

    float range_error_km = range_km - range_center_km;

    // bearing of sector center wrt North
    useNorthBearing = false;
    float effectiveBearing = bearing_center_rad + leaderKin.mfHeading_rad; // always use relative bearing for air formation
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    float bearing_error_rad = bearing_rad - effectiveBearing;

    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;


    bool inPosition = false;
    if (repositioning)
    {
        inPosition = (fabsf(range_error_km) < 0.25*range_span_km) && (fabsf(bearing_error_rad) < 0.25*bearing_span_rad);
    }
    else
    {
        inPosition = (fabsf(range_error_km) < 0.5*range_span_km) && (fabsf(bearing_error_rad) < 0.5*bearing_span_rad);
    }

    float climbSpeedOffset_kts = 0; // hack to reduce error while climbing/descending
    if (fabsf(dAlt_m) > 1.0f)
    {
        air->SetAltitude(leaderKin.mfAlt_m + altitudeOffset_m);
        if (dAlt_m > 600.0f) // leader above
        {
            climbSpeedOffset_kts = 50.0f;
        }
        else if (dAlt_m < -600.0f) // leader below
        {
            climbSpeedOffset_kts = -50.0f;
        }
    }

    if (inPosition)
    {
        // adjust goalSpeed_kts for faster accel/decel
        float goalSpeed_kts = leaderKin.mfSpeed_kts;
        float speedError_kts = goalSpeed_kts - air->mcKin.mfSpeed_kts;
        speedError_kts = std::max(speedError_kts, -5.0f);
        speedError_kts = std::min(speedError_kts, 5.0f);
        goalSpeed_kts += 2*speedError_kts;

        air->mcGS.mfGoalHeading_rad = leaderKin.mfHeading_rad;
        air->mcGS.mfGoalSpeed_kts = goalSpeed_kts;
        air->SetSpeed(goalSpeed_kts); // automatically set throttle
        repositioning = false;
        return;
    }

    // not in position, readjust to intercept formation position

    tcTrack formCenter;
    formCenter.mfLat_rad = leaderKin.mfLat_rad;
    formCenter.mfLon_rad = leaderKin.mfLon_rad;

    formCenter.Offset(range_center_km, effectiveBearing);

    float distance_error_km = air->mcKin.RangeToKm(formCenter);

    // distances from leader to ownship
    float north_km = cosf(bearing_rad)*range_km;
    float east_km = sinf(bearing_rad)*range_km;

    // distances from leader to goal position
    float goal_north_km = cosf(effectiveBearing) * range_center_km;
    float goal_east_km = sinf(effectiveBearing) * range_center_km;


    float maxMilitarySpeed_mps = 0;

    if (isAeroModel)
    {
        float fuelRate_kgps = 0;
		aero->CalculateSpeedParams(air->mcKin.mfAlt_m, 1.0, maxMilitarySpeed_mps, fuelRate_kgps, aero->GetDamageLevel(), aero->mpDBObject);
    }
    else
    {
        maxMilitarySpeed_mps = C_KTSTOMPS * air->mpDBObject->mfMaxSpeed_kts;
    }


    bool interceptValid = false;
    float intercept_speed_mps = 0;
    float intercept_hdg_rad = 0;

    
    if (distance_error_km < 5.0f)
    {
        float closingSpeed_mps = 5.0f + 7.0f*distance_error_km;

        intercept_hdg_rad = GetLazyInterceptHeadingClosingSpeed(goal_east_km - east_km, 
            goal_north_km - north_km, leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts,
            intercept_speed_mps, closingSpeed_mps, interceptValid);
    }
    else
    {
        intercept_hdg_rad = GetInterceptHeading(goal_east_km - east_km, goal_north_km - north_km,
            leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, maxMilitarySpeed_mps,
            interceptValid);
        intercept_speed_mps = maxMilitarySpeed_mps;
        if (!interceptValid && isAeroModel)
        {   // try AB
            float fuelRate_kgps = 0;
            float ABspeed_mps = 0;
            aero->CalculateSpeedParams(air->mcKin.mfAlt_m, 1.0, ABspeed_mps, fuelRate_kgps, aero->GetDamageLevel(), aero->mpDBObject);

            intercept_hdg_rad = GetInterceptHeading(goal_east_km - east_km, goal_north_km - north_km,
                leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, ABspeed_mps,
                interceptValid);
            intercept_speed_mps = ABspeed_mps;
        }
    }

    //// intercept for slowing down (only consider if close enough)
    //float intercept_speed_slow_kts = 0;
    //float intercept_hdg_slow_rad = 0;
    //bool slowValid = false;
    //if (distance_error_km < 5.0f)
    //{
    //    intercept_speed_slow_kts = leaderKin.mfSpeed_kts - 10.0f;
    //    float intercept_speed_slow_mps = C_KTSTOMPS*intercept_speed_slow_kts;

    //    intercept_hdg_slow_rad = GetLazyInterceptHeadingFixedSpeed(goal_east_km - east_km, 
    //        goal_north_km - north_km, leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts,
    //        intercept_speed_slow_mps, slowValid);
    //}

    //// intercept for speeding up
    //float intercept_speed_fast_kts = leaderKin.mfSpeed_kts + speed_offset_kts;
    //intercept_speed_fast_kts = std::min(intercept_speed_fast_kts, air->mpDBObject->mfMaxSpeed_kts);
    //bool fastValid = false;
    //float intercept_hdg_fast_rad = GetInterceptHeading(goal_east_km - east_km, goal_north_km - north_km,
    //    leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, C_KTSTOMPS*intercept_speed_fast_kts,
    //    fastValid);

    //float goalSpeed_kts = 0;
    //float goalHeading_rad = 0;
    //if (slowValid)
    //{
    //    // only allow 5 deg deviation from tgt heading for slow intercept hdg
    //    //float dh_rad = intercept_hdg_slow_rad - leaderKin.mfHeading_rad;
    //    //if (dh_rad > C_PI) dh_rad -= C_TWOPI;
    //    //if (dh_rad < -C_PI) dh_rad += C_TWOPI;
    //    //
    //    //if (dh_rad > 0.1f) dh_rad = 0.1f;
    //    //else if (dh_rad < -0.1f) dh_rad = -0.1f;

    //    //goalHeading_rad = leaderKin.mfHeading_rad + dh_rad;

    //    goalHeading_rad = intercept_hdg_slow_rad;
    //    goalSpeed_kts = intercept_speed_slow_kts;

    //}
    //else
    //{            
    //    goalSpeed_kts = intercept_speed_fast_kts + climbSpeedOffset_kts;
    //    goalHeading_rad = intercept_hdg_fast_rad;
    //}

    float goalSpeed_kts = C_MPSTOKTS * intercept_speed_mps;
    float goalHeading_rad = intercept_hdg_rad;

    // adjust goalSpeed_kts for faster accel/decel
    float speedError_kts = goalSpeed_kts - air->mcKin.mfSpeed_kts;
    speedError_kts = std::max(speedError_kts, -10.0f);
    speedError_kts = std::min(speedError_kts, 10.0f);
    goalSpeed_kts += 2*speedError_kts;

    air->mcGS.mfGoalHeading_rad = goalHeading_rad;
    air->mcGS.mfGoalSpeed_kts = goalSpeed_kts;
    air->SetSpeed(goalSpeed_kts);

    repositioning = true;




}


void tcFormation::UpdateFollow(tcPlatformObject* platform)
{
    // 从平台对象的仿真状态中获取领导对象
    tcGameObject* leader = platform->simState->GetObject(leaderId);
    // 如果领导对象为空，则断言失败并返回
    if (leader == 0)
    {
        assert(false);
        return;
    }

    // 获取领导对象的运动学信息
    const tcKinematics& leaderKin = leader->mcKin;

    // 计算当前平台与领导对象之间的距离（千米）
    float range_km = leaderKin.RangeToKm(platform->mcKin);
    // 计算当前平台相对于领导对象的方位角（弧度）
    float bearing_rad = leaderKin.HeadingToGeoRad(platform->mcKin.mfLon_rad, platform->mcKin.mfLat_rad);
    // 计算当前平台与理想位置之间的距离误差（千米）
    float range_error_km = range_km - range_center_km;
    // 计算有效方位角（根据是否使用北方位角进行调整）
    float effectiveBearing = useNorthBearing ? bearing_center_rad : bearing_center_rad + leaderKin.mfHeading_rad;
    // 将有效方位角规范化到[-π, π]范围内
    if (effectiveBearing < -C_PI) effectiveBearing += C_TWOPI;
    else if (effectiveBearing >= C_PI) effectiveBearing -= C_TWOPI;

    // 计算当前平台方位角与有效方位角之间的误差（弧度）
    float bearing_error_rad = bearing_rad - effectiveBearing;
    // 将方位角误差规范化到[-π, π]范围内
    if (bearing_error_rad < -C_PI) bearing_error_rad += C_TWOPI;
    else if (bearing_error_rad >= C_PI) bearing_error_rad -= C_TWOPI;

    // 判断当前平台是否处于目标位置
    bool inPosition = false;
    if (repositioning)
    {
        // 在重新定位过程中，使用更严格的标准
        inPosition = (fabsf(range_error_km) < 0.25*range_span_km) && (fabsf(bearing_error_rad) < 0.25*bearing_span_rad);
    }
    else
    {
        // 不在重新定位过程中，使用较宽松的标准
        inPosition = (fabsf(range_error_km) < 0.5*range_span_km) && (fabsf(bearing_error_rad) < 0.5*bearing_span_rad);
    }

    if (inPosition)
    {
        // 如果在目标位置，则设置目标航向和速度与领导对象相同，并停止重新定位
        platform->mcGS.mfGoalHeading_rad = leaderKin.mfHeading_rad;
        platform->mcGS.mfGoalSpeed_kts = leaderKin.mfSpeed_kts;
        repositioning = false;
    }
    else
    {
        // 计算目标位置（基于领导对象的位置和指定的距离与方位角）
        tcTrack formCenter;
        formCenter.mfLat_rad = leaderKin.mfLat_rad;
        formCenter.mfLon_rad = leaderKin.mfLon_rad;
        formCenter.Offset(range_center_km, effectiveBearing);

        // 计算从领导对象到目标位置的距离误差（千米）
        float distance_error_km = leaderKin.RangeToKm(formCenter);

        // 计算从领导对象到当前平台的北向和东向距离
        float north_km = cosf(bearing_rad)*range_km;
        float east_km = sinf(bearing_rad)*range_km;

        // 计算从领导对象到目标位置的北向和东向距离
        float goal_north_km = cosf(effectiveBearing) * range_center_km;
        float goal_east_km = sinf(effectiveBearing) * range_center_km;

        // 根据距离误差调整速度偏移量
        float speed_offset_kts = 10.0f;
        if (distance_error_km < 4.5f)
        {
            speed_offset_kts = 1.0f + 2*distance_error_km;
        }
        // 计算减速时的拦截航向
        // 定义减速拦截的期望速度（米/秒），初始化为0
        float intercept_speed_slow_mps = 0;
        // 标记减速拦截计算是否有效
        bool slowValid = false;
        // 调用GetLazyInterceptHeading函数计算减速拦截的航向（弧度），
        // 参数包括目标位置与当前位置的差值（东向和北向）、领前者的航向（弧度）、
        // 领前者速度（节转米/秒）、减速拦截的期望速度（米/秒，初始为0，实际值由函数内部计算）、
        // 以及一个标记变量来指示计算是否成功
        float intercept_hdg_slow_rad = GetLazyInterceptHeading(goal_east_km - east_km, goal_north_km - north_km,
                                                               leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, intercept_speed_slow_mps,
                                                               slowValid);
        // 将减速拦截的期望速度从米/秒转换为节
        float intercept_speed_slow_kts = C_MPSTOKTS*intercept_speed_slow_mps;
        // 确保减速拦截的期望速度不小于0节
        intercept_speed_slow_kts = std::max(intercept_speed_slow_kts, 0.0f);
        // 计算加速拦截的期望速度（节），为领前者速度加上一个速度偏移量
        float intercept_speed_fast_kts = leaderKin.mfSpeed_kts + speed_offset_kts;
        // 确保加速拦截的期望速度不超过平台最大速度
        intercept_speed_fast_kts = std::min(intercept_speed_fast_kts, platform->mpDBObject->mfMaxSpeed_kts);
        // 标记加速拦截计算是否有效，这里初始化为false，但稍后可能会被GetInterceptHeading函数修改
        bool fastValid = false;
        // 调用GetInterceptHeading函数计算加速拦截的航向（弧度），
        // 参数与减速拦截类似，但使用了加速拦截的期望速度
        float intercept_hdg_fast_rad = GetInterceptHeading(goal_east_km - east_km, goal_north_km - north_km,
                                                           leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, C_KTSTOMPS*intercept_speed_fast_kts,
                                                           fastValid);
        // 如果减速拦截计算有效
        if (slowValid)
        {
            // 则设置平台的目标航向和速度为减速拦截计算得到的值
            platform->mcGS.mfGoalHeading_rad = intercept_hdg_slow_rad;
            platform->mcGS.mfGoalSpeed_kts = intercept_speed_slow_kts;
        }
        else
        {
            // 否则，使用加速拦截计算得到的目标航向和速度
            platform->mcGS.mfGoalHeading_rad = intercept_hdg_fast_rad;
            platform->mcGS.mfGoalSpeed_kts = intercept_speed_fast_kts;
        }
        // 标记为正在重新定位
        repositioning = true;
    }
}

// tcFormation类的成员函数，用于更新平台在冲刺和漂移机动中的行为
void tcFormation::UpdateSprintDrift(tcPlatformObject* platform)
{
    // 初始化位置误差变量
    float drange_km = 0; // 距离误差（千米）
    float dbearing_rad = 0; // 方位角误差（弧度）
    float deast_km = 0; // 东向距离误差（千米）
    float dnorth_km = 0; // 北向距离误差（千米）
    tcKinematics leaderKin; // 领队的运动学状态

    // 调用GetPositionError函数计算位置误差和获取领队的运动学状态
    GetPositionError(platform, drange_km, dbearing_rad, deast_km, dnorth_km, leaderKin);

    // 如果当前机动类型为漂移
    if (maneuverType == DRIFT)
    {
        // 判断平台是否在指定范围内
        bool inSector = (fabsf(drange_km) < 0.5*range_span_km) && (fabsf(dbearing_rad) < 0.5*bearing_span_rad);

        // 设置平台的目标速度和目标航向为领队的速度和航向
        platform->mcGS.mfGoalSpeed_kts = 3.0f; // 注意：这里硬编码了3.0，可能需要根据实际情况调整
        platform->mcGS.mfGoalHeading_rad = leaderKin.mfHeading_rad;

        // 如果平台不在指定范围内，则改变机动类型为冲刺进入
        if (!inSector) maneuverType = SPRINT_IN;
    }
    // 如果当前机动类型为冲刺进入
    else if (maneuverType == SPRINT_IN)
    {
        // 计算拦截领队所需的速度和航向，直到足够接近
        float intercept_speed_fast_kts = platform->mpDBObject->mfMaxSpeed_kts; // 使用平台的最大速度
        bool fastValid = false; // 用于检查拦截计算是否有效（此代码段中未直接使用）
        float intercept_hdg_fast_rad = GetInterceptHeading(deast_km, dnorth_km,
                                                           leaderKin.mfHeading_rad, C_KTSTOMPS*leaderKin.mfSpeed_kts, C_KTSTOMPS*intercept_speed_fast_kts,
                                                           fastValid); // 调用GetInterceptHeading函数计算拦截航向

        // 设置平台的目标航向和速度
        platform->mcGS.mfGoalHeading_rad = intercept_hdg_fast_rad;
        platform->mcGS.mfGoalSpeed_kts = intercept_speed_fast_kts;

        // 判断平台是否接近指定范围的中心
        bool inSector = (fabsf(drange_km) < 0.2*range_span_km) && (fabsf(dbearing_rad) < 0.2*bearing_span_rad);
        if (inSector) maneuverType = SPRINT_OUT; // 如果在范围内，则改变机动类型为冲刺离开
    }
    // 如果当前机动类型为冲刺离开
    else // SPRINT_OUT
    {
        // 保持航向直到接近扇区边缘，然后漂移
        platform->mcGS.mfGoalHeading_rad = leaderKin.mfHeading_rad; // 保持与领队相同的航向
        platform->mcGS.mfGoalSpeed_kts = leaderKin.mfSpeed_kts + 5.0; // 设置略高于领队的速度

        // 判断平台是否接近扇区外缘
        bool inSectorOuter = (fabsf(drange_km) < 0.3*range_span_km) && (fabsf(dbearing_rad) < 0.3*bearing_span_rad);

        // 如果不在外缘范围内，则改变机动类型为漂移
        if (!inSectorOuter) maneuverType = DRIFT;
    }
}


tcFormation::tcFormation()
:  isActive(false),
   useNorthBearing(false),
   leaderId(-1),
   lastUpdateTime(0),
   repositioning(false),
   hasNewCommand(false),
   platformId(-1),
   altitudeOffset_m(0)
{
}


tcFormation::~tcFormation()
{
}
