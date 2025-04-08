/**
**  @file PointDefense.cpp
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

#include "tcPlatformObject.h"
#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "ai/PointDefense.h"
#include "ai/Brain.h"
//#include "scriptinterface/tcPlatformInterface.h"

#include "simmath.h"
#include "tcSensorMapTrack.h"
#include "tcWeaponDBObject.h"
#include "tcLauncher.h"

#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"

#include <assert.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif 

using namespace ai;


/**
* Saves state to command stream
*/
tcCommandStream& PointDefense::operator>>(tcCommandStream& stream)
{
    return stream;
}

/**
* Loads state to command stream
*/
tcCommandStream& PointDefense::operator<<(tcCommandStream& stream)
{
    return stream;
}



/**
* Read from stream
*/
tcGameStream& PointDefense::operator<<(tcGameStream& stream)
{
    Task::operator<<(stream);
    
    return stream;
}

/**
* Write to stream
*/
tcGameStream& PointDefense::operator>>(tcGameStream& stream)
{
    Task::operator>>(stream);

    return stream; 
}

void PointDefense::GetPointDefenseLaunchers(std::vector<unsigned int>& launchers)
{
    assert(platform != 0);

    unsigned int nLaunchers = platform->GetLauncherCount();
    for (unsigned int n=0; n<nLaunchers; n++)
    {
        std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(n);
        std::shared_ptr<tcWeaponDBObject> weaponData = std::dynamic_pointer_cast<tcWeaponDBObject>(launcher->mpChildDBObj);

        unsigned char launcherStatus = launcher->GetStatus(); // doesn't update, returns last status
        bool statusOkay = true;
        switch (launcherStatus)
        {
        case tcLauncher::BAD_LAUNCHER:
        case tcLauncher::LAUNCHER_EMPTY:
        case tcLauncher::LAUNCHER_BUSY:
        case tcLauncher::LAUNCHER_ERROR:
        case tcLauncher::LAUNCHER_INACTIVE:
        case tcLauncher::NO_FIRECONTROL:
        case tcLauncher::DAMAGED:
        case tcLauncher::LAUNCHER_LOADING:
        case tcLauncher::LAUNCHER_UNLOADING:
        case tcLauncher::LAUNCHER_EMPTY_AUTORELOAD:
            statusOkay = false;
            break;
        default:
            statusOkay = true;
            break;
        }

        if (((launcher->mnTargetFlags & 0x0008) != 0) && (weaponData != 0) && (weaponData->minRange_km < 1.0f) &&
            statusOkay)
        {
            launchers.push_back(n);
        }
    }
}




void PointDefense::GetPointDefenseTargets(std::vector<tcSensorMapTrack>& targets)
{
    const float maxRange_km = 12.0f;
    auto trackList = platform->GetTrackListValidROE(0x0060, maxRange_km);
    for (size_t n=0; n<trackList.size(); n++)
    {
        tcSensorMapTrack& track = trackList[n];
        double staleness_s = track.mfTimestamp - track.GetLastReportTime();
        bool valid = (!track.IsDestroyed()) && (staleness_s < 15.0f);
        if (valid)
        {
            targets.push_back(track);
        }
    }
}

/**
 * 更新点防御任务的状态。
 * 这个函数负责管理平台的点防御系统，包括获取目标、分配发射器和执行发射操作。
 *
 * @param t 当前的时间，用于确定是否需要更新任务状态。
 */
void PointDefense::Update(double t)
{
    // 如果当前时间还没有到达下一个更新间隔，直接返回
    if (!IsReadyForUpdate(t)) return;

    // 检查平台对象是否存在
    if (platform == 0)
    {
        assert(false);
        return;
    }

    // 获取点防御目标
    std::vector<tcSensorMapTrack> targets;
    GetPointDefenseTargets(targets);

    // 如果没有目标，设置较长的更新间隔，然后返回
    if (targets.size() == 0)
    {
        SetUpdateInterval(10.0f);
        return;
    }
    // 如果有目标，设置较短的更新间隔
    else
    {
        SetUpdateInterval(2.0f);
    }

    // 获取可用的发射器
    std::vector<unsigned int> launchers;
    GetPointDefenseLaunchers(launchers);

    // 遍历每个发射器
    for (size_t n=0; n<launchers.size(); n++)
    {
        unsigned int launcher_idx = launchers[n];

        // 获取目标数量
        size_t nTargets = targets.size();
        // 随机偏移量，用于随机选择目标
        size_t random_offset = rand() % nTargets;
        // 标记是否正在寻找目标
        bool lookingForTarget = true;
        // 遍历所有目标
        for (size_t k=0; (k<nTargets) && lookingForTarget; k++)
        {
            // 计算目标索引
            size_t target_idx = (k + random_offset) % nTargets;
            // 获取目标ID
            long targetId = targets[target_idx].mnID;
            // 为发射器指定目标
            platform->DesignateLauncherTarget(targetId, launcher_idx);

            // 获取目标位置
            GeoPoint p(targets[target_idx].mfLon_rad, targets[target_idx].mfLat_rad, targets[target_idx].mfAlt_m);
            // 为发射器指定目标位置
            platform->DesignateLauncherDatum(p, launcher_idx);

            // 获取发射器对象
            std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(launcher_idx);
            // 更新发射器状态
            launcher->UpdateStatus();
            // 获取发射器状态
            unsigned char launcherStatus = launcher->GetStatus();
            // 如果发射器准备就绪，发射导弹
            if (launcherStatus == tcLauncher::LAUNCHER_READY)
            {
                lookingForTarget = false;
                platform->SetLaunch(launcher_idx, 8);
            }
        }
    }

    // 标记当前时间为最后更新时间
    FinishUpdate(t);
}
PointDefense::PointDefense(std::shared_ptr<tcPlatformObject> platform_, Blackboard* bb, 
                                   long id_, double priority_, int attributes_, const std::string& taskName_)
: Task(platform_, bb, id_, priority_, attributes_, taskName_)
{
    assert(platform);
}



PointDefense::~PointDefense()
{
}



