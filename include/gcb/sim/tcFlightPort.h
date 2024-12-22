/**
**  @file tcFlightPort.h
**
**  tcFlightPort object: descibes objects that allow air objects to take off
**  and land. This includes land-based runways, carrier runways, helipads, VTOL pads.
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

#ifndef _FLIGHTPORT_H_
#define _FLIGHTPORT_H_

#include <vector>
#include "tcGameObject.h"

class tcStream;
class tcCommandStream;
class tcCreateStream;
class tcUpdateStream;
class tcAirObject;

namespace ai
{
	class tcMissionManager;
}

namespace database
{
    class tcFlightportDBObject;
}

/** Location info for air unit in flightport.
 *  TODO get this out of top level namespace.
 */
enum teLocation 
{
   NOWHERE = 0,   ///< 无位置，即不在任何位置
   HANGAR = 1,   ///< longer term storage or repair 机库，用于长期存放或维修
   ALERT15 = 2,    ///< out of hangar, on deck  15分钟警戒状态，已出机库，在甲板上
   ALERT5 = 3,   ///< ready to take off 5分钟警戒状态，准备起飞
   PRETAKEOFF = 4, ///< a hack to get a/c to stay in launch spot but take some time to takeoff 起飞前准备，一个让飞机停留在发射点但稍作等待的临时状态
   TAKEOFF = 5   ///< move to launch and take off 起飞，移动到发射点并起飞
};
enum teOperation
{
   OP_NONE = 0, ///无操作，表示当前没有进行任何任务或活动
   OP_TRANSIT = 1,///过境或移动，表示单位正在从一个地点移动到另一个地点
   OP_UNLOAD = 2, ///卸载，表示单位正在卸载货物、乘客或其他资源
   OP_LOAD = 3,   ///< or refuel 装载，表示单位正在装载货物、乘客或进行加油等活动
   OP_REPAIR = 4, ///<维修，表示单位正在进行维修工作，以修复损伤或故障
   OP_MAINTENANCE = 5 ///维护，表示单位正在进行日常维护或保养工作，以确保其处于良好状态
};

/**
* state info for units in the flightport
* This state info is unique info particular to flightport operations
* 这是飞行港口中单位的状态信息，这些状态信息是飞行港口操作特有的
*/
class tcAirState
{
public:
    teLocation current_location;     ///< 当前位置，表示单位当前所在的飞行港口区域（如机库、甲板等）
    int current_spot;                ///< 当前位置的具体编号，用于在特定区域（如甲板上的特定位置）内标识单位
    teLocation goal_location;        ///< 目标位置，表示单位计划前往的飞行港口区域
    int goal_spot;                   ///< 目标位置的具体编号，表示单位在目标区域内的具体目的地（如某个特定的发射点）
    bool inTransit;                  ///< 是否在移动中，表示单位是否正在从一个位置移动到另一个位置
    teOperation op;                  ///< 当前操作，表示单位当前正在执行的任务类型（如装载、维修等）
    double ready_time;               ///< 准备完成时间，表示单位完成当前操作并准备就绪的时间（可能是一个未来的时间点）
    std::shared_ptr<tcAirObject> obj;                ///< 关联对象，指向与当前状态相关联的空中单位对象（可能包含了更多关于该单位的信息）

    unsigned int lastMultiplayerUpdate; // for multiplayer client  ///< 上次多人游戏更新时间，用于多人游戏客户端，以跟踪状态信息的最后更新时间
	tcUpdateStream& operator<<(tcUpdateStream& stream);
	tcUpdateStream& operator>>(tcUpdateStream& stream);
	tcGameStream& operator<<(tcGameStream& stream);
	tcGameStream& operator>>(tcGameStream& stream);

	std::string LocationToString(teLocation loc);
	std::string OperationToString(teOperation op);
};

/**
 * Physical information about spot along with pointer to tcAirState object
 * for occupying unit. obj_info is NULL if the spot is empty.
 * // 注释：关于某个位置（点）的物理信息以及指向占据该位置的单位（如果有）的tcAirState对象的指针。如果位置为空，则obj_info为NULL。
 */
struct tsSpotInfo
{
    tcAirState *obj_info;
    ///< air state info for object occupying or in transit to spot, NULL if empty
    // 注释：指向占据该位置或正在前往该位置的对象的空中状态信息的指针。如果位置为空，则为NULL。

    float x,y,z;
    ///< surface assumed flat in between spots [m]
    // 注释：位置的x、y、z坐标（以米为单位），假设各点之间的表面是平坦的。

    float orientation;
    ///< orientation for runway, 0 along -z axis (heading axis for ships)
    // 注释：跑道的方向，0表示沿着-z轴（对于船只来说是航向轴）。

    float length;
    ///< [m]
    // 注释：长度（以米为单位）。这个长度可能指的是跑道、停机坪或其他设施的长度。

    bool IsEmpty() const
    {
        return obj_info == 0;
    }
    // 注释：一个常量成员函数，用于检查该位置是否为空。如果obj_info为NULL（即0），则返回true，表示位置为空。
};

/**
 * Models carrier flight deck, airstrips, helo pads.
 * Possibly should be modified to inherit from tcGameObject in the future.
 * // 注释：模拟航母飞行甲板、跑道、直升机停机坪等。未来可能需要修改为从tcGameObject继承。
 */
class tcFlightPort
{
public:
    std::vector<std::shared_ptr<tcAirObject>> toLand;
    ///< objects that have landed but haven't been added to units yet
    // 注释：已降落但尚未添加到单位列表中的空中对象。
    std::vector<tcAirState*> units;
    ///< air units in tcFlightPort
    // 注释：在tcFlightPort中的空中单位。
    std::vector<std::shared_ptr<tcAirObject>> toLaunch;
    ///< air units for game engine to launch (take ownership of)
    // 注释：游戏引擎需要发射（并接管）的空中单位。
    std::shared_ptr<tcGameObject> parent;
    ///< parent object of flightport
    // 注释：飞行港口的父对象。
    double last_update_time;
    // 注释（新增）：上次更新时间，用于跟踪飞行港口状态的最新更新时间。
    // （原有注释已保留，但此字段的用途通常与跟踪状态更新相关，因此我添加了一个通用的解释）

    int AddObject(std::shared_ptr<tcAirObject>obj, teLocation loc, unsigned int position);
    void AddSpot(teLocation loc, float x, float y, float z, float orientation = 0, float length = 0);
    int CheckLanding(std::shared_ptr<tcAirObject> obj);
    void Clear(); 
    int FindAirState(tcAirState* airstate);
	int FindAirState(std::shared_ptr<tcGameObject> obj);
    tcAirState* FindAirStateObj(std::shared_ptr<const tcGameObject> obj);
    const tcAirState* FindAirStateObj(std::shared_ptr<const tcGameObject> obj) const;
    int FindEmptySpot(std::vector<tsSpotInfo> *loc_vector);
    int FindEmptySpot(teLocation loc, std::vector<tsSpotInfo>*& loc_vector);
    tcAirState* GetAirState(unsigned n);
	const tcAirState* GetAirState(unsigned n) const;
    int GetAirStateIdx(long id) const;
    size_t GetCount() const {return units.size();}
    tsSpotInfo* GetCurrentSpotInfo(tcAirState *airstate);
    std::shared_ptr<tcFlightportDBObject> GetDatabaseObject() const;
    unsigned GetHangarCapacity() const {return hangarCapacity;}
    tcTrack GetLandingData(std::shared_ptr<const tcGameObject> obj);
    std::shared_ptr<tcGameObject> GetObject(unsigned n);
	std::shared_ptr<tcGameObject> GetObjectById(long id);
    std::shared_ptr<tcGameObject> GetObjectByName(const std::string& unitName);

    float GetTimeToDestination(const tcAirState* airstate) const;
    const std::string& GetTimeToDestinationString(const tcAirState* airstate) const;

    std::vector<tsSpotInfo>* GetLocVector(teLocation loc);
    void InitFromDatabase(std::shared_ptr<database::tcFlightportDBObject>dbObj);
    void InitRelPos(tcAirState *airstate);
	bool IsHeloOnly() const;
    int LaunchRunway(int runway); // order unit on runway to take off
    int LaunchID(long id);  // order unit with id to take off
    int LaunchAirstate(tcAirState* airstate);
	bool IsQueuedForTakeoff(long id) const;

    float GetMaxRunwayLength() const;

    bool MoveToLaunchQueue(tcAirState *airstate);
    void SetObjectDestination(unsigned n, teLocation loc, unsigned int position = 0);
	void SetObjectDestination(tcAirState* airstate, teLocation loc, unsigned int position = 0);
    void SetParent(std::shared_ptr<tcGameObject>newparent) {parent=newparent;}
    void SetHangarCapacity(unsigned cap) {hangarCapacity = cap;}
    void Update(double t);
    void UpdateLanded();
	void UpdateRefueling(tcAirState *airstate);
    void UpdateRelPos(tcAirState *airstate, double time);
    void UpdateUnitKin(tcAirState *airstate); // update unit kinematics based on parent info and rel_pos

	ai::tcMissionManager* GetMissionManager();
	ai::tcMissionManager* GetOrCreateMissionManager();

    tcCommandStream& operator<<(tcCommandStream& stream);
    tcCreateStream& operator<<(tcCreateStream& stream);
    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcGameStream& operator<<(tcGameStream& stream);

    tcCommandStream& operator>>(tcCommandStream& stream);
    tcCreateStream& operator>>(tcCreateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    void ClearNewCommand();
    bool HasNewCommand() const;

    static void InitTransitionTimes();

    tcFlightPort();
    ~tcFlightPort();
private:
    const float maxTakeoffDamage;
    ///< max damage level where takeoff is allowed
    // 注释：允许起飞的最大损伤程度。

    /* tcAirState objects for all units in flightport are stored in
** the units vector */
    // 注释（保留并解释）：飞行港口中所有单位的tcAirState对象都存储在units向量中。
    // （注意：这里的注释是跨行的，我将其整合到了一行中并保留了原意）

    std::vector<tsSpotInfo> ready_spots;
    ///< ready spots where units can be positioned before launch
    // 注释：准备点，单位在发射前可以停放的位置。

    std::vector<tsSpotInfo> launch_spots;
    ///< launch spots where units can take off from
    // 注释：发射点，单位可以从这里起飞。

    static float transitionTimesFast[6][6];
    ///< static array to hold transition times between spots for fast movement
    // 注释：静态数组，用于存储各点之间快速移动所需的过渡时间。

    static float transitionTimesNormal[6][6];
    ///< static array to hold transition times between spots for normal movement
    // 注释：静态数组，用于存储各点之间正常移动所需的过渡时间。

    std::shared_ptr<tcFlightportDBObject> mpDBObject;
    ///< pointer to multiplayer database object associated with this flightport
    // 注释：指向与此飞行港口关联的多人游戏数据库对象的指针。

    unsigned hangarCapacity;
    ///< maximum number of units that can be stored in the hangar
    // 注释：机库能够存储的最大单位数量。

    unsigned inHangarCount;
    ///< count of units in hangar or in transit to hangar
    // 注释：机库内或在前往机库的途中的单位数量。

    short int localId;
    ///< used to assign object id within flightport
    // 注释：用于在飞行港口内分配对象ID。

    // data for multiplayer commands
    struct CommandInfo
    {
        short int id;
        ///< id of unit that command applies to
        // 注释：命令所应用的单位的ID。

        unsigned char op;
        ///< 0, launch unit, 1-3 move unit
        // 注释：操作码，0表示发射单位，1-3表示移动单位。

        unsigned char pos;
        ///< position parameter to specify which launch or ready spot to move to
        // 注释：位置参数，用于指定要移动到哪个发射点或准备点。
    };

    std::vector<CommandInfo> commandList;
    ///< list of commands to be executed by the flightport
    // 注释：飞行港口要执行的命令列表。

    ai::tcMissionManager* missionManager;
    ///< pointer to mission manager for AI-related tasks
    // 注释：指向用于AI相关任务的任务管理器的指针。

    size_t nextUpdateIdx;
    ///< to track partial updates on multiplayer server
    // 注释：用于跟踪多人游戏服务器上部分更新的索引。
	teLocation GetNextStop(teLocation current, teLocation destination) const;
    void MoveObjectToDestination(tcAirState *airstate, teLocation destination, int spot);
	bool IsSpotEmpty(teLocation loc, unsigned int spot);
	void ResyncSpots();
    void RemoveStaleUnits();
    void RemoveDestroyedUnits();
    void SetReadyTime(double t, tcAirState* airstate, teLocation nextLocation);
    void UpdateMaintenance(tcAirState* airstate);
    void UpdatePlatform(tcAirState* airstate);
};
#endif

