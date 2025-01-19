/** 
**  @file tcLauncher.h
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

#ifndef _TCLAUNCHER_H_
#define _TCLAUNCHER_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


#include "simmath.h"
#include "AError.h"
#include <vector>

namespace database
{
    class tcDatabase;
    class tcLauncherDBObject;
    class tcDatabaseObject;
    enum teWeaponLaunchMode;
}

using namespace database;

class tcGameObject;
class tcPlatformObject;
class tcSimState;
class tcSensorState;
class tcRadar;
class tcStream;
class tcCommandStream;
class tcCreateStream;
class tcUpdateStream;
class tcGameStream;
class tcStores;
class tcSensorMapTrack;

/**
 * State for individual launcher.
 * 该类表示单个发射器的状态，用于管理发射器的属性、状态和行为。
 */
class tcLauncher
{
public:
    // 发射器状态枚举，表示发射器的各种可能状态
    enum teLauncherStatus
    {
        LAUNCHER_READY = 0, ///< 发射器准备就绪
        BAD_LAUNCHER = 1, ///< 发射器索引不存在
        LAUNCHER_EMPTY = 2, ///< 发射器为空
        LAUNCHER_BUSY = 3, ///< 发射器正在自动装填
        NO_DATUM = 4, ///< 没有目标点
        NO_TARGET = 5, ///< 没有目标
        NOT_DETECTED_FC = 6, ///< 火控传感器无法检测到目标（可能已关闭）
        NOT_DETECTED_SEEKER = 7, ///< 寻的器无法检测到目标
        FC_BUSY = 8, ///< 火控传感器没有空闲的跟踪通道
        LAUNCHER_ERROR = 9, ///< 发射器错误
        LAUNCHER_INACTIVE = 10, ///< 发射器未激活
        NO_FIRECONTROL = 11, ///< 没有火控系统
        TOO_DEEP = 12, ///< 对于潜艇发射来说太深
        TOO_LOW = 13, ///< 对于飞机导弹发射来说太低
        TOO_HIGH = 14, ///< 对于飞机导弹发射来说太高
        DAMAGED = 15, ///< 由于损坏无法操作
        INVALID_TARGET = 16, ///< 对目标类型无效
        OUT_OF_RANGE = 17, ///< 目标超出最大射程
        INVALID_FUEL_OPERATION = 18, ///< 外部燃料箱的无效操作
        LAUNCHER_LOADING = 19, ///< 发射器正在装填（用于多人游戏）
        LAUNCHER_UNLOADING = 20, ///< 发射器正在卸载（用于多人游戏）
        OUT_OF_FOV = 21, ///< 目标在发射器的视场外
        TOO_CLOSE = 22, ///< 目标在最小射程内
        LAUNCHER_EMPTY_AUTORELOAD = 23, ///< 发射器为空，准备自动装填（延迟自动装填的临时解决方案）
        ROE_HOLD = 24 ///< 发射器准备就绪，但发射违反交战规则（ROE）
    }; ///< 发射器状态码

    short int mbActive; ///< 发射器是否激活

    std::string displayName; ///< 发射器的显示名称
    long mnDBKey; ///< 发射器在数据库中的键值
    std::shared_ptr<tcLauncherDBObject>mpLauncherDBObj; ///< 发射器的数据库对象
    long mnChildDBKey; ///< 当前装载的子对象（如导弹、鱼雷）的数据库键值
    std::shared_ptr<tcDatabaseObject>mpChildDBObj; ///< 当前装载的子对象的数据库对象
    bool isExternalFuelTank; ///< 如果子对象是外部燃料箱，则为true
    float itemWeight_kg; ///< 当前装载物品的单位重量（千克）

    float mfTimeToReady; ///< 发射器准备就绪的时间
    short int mnCurrent; ///< 当前装载的物品数量
    short int mnUncommitted; ///< 未提交的物品数量（mnCurrent - mnUncommitted = 待发射的数量）
    bool isLoading; ///< 如果发射器正在装载或卸载武器，则为true
    unsigned short capacity; ///< 当前子类别的最大容量
    unsigned char repeatShots; ///< 设置为非零值以自动重复发射（用于火炮）

    GeoPoint msDatum; ///< 传递给武器导航的目标点
    long mnTargetID; ///< 寻的器可以获取的目标ID
    teWeaponLaunchMode meLaunchMode; ///< 武器发射模式
    short int mnTargetFlags; ///< 目标标志（0x01 - 水面，0x02 - 空中，0x03 - 地面）
    float pointingAngle; ///< 当前瞄准方位角（相对于船头/机头的弧度）
    float pointingElevation; ///< 当前瞄准仰角（相对于地平线的弧度）
    float firingArc_deg; ///< 发射器的射击角度范围（来自平台发射器表）
    float mountPointingAngle; ///< 可旋转发射器的旋转区域中心或固定发射器的固定角度（相对角度）
    float cycleTime_s; ///< 当前装载子对象的发射周期时间（来自发射器配置表）
    bool isReloadable; ///< 发射器是否可重新装填（来自平台发射器表）

    std::shared_ptr<tcSensorState> fireControlSensor; ///< 用于火控引导的传感器
    unsigned char fireControlSensorIdx; ///< 传感器在父平台上的索引

    // 鱼雷编程参数
    bool usePassive; ///< 是否使用被动声纳
    float preEnableSpeed_kts; ///< 启用前的速度（节）
    float runDepth_m; ///< 运行深度（米）
    float ceiling_m; ///< 最大高度（米）
    float floor_m; ///< 最小高度（米）
    float runToEnable_m; ///< 启用前的运行距离（米）

    // 序列化和反序列化操作符重载
    tcCommandStream& operator<<(tcCommandStream& stream);
    tcCreateStream& operator<<(tcCreateStream& stream);
    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcGameStream& operator<<(tcGameStream& stream);

    tcCommandStream& operator>>(tcCommandStream& stream);
    tcCreateStream& operator>>(tcCreateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    // 清除待发射状态
    void ClearPendingLaunch();
    // 检查命令信息是否匹配
    bool CommandInfoMatches(const tcLauncher& launcher);
    // 从另一个发射器复制命令信息
    void CopyCommandInfoFrom(const tcLauncher& launcher);
    // 获取当前子对象的类名
    const std::string& GetChildClassName() const;
    // 获取当前子对象的显示名称
    const std::string& GetChildClassDisplayName() const;
    // 获取当前子对象的数据库对象
    std::shared_ptr<tcDatabaseObject> GetChildDatabaseObject() const;

    // 获取发射器名称
    const std::string& GetLauncherName() const;
    // 获取发射周期时间
    float GetCycleTime() const;
    // 获取火控跟踪数量
    unsigned GetFireControlTrackCount() const; ///< 活动的火控跟踪数量（如果不可用则为0）
    // 获取最大火控跟踪数量
    unsigned GetMaxFireControlTracks() const; ///< 最大火控跟踪数量（如果不可用则为999）
    // 获取发射器状态
    int GetLauncherStatus();
    // 获取父平台对象
    std::shared_ptr<tcGameObject> GetParent() const;
    // 获取当前瞄准仰角
    float GetPointingElevation() const;
    // 获取发射器的扇形区域中心
    float GetSectorCenter() const; ///< 返回发射器扇形区域的中心角度（弧度）
    // 获取发射器的扇形区域宽度
    float GetSectorWidth() const; ///< 返回发射器扇形区域的宽度（弧度）
    // 获取发射器的总重量
    float GetWeight() const;
    // 获取当前装载物品的重量
    float GetItemWeight() const;
    // 检查是否自动瞄准
    bool IsAutoPoint() const;
    // 检查目标是否在发射器的视场内
    bool CheckTraversalFOV() const; ///< 如果目标在发射器的射击角度范围内，则返回true（用于火炮）
    // 获取自动瞄准的角度
    bool GetAutoPointing(float& az_rad, float& el_rad) const;

    // 检查发射器是否损坏
    bool IsDamaged() const;
    // 检查发射器是否正在装载
    bool IsLoading() const;
    // 检查发射器是否对目标分类有效
    bool IsEffective(unsigned int targetClassification) const;
    // 检查发射器是否对目标跟踪有效
    bool IsEffective(const tcSensorMapTrack& track) const;
    // 检查子对象是否为“发射后不管”类型
    bool IsChildFireAndForget();
    // 检查子对象是否为核武器
    bool IsLoadedNuclear() const;

    // 设置子对象的类
    void SetChildClass(const std::string& childClass, bool ignoreRestrictions = false);
    // 设置子对象的数量
    void SetChildQuantity(unsigned int quantity);
    // 设置发射器的损坏状态
    void SetDamaged(bool state);
    // 设置目标点
    void SetDatum(double lon_rad, double lat_rad, float alt_m);
    // 设置发射数量
    void SetLaunch(unsigned int quantity);
    // 设置装载状态
    void SetLoadState(bool state);
    // 设置父平台对象
    void SetParent(std::shared_ptr<tcPlatformObject>obj);
    // 设置视场角度
    void SetFOV(float fov_deg_);

    // 获取发射器对某物品的最大容量
    unsigned short GetCapacityForItem(const std::string& item) const;
    // 获取发射器对某物品的最大容量，并返回装载时间和周期时间
    unsigned short GetCapacityForItem(const std::string& item, float& loadTime_s, float& cycleTime_s) const;
    // 获取兼容物品的数量
    unsigned int GetCompatibleCount() const;
    // 获取兼容物品的名称
    const std::string& GetCompatibleName(unsigned int idx) const;
    // 获取兼容物品的数量
    unsigned int GetCompatibleQuantity(unsigned int idx) const;
    // 获取所有兼容物品的列表
    std::vector<std::string> GetAllCompatibleList();
    // 检查某物品是否兼容
    bool IsItemCompatible(const std::string& item) const;
    // 重新装填发射器
    bool Reload();
    // 查找装载的存储对象
    std::shared_ptr<tcStores> FindLoadingStores(unsigned int& opId);
    // 获取装载时间
    float GetLoadingTime();
    // 取消正在进行的装载操作
    void CancelLoadInProgress();
    // 排队自动重新装填
    void QueueAutoReload();

    // 获取发射器状态
    unsigned char GetStatus() const;
    // 更新发射器状态
    void UpdateStatus();
    // 更新发射器状态（基于寻的器跟踪）
    void UpdateStatusSeekerTrack(std::shared_ptr<tcGameObject> target);

    // 更新损坏评分
    void UpdateScoreForDamage(std::shared_ptr<tcGameObject> damager);
    // 激活火控传感器
    void ActivateFireControl();
    // 检查是否自动再次发射
    bool AutoLaunchAgain();
    // 设置发射器的重复发射模式
    void SetRepeatShotsForType();

    // 更新火控传感器
    void UpdateFireControlSensor();

    // 静态方法：附加仿真状态
    static void AttachSimState(tcSimState* ss);
    // 静态方法：翻译状态码为字符串
    static std::string TranslateStatus(int statusCode);
    // 翻译状态码为详细字符串
    const std::string& TranslateStatusDetailed(int statusCode) const;

    // 构造函数
    tcLauncher();
    // 带参数的构造函数
    tcLauncher(std::shared_ptr<tcLauncherDBObject> dbObj, std::shared_ptr<tcPlatformObject> parent_);
    // 析构函数
    ~tcLauncher();

private:
    std::shared_ptr<tcPlatformObject> parent; ///< 父平台对象
    bool isDamaged; ///< 发射器是否损坏
    unsigned char status; ///< 发射器状态
    static tcSimState* simState; ///< 仿真状态对象

    // 初始化新子对象
    void InitForNewChild(bool ignoreRestrictions = false);
    // 更新瞄准角度
    void UpdatePointingAngle();
};

// /**
//  * State for individual launcher.
//  */
// class tcLauncher
// {
// public:
//     enum teLauncherStatus
//     {
//         LAUNCHER_READY = 0,
//         BAD_LAUNCHER = 1, ///< launcher index does not exist
//         LAUNCHER_EMPTY = 2,
//         LAUNCHER_BUSY = 3, ///< launcher auto reloading
//         NO_DATUM = 4,
//         NO_TARGET = 5,
//         NOT_DETECTED_FC = 6, ///< fire control sensor can't detect target (could be off)
//         NOT_DETECTED_SEEKER = 7,  ///< seeker can't detect target
//         FC_BUSY = 8,  ///< fire control sensor has no free tracks
//         LAUNCHER_ERROR = 9,
//         LAUNCHER_INACTIVE = 10,
//         NO_FIRECONTROL = 11,
//         TOO_DEEP = 12, ///< too deep for sub launch
// 		TOO_LOW = 13, ///< too low for aircraft missile launch
// 		TOO_HIGH = 14, ///< too high for aircraft missile launch
//         DAMAGED = 15, ///< cannot operate due to damage
// 		INVALID_TARGET = 16, ///< not effective vs. target type
// 		OUT_OF_RANGE = 17, ///< target is beyond max range
// 		INVALID_FUEL_OPERATION = 18, ///< invalid op for external fuel tank
//         LAUNCHER_LOADING = 19, ///< added for multiplayer, loading from magazine
//         LAUNCHER_UNLOADING = 20, ///< added for multiplayer, unloading to magazine
//         OUT_OF_FOV = 21, ///< target is outside of field of view of this launcher
//         TOO_CLOSE = 22, ///< target is inside minimum range
//         LAUNCHER_EMPTY_AUTORELOAD = 23, ///< empty, try autoreload when ready, workaround to delay auto-reload until after launch
//         ROE_HOLD = 24 ///< ready, but launch violates ROE
//     }; ///< launcher status codes

//     short int mbActive;

//     std::string displayName;
//     long mnDBKey; ///< key in launcher database
//     std::shared_ptr<tcLauncherDBObject>mpLauncherDBObj;
//     long mnChildDBKey;
//     std::shared_ptr<tcDatabaseObject>mpChildDBObj;
// 	bool isExternalFuelTank; ///< true if child is fuel tank
//     float itemWeight_kg; ///< current unit weight of loaded items

//     float mfTimeToReady;
//     short int mnCurrent;
//     short int mnUncommitted; ///< mnCurrent - mnUncommitted = # pending launch
//     bool isLoading; ///< true if launcher is offline to load/unload weapons
//     unsigned short capacity; ///< max capacity for current child class
//     unsigned char repeatShots; ///< set to non-zero to automatically repeat shots (for guns)

//     GeoPoint msDatum; ///< datum to pass to weapon nav guidance
//     long mnTargetID; ///< track that seeker can acquire
//     teWeaponLaunchMode meLaunchMode;
//     short int mnTargetFlags;  ///< 0x01 - surface, 0x02 - air, 0x03 - land
//     float pointingAngle; ///< current boresight azimuth angle in radians relative nose/bow
// 	float pointingElevation; ///< elevation angle in radians relative (to horizon?)
//     float firingArc_deg; ///< from platform_launcher table
// 	float mountPointingAngle; ///< center of traversal region for pointable launchers or fixed pointing angle for fixed launchers (RELATIVE angle)
//     float cycleTime_s; ///< from launcher_configuration table of current loaded child
//     bool isReloadable; ///< from platform_launcher table

//     std::shared_ptr<tcSensorState> fireControlSensor; ///< sensor for fire control guidance
//     unsigned char fireControlSensorIdx; ///< index of sensor on parent platform

//     // torpedo programming params
//     bool usePassive;
//     float preEnableSpeed_kts;
//     float runDepth_m;
//     float ceiling_m;
//     float floor_m;
//     float runToEnable_m;

//     tcCommandStream& operator<<(tcCommandStream& stream);
//     tcCreateStream& operator<<(tcCreateStream& stream);
//     tcUpdateStream& operator<<(tcUpdateStream& stream);
//     tcGameStream& operator<<(tcGameStream& stream);

//     tcCommandStream& operator>>(tcCommandStream& stream);
//     tcCreateStream& operator>>(tcCreateStream& stream);
//     tcUpdateStream& operator>>(tcUpdateStream& stream);
//     tcGameStream& operator>>(tcGameStream& stream);

//     void ClearPendingLaunch();
//     bool CommandInfoMatches(const tcLauncher& launcher);
//     void CopyCommandInfoFrom(const tcLauncher& launcher);
//     const std::string& GetChildClassName() const;
//     const std::string& GetChildClassDisplayName() const;
//     std::shared_ptr<tcDatabaseObject> GetChildDatabaseObject() const;
    
//     const std::string& GetLauncherName() const;
// 	float GetCycleTime() const;
// 	unsigned GetFireControlTrackCount() const; ///< active FC tracks (0 if N/A)
// 	unsigned GetMaxFireControlTracks() const; ///< max FC tracks (999 if N/A)
//     int GetLauncherStatus();
// 	std::shared_ptr<tcGameObject> GetParent() const;
// 	float GetPointingElevation() const;
//     float GetSectorCenter() const; ///< returns center of engagement sector in radians
//     float GetSectorWidth() const; ///< returns width of engagement sector in radians
//     float GetWeight() const;
//     float GetItemWeight() const;
//     bool IsAutoPoint() const;
//     bool CheckTraversalFOV() const; ///< true to require target to be within FiringArc_deg of launcher (gun rounds)
//     bool GetAutoPointing(float& az_rad, float& el_rad) const;

//     bool IsDamaged() const;
// 	bool IsLoading() const;
// 	bool IsEffective(unsigned int targetClassification) const;
// 	bool IsEffective(const tcSensorMapTrack& track) const;
// 	bool IsChildFireAndForget();
//     bool IsLoadedNuclear() const;

//     void SetChildClass(const std::string& childClass, bool ignoreRestrictions = false);
//     void SetChildQuantity(unsigned int quantity);
//     void SetDamaged(bool state);
// 	void SetDatum(double lon_rad, double lat_rad, float alt_m);
// 	void SetLaunch(unsigned int quantity);
//     void SetLoadState(bool state);
//     void SetParent(std::shared_ptr<tcPlatformObject>obj);
// 	void SetFOV(float fov_deg_);

//     /// @return max quantity of item that launcher can hold, 0 if not compatible
//     unsigned short GetCapacityForItem(const std::string& item) const;
//     unsigned short GetCapacityForItem(const std::string& item, float& loadTime_s, float& cycleTime_s) const;
//     unsigned int GetCompatibleCount() const;
//     const std::string& GetCompatibleName(unsigned int idx) const;
// 	unsigned int GetCompatibleQuantity(unsigned int idx) const;
//     std::vector<std::string> GetAllCompatibleList();
//     bool IsItemCompatible(const std::string& item) const;
//     bool Reload();
//     std::shared_ptr<tcStores> FindLoadingStores(unsigned int& opId);
//     float GetLoadingTime();
//     void CancelLoadInProgress();
//     void QueueAutoReload();

// 	unsigned char GetStatus() const;
// 	void UpdateStatus();
//     void UpdateStatusSeekerTrack(std::shared_ptr<tcGameObject> target);

//     void UpdateScoreForDamage(std::shared_ptr<tcGameObject> damager);
//     void ActivateFireControl();
// 	bool AutoLaunchAgain();
//     void SetRepeatShotsForType();

//     void UpdateFireControlSensor();

//     static void AttachSimState(tcSimState* ss);
//     static std::string TranslateStatus(int statusCode);
//     const std::string& TranslateStatusDetailed(int statusCode) const;

//     tcLauncher();
//     tcLauncher(std::shared_ptr<tcLauncherDBObject> dbObj, std::shared_ptr<tcPlatformObject> parent_);
//     ~tcLauncher();
// private:
//     std::shared_ptr<tcPlatformObject> parent;
//     bool isDamaged;
// 	unsigned char status;
//     static tcSimState* simState;

// 	void InitForNewChild(bool ignoreRestrictions = false);
// 	void UpdatePointingAngle();

// };
#endif
