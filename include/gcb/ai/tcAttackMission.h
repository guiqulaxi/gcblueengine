/**
**  @file tcAttackMission.h
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

#if _MSC_VER > 1000
#pragma once
#endif

#ifndef _TCATTACKMISSION_H_
#define _TCATTACKMISSION_H_

#include "ai/tcMission.h"
#include "simmath.h"
#include "tcDateTime.h"
#include <chrono>
class tcFlightPort;
class tcPoint;
class tcStream;
class tcGameStream;
class tcAirObject;

namespace scriptinterface
{
    class tcScenarioLogger;
}

namespace ai {

class BlackboardInterface;

/**
* Modified starting FEB 2009 to make this handle a variety of mission types
*/
class tcAttackMission : public tcMission
{
public:
	enum {NO_ANCHOR=0, NORTH_ANCHOR=1, HEADING_ANCHOR=2};
	void SetTargetDatum(float lon_rad, float lat_rad); // target for bombing or general area to search
    float GetTargetLon() const;
    float GetTargetLat() const;
    bool HasTarget() const;
    bool HasTargetDatum() const;

    void SetLaunchTime(const tcDateTime& dateTime);
    const tcDateTime& GetLaunchTime() const;
    void AdjustLaunchTimeHours(double offset_hr);

    void SetRandomLaunchTime(const tcDateTime& earliest, float window_min);
    const char* GetLaunchTimeString() const;
    void SetLaunchTimeFromString(const char* s);

    int GetSecondsToLaunch() const;

    unsigned int GetAirborneAircraftCount() const;

    void SetLandingTarget(const std::string& s);
    const std::string& GetLandingTarget() const;

    void SetArea(const std::vector<GeoPoint>& area);
    void SetAreaByString(const std::string& s);
    const char* GetAreaString() const;
    const std::vector<GeoPoint>& GetArea() const;
	void GetAreaCenter(double& lon_rad, double& lat_rad);
	void RecenterArea(double lon_rad, double lat_rad);
	void UpdateInFlightAircraft();

    void SetPatrolAnchor(const std::string& unitName, int mode);
    const std::string& GetPatrolAnchorUnit() const;
    int GetPatrolAnchorMode() const;
    void TransformToRelativePatrolArea();
    void TransformToAbsolutePatrolArea();

    unsigned int GetWaveQuantity() const;
    void SetWaveQuantity(unsigned int val);

    void SetMissionType(const std::string& s);
    const char* GetMissionType() const;

	void SetTargetType(int val);
	int GetTargetType() const;

	void SetAutoAdd(bool state);
	bool GetAutoAdd() const;

	void SetRepeatIntervalHours(float val);
	float GetRepeatIntervalHours() const;

	virtual void Update(double t);

    void UpdateRelativePosition();

    void SaveToPython(scriptinterface::tcScenarioLogger& logger);

    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

	const tcAttackMission& operator=(const tcAttackMission& src);
	tcAttackMission(const tcAttackMission& src);
    tcAttackMission(unsigned int id_, tcMissionManager* mm);
	tcAttackMission();
	virtual ~tcAttackMission();

protected:
    //    std::chrono::system_clock::time_point earliestLaunchTime; // 这行代码被注释掉了，原本用于定义最早发射时间的系统时钟时间点
    tcDateTime earliestLaunchTime; ///< 最早随机发射时间
    float launchWindow_min; ///< 在最早发射时间和最早发射时间加上发射窗口之间的时间范围内随机选择一个时间
    //    tcDateTime launchTime; // 这行代码被注释掉了，原本用于表示实际开始发射任务飞机的时间
    tcDateTime launchTime; ///< 实际开始发射任务飞机的时间

    float repeatInterval_hr; ///< 如果没有设置重复，则为0；表示发射后多少小时重新发射任务

    unsigned int quantity; ///< 执行任务所需的飞机数量
    int targetType; ///< 派生出的目标类型
    bool autoAdd; ///< 是否根据目标类型自动添加飞机

    float targetLon_rad; ///< 目标经度（弧度制）
    float targetLat_rad; ///< 目标纬度（弧度制）
    std::string landingTarget; ///< 着陆单位
    std::vector<GeoPoint> patrolArea; ///< 巡逻区域，包含多个地理坐标点
    std::string patrolAnchorUnit; ///< 巡逻锚点单位
    int patrolAnchorMode; ///< 枚举类型 {NO_ANCHOR=0, NORTH_ANCHOR=1, HEADING_ANCHOR=2}；表示没有锚点、以正北为锚点、以当前航向为锚点
    std::string missionType; ///< 类型字符串，用于向脚本任务规划模板传递信息

    // 如果patrolAnchorMode不为0，则使路线相对于主机平台
    GeoPoint referencePosition; ///< 参考位置
    float referenceHeading_rad; ///< 参考航向（弧度制）

    virtual void AddMissionAircraft(const std::string& name, const std::string& role);
    virtual void RemoveMissionAircraft(const std::string& name);

    void UpdateTargetInfo();
    void RemoveInactiveAircraft();
	void MonitorMissionInProgress();
    void InitializeLaunchTime();
	void UploadUnitMissionInfo( std::shared_ptr<tcAirObject> air);
    void UploadUnitPatrolInfo(ai::BlackboardInterface& bb);
    void GetReadyAircraft(std::vector<unsigned int>& readyAircraft);
    void GetAircraftToLoad(std::vector<unsigned int>& loadTheseAircraft);
    void UpdateActiveAircraft(unsigned int& nActive);
    void ReadyAllAircraft();
    void ReadyOverweightAircraft();
    
    void GetAreaBounds(tcGeoRect& r);
    bool MissionTypeIsReady();
    

};

} // namespace


#endif
