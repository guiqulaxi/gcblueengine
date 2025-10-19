/**
**  @file tcMissileDBObject.h
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

#ifndef _MISSILEDBOBJECT_H_
#define _MISSILEDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcWeaponDBObject.h"
#include "tcAirDetectionDBObject.h"
#include <vector>
#include <string>
namespace database
{
class tcSqlReader;

/**
   * 目前未使用。理论上，不同的伤害类型对不同的目标类型有不同的效果。
   */
enum teDamageType
{
    DT_GENERIC // 通用伤害类型
};

/**
   * teAltitudeMode 决定了飞行段的高度控制方式。
   */
enum teAltitudeMode
{
    AM_ASL = 0, /// 海平面参考高度
    AM_AGL = 1, /// 地形参考高度（使用高度计）
    AM_INTERCEPT = 2, /// 如果传感器有跟踪目标，则设置为拦截高度，否则保持当前高度
    AM_DATUM = 3, /// 设置为撞击基准高度
    AM_INTERCEPT_HIGH = 4, /// 如果目标较高，则设置为拦截高度，否则保持当前高度
    AM_ASL_LOFT = 5 /// 类似于 AM_ASL，但限制最大俯仰角
};

/**
   * teGuidanceMode 决定了飞行段的制导类型。
   */
enum teGuidanceMode
{
    GM_COMMAND = 0,  /// 指令制导
    GM_NAV = 1,  /// 惯性导航或 GPS 导航
    GM_SENSOR1 = 2, /// 使用传感器制导
    GM_DEPLOY = 3 /// 在此段开始时部署有效载荷
};

/**
   * 控制导弹飞行段行为的信息结构体。
   */
struct tsMissileFlightSegment
{
    float mfRange_km;    /// 此段的最小范围（公里）
    float mfAltitude_m;  /// 此段的高度（米）
    teAltitudeMode meAltitudeMode;   /// 高度模式
    teGuidanceMode meGuidanceMode;   /// 制导模式
};

#define MAX_MISSILE_FLIGHT_SEGMENTS 8 // 最大飞行段数

/**
   * 导弹数据库对象类，继承自 tcWeaponDBObject。
   */
class tcMissileDBObject : public tcWeaponDBObject
{
public:
    // 飞行模型参数
    float mfDragArea_sm;                ///< area for parasitic drag 这是用于寄生阻力的面积。寄生阻力是与物体形状和大小有关的阻力，不包括由于空气动力产生的推力
    float mfGmax;                       ///< max Gs 这是最大重力加速度，通常用于描述飞行器可以承受的最大过载
    float mfMaxTurnRate_degps;          ///< max (slow speed) turn rate 这是最大（低速）的旋转速率，以度每秒（degrees per second）为单位
    float mfCdpsub;                     ///< parasitic drag coeff, subsonic 这是亚音速的寄生阻力系数。
    float mfCdptran;                    ///< transonic 这是跨音速的寄生阻力系数。当飞行器在接近音速时，其阻力特性会发生变化。
    float mfCdpsup;                     ///< supersonic 这是超音速的寄生阻力系数。
    float mfMcm;                        ///< critical mach number 临界马赫数，这是描述飞行器或物体在某一速度下从亚音速过渡到超音速的马赫数。
    float mfMsupm;                      ///< supersonic mach number 超音速马赫数。描述飞行器或物体在超音速下的速度特性。
    float mfBoostThrust_N;              ///< boost thrust [N] 助推推力，以牛顿（N）为单位。在某些情况下，如火箭或某些导弹，在发射阶段需要更大的推力来达到所需的速度。
    float mfBoostTime_s;                ///< boost time [s] 助推时间，以秒为单位。描述助推阶段持续的时间长度。
    float mfSustThrust_N;               ///< sustainer thrust [N] 维持推力，以牛顿为单位。在达到所需速度后，可能需要较小的推力来维持飞行或推进。
    float mfSustTime_s;                 ///< sustainer time [s] 维持时间，以秒为单位。描述维持阶段持续的时间长度。
    float mfShutdownSpeed_mps;          ///< self destructs below this speed after flameout 在失去动力（flameout）后，飞行器或物体将在低于此速度时自动销毁或采取其他行动。这可能是为了防止故障或失去控制的飞行器造成损害。

    // 其他参数
    //float mfDamage;                   /// 伤害值（已注释）
    //teDamageType meDamageType;        /// 伤害类型枚举（已注释）
    //float mfRange_km;                 /// 标称范围（公里）（已注释，替换为 tcWeaponDBObject 中的 maxRange_km）

    // 传感器信息
    std::string maSensorClass;           /// 传感器数据库类名
    int sensorKey;                     /// 主传感器的快速访问键
    bool needsFireControl;              /// 如果传感器依赖火控传感器进行制导，则为 true
    bool acceptsWaypoints;              /// 如果导弹可以接受预规划（或数据链）航点，则为 true

    int fireAndForget;				  /// -1 未初始化，0 非发射后不管，1 发射后不管
    int isARM;                          /// -1 未初始化，0 非反辐射导弹，1 反辐射导弹

    float seekerFOV_rad;                /// 传感器视场角（弧度）
    
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

    float aczConstant_kts;              /// 空气动力学常数（节）
    float invMass_kg;                   /// 1/质量（千克），避免除法运算

    /// 飞行剖面，飞行段信息数组
    unsigned mnNumSegments;             /// 飞行段数量
    std::vector<tsMissileFlightSegment> maFlightProfile; /// 飞行段信息

    virtual const char* GetClassName() const {return "Missile";} /// 返回数据库对象的类名
    teWeaponLaunchMode GetLaunchMode() const; /// 获取发射模式
    int GetSensorKey(); /// 获取传感器键值
    float GetSeekerFOV(); /// 返回传感器视场角（弧度）
    bool HasAllEmitters(std::vector<int>& emitters); /// 检查是否包含所有发射器
    bool IsFireAndForget(); /// 是否为发射后不管导弹
    bool IsCommandLaunched() const; /// 是否为指令发射导弹
    bool IsARM(); /// 是否为反辐射导弹
    bool NeedsFireControl() const; /// 是否需要火控传感器
    bool AcceptsWaypoints() const; /// 是否接受航点
    float EstimateSpeed_mps() const; /// 估计速度（米/秒）
    virtual void PrintToFile(tcFile& file); /// 打印信息到文件

    static void AddSqlColumns(std::string& columnString); /// 添加 SQL 列
    void ReadSql(tcSqlReader& entry); /// 从 SQL 读取数据
    void WriteSql(std::string& valueString) const; /// 写入 SQL 数据
    void WritePythonValue(std::string& valueString) const; /// 写入 Python 值
    void WritePython(std::string& valueString) const; /// 写入 Python 数据
    void CalculateParams(); /// 计算参数

    tcMissileDBObject(); /// 构造函数
    tcMissileDBObject(const tcMissileDBObject& obj); /// 拷贝构造函数
    virtual ~tcMissileDBObject(); /// 析构函数
    virtual std::shared_ptr<tcGameObject> CreateGameObject() override; /// 创建游戏对象

private:
    std::string teAltitudeModeToString(teAltitudeMode data) const; /// 将高度模式转换为字符串
    std::string teGuidanceModeToString(teGuidanceMode data) const; /// 将制导模式转换为字符串
};
}

// namespace database
// {
//    class tcSqlReader;

//    /**
//    * This isn't used currently. Notionally there will be different
//    * damage types that have varying effectiveness vs. different
//    * target types.
//    */
//    enum teDamageType
//    {
//       DT_GENERIC
//    };

//    /**
//    * teAltitudeMode determines how altitude is controlled for flight segment.
//    */
//    enum teAltitudeMode
//    {
// 	   /// sea level reference
// 	   AM_ASL = 0,
// 	   /// terrain reference (altimeter)
// 	   AM_AGL = 1,
// 	   /// set altitude to intercept if seeker has track, otherwise maintain altitude
// 	   AM_INTERCEPT = 2,
// 	   /// set altitude to impact datum
// 	   AM_DATUM = 3,
// 	   /// Intercept if higher, otherwise maintain altitude
// 	   AM_INTERCEPT_HIGH = 4,
// 	   /// Same as AM_ASL but limit max pitch
// 	   AM_ASL_LOFT = 5
//    };

//    /**
//    * teGuidanceMode determines guidance type that is used flight segment.
//    */
//    enum teGuidanceMode
//    {
//        GM_COMMAND = 0,  ///< command guidance
//        GM_NAV = 1,  ///< inertial, GPS
//        GM_SENSOR1 = 2, ///< use seeker
//        GM_DEPLOY = 3 ///< deploy payload at start of this segment
//    };

//    /**
//    * Info that controls missile behavior for flight segment.
//    */
//    struct tsMissileFlightSegment
//    {
//       float mfRange_km;    ///< min range for this segment
//       float mfAltitude_m;  ///< altitude for segment
//       teAltitudeMode meAltitudeMode;   ///< altitude mode

//       teGuidanceMode meGuidanceMode;   ///< guidance mode
//    };

// #define MAX_MISSILE_FLIGHT_SEGMENTS 8


//    class tcMissileDBObject : public tcWeaponDBObject
//    {
//    public:
//       // flight model parameters
//       float mfDragArea_sm;                ///< area for parasitic drag 这是用于寄生阻力的面积。寄生阻力是与物体形状和大小有关的阻力，不包括由于空气动力产生的推力
//       float mfGmax;                       ///< max Gs 这是最大重力加速度，通常用于描述飞行器可以承受的最大过载
//       float mfMaxTurnRate_degps;          ///< max (slow speed) turn rate 这是最大（低速）的旋转速率，以度每秒（degrees per second）为单位
//       float mfCdpsub;                     ///< parasitic drag coeff, subsonic 这是亚音速的寄生阻力系数。
//       float mfCdptran;                    ///< transonic 这是跨音速的寄生阻力系数。当飞行器在接近音速时，其阻力特性会发生变化。
//       float mfCdpsup;                     ///< supersonic 这是超音速的寄生阻力系数。
//       float mfMcm;                        ///< critical mach number 临界马赫数，这是描述飞行器或物体在某一速度下从亚音速过渡到超音速的马赫数。
//       float mfMsupm;                      ///< supersonic mach number 超音速马赫数。描述飞行器或物体在超音速下的速度特性。
//       float mfBoostThrust_N;              ///< boost thrust [N] 助推推力，以牛顿（N）为单位。在某些情况下，如火箭或某些导弹，在发射阶段需要更大的推力来达到所需的速度。
//       float mfBoostTime_s;                ///< boost time [s] 助推时间，以秒为单位。描述助推阶段持续的时间长度。
//       float mfSustThrust_N;               ///< sustainer thrust [N] 维持推力，以牛顿为单位。在达到所需速度后，可能需要较小的推力来维持飞行或推进。
//       float mfSustTime_s;                 ///< sustainer time [s] 维持时间，以秒为单位。描述维持阶段持续的时间长度。
//       float mfShutdownSpeed_mps;          ///< self destructs below this speed after flameout 在失去动力（flameout）后，飞行器或物体将在低于此速度时自动销毁或采取其他行动。这可能是为了防止故障或失去控制的飞行器造成损害。

//       // other parameters
//       //float mfDamage;                   ///< damage value
//       //teDamageType meDamageType;        ///< damage type enumeration
//       //float mfRange_km;                   ///< [km] nominal range (replaced with maxRange_km in tcWeaponDBObject
    
//       // sensor info
//       std::string maSensorClass;           ///< seeker database class name
//       int sensorKey;                     ///< key for fast access of primary seeker
// 	  bool needsFireControl;              ///< true if seeker depends on a fire control sensor for guidance
//       bool acceptsWaypoints;              ///< true if missile can accept preplan (or datalink) waypoints

// 	  int fireAndForget;				  ///< -1 not initialized, 0 not FF, 1 FF
//       int isARM;                          ///< -1 not initialized, 0 not ARM, 1 ARM

//       float seekerFOV_rad;                ///< for fast lookup of seeker field of view
//       float aczConstant_kts;
//       float invMass_kg;                   ///< 1/mass_kg to avoid divide

//       /// flight profile, array of flight segment info
//       unsigned mnNumSegments;
//       // std::array<tsMissileFlightSegment,MAX_MISSILE_FLIGHT_SEGMENTS>  maFlightProfile;
//       std::vector<tsMissileFlightSegment> maFlightProfile;

//       virtual const char* GetClassName() const {return "Missile";} ///< returns class name of database object
//       teWeaponLaunchMode GetLaunchMode() const;
//       int GetSensorKey();
//       float GetSeekerFOV(); ///< @returns FOV in radians
// 	  bool HasAllEmitters(std::vector<int>& emitters);
// 	  bool IsFireAndForget();
//       bool IsCommandLaunched() const;
//       bool IsARM();
// 	  bool NeedsFireControl() const;
//       bool AcceptsWaypoints() const;
//       float EstimateSpeed_mps() const;
//       virtual void PrintToFile(tcFile& file);

// 	  static void AddSqlColumns(std::string& columnString);
// 	  void ReadSql(tcSqlReader& entry);
//       void WriteSql(std::string& valueString) const;
//       void WritePythonValue(std::string& valueString) const;
//       void WritePython(std::string& valueString) const;
//       void CalculateParams();

//       tcMissileDBObject();
//       tcMissileDBObject(const tcMissileDBObject& obj); ///< copy constructor
//       virtual ~tcMissileDBObject();
//       virtual  std::shared_ptr<tcGameObject>CreateGameObject() override;
//   private:
//       std::string teAltitudeModeToString(teAltitudeMode data) const;
//       std::string teGuidanceModeToString(teGuidanceMode data) const;
//   //     void SetAirDetectionDBObject(std::shared_ptr<tcAirDetectionDBObject> obj)
//   //     {
//   //         airDetectionDBObject=obj;
//   //     }

//   // private:

//   //     std::shared_ptr<tcAirDetectionDBObject> airDetectionDBObject;

//    };

// }

#endif

