/**  
**  @file tcDamageModel.h
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


#ifndef _TCDAMAGEMODEL_H_
#define _TCDAMAGEMODEL_H_

#ifdef WIN32
#pragma once
#endif


class tcGameObject;
class tcWeaponObject;
class tcBallisticWeapon;

namespace database
{
    class tcDatabase;
    class tcWeaponDamage;
}

    struct Damage
    {
        bool isPenetration; // 武器是否能穿透，如果不能穿透则忽略爆炸伤害
        // 此变量指示武器在撞击目标时是否具有穿透能力，若不具备，则不考虑其爆炸造成的伤害

        float kinetic_J; // 动能撞击伤害，单位焦耳（J）
        // 表示武器因撞击而传递给目标的动能伤害量

        float explosive_kg; // 武器穿透时内部爆炸造成的伤害，单位等效千克TNT
        // 当武器穿透目标时，其内部爆炸产生的伤害量，用等效的TNT千克数来表示

        float blast_psi; // 爆炸产生的超压，单位每平方英寸磅力（PSI）
        // 爆炸事件在目标周围产生的超压值，用于评估爆炸冲击波对目标的物理影响

        float waterBlast_psi; // 水下爆炸产生的超压，单位也是PSI
        // 当爆炸发生在水下时，产生的超压值，同样用PSI来衡量

        float thermal_J_cm2; // 热伤害，单位每平方厘米焦耳（J/cm²）
        // 爆炸产生的热量对目标造成的伤害量，用每平方厘米上的焦耳数来表示

        float fragHits; // 碎片命中次数
        // 爆炸产生的碎片命中目标的次数，这是一个量化指标

        float fragEnergy_J; // 碎片能量，单位焦耳（J）
        // 每个碎片撞击目标时携带的能量量，用焦耳来表示

        // 成员函数声明
        void Clear(); // 清除结构体中的所有数据，将成员变量重置为默认值（通常是将它们设置为0或false）
        // 这个函数用于重置Damage结构体，以便它可以被重新使用或准备存储新的伤害数据
    };

/**
* Singleton class for advanced damage modeling
*/
class tcDamageModel
{
public:
    /// 细节描述一种碎裂型武器
    struct FragWeapon
    {
        float charge_kg; ///< 等效的TNT千克数，表示爆炸威力
        float metal_kg; ///< 碎裂金属的总质量，单位千克
        float fragment_kg; ///< 单个碎片的质量，单位千克
        float spread_factor; ///< 散布因子，1表示全方位均匀散布，0.5表示半球形散布等
    };

    /// 描述碎片命中的详细信息
    struct FragHits
    {
        float hits; ///< 命中的次数（使用泊松分布得到的实际命中次数，而非平均值）
        float ke_J; ///< 碎片撞击时的动能，单位焦耳（J）
        float v_mps; ///< 碎片撞击时的速度，单位米每秒（mps）
    };

    void CalculateTotalDamage(tcWeaponObject* weapon, tcGameObject* target, Damage& damage);
	void CalculateTotalDamageCluster(tcBallisticWeapon* ballistic, tcGameObject* target, Damage& damage);

    float CalculateBlastOverpressure(float range_m, float w_kg) const;
    float CalculateWaterBlastOverpressure(float range_m, float w_kg) const;
    FragHits CalculateFragmentImpact(float range_m, float altitude_m, const FragWeapon& weap, float targetArea_m2) const;
    float CalculateRadiationIntensity(float range_m, float w_kg) const;

    const database::tcWeaponDamage* GetWeaponDamageModel(tcWeaponObject* weapon) const;


    static tcDamageModel* Get();
private:
    database::tcDatabase* database;

    tcDamageModel();
    virtual ~tcDamageModel();

};


#endif
