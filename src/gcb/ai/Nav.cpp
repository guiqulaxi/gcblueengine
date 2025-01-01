/**
**  @file Nav.cpp
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

#include "ai/Nav.h"
#include "ai/Brain.h"
//#include "scriptinterface/tcPlatformInterface.h"
#include "simmath.h"

#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "tcShipDBObject.h"
#include "tcSubDBObject.h"
#include "tcCarrierObject.h"
#include "tcSurfaceObject.h"
#include "tcSubObject.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif 

using namespace ai;
using scriptinterface::tcPlatformInterface;


/**
* Saves state to command stream
* Used to save waypoints for client to display
*/
tcCommandStream& Nav::operator>>(tcCommandStream& stream)
{
    Route::operator>>(stream);
	
	return stream;
}

/**
* Loads state to command stream
* Used to load waypoints for client to display
*/
tcCommandStream& Nav::operator<<(tcCommandStream& stream)
{
    Route::operator<<(stream);

	return stream;
}



/**
* Read from stream
*/
tcGameStream& Nav::operator<<(tcGameStream& stream)
{
    Task::operator<<(stream);

    Route::operator<<(stream);
    
    return stream;
}

/**
* Write to stream
*/
tcGameStream& Nav::operator>>(tcGameStream& stream)
{
    Task::operator>>(stream);

    Route::operator>>(stream);

    return stream; 
}


void Nav::AddTasksForCurrentWaypoint()
{
    if ((platform != 0) && (currentWaypoint < waypoints.size()))
    {
        for (size_t n=0; n<waypoints[currentWaypoint].tasks.size(); n++)
        {
            platform->GetBrain()->AddTask(waypoints[currentWaypoint].tasks[n], 4.0f, 0);
        }
    }
}



void Nav::AddWaypoint(double lon_rad, double lat_rad, float alt_m, float speed_kts)
{
    Route::AddWaypoint(lon_rad, lat_rad, alt_m, speed_kts);

	platform->GetBrain()->SetNewCommand();
}

void Nav::ClearWaypoints()
{
	if (waypoints.size())
	{
	    platform->GetBrain()->SetNewCommand();
	}

    Route::ClearWaypoints();
}

void Nav::DeleteWaypoint(size_t idx)
{
    if (idx < waypoints.size())
	{
        Route::DeleteWaypoint(idx);
		
		platform->GetBrain()->SetNewCommand();
	}
	else
	{
		fprintf(stderr, "Nav::DeleteWaypoint - bad idx\n");
	}
}

void Nav::EditWaypoint(size_t idx, double lon_rad, double lat_rad, float alt_m, float speed_kts)
{
	if (idx < waypoints.size())
	{
        Route::EditWaypoint(idx, lon_rad, lat_rad, alt_m, speed_kts);
		
		platform->GetBrain()->SetNewCommand();
	}
	else
	{
		fprintf(stderr, "Nav::EditWaypoint - bad idx\n");
	}
}

void Nav::EditWaypointReference(size_t idx, unsigned char referenceMode, long referencePlatform)
{
    Route::EditWaypointReference(idx, referenceMode, referencePlatform);

    platform->GetBrain()->SetNewCommand();
}

/**
* Inserts waypoint before waypoint at idx
*/
void Nav::InsertWaypoint(size_t idx, double lon_rad, double lat_rad, float alt_m, float speed_kts)
{
	if (idx < waypoints.size())
	{
        Route::InsertWaypoint(idx, lon_rad, lat_rad, alt_m, speed_kts);
		
		platform->GetBrain()->SetNewCommand();
	}
	else
	{
		fprintf(stderr, "Nav::InsertWaypoint - bad idx\n");
	}
}

void Nav::SetRoute(const Route* route)
{
    Route::operator=(*route);
}




    /**
 * 更新导航任务的状态。
 * 这个函数是导航任务的核心，负责根据当前位置和目标航点计算出正确的航向和速度。
 * 它还负责在到达航点时更新任务状态，包括添加新的任务或结束当前任务。
 *
 * @param t 当前的时间，用于确定是否需要更新任务状态。
 */
    void Nav::Update(double t)
{
    // 如果当前时间还没有到达下一个更新间隔，直接返回
    if (!IsReadyForUpdate(t)) return;

    // 检查是否已经到达了航点列表的末尾
    if (currentWaypoint >= waypoints.size())
    {
        // 如果设置了循环模式，则回到第一个航点
        if (loop)
        {
            currentWaypoint = 0;
            // 确保至少有一个航点存在
            assert(waypoints.size() > 0);
        }
        // 如果没有设置循环模式，则结束任务
        else
        {
            EndTask();
            return;
        }
    }

    // 更新所有相对航点的坐标
    for (size_t n=0; n<waypoints.size(); n++)
    {
        Route::UpdateRelativeWaypointCoordinate(n);
    }

    // 如果连接被其他高优先级任务锁定，则返回
    if (!Write("ConnLock", "")) return;

    // 确保平台对象存在
    if (platform == 0)
    {
        assert(false);
        return;
    }

    // 获取当前航点的数据
    WaypointData& waypointData = waypoints[currentWaypoint];

    // 获取当前航点的经度和纬度
    double lon_rad = waypointData.waypoint.mfLon_rad;
    double lat_rad = waypointData.waypoint.mfLat_rad;

    // 计算从当前位置到目标航点的航向和距离
    float heading_deg = platform->GetHeadingToDatum(lon_rad, lat_rad);
    float range_m = 1000.0f * platform->GetRangeToDatum(lon_rad, lat_rad);
    // 将速度从节转换为米/秒
    float speed_mps = C_KTSTOMPS * platform->mcKin.mfSpeed_kts;
    // 计算预计到达时间（秒）
    float eta_s = (speed_mps > 0) ? (range_m / speed_mps) : 9999.0f;

    // 应用前一个航点的速度和高度命令
    if (currentWaypoint > 0)
    {
        float alt_m = waypoints[currentWaypoint-1].waypoint.mfAlt_m;
        float speed_kts = waypoints[currentWaypoint-1].speed_kts;
        if (speed_kts > 0) platform->SetSpeed(speed_kts);
        if ((alt_m > 0) || ((alt_m < 0) && platform->IsSub()))
        {
            platform->SetAltitude(alt_m);
        }
    }

    // 根据预计到达时间调整更新间隔
    if (eta_s >= 30.0f)
    {
        SetUpdateInterval(20.0f);
    }
    else if (eta_s >= 2.0f)
    {
        SetUpdateInterval(1.0f);
    }
    else
    {
        bool isLastWaypoint = (currentWaypoint == (waypoints.size()-1)) && (!loop);

        SetUpdateInterval(1.0f);

        // 设置当前航点的速度和高度
        float alt_m = waypointData.waypoint.mfAlt_m;
        float speed_kts = waypointData.speed_kts;
        if (speed_kts > 0)
        {
            platform->SetSpeed(speed_kts);
        }
        else if (isLastWaypoint && (platform->IsHelo() || (platform->IsGroundVehicle())))
        {
            platform->SetSpeed(0); // 命令直升机悬停或地面车辆停止
        }

        if ((alt_m > 0) || ((alt_m < 0) && platform->IsSub()))
        {
            platform->SetAltitude(alt_m);
        }

        // 为当前航点添加任务
        AddTasksForCurrentWaypoint();
        // 移动到下一个航点
        currentWaypoint++;
    }

    // 设置平台的航向
    platform->SetHeading(heading_deg);

    // 标记当前时间为最后更新时间
    FinishUpdate(t);
}


Nav::Nav(std::shared_ptr<tcPlatformObject> platform_, Blackboard* bb, 
                                   long id_, double priority_, int attributes_, const std::string& taskName_)
: Task(platform_, bb, id_, priority_, attributes_, taskName_),
  Route()
{
    assert(platform);
    Route::SetPlatformId(platform->mnID);

    // set up automatic path finding
    if ((typeid(*platform) == typeid(tcCarrierObject)) ||
        (typeid(*platform) == typeid(tcSurfaceObject)))
    {
        if (std::shared_ptr<tcShipDBObject> shipData = std::dynamic_pointer_cast<tcShipDBObject>(platform->mpDBObject))
        {
            SetMaxPathAltitude_m(-(shipData->draft_m + 3.0f));
        }
    }


    if (typeid(*platform) == typeid(tcSubObject))
    {
        SetMaxPathAltitude_m(-18.0f);
    }
}



Nav::~Nav()
{
}



