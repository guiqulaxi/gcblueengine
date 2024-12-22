/**
**  @file tcSensorMapTrack.h
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


#ifndef _SENSORMAPTRACK_H_ 
#define _SENSORMAPTRACK_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "simmath.h"
#include "tcFile.h"
#include <vector>
#include <deque>
#include "tcAllianceInfo.h"
#include "tcSensorReport.h"

class tcSimState;
class tcUpdateStream;
class tcGameStream;
class tcGameObject;
namespace database
{
	class tcDatabase;
}
using database::tcDatabase;



struct EmitterInfo 
{
	long mnEmitterID; ///< database ID of emitter
	double mfTimestamp;
	int mnMode;

    std::string GetEmitterName() const;
};



/**
* State info for track stored in alliance sensor map.
* The targetedRating is used by the AI to avoid inefficient ganging up on track.
* engageRating controls how much ordance
* 每一个平台都会对应一个 tcSensorMapTrack
*/
class tcSensorMapTrack : public tcTrack
{
public:
        // 定义一些常量
    enum {MAX_SENSOR_REPORTS = 64, GOAL_SENSOR_REPORTS = 8, MAX_EMITTERS = 4};

    // 存储最近来自传感器的数据
    std::deque<tcSensorReport> maSensorReport;

    // 存储传感器对外辐射信息
    std::vector<EmitterInfo> emitterInfo;
    // 评估的损伤值
    float assessedDamage;
    // 拦截此跟踪的平台ID列表
    std::vector<long> intercepts;
    // 跟踪/参与此跟踪的武器ID列表
    std::vector<long> engaged;
    // 与检测到的发射器一致的平台ID列表
    std::vector<long> ambiguityList;

    // 误差多边形
    std::vector<tcPoint> errorPoly;
    // 误差多边形经度宽度（弧度）
    float errorPolyLonWidth_rad;
    // 误差多边形纬度宽度（弧度）
    float errorPolyLatWidth_rad;
    // 是否始终可见，直到被丢弃
    bool alwaysVisible;

    // 静态成员变量，用于调试目的（SEP2010）
    static unsigned int ambiguityListUpdates;
    // 静态成员变量，由 tcMultiplayerInterface 设置，以确定服务器是否将跟踪详细信息传递给客户端
    static bool sendDetailedTrackInfo;

    // 添加武器参与
    bool AddEngagement(long id);
    // 添加拦截平台
    bool AddIntercept(long id);
    // 添加传感器报告
    bool AddReport(const tcSensorReport& report);
    // 移除指定索引的报告
    void RemoveReport(size_t n);
    // 移除多个指定索引的报告
    void RemoveReports(const std::vector<size_t>& reportsToRemove);

    // 静态方法，设置指向 tcSimState 对象的指针
    static void AttachDatabase(tcDatabase* db) {database = db;}
    static void AttachSimState(tcSimState* ss) {simState = ss;}

    // 清空跟踪信息
    virtual void Clear();

    // 获取发射器数量
    size_t GetEmitterCount() const;
    // 获取指定索引的发射器信息（非修改）
    const EmitterInfo* GetEmitter(unsigned idx);
    // 获取指定索引的发射器信息（修改版）
    EmitterInfo GetEmitterInfo(unsigned idx);

    // 获取参与此跟踪的武器数量
    unsigned GetEngagedCount() const;
    // 获取拦截此跟踪的平台数量
    unsigned GetInterceptCount() const;

    // 获取贡献者数量
    size_t GetContributorCount() const;
    // 获取指定索引的贡献者名称
    const char* GetContributorName(unsigned idx) const;
    // 获取数据库ID
    long GetDatabaseId() const;
    // 获取最后报告时间
    double GetLastReportTime() const;

    // tc3DModel 相关的方法（已注释）
    //tc3DModel* GetModel() const;
    //void SetModel(tc3DModel* model_);

    // 获取自身指针（多态用途）
    const tcTrack* GetTrack() const {return this;}
    // 标识跟踪
    void IdentifyTrack(long id);
    // 设置隶属关系
    void SetAffiliation(tcAllianceInfo::Affiliation affil);

    // 检查是否已标识
    bool IsIdentified() const;
    // 检查是否为仅方位跟踪
    virtual bool IsBearingOnly() const;
    // 获取跟踪误差（公里）
    float TrackErrorKm() const;
    // 检查是否为新跟踪
    bool IsNew() const;
    // 检查是否已销毁
    bool IsDestroyed() const;
    // 检查是否已过时
    bool IsStale() const;
    // 标记为已销毁
    void MarkDestroyed();
    // 标记为已过时
    void MarkStale();
    // 清除过时状态
    void ClearStale();

    // 获取过时时间
    float GetStaleTime() const;
    // 获取老化时间
    float GetAgeOutTime() const;
    // 获取跟踪持续时间
    float GetTrackLife() const;

    // 计算到指定位置的距离（公里）
    float RangeToKm(float lon_rad, float lat_rad);
    // 计算到指定位置的方位（弧度）
    float BearingToRad(float lon_rad, float lat_rad);

    // 获取或创建指定平台和传感器的报告
    tcSensorReport* GetOrCreateReport(long platformID, long sensorID);

    // 更新模糊列表
    void UpdateAmbiguityList();
    // 更新分类
    void UpdateClassification(UINT16 mnClassification);
    // 更新发射器信息
    bool UpdateEmitter(EmitterInfo*& rpEmitterInfo, long anEmitterID);

    // 更新参与此跟踪的武器列表
    void UpdateEngagements();
    // 更新拦截此跟踪的平台列表
    void UpdateIntercepts();

    // 更新跟踪信息
    void UpdateTrack(double tCoast_s);

    // 获取与此跟踪相关联的 tcGameObject 对象
    std::shared_ptr<tcGameObject> GetAssociated();
    // 获取与此跟踪相关联的 tcGameObject 对象的常量指针
    std::shared_ptr<const tcGameObject> GetAssociatedConst() const;

    // 序列化/反序列化到更新流
    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);

    // 序列化/反序列化到游戏流
    tcGameStream& operator<<(tcGameStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    // 赋值操作符（注意：这里的实现可能不正确，应返回 *this）
    std::shared_ptr<tcSensorMapTrack> operator= (std::shared_ptr<tcSensorMapTrack>pa) {return pa;}
    // 复制构造函数和赋值操作符（可能未完全实现）
    tcSensorMapTrack& operator= (const tcSensorMapTrack&);
    tcSensorMapTrack(const tcSensorMapTrack& src);
    // 构造函数和析构函数
    tcSensorMapTrack(const tcTrack& src);
    tcSensorMapTrack();
    ~tcSensorMapTrack();

    // 静态方法，设置自动销毁评估状态
    static void SetAutoKillAssess(bool state);

private:
    // 静态成员变量，指向 tcSimState 和 tcDatabase
    static tcSimState* simState;
    static tcDatabase* database;
    // 自动销毁评估标志
    static bool autoKillAssess;
    // 跟踪状态标志（过时、已销毁）
    enum {TRACK_STALE = 1, TRACK_DESTROYED = 2};
    unsigned char sensorFlags;
    // 数据库ID
    long mnDatabaseID;
    // tc3DModel 相关成员（已注释）
    //tc3DModel* model;

    // 不同类型的过时和老化时间

    // age out and stale times for tracks
    static float unknownStale;
    static float unknownAgeOut;
    static float missileStale;
    static float missileAgeOut;
    static float torpedoStale;
    static float torpedoAgeOut;
    static float airStale;
    static float airAgeOut;
    static float surfaceStale;
    static float surfaceAgeOut;
    static float groundStale;
    static float groundAgeOut;
    static float reportAgeOut;

    // 尝试进行被动三角测量以更新或验证目标的位置信息
    bool AttemptPassiveTriangulation();

    // 停止或终止当前的评估或分析过程
    void KillAssess();

    // 更新目标的“始终可见”状态，这可能与目标的显示或追踪策略有关
    void UpdateAlwaysVisible();

    // 更新通用的模型参数或状态，这些参数可能与目标的运动模式或外观相关
    void UpdateGenericModel();

    // 使用被动追踪方法更新目标的轨迹信息
    void UpdateTrackWithPassive();

    // 更新与发射器（可能是雷达、激光等）相关的信息，如位置、方向等
    void UpdateEmitters();

    // 验证目标的轨迹信息，可能包括检查轨迹的合理性或进行错误检测
    void ValidateTrack();

    // 根据给定的时间t和基础传感器报告base，预测并生成未来的传感器报告prediction
    void PredictReport(double t, const tcSensorReport& base, tcSensorReport& prediction);

    // 获取模型的参数，这些参数可能用于描述目标的运动特性
    // 包括线性时间（秒）、默认速度（米/秒）、默认爬升角（弧度）、加速度（米/秒^2）、
    // 爬升率（弧度/秒）和航向变化率（弧度/秒）
    void GetModelParameters(float& linearTime_s, float& defaultSpeed_mps, float& defaultClimbAngle_rad,
                            float& accel_mps2, float& climbRate_radps, float& headingRate_radps);
    // 更新错误多边形（可能是用于估计目标位置不确定性的图形表示）的宽度
    void UpdateErrorPolyWidth();

    // 修剪（删除）旧的或不再相关的报告信息，以保持数据的时效性和准确性
    void PruneReports();
};

#endif 

