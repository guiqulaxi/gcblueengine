/** 
**  @file tcMissileObject.h
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

#ifndef _TCMISSLEOBJECT_H_
#define _TCMISSLEOBJECT_H_

#include "tcAero.h"
#include "tcWeaponObject.h"
#include "tcGuidanceState.h"
#include "tcRadar.h"
#include "tcSensorPlatform.h"
#include "tcSensorMapTrack.h"

class tcUpdateStream;
class tcGameStream;

/**
 * 表示导弹的类。
 * 该类继承自 tcWeaponObject，用于管理导弹的飞行、制导、目标跟踪等行为。
 *
 * @see tcGameObject
 */
class tcMissileObject : public tcWeaponObject
{
public:
    float goalHeading_rad; /// 目标航向（弧度）
    float goalPitch_rad;   /// 目标俯仰角（弧度）
    float goalAltitude_m;  /// 目标高度（米）
    double mfInterceptTime; /// 拦截时间
    bool subSurfaceLaunch; /// 是否为水下发射阶段（用于潜射导弹）

    // 以下三个变量是否都需要？需要重构
    float mfLastGuidanceUpdate; /// 上次制导更新的时间
    double guidanceStatusTime;  /// 制导状态时间
    float mfGuidanceUpdateInterval; /// 制导更新间隔

    GeoPoint msWaypoint;   /// 导航基准点
    std::vector<GeoPoint> preplanRoute; /// 预规划路径（适用于支持此功能的导弹）
    float mfRangeToObjective_km; /// 到目标的距离（用于段切换判断）
    unsigned int mnCurrentSegment; /// 当前飞行段

    Aero::tsMissileKState msKState; /// 导弹的运动状态
    std::shared_ptr<tcMissileDBObject> mpDBObject; /// 指向导弹数据库对象的指针

    void Clear(); /// 清除导弹状态
    virtual void LaunchFrom(std::shared_ptr<tcGameObject> obj, unsigned nLauncher); /// 从指定对象发射导弹
    void RandInitNear(float afLon_deg, float afLat_deg); /// 在指定经纬度附近随机初始化导弹
    virtual void Update(double afStatusTime); /// 更新导弹状态
    virtual void UpdateGuidance(double afStatusTime); /// 更新制导系统
    virtual void SetHeading(float afNewHeading) { goalHeading_rad = afNewHeading; } /// 设置目标航向
    teAltitudeMode GetCurrentAltitudeMode(); /// 获取当前高度模式
    teGuidanceMode GetCurrentGuidanceMode(); /// 获取当前制导模式
    float GetDistanceFromLaunch() const; /// 获取从发射点开始的距离
    void SetSeekerTarget(long id); /// 设置传感器目标
    virtual void ApplyRepairs(float repair); /// 应用修复

    void UpdateTargetPos(float lon_rad, float lat_rad); /// 更新目标位置

    virtual std::shared_ptr<tcRadar> GetSeekerRadar() const; /// 获取传感器雷达
    virtual std::shared_ptr<tcSensorState> GetSeekerSensor() const; /// 获取传感器状态
    virtual void DesignateTarget(long anID); /// 指定目标
    virtual int GetGuidanceParameters(tsGuidanceParameters& gp); /// 获取制导参数
    float RuntimeRemaining(); /// 获取剩余运行时间
    bool StillNeedsIlluminator(long& platformId) const; /// 检查是否仍需要照射器

    virtual float GetOpticalCrossSection() const; /// 获取光学横截面
    virtual float GetIRSignature(float az_deg) const; /// 获取红外特征

    void SetRandomPreplan(const std::string& planType); /// 设置随机预规划路径

    void PrintToFile(tcFile&) override; /// 打印信息到文件
    void SaveToFile(tcFile& file) override; /// 保存到文件
    void LoadFromFile(tcFile& file); /// 从文件加载
    virtual void Serialize(tcFile& file, bool mbLoad); /// 序列化

    virtual tcUpdateStream& operator<<(tcUpdateStream& stream); /// 更新流操作符重载
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream); /// 更新流操作符重载
    virtual tcGameStream& operator<<(tcGameStream& stream); /// 游戏流操作符重载
    virtual tcGameStream& operator>>(tcGameStream& stream); /// 游戏流操作符重载

    struct MissileTrajectory
    {
        std::vector<double> time_s; /// 时间（秒）
        std::vector<double> range_m; /// 地面覆盖距离（米）
        std::vector<double> altitude_m; /// 高度（米）
        std::vector<double> speed_mps; /// 速度（米/秒）
    };

    static float EstimateRangeKm(float evalMin_km, float evalMax_km, float evalStep_km,
                                 float launchSpeed_kts, float launchAltitude_m, float targetAltitude_m, std::shared_ptr<tcMissileDBObject> missileData, bool logData = true); /// 估计导弹射程（公里）
    static float EstimateRangeFaster(float evalMin_km, float evalMax_km, unsigned int nSteps,
                                     float launchSpeed_kts, float launchAltitude_m, float targetAltitude_m, std::shared_ptr<tcMissileDBObject> missileData); /// 快速估计导弹射程
    static bool EvaluateTarget(tcKinematics& missileKin, const tcSensorMapTrack& target, std::shared_ptr<tcMissileDBObject> missileData, MissileTrajectory* trajectory = 0); /// 评估目标
    tcMissileObject(); /// 构造函数
    tcMissileObject(tcMissileObject&); /// 拷贝构造函数
    tcMissileObject(std::shared_ptr<tcMissileDBObject> obj); /// 使用数据库对象初始化导弹
    ~tcMissileObject(); /// 析构函数

private:
    struct MissileSimData
    {
        Aero::tsMissileKState kstate; /// 导弹的运动状态
        tcKinematics missileKin; /// 导弹的运动学数据
        GeoPoint waypoint;   /// 导航基准点
        float rangeToObjective_km; /// 到目标的距离（用于段切换判断）
        float seekerDetectionRange_km; /// 传感器检测范围（公里）
        unsigned int segment; /// 当前飞行段
        float goalAltitude_m; /// 目标高度（米）
        float goalHeading_rad; /// 目标航向（弧度）
        float goalPitch_rad; /// 目标俯仰角（弧度）
        tcTrack targetTrack; /// 目标跟踪信息
        double interceptTime_s; /// 拦截时间（秒）
        float terrainHeight_m; /// 地形高度（米）
        bool endFlight; /// 是否结束飞行
        bool forceHit; /// 如果为 true，则将飞行结束视为“命中”
    };

    float distanceFromLaunch; /// 从发射点开始的距离（米）
    bool isTerminal; /// 是否为终端阶段
    bool isCommandHandoff; /// 是否处于指令切换模式

    void UpdateDetonation(); /// 更新引爆逻辑
    void UpdateGoalPitch(); /// 更新目标俯仰角
    void UpdateDatumInterceptGuidance(double t, bool& useInterceptPitch, float& interceptPitch_rad); /// 更新基准拦截制导
    static void UpdateGoalPitchSim(MissileSimData& simData, const std::shared_ptr<tcMissileDBObject> missileData); /// 更新模拟目标俯仰角

    void UpdateCommandHandoff(); /// 更新指令切换逻辑
    void UpdateSubsurface(double t); /// 更新水下发射阶段
    float GlimitedTurnRate() const; /// 获取受 G 限制的转向速率
    static float GlimitedTurnRate(float speed_kts, const std::shared_ptr<tcMissileDBObject> missileData); /// 静态方法：获取受 G 限制的转向速率

    static void UpdateGuidanceSim(MissileSimData& simData, const std::shared_ptr<tcMissileDBObject> missileData); /// 更新模拟制导
    static float EstimateSeekerDetectionRange(const tcSensorMapTrack& target, std::shared_ptr<tcMissileDBObject> missileData); /// 估计传感器检测范围
};

#endif
