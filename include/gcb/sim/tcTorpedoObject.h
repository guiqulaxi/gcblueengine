/**
**  @file tcTorpedoObject.h
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

#ifndef _TCTORPEDOOBJECT_H_
#define _TCTORPEDOOBJECT_H_

#include "tcSensorPlatform.h"
#include "tcWeaponObject.h"
#include "tcGuidanceState.h"
#include "tcSonar.h"

class tcUpdateStream;
class tcGameStream;

namespace database
{
    class tcTorpedoDBObject;
}

/**
* A class that models a torpedo.
*
* @see tcGameObject
*/
class tcTorpedoObject : public tcWeaponObject
{
public:
    /**
    *  鱼雷搜索模式
    */
    enum TorpedoSearchMode // 定义鱼雷搜索模式的枚举类型
    {
        SEARCH_STRAIGHT = 0,   // 直线搜索模式
        SEARCH_SNAKE = 1,      // 蛇形搜索模式
        SEARCH_LEFTCIRCLE = 2, // 左圆搜索模式
        SEARCH_RIGHTCIRCLE = 3 // 右圆搜索模式
    };
    float goalDepth_m;         // 目标深度（米）
    float goalHeading_rad;     // 目标航向（弧度）
    float goalPitch_rad;       // 目标俯仰角（弧度）
    float goalSpeed_kts;       // 目标速度（节）
    double interceptTime;      // 截击时间（秒或根据上下文可能的其他单位）
    float runTime; ///< [s] time elapsed since launch 自发射以来的已用时间（秒）
    float searchStartTime; ///< [s] run time that search started, used for heading guidance 搜索开始时的已用时间（秒），用于航向引导


    // are all 3 of these necessary? needs refactoring
    double lastGuidanceUpdate; // 上次引导更新的时间（可能根据上下文有不同的单位）
    float guidanceUpdateInterval; // 引导更新间隔（秒）

    GeoPoint waypoint;   // nav datum 导航数据点（可能包含经纬度等信息）
    float runToEnable_m;  //启动前需运行的距离（米）
    float ceiling_m; // min depth 最小深度（米）
    float floor_m; // max depth 最大深度（米）
    bool isWireActive; // true if wire is available to receive remote commands 线导雷
    bool autoWireUpdates; ///< true to automatically update guidance based on intended target and sensor map 如果要根据预定目标和传感器地图自动更新引导则为真

    std::shared_ptr<tcSonar> seeker;

    float battery_kJ;  ///< current battery charge 当前电池电量（千焦耳）
    float searchHeading_rad; ///< center of "S" sector to search 搜索的中心航向（弧度），即“S”形搜索的中心线
    int searchMode; //搜索模式（使用上面定义的枚举类型）

    std::shared_ptr<tcTorpedoDBObject>mpDBObject; // pointer to valid database obj

    void Clear();
	virtual void LaunchFrom(std::shared_ptr<tcGameObject> obj, unsigned nLauncher);
    void RandInitNear(float afLon_deg, float afLat_deg);

    virtual void Update(double afStatusTime);
   // virtual void UpdateEffects();
    virtual void UpdateGuidance(double t);

    void SetAltitude(float alt_m);
    virtual void SetHeading(float newHeading);
    virtual void SetSpeed(float newSpeed);
    virtual std::shared_ptr<tcSonar> GetSensorState();
	virtual float GetSonarSourceLevel(float az_deg) const;
    virtual void DesignateTarget(long anID);
    virtual int GetGuidanceParameters(tsGuidanceParameters& gp);
    float RuntimeRemaining();
    void PrintToFile(tcFile&) override;
    void SaveToFile(tcFile& file) override;
    void LoadFromFile(tcFile& file);
    virtual void Serialize(tcFile& file, bool mbLoad);

    virtual tcUpdateStream& operator<<(tcUpdateStream& stream);
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream);
    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

    tcTorpedoObject();
    tcTorpedoObject(tcTorpedoObject&);
    tcTorpedoObject(std::shared_ptr<tcTorpedoDBObject>obj);
    ~tcTorpedoObject();
protected:
    virtual void UpdateDrop(float dt_s);
    virtual void UpdateSpeedSimple(float dt_s);
    void UpdateDetonation();//起爆
	void UpdateDetonationUnguided();
    void UpdateDepthCharge(float dt_s);
	void UpdateDepthChargeDetonation();
    void UpdateBottomMine(float dt_s);
    void UpdateBottomMineTrigger(double t);
    void UpdateAutoWireGuidance();

};
#endif
