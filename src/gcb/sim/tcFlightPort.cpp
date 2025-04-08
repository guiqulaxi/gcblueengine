/** 
**  @file tcFlightport.cpp 
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

#ifndef WX_PRECOMP
//#include "wx/wx.h"
#endif

#include "tcFlightPort.h"
#include "tcAirObject.h"
#include "tcAeroAirObject.h"
#include "tcHeloObject.h"
#include "tcAirDBObject.h"
#include "tcFlightportDBObject.h"
#include "tcPlatformDBObject.h"
#include "tcCarrierObject.h"
#include "ai/BlackboardInterface.h"
#include "ai/Brain.h"
#include "ai/Task.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "tcPlatformObject.h"
#include "tcLauncher.h"
#include "ai/tcMissionManager.h"
#include "tcTime.h"
#include "tcFloatCompressor.h"
#include "tcOptions.h"
// #include "scriptinterface/tcPlatformInterface.h"
#include "strutil.h"

#include <assert.h>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

/**
*   case HANGAR: return "Hangr";
*   case ALERT15: return "Deck";
*   case ALERT5: return "Runwy";
*   case TRANSIT: return "Trans";
*   default: return "Error";
*/
std::string tcAirState::LocationToString(teLocation loc)
{
    switch (loc) 
    {
    case HANGAR: return "Hangr";
    case ALERT15: return "AL15";
    case ALERT5: return "AL05";
    case PRETAKEOFF: return "PTO";
    case TAKEOFF: return "TO";
    default: return "Error";
    }
}

/**
*   case OP_NONE: return "None";
*   case OP_TRANSIT: return "Transit";
*   case OP_UNLOAD: return "Unload";
*   case OP_LOAD: return "Load";
*   case OP_REPAIR: return "Repair";
*   case OP_MAINTENANCE: return "Maint";
*   default: return "Error";
*/
std::string tcAirState::OperationToString(teOperation op)
{   
    switch (op)
    {
    case OP_NONE: return "None";
    case OP_TRANSIT: return "Transit";
    case OP_UNLOAD: return "Unload";
    case OP_LOAD: return "Load";
    case OP_REPAIR: return "Repair";
    case OP_MAINTENANCE: return "Maint";
    default: return "Error";
    }
}

/**
* Loads state from update stream
*/
tcUpdateStream& tcAirState::operator<<(tcUpdateStream& stream)
{
    bool detailedUpdate = (stream.GetDetailLevel() > 0);
    
    char val;

	stream >> val;
	current_location = (teLocation)val;
	
	stream >> val;
	current_spot = val;

	stream >> val;
	goal_location = (teLocation)val;

	stream >> val;
	goal_spot = val;

	stream >> val;
	op = (teOperation)val;

	float x;
    tcIntervalCompressor intervalCompressor(x, 0.0f, 655350.0f);
    stream >> intervalCompressor;
	ready_time = x;
	
	// if this obj is in a ready or launch spot, then update launcher and fuel state
    if (detailedUpdate || (current_location != HANGAR))
    {
        if (std::shared_ptr<tcPlatformObject> platform = obj)
        {
            size_t nLaunchers = platform->GetLauncherCount();
            for (size_t n=0; n<nLaunchers; n++)
            {
                std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(n);
                launcher->operator<<(stream);

                unsigned char isLoading;
                stream >> isLoading;
                launcher->SetLoadState(isLoading != 0);
            }
            float fuel;
            tcIntervalCompressor intervalCompressor(fuel, 0.0f, 655350.0f);
            stream >> intervalCompressor;
            platform->fuel_kg = fuel;

            char isRefueling;
            stream >> isRefueling;
            platform->SetRefueling(isRefueling != 0);
        }
    }



	return stream;
}

/**
* Saves state to update stream
*/
tcUpdateStream& tcAirState::operator>>(tcUpdateStream& stream)
{
    bool detailedUpdate = (stream.GetDetailLevel() > 0);

    //if (detailedUpdate)
    //{
    //    int jj = 55;
    //}

	char val;

	val = (char)current_location;
	stream << val;

	val = ((char)current_spot);
	stream << val;

	val = ((char)goal_location);
	stream << val;

	val = ((char)goal_spot);
	stream << val;

	val = ((char)op);
	stream << val;

	float x = (float)ready_time;
	stream << tcIntervalCompressor(x, 0.0f, 6500.0f);
	
    if (detailedUpdate || (current_location != HANGAR))
    {
        if (std::shared_ptr<tcPlatformObject> platform = obj)
        {
            size_t nLaunchers = platform->GetLauncherCount();
            for (size_t n=0; n<nLaunchers; n++)
            {
                std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(n);
                launcher->operator>>(stream);

                // additional info that we don't want part of the normal launcher update (could use detail level instead)
                unsigned char isLoading = launcher->IsLoading() ? 1 : 0;
                stream << isLoading;
            }
            float fuel = platform->fuel_kg;
            stream << tcIntervalCompressor(fuel, 0.0f, 655350.0f);

            char isRefueling = platform->IsRefueling() ? 1 : 0;
            stream << isRefueling;
            platform->SetRefueling(isRefueling != 0);
        }
    }


	return stream;
}


/**
* Loads state from game stream
*/
tcGameStream& tcAirState::operator<<(tcGameStream& stream)
{
	char val;

	stream >> val;
    current_location = teLocation(val);

    stream >> val;
	current_spot = int(val);

    stream >> val;
    goal_location = teLocation(val);

    stream >> val;
	goal_spot = int(val);

    stream >> inTransit;

    stream >> val;
    op = teOperation(val);

	stream >> ready_time;

	return stream;
}

/**
* Saves state to game stream
*/
tcGameStream& tcAirState::operator>>(tcGameStream& stream)
{
	char val;

	val = (char)current_location;
	stream << val;

	val = ((char)current_spot);
	stream << val;

	val = ((char)goal_location);
	stream << val;

	val = ((char)goal_spot);
	stream << val;

    stream << inTransit;

	val = ((char)op);
	stream << val;

	stream << ready_time;


	return stream;
}


float tcFlightPort::transitionTimesFast[6][6];
float tcFlightPort::transitionTimesNormal[6][6];


void tcFlightPort::InitTransitionTimes()
{
    for (int m=0; m<6; m++)
    {
        for (int n=0; n<6; n++)
        {
            transitionTimesFast[m][n] = 0;
            transitionTimesNormal[m][n] = 0;
        }
    }

   /*
   NOWHERE = 0,
   HANGAR = 1,   ///< longer term storage or repair
   ALERT15 = 2,    ///< out of hangar, on deck
   ALERT5 = 3,   ///< ready to take off
   PRETAKEOFF = 4, ///< a hack to get a/c to stay in launch spot but take some time to takeoff
   TAKEOFF = 5   ///< move to launch and take off
   */
   transitionTimesFast[HANGAR][ALERT15] = 60.0f;
   transitionTimesFast[HANGAR][ALERT5] = 120.0f;
   transitionTimesFast[HANGAR][TAKEOFF] = 180.0f;
   transitionTimesFast[ALERT15][ALERT5] = 60.0f;
   transitionTimesFast[ALERT15][TAKEOFF] = 120.0f;
   // these are all the same state transitions (why?? 23AUG2009)
   transitionTimesFast[ALERT5][PRETAKEOFF] = 60.0f;
   transitionTimesFast[PRETAKEOFF][TAKEOFF] = 60.0f;
   transitionTimesFast[ALERT5][TAKEOFF] = 60.0f; 

   transitionTimesNormal[HANGAR][ALERT15] = 900.0f; // 15 min to move from "hangar" to ready (alert30 to alert15)
   transitionTimesNormal[HANGAR][ALERT5] = 1500.0f;
   transitionTimesNormal[HANGAR][TAKEOFF] = 1800.0f;
   transitionTimesNormal[ALERT15][ALERT5] = 600.0f; // alert15 to alert5
   transitionTimesNormal[ALERT15][TAKEOFF] = 900.0f;
   // these are all the same state transitions
   transitionTimesNormal[ALERT5][PRETAKEOFF] = 300.0f; // 5 minutes to takeoff from alert5
   transitionTimesNormal[PRETAKEOFF][TAKEOFF] = 300.0f; // 5 minutes to takeoff from alert5
   transitionTimesNormal[ALERT5][TAKEOFF] = 300.0f; // 5 minutes to takeoff from alert5



}

/**
* Loads state from update stream
* Objects that are not updated are deleted
*/
tcUpdateStream& tcFlightPort::operator<<(tcUpdateStream& stream)
{
	static tcAirState tempAirState;

    unsigned int updateTimestamp = tcTime::Get()->GetUpdated30HzCount();

	unsigned short nChildren = GetCount();

    unsigned char detailedUpdate;
    stream >> detailedUpdate;

    if (detailedUpdate == 1)
    {
        stream.SetDetailLevel(1);
    }
    else
    {
        stream.SetDetailLevel(0);
    }

	unsigned char nUpdate;	
	stream >> nUpdate;


	unsigned short updateIdx = 0;
	unsigned short childIdx = 0;
	unsigned nUpdated = 0;

	while ((updateIdx < nUpdate))
	{
		short int updateId;
		stream >> updateId;

		bool foundMatch = false;
		childIdx = 0;
		while ((!foundMatch) && (childIdx < nChildren))
		{
			tcAirState* airState = GetAirState(childIdx);
			std::shared_ptr<tcGameObject> obj = airState->obj;
			assert(obj);

			short int childId = (short)obj->mnID;
			if (childId == updateId)
			{
				*airState << stream;
                airState->lastMultiplayerUpdate = updateTimestamp;

				foundMatch = true;
				nUpdated++;
			}
			childIdx++;
		}

        if (!foundMatch)
        {
            parent->SetRecreate(true); // request re-create
        }

		updateIdx++;
	}

	for ( ; updateIdx < nUpdate; updateIdx++)
	{
		tempAirState << stream;
	}


	ResyncSpots();

	/* request recreate if not all updates were matched (new child)
	** or if not all children were update (deleted child)
	** In future, would be more efficient to have messages to selectively add
	** and delete children vs. re-creating all of the children.
	*/
	//if ((nUpdated < nUpdate) || (nUpdated < nChildren))
	//{
	//	parent->SetRecreate(true);
	//}

	/*
	std::vector<tcAirState*>::iterator iter = units.begin();
	while (iter != units.end())
	{
		if ((*iter)->obj == 0)
		{
			units.erase(iter++);
		}
		else
		{
			++iter;
		}
	}
	*/

    return stream;
}

/**
* Saves state to update stream
* Do partial update if stream size limit is reached
*/
tcUpdateStream& tcFlightPort::operator>>(tcUpdateStream& stream)
{
    // if freeSpace < 0, the message should be rejected anyway so don't worry about special case
    // for this
    long freeSpace = stream.GetMaxSize() - stream.size() - 2; // 1 byte for update count header, 1 for detailedUpdate

    tcUpdateStream tempStream1;
    tcUpdateStream tempStream2;

    unsigned char detailedUpdate;
    if (stream.GetDetailLevel() > 0)
    {
        detailedUpdate = 1;
    }
    else
    {
        detailedUpdate = 0;
    }


    unsigned short nChildren = GetCount();
    if (nextUpdateIdx >= nChildren) nextUpdateIdx = 0;

    unsigned char nUpdates = 0;

	//stream << nChildren;

    while ((nextUpdateIdx < nChildren) && (freeSpace > 0))
	{
        tempStream1.clear();
        tempStream1.SetDetailLevel(stream.GetDetailLevel());

		tcAirState* airState = GetAirState(nextUpdateIdx);
		std::shared_ptr<tcGameObject> obj = airState->obj;
		assert(obj);

		short int localId = (short int)obj->mnID;
		tempStream1 << localId;

        *airState >> tempStream1;

        if ((long)tempStream1.size() <= freeSpace)
        {
            tempStream2 << tempStream1;
            freeSpace -= tempStream1.size();
            nextUpdateIdx++;
            nUpdates++;
        }
        else
        {
            freeSpace = 0;
        }

    }

    stream << detailedUpdate;
    stream << nUpdates;

    stream << tempStream2;

    if (nextUpdateIdx >= nChildren)
    {
        nextUpdateIdx = 0;
        stream.SetDoneFlag(true);
    }
    else
    {
        stream.SetDoneFlag(false);
    }



    return stream;
}


/**
* Loads state from command stream
*/
tcCommandStream& tcFlightPort::operator<<(tcCommandStream& stream)
{
	unsigned char nCommands;
	stream >> nCommands;

	for (unsigned char n=0; n<nCommands; n++)
	{
		short int id;
		unsigned char op;
		unsigned char pos;

		stream >> id;
		stream >> op;
		stream >> pos;

		if (op == 0) // launch command
		{
			LaunchID(id);
		}
		else // search for matching id and set new destination
		{
			bool found = false;
			size_t obj_count = units.size();
			for (size_t n=0; (n<obj_count)&&(!found); n++)
			{
				tcAirState *airstate = units[n];
				if (airstate->obj->mnID == (long)id)
				{
					found = true;
					SetObjectDestination(n, (teLocation)op, pos);
				}
			}
		}
	}

    // load mission manager commands (always do this even if no commands)
    ai::tcMissionManager* mm = GetOrCreateMissionManager();
    return mm->operator<<(stream);
}

/**
* Saves state to command stream
*/
tcCommandStream& tcFlightPort::operator>>(tcCommandStream& stream)
{
	unsigned char nCommands = commandList.size();
	stream << nCommands;

	for (unsigned char n=0; n<nCommands; n++)
	{
		stream << commandList[n].id;
		stream << commandList[n].op;
		stream << commandList[n].pos;
	}

    // save mission manager commands (always do this even if no commands)
    ai::tcMissionManager* mm = GetOrCreateMissionManager();
    return mm->operator>>(stream);
}

/**
* Loads state from game stream
*/
tcGameStream& tcFlightPort::operator<<(tcGameStream& stream)
{
    assert(units.size() == 0);

    stream >> last_update_time;
    stream >> inHangarCount;
    stream >> localId;

    size_t nUnits = units.size();

    stream >> nUnits;

    for (size_t n=0; n<nUnits; n++)
    {
        long objId;
        stream >> objId;

        tcAirState* airstate = new tcAirState;

        airstate->lastMultiplayerUpdate = 0;

        std::shared_ptr<tcAirObject> obj = std::dynamic_pointer_cast<tcAirObject>(parent->GetChildById(objId));
        airstate->obj = obj;
        assert(obj != 0);
        
        airstate->operator<<(stream);

        units.push_back(airstate);

        // update spot (if pos not hangar)
        tsSpotInfo* spot = GetCurrentSpotInfo(airstate);
        if (spot != 0) spot->obj_info = airstate;
    }

    bool hasMissionManager;
    stream >> hasMissionManager;
    if (hasMissionManager)
    {
        missionManager = GetOrCreateMissionManager();
        missionManager->operator<<(stream);   
    }

    stream.ReadCheckValue(1278);

    return stream;
}

/**
* Saves state to game stream
*/
tcGameStream& tcFlightPort::operator>>(tcGameStream& stream)
{
    stream << last_update_time;
    stream << inHangarCount;
    stream << localId;

    size_t nUnits = units.size();

    stream << nUnits;

    for (size_t n=0; n<nUnits; n++)
    {
        stream << units[n]->obj->mnID;
        units[n]->operator>>(stream);
    }

    bool hasMissionManager = (missionManager != 0);
    stream << hasMissionManager;
    if (hasMissionManager)
    {
        missionManager->operator>>(stream);   
    }

    stream.WriteCheckValue(1278);

    return stream;
}






void tcFlightPort::ClearNewCommand()
{
	commandList.clear();

    if (missionManager != 0) missionManager->ClearNewCommand();
}

bool tcFlightPort::HasNewCommand() const
{
    bool missionManagerCommand = (missionManager != 0) && (missionManager->HasNewCommand());

	return (commandList.size() > 0) || missionManagerCommand;
}

/** 
* Adds obj to loc if available, otherwise adds to best available location.
* If no location is available (can't add) returns 0, otherwise 1.
* @param obj Game object to add.
* @param loc Desired location for obj.
* @param position Desired position for obj (e.g. which runway)
* @return 1 success, 0 failure
*/
/**
* 将对象obj添加到指定位置loc，如果不可行，则添加到最佳可用位置。
* 如果没有可用位置（无法添加），返回0，否则返回1。
* @param obj 要添加的游戏对象。
* @param loc obj的期望位置。
* @param position obj的期望位置（例如哪个跑道）。
* @return 1表示成功，0表示失败。
*/
int tcFlightPort::AddObject(std::shared_ptr<tcAirObject>obj, teLocation loc, unsigned int position)
{
    std::vector<tsSpotInfo> *bestLocation = NULL; // 最佳位置指针，初始化为空
    int emptySpotIdx = -1; // 空位索引，初始化为-1

    // 如果指定位置不存在于该飞行港口，则覆盖位置
    if ((loc == HANGAR) && (inHangarCount >= hangarCapacity)) loc = ALERT15; // 如果指定为机库且机库已满，则改为ALERT15
    if ((loc == ALERT15) && (ready_spots.size() == 0)) loc = ALERT5; // 如果指定为ALERT15且没有准备位置，则改为ALERT5

    if (loc == ALERT5) // 如果位置是ALERT5
    {
        // 如果指定位置在发射位置范围内且为空，则使用该位置
        if ((position < launch_spots.size()) && launch_spots[position].IsEmpty())
        {
            emptySpotIdx = (int)position;
        }
        else
        {
            // 否则，查找发射位置中的空位置
            emptySpotIdx = FindEmptySpot(&launch_spots);
        }
        // 如果找到空位，则设置最佳位置为发射位置
        if (emptySpotIdx >= 0)
            bestLocation = &launch_spots;
        else
            loc = ALERT15; // 如果没有空发射位置，则尝试ALERT15
    }
    if (loc == ALERT15) // 如果位置是ALERT15
    {
        // 如果指定位置在准备位置范围内且为空，则使用该位置
        if ((position < ready_spots.size()) && ready_spots[position].IsEmpty())
        {
            emptySpotIdx = (int)position;
        }
        else
        {
            // 否则，查找准备位置中的空位置
            emptySpotIdx = FindEmptySpot(&ready_spots);
        }
        // 如果找到空位，则设置最佳位置为准备位置
        if (emptySpotIdx >= 0)
            bestLocation = &ready_spots;
        else
            loc = HANGAR; // 如果没有空准备位置，则尝试机库
    }

    // 如果指定位置是机库且机库已满，则返回0（失败）
    if ((loc == HANGAR)&&(inHangarCount >= hangarCapacity)) return 0;

    // 为新对象创建airstate
    tcAirState *airstate = new tcAirState;
    airstate->obj = obj; // 设置对象
    airstate->obj->mnID = localId++; // 为对象分配本地ID
    airstate->op = OP_NONE; // 设置操作为无
    airstate->ready_time = last_update_time; // 设置准备时间为最后更新时间
    airstate->current_location = loc; // 设置当前位置
    airstate->current_spot = emptySpotIdx; // 设置当前位置索引
    airstate->goal_location = loc; // 设置目标位置为当前位置
    airstate->goal_spot = airstate->current_spot; // 设置目标位置索引为当前位置索引
    airstate->inTransit = false; // 设置不在运输中
    airstate->lastMultiplayerUpdate = tcTime::Get()->GetUpdated30HzCount(); // 设置最后的多人更新时间
    units.push_back(airstate); // 将airstate添加到飞行港口的units向量中

    // 如果位置是机库，则增加机库中的对象计数
    if (loc == HANGAR) inHangarCount++;
    // 如果最佳位置不为空且空位索引有效
    if ((bestLocation != NULL)&&(emptySpotIdx >= 0))
    {
        tsSpotInfo *spot = &bestLocation->at(emptySpotIdx); // 获取空位信息
        spot->obj_info = airstate; // 设置空位信息中的对象为airstate
    }
    InitRelPos(airstate); // 初始化airstate的相对位置
    return 1; // 返回1（成功）
}
/**
* Add spot to flightport. 
*/
/**
* 向飞行港添加停靠点。
*/
void tcFlightPort::AddSpot(teLocation loc, float x, float y, float z,
                           float orientation, float length)
{
    tsSpotInfo spot; // 定义一个停靠点信息结构体变量
    spot.x = x; // 设置停靠点的x坐标
    spot.y = y; // 设置停靠点的y坐标
    spot.z = z; // 设置停靠点的z坐标
    spot.orientation = orientation; // 设置停靠点的朝向
    spot.length = length; // 设置停靠点的长度
    spot.obj_info = NULL; // 初始时，停靠点的对象信息为空

    // 根据传入的地点类型，将停靠点添加到不同的列表中
    if (loc == ALERT5) { // 如果地点是ALERT5
        launch_spots.push_back(spot); // 将停靠点添加到发射点列表中
        return; // 添加完成后返回
    }
    else if (loc == ALERT15) { // 如果地点是ALERT15
        ready_spots.push_back(spot); // 将停靠点添加到准备点列表中
        return; // 添加完成后返回
    }
}
/**
* Determines if obj has landed on runway or crashed into flightport.
* If object successfully lands, it is added to the toLand queue.
* Landing criteria are very crude in this version. Anything close is
* considered landed. Crashes are not checked. Higher-level code is relied 
* on to check that the obj is decending.
* @param obj Object to attempt landing
* @return -1 if crash, 0 if not close enough for landing, 1 if landed
*/
/**
* 判断对象是否已在跑道上着陆或撞毁在飞行港上。
* 如果对象成功着陆，则将其添加到待着陆队列中。
* 此版本的着陆判定非常粗略。任何接近的对象都被视为已着陆。
* 不检查坠毁情况。依赖更高层次的代码来检查对象是否在下降。
* @param obj 尝试着陆的对象
* @return -1 表示坠毁，0 表示距离着陆点不够近，1 表示已着陆
*/
int tcFlightPort::CheckLanding(std::shared_ptr<tcAirObject>obj)
{
     std::shared_ptr<tcAirObject> air = obj; // 将传入的对象指针赋值给局部变量air
    bool isAir = (air != 0); // 判断air是否非空，即是否为有效的空中对象
    //bool isHelo =  std::dynamic_pointer_cast<tcHeloObject>>(air) != 0; // 原始代码中的动态类型转换，用于判断是否为直升机（已被注释）
    bool isHelo = typeid(*air) == typeid(tcHeloObject); // 使用RTTI（运行时类型识别）判断air是否为直升机对象
    bool compatible = isAir && (!mpDBObject->heloOnly || isHelo); // 判断对象是否与飞行港兼容（是否为空中对象且飞行港接受直升机或对象为直升机）

    std::shared_ptr<tcCarrierObject> carrier = std::dynamic_pointer_cast<tcCarrierObject>(parent); // 判断父对象是否为航母
    bool carrierLanding = (carrier != 0); // 判断是否在航母上着陆
    bool carrierCompatible = air->mpDBObject->IsCarrierCompatible(); // 判断对象是否与航母兼容

    compatible = compatible && (!carrierLanding || carrierCompatible); // 更新兼容状态，确保对象与当前着陆环境（飞行港或航母）兼容

    if (!compatible) return 0; // 如果不兼容，则返回0表示未着陆

    int nRunways = (int)launch_spots.size(); // 获取跑道（发射点）的数量
    for (int n=0;n<nRunways;n++) // 遍历所有跑道
    {
        tsSpotInfo *spot = &launch_spots.at(n); // 获取当前跑道的信息指针
        // 下面的代码块被注释掉了，原用于计算对象与跑道中心的相对位置
        //float dx = obj->rel_pos.dx - spot->x;
        //float dy = obj->rel_pos.dy - spot->y;
        //float dz = obj->rel_pos.dz - spot->z;

        // 下面的条件判断被简化，原用于检查对象是否在跑道附近着陆
        //if ((dx*dx + dz*dz <= 1600.0f)&&(dy < 25.0f)&&(dy > -25.0f))
        // 简化后的条件判断：如果跑道长度足够或正在航母上着陆
        if ((spot->length >= air->mpDBObject->minimumRunway_m) || carrierLanding)
        {
            air->GetBrain()->RemoveAllTasks(); // 清除对象的所有任务
            air->SetLandingState(false); // 收回起落架
            toLand.push_back(obj); // 将对象添加到待着陆队列中
            return 1; // 返回1表示已着陆
        }
    }

    return 0; // 如果没有在任何跑道上着陆，则返回0
}


void tcFlightPort::Clear() 
{
    size_t nSpots = units.size();
    for(size_t n=0;n<nSpots;n++) 
    {
        tcAirState *airstate = units.at(n);
		parent->RemoveChild(airstate->obj);
        // delete airstate->obj;
        delete airstate;
    }
    units.clear();

	for (size_t n=0; n<toLaunch.size(); n++)
	{
        // delete toLaunch[n];
	}
    toLaunch.clear();


	for (size_t n=0; n<toLand.size(); n++)
	{
        // delete toLand[n];
	}
    toLand.clear();

	for (size_t n=0; n<ready_spots.size(); n++)
	{
		ready_spots[n].obj_info = 0;
	}

	for (size_t n=0; n<launch_spots.size(); n++)
	{
		launch_spots[n].obj_info = 0;
	}

    inHangarCount = 0;

    last_update_time = 0;

	if (missionManager != 0)
	{
		delete missionManager;
		missionManager = 0;
	}

    nextUpdateIdx = 0;
}

/**
 * Search units vector and return matching index. Return -1 if not found.
 */
int tcFlightPort::FindAirState(tcAirState *airstate)
{
    size_t nUnits = units.size();
    for(size_t n=0;n<nUnits;n++) 
    {
        tcAirState* airstate_n = units.at(n);
        if (airstate_n == airstate) return (int)n;
    }
    return -1; // not found
}

/**
 * Searches loc for empty spot returns spot index if found,
 * otherwise returns -1.
 */
int tcFlightPort::FindEmptySpot(std::vector<tsSpotInfo> *loc_vector)
{
    size_t nSpots = loc_vector->size();
    for(size_t n=0;n<nSpots;n++) 
    {
        tsSpotInfo *spot = &loc_vector->at(n);
        if (spot->obj_info == NULL) return (int)n;
    }
    return -1;
}

/**
 * Searches for empty spot at loc and returns spot index if found,
 * otherwise returns -1.
 */
int tcFlightPort::FindEmptySpot(teLocation loc, std::vector<tsSpotInfo>*& loc_vector)
{
    loc_vector = GetLocVector(loc);
    if (loc == HANGAR) return (inHangarCount >= hangarCapacity) ? -1 : 0;
    if ((loc == TAKEOFF)||(loc == NOWHERE)) return -1; // error
   
    return FindEmptySpot(loc_vector);   
}

/**
* Search (linear) units vector for obj
* @return index with matching obj or -1 if not found.
*/
int tcFlightPort::FindAirState(std::shared_ptr<tcGameObject> obj)
{
	assert(obj);

	size_t nUnits = units.size();
    for(size_t n=0; n<nUnits; n++) 
    {
        tcAirState* airstate_n = units[n];
		if (airstate_n->obj == obj) return (int)n;
    }
    return -1; // not found
}

/**
* Search (linear) units vector for obj
* @return tcAirState ptr for matching obj or 0 if not found.
*/
tcAirState* tcFlightPort::FindAirStateObj(std::shared_ptr<const tcGameObject> obj)
{
	assert(obj);

	size_t nUnits = units.size();
    for(size_t n=0; n<nUnits; n++) 
    {
        tcAirState* airstate_n = units[n];
		if (airstate_n->obj == obj) return airstate_n;
    }
    return 0; // not found
}

/**
* Search (linear) units vector for obj
* @return tcAirState ptr for matching obj or 0 if not found.
*/
const tcAirState* tcFlightPort::FindAirStateObj(std::shared_ptr<const tcGameObject> obj) const
{
	assert(obj);

	size_t nUnits = units.size();
    for(size_t n=0; n<nUnits; n++) 
    {
        const tcAirState* airstate_n = units[n];
		if (airstate_n->obj == obj) return airstate_n;
    }
    return 0; // not found
}


tcAirState* tcFlightPort::GetAirState(unsigned n)
{
	return units[n];
}

const tcAirState* tcFlightPort::GetAirState(unsigned n) const
{
	return units[n];
}

int tcFlightPort::GetAirStateIdx(long id) const
{
    size_t nUnits = units.size();
    for(size_t n=0;n<nUnits;n++) 
    {
        tcAirState* airstate = units.at(n);
        if (airstate->obj->mnID == id) return (int)n;
    }
    return -1; // not found
}

std::shared_ptr<tcFlightportDBObject> tcFlightPort::GetDatabaseObject() const
{
    return mpDBObject;
}

/**
* @returns game object for unit with index n
*/
std::shared_ptr<tcGameObject> tcFlightPort::GetObject(unsigned n)
{
	assert(n < units.size());

	return units[n]->obj;
}

/**
* @return game object for unit with matching id
*/
std::shared_ptr<tcGameObject> tcFlightPort::GetObjectById(long id)
{
	int idx = GetAirStateIdx(id);
	if (idx < 0) return 0;
	return GetObject(unsigned(idx));
}

std::shared_ptr<tcGameObject> tcFlightPort::GetObjectByName(const std::string& unitName)
{
    size_t nUnits = units.size();
    for (size_t n=0; n<nUnits; n++) 
    {
        tcAirState* airstate = units[n];
        if ((airstate->obj != 0) && (airstate->obj->mzUnit == unitName.c_str()))
        {
            return airstate->obj;
        }
    }
    return 0;
}

/**
* @return length of longest runway in meters
*/
float tcFlightPort::GetMaxRunwayLength() const
{
    float maxRunway_m = 0;
	for (size_t n=0; n<launch_spots.size(); n++)
	{
        maxRunway_m = std::max(maxRunway_m, launch_spots[n].length);
	}
    return maxRunway_m;
}

ai::tcMissionManager* tcFlightPort::GetMissionManager()
{
	return missionManager;
}

ai::tcMissionManager* tcFlightPort::GetOrCreateMissionManager()
{
	if (missionManager == 0)
	{
        missionManager = new ai::tcMissionManager(this);
	}
	
	return missionManager;
}

/**
* @return time in seconds
* For displaying status to player. Show time to move to ultimate destination.
* Or for maintenance or load/unload, show time until operation is done
*/
float tcFlightPort::GetTimeToDestination(const tcAirState* airstate) const
{
    assert(airstate != 0);

    float ready_s = airstate->ready_time - last_update_time;

    if ((airstate->op == OP_MAINTENANCE) || (airstate->op == OP_REPAIR))
    {
        return ready_s;
    }

    ready_s = std::max(ready_s, 0.0f);
    if (airstate->goal_location != airstate->current_location)
    {
        if (tcOptions::Get()->fastAircraftReady != 0)
        {
            ready_s += transitionTimesFast[airstate->current_location][airstate->goal_location];
            
            if ((!airstate->inTransit) || (airstate->current_location == PRETAKEOFF))
            {
                teLocation nextStop = GetNextStop(airstate->current_location, airstate->goal_location);
                if (nextStop > 0) 
                {
                    ready_s -= transitionTimesFast[airstate->current_location][nextStop];
                }
            }           
        }
        else
        {
            ready_s += transitionTimesNormal[airstate->current_location][airstate->goal_location];

            if ((!airstate->inTransit) || (airstate->current_location == PRETAKEOFF))
            {
                teLocation nextStop = GetNextStop(airstate->current_location, airstate->goal_location);
                if (nextStop > 0) 
                {
                    ready_s -= transitionTimesNormal[airstate->current_location][nextStop];
                }
            }
        }
        
    }

    return ready_s;
}

const std::string& tcFlightPort::GetTimeToDestinationString(const tcAirState* airstate) const
{
    static std::string readyTimeString;
    readyTimeString.clear();

    long ready_s = long(GetTimeToDestination(airstate) + 0.5f);
    if (ready_s > 0)
    {
	    long hours = ready_s / 3600;
        long min = (ready_s - 3600*hours)/60;
        long sec = ready_s % 60;
        
        if (ready_s > 59)
        {
            readyTimeString=strutil::format(" %02d:%02d", hours, min);
//            readyTimeString.Printf(" %02d:%02d", hours, min);
        }
        else
        {
           readyTimeString=strutil::format(" %02ds", sec);
//            readyTimeString.Printf(" %02ds", sec);
        }

        switch (airstate->goal_location)
        {
        case HANGAR:
            readyTimeString += " -";
            break;
        case ALERT15:
            readyTimeString += " R15";
            break;
        case ALERT5:
            readyTimeString += " R5";
            break;
        case PRETAKEOFF:
        case TAKEOFF:
            readyTimeString += " L";
            break;
        }
    }
    else
    {
        return readyTimeString; // empty string
    }

    if ((airstate->op == OP_MAINTENANCE) || (airstate->op == OP_REPAIR))
    {
        readyTimeString += "*";
    }
    else if (!airstate->inTransit)
    {
        readyTimeString += "!";
    }

    return readyTimeString;
}


int tcFlightPort::LaunchAirstate(tcAirState* airstate)
{
    if (airstate == NULL) return 0; // not found on runway

	if (parent->IsClientMode())
	{
		CommandInfo cmd;
		cmd.id = (unsigned short)airstate->obj->mnID;
		cmd.op = 0;
		commandList.push_back(cmd);
		return 1;
	}

    bool notReady = (airstate->ready_time > last_update_time);
    bool damaged = (airstate->obj->GetDamageLevel() > maxTakeoffDamage);

    if (airstate->current_location != PRETAKEOFF)
    {
        SetObjectDestination(airstate, TAKEOFF, 0);
        return 0;
    }

	if (notReady || damaged)
	{
		if (damaged) // added this 2APR2011 to keep aircraft from getting stuck launching after damaged
		{
			airstate->current_location = ALERT5;
			SetObjectDestination(airstate, HANGAR, 0);
		}
		return 0; // not ready yet or damaged, do not allow takeoff
	}
    
     std::shared_ptr<tcAirObject> air = airstate->obj;
    if (air == 0)
    {
        fprintf(stderr, "tcFlightPort::Launch -- tried to launch non-air object\n");
        assert(false);
        return 0;
    }

    if (air->IsOverweight())
    {
        if (airstate->goal_location == TAKEOFF) // dequeue for takeoff
        {
            airstate->goal_location = ALERT5;
            airstate->goal_spot = airstate->current_spot;
        }
        return 0; // too heavy to launch
    }

    MoveToLaunchQueue(airstate);

    tsSpotInfo* spotInfo = GetCurrentSpotInfo(airstate);
    if (spotInfo != 0)
    {
        spotInfo->obj_info = 0; // set spot empty
    }
    return 1;
}

int tcFlightPort::LaunchRunway(int runway)
{
    int nRunways = (int)launch_spots.size();
    if ((runway < 0)||(runway >= nRunways)) return 0;

    tsSpotInfo *spot = &launch_spots[runway];

    tcAirState* airstate = spot->obj_info;

    return LaunchAirstate(airstate);
}

/// Find runway that object with id is on
int tcFlightPort::LaunchID(long id)
{
	if (parent->IsClientMode())
	{
		CommandInfo cmd;
		cmd.id = id;
		cmd.op = 0;
		commandList.push_back(cmd);
		return 1;
	}

  //  size_t nSpots = launch_spots.size();
  //  for (size_t n=0;n<nSpots;n++) 
  //  {
  //      tsSpotInfo *spot = &launch_spots.at(n);
		//if ((spot->obj_info != 0) && (spot->obj_info->obj != 0) && 
		//	(spot->obj_info->obj->mnID == id))
  //      {
		//	bool isReady = (spot->obj_info->ready_time <= last_update_time);
		//	if (isReady)
		//	{
		//		Launch((int)n);
		//		return 1;
		//	}
		//	else
		//	{
		//		return 0;
		//	}
  //      }
  //  }

	// queue for takeoff by moving to TAKEOFF destination
	int idx = GetAirStateIdx(id);
	if (idx >= 0)
	{
		tcAirState* airState = GetAirState(idx);
		if (airState != 0)
		{
			SetObjectDestination(airState, TAKEOFF, 0);
			return 1;
		}
	}


    fprintf(stderr, "tcFlightPort::LaunchID - Bad air state (id:%d)\n", id);
	//assert(false);
	return 0;

}

/**
 * Move object to new location if valid. Remove object from old location. 
 */
void tcFlightPort::MoveObjectToDestination(tcAirState *airstate, teLocation destination, int spot)
{
    if (spot == -1) return; // no valid goal spot yet
    if (airstate->current_location == destination) return; // no need to move (may need spot move in future)
    if (airstate->inTransit) return; // already moving, error

	assert(destination != TAKEOFF);
    if (destination == HANGAR) inHangarCount++;

    if (destination == PRETAKEOFF)
    {
        assert(airstate->current_location == ALERT5);
        airstate->current_location = PRETAKEOFF;
        airstate->inTransit = true;
        return; // no need to move between loc vectors, since is virtual loc and should already be in ALERT5
    }

    std::vector<tsSpotInfo>* current_loc_vect = GetLocVector(airstate->current_location);
    std::vector<tsSpotInfo>* dest_loc_vect = GetLocVector(destination);
    
    if (current_loc_vect)
    {
        tsSpotInfo& current_spot = current_loc_vect->at(airstate->current_spot);
        current_spot.obj_info = NULL; // remove from current spot
    }
    if (dest_loc_vect)
    {
        tsSpotInfo& dest_spot = dest_loc_vect->at(spot);
        dest_spot.obj_info = airstate; // add to dest spot
    }

    airstate->current_location = destination;
    airstate->current_spot = spot;

	airstate->inTransit = true;

    airstate->op = OP_TRANSIT;
}
/**
 * Find airstate in units vector. Add std::shared_ptr<tcGameObject> to toLaunch vector. 
 * Remove airstate from units vector.
 */
bool tcFlightPort::MoveToLaunchQueue(tcAirState *airstate)
{
    int unit_idx = FindAirState(airstate);
    if (unit_idx == -1) return false; // error not found
    UpdateUnitKin(airstate);
    toLaunch.push_back(airstate->obj);
    // delete launched element and move last element into its place
    tcAirState*& launched = units.at(unit_idx);
    delete launched;
    tcAirState *back = units.back();
    launched = back;
    units.pop_back(); // remove last element
    return true;
}

/**
* Remove units that are marked destroyed from the flight deck
*/
void tcFlightPort::RemoveDestroyedUnits()
{
    size_t nUnits = units.size();
    std::vector<tcAirState*> temp;

    for (size_t n=0; n<nUnits; n++)
    {
        if (!units[n]->obj->IsDestroyed())
        {
            temp.push_back(units[n]);
        }
        else
        {
            parent->RemoveChild(units[n]->obj);
            // delete(units[n]->obj);
            delete units[n];
        }
    }

    units = temp;

    ResyncSpots();
}

/**
* For multiplayer client
*/
void tcFlightPort::RemoveStaleUnits()
{
    unsigned int t = tcTime::Get()->GetUpdated30HzCount();


    int minTimeLag = 999;
    int maxTimeLag = 0;

    size_t nUnits = units.size();
    for (size_t n=0; n<nUnits; n++)
    {
        int lag = t - units[n]->lastMultiplayerUpdate;
        if (lag < minTimeLag) minTimeLag = lag;
        else if (lag > maxTimeLag) maxTimeLag = lag;
    }

    // remove units with lastMultiplayerUpdate more than 3 seconds
    // older than latest update
    int lagThresh = minTimeLag + 90;
    std::vector<tcAirState*> temp;

    for (size_t n=0; n<nUnits; n++)
    {
        int lag = t - units[n]->lastMultiplayerUpdate;
        if (lag <= lagThresh)
        {
            temp.push_back(units[n]);
        }
        else
        {
            parent->RemoveChild(units[n]->obj);
            // delete(units[n]->obj);
            delete units[n];
        }
    }

    units = temp;

    ResyncSpots();
}

/**
 * @return pointer to tsSpotInfo for current location and spot.
 */
tsSpotInfo* tcFlightPort::GetCurrentSpotInfo(tcAirState *airstate)
{
    std::vector<tsSpotInfo>* loc_vect = GetLocVector(airstate->current_location);
    if (loc_vect == NULL) return NULL;
    int spot_idx = airstate->current_spot;
    if ((spot_idx < 0)||(spot_idx >= (int)loc_vect->size())) return NULL; // error, bad spot idx
    return &loc_vect->at(spot_idx);
}

/**
* This version returns info for the first runway spot only
*
* @return track with landing point coord and heading with orientation 
*/
tcTrack tcFlightPort::GetLandingData(std::shared_ptr<const tcGameObject> obj)
{
	tcTrack data;

    int nRunways = (int)launch_spots.size();

	if (nRunways > 0)
	{
		tsSpotInfo *spot = &launch_spots.at(0);

		assert(obj);
		GeoPoint p = obj->RelPosToLatLonAlt(spot->x, spot->y, spot->z);

		data.mfLat_rad = p.mfLat_rad;
		data.mfLon_rad = p.mfLon_rad;
		data.mfAlt_m = p.mfAlt_m;
		data.mfHeading_rad = spot->orientation + obj->mcKin.mfHeading_rad;
		if (data.mfHeading_rad >= C_PI) data.mfHeading_rad -= C_TWOPI;
		else if (data.mfHeading_rad < -C_PI) data.mfHeading_rad += C_TWOPI;
		
		data.mnID = obj->mnID;

		return data;
	}
	else
	{
		data.mnID = -1;
		return data;
	}

}

/**
 * @return location vector corresponding to loc, or NULL if loc = HANGAR, TRANSIT, or NOWHERE.
 */
std::vector<tsSpotInfo>* tcFlightPort::GetLocVector(teLocation loc)
{
    switch (loc)
    {
    case HANGAR: return NULL; break;
    case ALERT15: return &ready_spots; break;
    case ALERT5: return &launch_spots; break;
    case PRETAKEOFF: return &launch_spots; break;
    default: return NULL; break;
    }
}

/**
* Initialize flightport using data in dbObj.
*/
void tcFlightPort::InitFromDatabase(std::shared_ptr<tcFlightportDBObject> dbObj)
{
    assert(dbObj);

    Clear();

	mpDBObject = dbObj;

    hangarCapacity = mpDBObject->hangarCapacity;
    inHangarCount = 0;
	
    size_t nSpots = dbObj->spotInfo.size();
    for(size_t spot=0;spot<nSpots;spot++)
    {
        tcFlightportDBObject::spotDBInfo info = dbObj->spotInfo[spot];

        teLocation loc = (info.isLaunch) ? ALERT5 : ALERT15;
        AddSpot(loc, info.x, info.y, info.z, C_PIOVER180*info.orientation_deg, info.length);
    }

}

/**
* Set unit position and orientation to match that of current spot.
* Set visible to false if in hangar, otherwise true. This should be called
* once during initialization. Additional calls can be used to handle non-animated
* movement. Eventually UpdateRelPos should handle all of the movement after init.
*/
/**
* 设置单位的位置和方向以匹配当前停机位的信息。
* 如果飞机在机库内，则将其设置为不可见，否则设置为可见。这个方法应在初始化时调用一次。
* 额外的调用可用于处理非动画移动。最终，UpdateRelPos方法应处理初始化后的所有移动。
*/
void tcFlightPort::InitRelPos(tcAirState *airstate)
{
    // 获取与当前飞机状态相关联的游戏对象
    std::shared_ptr<tcGameObject>pGameObj = airstate->obj;
    // 如果飞机当前位于机库或预警15分钟内区域
    if ((airstate->current_location == HANGAR)||(airstate->current_location == ALERT15))
    {
        // 将游戏对象的位置设置为原点（0,0,0）
        pGameObj->SetRelativePosition(0,0,0);
        // 将游戏对象设置为不可见
        pGameObj->SetVisible(false);
        // 结束当前方法的执行
        return;
    }
    // 如果飞机不在机库或预警区域内，则将其设置为可见
    pGameObj->SetVisible(true);

    // 获取当前停机位的信息
    tsSpotInfo *spotinfo = GetCurrentSpotInfo(airstate);
    // 如果无法获取停机位信息（即spotinfo为NULL），则返回并处理错误
    if (spotinfo == NULL) return; // error

    // 根据停机位信息设置游戏对象的位置
    pGameObj->SetRelativePosition(spotinfo->x,spotinfo->y,spotinfo->z);
    // 设置游戏对象的方向，使用停机位信息的方向并转换为弧度（C_PIOVER180是π/180的常量，用于将角度转换为弧度）
    // 这里只设置了y轴方向的角度，x轴和z轴方向的角度保持为0
    pGameObj->SetRelativeOrientation(C_PIOVER180*spotinfo->orientation, 0, 0);
}
/**
* @return true if all launch spots are heloOnly
*/
bool tcFlightPort::IsHeloOnly() const
{
	return mpDBObject->heloOnly != 0;
}

/**
* @return true if unit matching id is queued for takeoff 
* (goal loc == TAKEOFF)
*/
bool tcFlightPort::IsQueuedForTakeoff(long id) const
{
	int idx = GetAirStateIdx(id);
	if (idx < 0) return false;

    const tcAirState* airState = GetAirState((unsigned)idx);
	if (airState != 0)
	{
		return (airState->goal_location == TAKEOFF);
	}
	else
	{
		assert(false);
		return false;
	}
}

/**
* Use to check status of specific spot, e.g. runway 1
* @return true if spot is empty, hangar spot is empty if hangar is not full
*/
bool tcFlightPort::IsSpotEmpty(teLocation loc, unsigned int spot)
{
    if (loc == HANGAR) return (inHangarCount < hangarCapacity);

    if (loc == PRETAKEOFF) return true;

	std::vector<tsSpotInfo>* loc_vector = GetLocVector(loc);

    if ((loc == NOWHERE)||(loc == TAKEOFF))
	{
		assert(false);
		return false; // error
	}
   
	if (spot >= loc_vector->size()) return false;

	return ((*loc_vector)[spot].obj_info == 0);
}

/**
* Workaround for multiplayer client. 
* This clears spot info and reassigns units to spots based on the info in airstate
*/
void tcFlightPort::ResyncSpots()
{
	// first clear the obj_info in each ready and launch spot
	for (size_t n=0; n<ready_spots.size(); n++)
	{
		ready_spots[n].obj_info = 0;
	}

	for (size_t n=0; n<launch_spots.size(); n++)
	{
		launch_spots[n].obj_info = 0;
	}

    inHangarCount = 0;

	for (size_t n=0; n<units.size(); n++)
	{
		tcAirState* airstate = units[n];
		if (airstate->current_location == HANGAR)
		{
            inHangarCount++;
		}
		else if (airstate->current_location == ALERT15)
		{
			if ((airstate->current_spot >= 0) && ((unsigned)airstate->current_spot < ready_spots.size()))
			{
				ready_spots[airstate->current_spot].obj_info = airstate;
			}
		}
		else if ((airstate->current_location == ALERT5) || (airstate->current_location == PRETAKEOFF))
		{
			if ((airstate->current_spot >= 0) && ((unsigned)airstate->current_spot < launch_spots.size()))
			{
				launch_spots[airstate->current_spot].obj_info = airstate;
			}
		}
	}
}

/**
* 
*/
void tcFlightPort::SetObjectDestination(unsigned n, teLocation loc, unsigned int position)
{
    if (n >= (unsigned)units.size()) return; // error, out of range
    tcAirState* airstate = units.at(n);
    
	SetObjectDestination(airstate, loc, position);
}

/**
* 
*/
void tcFlightPort::SetObjectDestination(tcAirState* airstate, teLocation loc, unsigned int position)
{
	assert(airstate != 0);

    teLocation currentLoc = airstate->current_location;
    bool validMove = false;
    
	validMove = (currentLoc != loc);

	/*
    if (loc == HANGAR)
    {
        validMove = (currentLoc == ALERT15);
    }
    else if (loc == ALERT15)
    {
        validMove = (currentLoc == ALERT15) || (currentLoc == HANGAR) ||
                    (currentLoc == ALERT5);
    }
    else if (loc == ALERT5)
    {
        validMove = (currentLoc == ALERT15);
    }
    
	*/
    if (!validMove) return;

    if ((loc == TAKEOFF) && (airstate->current_location == PRETAKEOFF))
    {
        LaunchAirstate(airstate);
        return;
    }
    
    airstate->goal_location = loc;
	airstate->goal_spot = position;

    if (parent->IsClientMode())
	{
		CommandInfo cmd;
		cmd.id = (short int)airstate->obj->mnID;
		cmd.op = loc;
		cmd.pos = position;
		commandList.push_back(cmd);
		return;
	}
}


void tcFlightPort::UpdateRelPos(tcAirState *airstate, double time)
{
//    std::shared_ptr<tcGameObject>pGameObj = airstate->obj;
    if (airstate->inTransit)
    {
        if (time >= airstate->ready_time) 
		{
			if (airstate->current_location == HANGAR) inHangarCount--;
			if (airstate->goal_location == HANGAR) inHangarCount++;

            airstate->op = OP_NONE;
			airstate->inTransit = false;

			
			assert(inHangarCount <= hangarCapacity);

            InitRelPos(airstate);
        }
    }
}

/**
* Update the kinematics of entities in launch queue. Called once
* when moving to launch queue.
*/
void tcFlightPort::UpdateUnitKin(tcAirState *airstate)
{
     std::shared_ptr<tcAirObject> air_unit = airstate->obj;
    if (air_unit == NULL) return; // error
    std::shared_ptr<tcGameObject> parent = air_unit->parent;
    if (parent == NULL) return; // error

    air_unit->mcKin = parent->mcKin;
    air_unit->mcKin.mfHeading_rad += air_unit->rel_pos.yaw;
    air_unit->mcKin.mfAlt_m += air_unit->rel_pos.dz;
    air_unit->SetHeading(air_unit->mcKin.mfHeading_rad);
    air_unit->mfStatusTime = parent->mfStatusTime;

    GeoPoint childPos = parent->RelPosToLatLonAlt(air_unit->rel_pos);
    air_unit->mcKin.mfAlt_m = childPos.mfAlt_m;
    air_unit->mcKin.mfLat_rad = childPos.mfLat_rad;
    air_unit->mcKin.mfLon_rad = childPos.mfLon_rad;

    if (air_unit == 0)
    {
        assert(false);
        return;
    }



	// write base name to unit blackboard to allow it to RTB when mission complete
    std::shared_ptr<Brain>  brain = air_unit->GetBrain();
    assert(brain);
    ai::BlackboardInterface bb = brain->GetBlackboardInterface();

    bb.Write("Home", parent->mzUnit.c_str());


    if (std::shared_ptr<tcAeroAirObject> aa_unit = std::dynamic_pointer_cast<tcAeroAirObject>(air_unit))
    {
		aa_unit->mcKin.mfSpeed_kts += 200.0f;
        aa_unit->SetThrottleFraction(1.1f);
        aa_unit->SetAltitude(air_unit->mcKin.mfAlt_m + 500.0f);
        aa_unit->SetLandingState(0); 
        brain->AddTask("JetTakeoff", 2.0f);

    }
    else if (std::shared_ptr<tcHeloObject> helo_unit = std::dynamic_pointer_cast<tcHeloObject>(air_unit))
	{
		helo_unit->mcKin.mfClimbAngle_rad = 1.5f;
		helo_unit->SetSpeed(100);
        helo_unit->SetAltitude(helo_unit->mcKin.mfAlt_m + 500.0f);
		helo_unit->SetLandingState(0); 
	}
    else if (air_unit != 0)
    {
		air_unit->mcKin.mfSpeed_kts += 200.0f;
        air_unit->SetSpeed(air_unit->mpDBObject->mfMaxSpeed_kts);
        air_unit->SetAltitude(air_unit->mcKin.mfAlt_m + 500.0f);
        air_unit->SetLandingState(0); 
    }
    brain->AddTask("RTB", 2.0f, ai::Task::PERMANENT | ai::Task::HIDDEN);
}

/**
* @return next location if jumping more than one stage 
* e.g. HANGAR to ALERT5 would stop at ALERT15 first
*/
teLocation tcFlightPort::GetNextStop(teLocation current, teLocation destination) const
{
	if (destination == HANGAR) return HANGAR;
	else if (destination == ALERT15) return ALERT15;
	else if (destination == ALERT5)
	{
		return (current == HANGAR) ? ALERT15 : ALERT5;
	}
	else if (destination == TAKEOFF)
	{
		switch (current)
		{
		case HANGAR: return ALERT15; break;
		case ALERT15: return ALERT5; break;
		case ALERT5: return PRETAKEOFF; break;
        case PRETAKEOFF: return TAKEOFF; break;
		default: assert(false); return current; break;
		}
	}
	else
	{
		assert(false);
		return current;
	}

}

/**
* Sets ready time of unit based on next destination. Check options
* to see if player has selected quick launch under realism settings
*/
void tcFlightPort::SetReadyTime(double t, tcAirState* airstate, teLocation nextLocation)
{
    assert((airstate->current_location >= 0) && (airstate->current_location < 6));
    assert((nextLocation >= 0) && (nextLocation < 6));
    assert(transitionTimesNormal[0][0] == 0); // crude check for unitialized static variable

    if (tcGameObject::IsEditMode())
    {
        airstate->ready_time = t;
    }
    else if (tcOptions::Get()->fastAircraftReady != 0)
    {
        airstate->ready_time = t + transitionTimesFast[airstate->current_location][nextLocation];
    }
    else
    {
        airstate->ready_time = t + transitionTimesNormal[airstate->current_location][nextLocation];
    }

    // OLD LOGIC (< 22 AUG 2009):  airstate->ready_time = tcGameObject::IsEditMode() ? t : t + 30.0; // short times for test
}

/**
*
*/
void tcFlightPort::Update(double t)
{
    // 如果距离上次更新时间不到1秒且不在编辑模式下，则直接返回
    if (((t - last_update_time) < 1.0f) && !tcGameObject::IsEditMode()) return;
    last_update_time = t; // 更新上次更新时间

    RemoveDestroyedUnits(); // 移除已销毁的单位

    // 如果是多人游戏客户端模式，则仅更新相对位置用于显示，省略其他更新
    if (parent->IsClientMode())
    {
        RemoveStaleUnits(); // 移除过时单位

        size_t obj_count = units.size(); // 获取单位数量
        for(size_t n=0;n<obj_count;n++) // 遍历每个单位
        {
            UpdateRelPos(units[n], t); // 更新相对位置
            units[n]->inTransit = (units[n]->goal_location != units[n]->current_location); // 设置是否在运输中
        }

        if (missionManager != 0) missionManager->PerformDeletions(); // 如果任务管理器存在，则执行删除操作

        return; // 客户端模式更新完毕，返回
    }

    UpdateLanded(); // 更新已着陆的单位

    std::vector<long> idsToLaunch; // 初始化待起飞ID队列

    // 遍历每个单位
    size_t obj_count = units.size();
    for(size_t n=0;n<obj_count;n++)
    {
        tcAirState *airstate = units.at(n); // 获取当前单位的状态

        UpdateMaintenance(airstate); // 更新维护状态

        UpdateRefueling(airstate); // 更新加油状态

        UpdatePlatform(airstate); // 更新平台状态

        bool moveable = false; // 是否可移动
        if ( std::shared_ptr<tcAirObject> air = airstate->obj) // 如果存在对应的航空对象
        {
            // 如果不在加油、不在装载且不在维护状态，则设置为可移动
            moveable = !air->IsRefueling() && !air->IsLoading() && (airstate->op != OP_MAINTENANCE);

            air->mfStatusTime = t; // 更新状态时间
        }
        else
        {
            assert(false); // 断言失败，表示不应该执行到这里
        }

        // 如果单位不在运输中、可移动且当前位置不是目标位置
        bool inTransit = airstate->inTransit;
        bool needsAction = (!inTransit) && moveable && (airstate->current_location != airstate->goal_location);
        if (needsAction)
        {
            assert(airstate->current_location != TAKEOFF); // 断言当前位置不是起飞状态

            // 如果是预起飞状态，则将其ID加入待起飞队列
            if (airstate->current_location == PRETAKEOFF)
            {
                idsToLaunch.push_back(airstate->obj->mnID);
            }
            else
            {
                teLocation nextLoc = GetNextStop(airstate->current_location, airstate->goal_location); // 获取下一个位置
                int nextSpot = airstate->goal_spot; // 猜测目标位置

                // 如果目标位置没有空位，则寻找空位
                if (!IsSpotEmpty(nextLoc, nextSpot))
                {
                    std::vector<tsSpotInfo> *loc_vector = 0; // 初始化位置向量（此处未使用，可能是遗留代码）
                    int spot_idx = FindEmptySpot(nextLoc, loc_vector); // 寻找空位
                    nextSpot = spot_idx; // 更新目标位置索引
                }
                SetReadyTime(t, airstate, nextLoc); // 设置准备时间

                MoveObjectToDestination(airstate, nextLoc, nextSpot); // 移动对象到目标位置
            }
        }
        UpdateRelPos(airstate, t); // 更新相对位置
    }

    // 遍历待起飞队列，执行起飞操作
    for (size_t n=0; n<idsToLaunch.size(); n++)
    {
        LaunchID(idsToLaunch[n]); // 执行起飞
    }

    if (missionManager != 0) missionManager->Update(t); // 如果任务管理器存在，则更新任务管理器
}

/**
* Move landed units to hangar. In the future this will animate landing
* and set unit spot to the appropriate landing area. Launch spots may
* see double use as landing areas
*/
/**
* 将着陆单位移动到机库。未来这将包括着陆动画
* 并将单位位置设置为适当的着陆区域。发射点
* 可能也用作着陆区域
*/
void tcFlightPort::UpdateLanded()
{
    size_t landing_count = toLand.size(); // 获取待着陆对象数量
    for(size_t n=0;n<landing_count;n++) // 遍历待着陆对象
    {
        std::shared_ptr<tcAirObject> obj = toLand.at(n); // 获取当前待着陆对象

        // 将着陆对象添加到机库并设置为维护状态
        if (AddObject(obj, HANGAR, 0))
        {
            double maintenanceTime_s = 300.0; // "快速"维护时间

            // 确认对象是指向tcAirObject的有效指针
            if ( std::shared_ptr<tcAirObject> air = obj)
            {
                air->SetLoadoutTag(""); // 着陆时清除负载标签，无论装备状态如何
                air->UnloadAllLaunchers(); // 卸载所有发射器
                // 如果选项中的快速维护被禁用
                if (tcOptions::Get()->fastMaintenance == 0)
                {
                    maintenanceTime_s = (double)air->mpDBObject->GetRandomMaintenanceTime(); // 使用随机维护时间
                }
            }
            int airStateIdx = FindAirState(obj); // 查找当前对象的飞行状态索引
            // 获取飞行状态对象
            if (tcAirState* airState = GetAirState((unsigned int)(airStateIdx)))
            {
                airState->op = OP_MAINTENANCE; // 设置操作状态为维护
                airState->ready_time = last_update_time + maintenanceTime_s; // 设置就绪时间为当前时间加上维护时间
            }
            else
            {
                assert(false); // 如果未找到飞行状态对象，则断言失败
            }

        }
        else
        {
            // 将无法添加到机库的对象移到待发射列表中（之前代码注释掉的是销毁对象的操作）
            toLaunch.push_back(obj); // 将其踢出着陆列表，加入发射列表
        }
    }
    toLand.clear(); // 清空待着陆列表
}

void tcFlightPort::UpdateMaintenance(tcAirState* airstate)
{
    assert(airstate != 0);
    if ((airstate->op == OP_MAINTENANCE) && (airstate->ready_time <= last_update_time))
    {
        airstate->op = OP_NONE;
        airstate->ready_time = last_update_time;
    }
}

void tcFlightPort::UpdatePlatform(tcAirState* airstate)
{
    assert(airstate != 0);
    if (airstate->obj != 0)
    {
        airstate->obj->UpdateMagazines(last_update_time);

        if (airstate->obj->IsOverweight())
        {
            airstate->obj->LightenLoad();
        }
    }
}


/**
* If units not in hangar, schedule refuel operations to top off fuel if needed
* Assumes that 
*/
/**
* 如果飞机不在机库中，根据需要安排加油操作以加满燃油
* 假设...（此处省略了具体假设）
*/
void tcFlightPort::UpdateRefueling(tcAirState *airstate) // 定义UpdateRefueling函数，用于更新加油状态，接收一个指向tcAirState的指针作为参数
{
    assert(airstate != 0); // 断言airstate指针不为空，确保传入了一个有效的指针
     std::shared_ptr<tcAirObject> aircraft = airstate->obj; // 从airstate中获取指向飞机的指针
    if ((aircraft != 0) && (airstate->current_location != HANGAR) && // 如果飞机指针不为空，且飞机当前位置不在机库
        (!aircraft->IsOverweight()) && (!aircraft->IsRefueling())) // 并且飞机没有超重，也没有正在进行加油操作
    {
        float fuelMargin_kg = aircraft->GetFuelCapacity() - aircraft->fuel_kg; // 计算飞机的剩余燃油容量（千克）
        float weightMargin_kg = aircraft->mpDBObject->maxTakeoffWeight_kg - aircraft->GetTotalWeight(); // 计算飞机的最大起飞重量与当前总重量之差（千克）
        if ((fuelMargin_kg > 1.0f) && (weightMargin_kg > 10.0f)) // 如果剩余燃油容量大于1千克，且重量裕量大于10千克
        {
            unsigned long fuelToAdd_kg = (unsigned long)floorf(std::min(fuelMargin_kg, weightMargin_kg)); // 计算需要添加的燃油量（千克），取剩余燃油容量和重量裕量中的较小值，并向下取整
            aircraft->LoadOther("Fuel", fuelToAdd_kg);
            // tcPlatformInterface platformInterface(aircraft); // 创建一个平台接口对象，用于与飞机进行交互
            // platformInterface.LoadOther("Fuel", fuelToAdd_kg); // 通过平台接口为飞机加载指定量的燃油
        }
    }
}

tcFlightPort::tcFlightPort() 
: localId(10), 
  parent(0),
  mpDBObject(0),
  missionManager(0),
  nextUpdateIdx(0),
  maxTakeoffDamage(0.1f)
{

    Clear();

	ready_spots.clear();
    launch_spots.clear();
}

tcFlightPort::~tcFlightPort() 
{
	Clear();
}
