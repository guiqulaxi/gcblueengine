/**
**  @file tcDamageModel.cpp
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
////#include "wx/wx.h" 
#endif

#include "tcDamageModel.h"
#include "tcAero.h"
#include "math_constants.h"
#include "randfn.h"
#include "tcGameObject.h"
#include "tcWeaponObject.h"
#include "tcDatabase.h"
#include "tcPlatformObject.h"
#include "tcPlatformDBObject.h"
#include "tcWeaponDamage.h"
#include "tcBallisticWeapon.h"
#include "tcBallisticDBObject.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



void Damage::Clear()
{
    isPenetration = false;
    kinetic_J = 0;
    explosive_kg = 0;
    blast_psi = 0;
    waterBlast_psi = 0;
    thermal_J_cm2 = 0;
    fragHits = 0;
    fragEnergy_J = 0;
}

/**
* Singleton accessor
*/
tcDamageModel* tcDamageModel::Get()
{
    static tcDamageModel instance;

    return &instance;
}

/**
 * @return blast overpressure in PSI
 * 该函数返回爆炸产生的超压值，单位为每平方英寸磅力（PSI）
 * See http://www.fas.org/man/dod-101/navy/docs/es310/warheads/Warheads.htm ,
 *   参考网址：关于战争头部（核弹等）的ES310课程大纲，最后修订于1998年1月20日
 */
float tcDamageModel::CalculateBlastOverpressure(float range_m, float w_kg) const
{
    // 检查传入的爆炸物质量（w_kg）和距离（range_m）是否都大于0
    if ((w_kg > 0) && (range_m > 0))
    {
        // 计算缩放后的距离，这是根据爆炸物质量和距离的关系进行的一个转换
        // 使用公式 range_m * (1.1e-6 * w_kg)^(-0.333) 进行计算
        // 这里的powf函数用于计算浮点数的幂
        float scaled_range_m = range_m * powf((1.1e-6 * w_kg), -0.333f);

        // 使用缩放后的距离计算爆炸超压
        // 公式为 3.25e6 * (scaled_range_m)^(-2.3) + 4800.0f * ((scaled_range_m + 305.0f)^(-1.2))
        // 这个公式可能来源于经验公式或者实验数据，用于估算在不同距离和爆炸物质量下的爆炸超压
        return (3.25e6 * powf(scaled_range_m, -2.3f)) + (4800.0f * powf((scaled_range_m + 305.0f), -1.2f));
    }
    else
    {
        // 如果爆炸物质量或距离小于或等于0，则不计算爆炸超压，直接返回0
        return 0;
    }
}
/**
 * 计算碎片命中数据
 */
tcDamageModel::FragHits
tcDamageModel::CalculateFragmentImpact(float range_m, float altitude_m,
                                       const tcDamageModel::FragWeapon& weap, float targetArea_m2) const
{
    FragHits result; // 初始化FragHits结构体变量，用于存储计算结果
    result.hits = 0; // 初始化命中次数为0
    result.ke_J = 0; // 初始化碎片撞击时的动能为0
    result.v_mps = 0; // 初始化碎片撞击时的速度为0

    // TNT爆炸的热值，单位J/kg，来源于http://www.fas.org/man/dod-101/navy/docs/es310/warheads/Warheads.htm
    const float delta_E = 2.7e6;
    // 弹头形状因子
    const float K_shape = 0.5f;
    // 碎片密度，单位kg/m³，这里假设为钢材的密度
    const float frag_density_kg_m3 = 8000.0f;
    // 根据Gurney方程计算的速度因子，来源于http://en.wikipedia.org/wiki/Gurney_equations
    const float Cgurney = sqrtf(2.0*delta_E);

    // 获取给定海拔处的空气密度
    float rho = Aero::GetAirDensity(altitude_m);

    // 计算总的碎片数量
    float N_frag = weap.metal_kg / weap.fragment_kg;

    // 根据碎片质量和密度计算碎片的投影面积（假设为球形碎片的投影）
    float A_frag_m2 = powf((1.3293f * weap.fragment_kg / frag_density_kg_m3), 0.667f);

    // 计算炸药与金属的质量比
    float CtoM = weap.charge_kg / weap.metal_kg;

    // 根据Gurney方程和弹头形状因子计算碎片的初始速度
    float v0_mps = Cgurney * sqrtf((CtoM / (1.0f + K_shape*CtoM)));

    // 考虑空气阻力，计算碎片在给定距离处的速度
    float v_mps = v0_mps * expf(-rho*0.5f*A_frag_m2*range_m/(2.0f * weap.fragment_kg));
    // 计算碎片撞击时的动能
    float ke_J = 0.5f*weap.fragment_kg*v_mps*v_mps;

    // 计算平均命中次数，考虑目标面积、碎片数量、散布因子和距离
    float avg_hits = targetArea_m2*(N_frag / (weap.spread_factor*4*C_PI*range_m*range_m));
    // 注意：C_PI应该是π的常量值，这里假设它已经在其他地方被定义

    // 使用泊松分布计算实际命中次数，但不超过50次
    result.hits = (float)std::min(Poisson(avg_hits), (unsigned int)50);
    // 注意：Poisson函数应该是一个自定义函数，用于生成泊松分布的随机数，这里假设它已经在其他地方被定义

    // 设置计算结果
    result.ke_J = ke_J;
    result.v_mps = v_mps;

    return result; // 返回计算结果
}

/**
* Intended for nuclear thermal radiation damage, but maybe can be used for lasers and similar
* @return J/cm2 radiation intensity
*/
/**
 * 旨在计算核热辐射损伤，但也许可用于激光和类似能量源
 * @return 返回辐射强度，单位为J/cm²
 */
float tcDamageModel::CalculateRadiationIntensity(float range_m, float w_kg) const
{
    // 如果爆炸物质量小于或等于0，则辐射强度为0
    if (w_kg <= 0)
    {
        return 0;
    }
    else
    {
        // 能量释放系数，这里假设为270 J/kg，对于核爆炸来说这个值可能不准确，
        // 但对于此函数作为一般辐射强度计算的示例来说是可以接受的。
        // 注意：这个值远低于实际核爆炸中的能量释放系数。
        const float delta_E = 2.7e2;

        // 计算辐射强度，使用反平方律，C_FOURPI是4π的常量值，用于单位转换和球体表面积的计算。
        // range_m是距离爆炸中心的距离，w_kg是爆炸物的质量。
        // 该公式基于核爆炸产生的电磁脉冲（EMP）效应，但也可以类比用于其他类型的辐射源。
        // 注意：这里的计算假设了一个非常简化的模型，实际情况会更加复杂。
        float J_cm2 = w_kg*delta_E / (C_FOURPI*range_m*range_m);

        // 返回计算得到的辐射强度
        return J_cm2;
    }
}

/**
* This version calculates damage for weapon with many submunitions. Each submunition is randomly tested
* for impact or proximity damage to target
*/
/**
 * 此版本计算携带多个子弹药的武器的总损伤。每个子弹药都会随机测试是否对目标造成直接命中或近距离损伤。
 */
void tcDamageModel::CalculateTotalDamageCluster(tcBallisticWeapon* ballistic, tcGameObject* target, Damage& damage)
{
    // 设置最大命中次数为10次
    const unsigned int maxHits = 10;

    // 获取子弹药的损伤半径（米）
    float damageRadius_m = ballistic->mpDBObject->clusterEffectRadius_m;
    // 计算子弹药作用区域面积（平方米）
    float clusterArea_m2 = C_PI * damageRadius_m * damageRadius_m;

    // 获取目标的跨度（米）
    float targetSpan_m = target->GetSpan();
    // 计算目标近似面积（平方米），这里假设目标为圆形并取四分之一面积作为矩形目标的近似
    float targetArea_m2 = (C_PI * 0.25) * targetSpan_m * targetSpan_m;

    // 获取武器的损伤模型
    const database::tcWeaponDamage* weaponDamage = ballistic->GetDamageModel();
    // 确保损伤模型不为空，否则返回错误
    assert(weaponDamage != 0);
    if (weaponDamage == 0) return; // 错误

    // 获取武器的最大作用半径（米）
    float weaponRadius_m = weaponDamage->maxRange_m;
    // 计算武器作用区域面积（平方米）
    float weaponArea_m2 = C_PI * weaponRadius_m * weaponRadius_m;
    // 取目标和武器作用区域面积中的较小值作为计算基础
    targetArea_m2 = std::min(targetArea_m2, weaponArea_m2);

    // 计算子弹药在子弹药作用区域内造成近距离损伤的概率
    float pnear = weaponArea_m2 / clusterArea_m2;
    // 计算子弹药在子弹药作用区域内造成直接命中的概率
    float pdirect = targetArea_m2 / clusterArea_m2;
    // 获取子弹药数量
    unsigned int nCluster = ballistic->mpDBObject->clusterCount;
    // 记录实际命中次数
    unsigned int nHits = 0;
    // 记录直接命中次数
    unsigned int nDirect = 0;
    // 遍历所有子弹药，模拟命中情况
    for (unsigned int n=0; (n<nCluster) && (nHits<maxHits); n++)
    {
        float randval = randf(); // 生成一个随机数
        // 如果随机数小于近距离损伤概率，则记录一次命中
        nHits += (unsigned int)(randval < pnear);
        // 如果随机数小于直接命中概率，则记录一次直接命中
        nDirect += (unsigned int)(randval < pdirect);
    }

    // 暂时将所有损伤视为爆炸或破片/非直接损伤
    // 计算最小作用范围（米），取目标跨度的0.1倍和50米中的较小值，但不得小于10米
    float minRange_m = std::min(0.1f * target->GetSpan(), 50.0f);
    minRange_m = std::max(minRange_m, 10.0f);

    // 遍历所有命中，计算损伤
    for (unsigned int n=0; n<nHits; n++)
    {
        // 计算命中点到目标的距离（米），使用武器最大作用半径的一个随机比例
        float range_m = (1.0 - (randf() * randf())) * weaponRadius_m;
        // 确保距离不小于最小作用范围
        range_m = std::max(range_m, minRange_m);

        // 计算爆炸超压损伤（psi），并累加到总损伤中
        damage.blast_psi += CalculateBlastOverpressure(range_m, weaponDamage->blastCharge_kg);

        // 如果武器包含破片载荷，则计算破片损伤
        if (weaponDamage->fragCharge_kg > 0)
        {
            // 设置破片武器的参数
            FragWeapon fragWeap;
            fragWeap.charge_kg = weaponDamage->fragCharge_kg;
            fragWeap.metal_kg = weaponDamage->fragMetal_kg;
            fragWeap.fragment_kg = weaponDamage->fragFragment_kg;
            fragWeap.spread_factor = weaponDamage->fragSpread;

            // 计算目标半径（米），取目标跨度的一半
            float targetRadius_m = 0.5*target->GetSpan();
            // 计算目标面积（平方米），这里使用圆形面积的近似值的一半作为矩形目标的近似
            float targetArea_m2 = 0.5 * C_PI * targetRadius_m * targetRadius_m; // 近似值，0.5用于矩形形状
            // 计算破片的有效作用范围（米），取命中点到目标的距离和目标半径中的较大值
            float fragRange_m = std::max(range_m, targetRadius_m);

            // 计算破片对目标的命中情况
            tcDamageModel::FragHits fragHits =
                CalculateFragmentImpact(fragRange_m, target->mcKin.mfAlt_m, fragWeap, targetArea_m2);

            // 如果命中次数大于0，则更新破片命中次数和破片能量
            if (fragHits.hits > 0)
            {
                damage.fragHits += fragHits.hits;
                // 计算当前破片命中次数占总命中次数的比例
                float alpha = fragHits.hits / damage.fragHits;
                // 使用加权平均法更新破片能量
                damage.fragEnergy_J = (1-alpha)*damage.fragEnergy_J + alpha*fragHits.ke_J;
            }
        }
    }
}

/**
* @param damage damage description for this weapon detonation
* Point defense and air cannons should use a different model
*/
// 定义一个函数，用于计算给定武器对目标造成的总伤害。点防御和防空炮应使用不同的模型。
void tcDamageModel::CalculateTotalDamage(tcWeaponObject* weapon, tcGameObject* target, Damage& damage)
{
    // 检查武器和目标是否为空，如果为空则断言失败并返回。
    if ((weapon == 0) || (target == 0))
    {
        assert(false);
        return;
    }

    // 判断武器是否成功引爆。
    bool goodDetonation = weapon->IsGoodDetonation();

    // 清除之前的伤害数据。
    damage.Clear();

    // 获取武器的伤害模型。
    const tcWeaponDamage* weaponDamage = GetWeaponDamageModel(weapon);

    /* 命中目标
     * if missile is targeted and has scored direct hit, then apply
    ** kinetic damage from missile (big fragment) and apply
    ** internal damage assuming missile has delayed warhead that explodes
    ** after penetrating target exterior
    */
    // 如果武器直接命中目标，并且目标ID匹配。
    if (weapon->IsDirectHit() && (weapon->GetIntendedTarget() == target->mnID))
    {
        // 计算武器与目标之间的相对速度。
        float speed_collide = weapon->mcKin.CalculateRangeRate(target->mcKin);
        // 如果相对速度为负，则断言失败，并设为零（表示距离增加的情况，不应发生）。
        if (speed_collide < 0)
        {
            assert(false);
            speed_collide = 0; // opening range rate case, shouldnt happen
        }
        // 计算动能。
        float kinEnergy_J = 0.5*weapon->GetMassKg()*speed_collide*speed_collide;

        // 根据动能计算动能伤害。
        damage.kinetic_J = kinEnergy_J;

        // 设置是否能够穿透目标。
        damage.isPenetration = weaponDamage->isPenetration;

        // 假设爆炸和碎片的伤害是等效的，将它们加在一起并设置为伤害值的一部分。
        damage.explosive_kg = weaponDamage->blastCharge_kg + weaponDamage->fragCharge_kg + weaponDamage->fragMetal_kg;
        return;
    }

    // 如果武器是直接命中类型但未命中目标，或者武器未成功引爆，则不造成伤害。
    if (weapon->IsDirectHit() || (!goodDetonation)) return;

    // 尝试将武器动态转换为弹道武器。
    tcBallisticWeapon* ballistic = dynamic_cast<tcBallisticWeapon*>(weapon);
    // 如果转换成功且武器是子母弹。
    if ((ballistic != 0) && ballistic->IsClusterBomb())
    {
        // 计算子母弹对目标的总伤害。
        CalculateTotalDamageCluster(ballistic, target, damage);
        return;
    }

    // 判断是否为水下或地下爆炸。
    bool underwaterExplosion = ((weapon->mcKin.mfAlt_m <= -1.0f) && (weapon->mcTerrain.mfHeight_m < -1.0f));
    bool targetUnderwater = (target->mcKin.mfAlt_m <= 0) && (target->mcTerrain.mfHeight_m < -1.0f);
    bool targetAbovewater = (target->mcKin.mfAlt_m >= -3.0f); // 目标可以同时在水下和水面上

    // 判断爆炸是否会影响目标。
    bool affectsTarget = (underwaterExplosion && targetUnderwater) || (!underwaterExplosion && targetAbovewater);
    if (!affectsTarget) return;//通过水面水下来判断爆炸是否影响目标

    // 计算武器与目标之间的距离。
    float range_m = 1000.0f * weapon->mcKin.RangeToKmAlt(target->mcKin);

    // 如果是水下爆炸。
    if (underwaterExplosion)
    {
        float damageRange_m = range_m;
        Vector3d collisionPoint;
        float collisionRange_m;

        // 如果距离小于250米，则检查与目标之间的碰撞。
        if (damageRange_m < 250.0f) // dont check collisions for distance platforms affected by blast
        {
            // 沿着指向原点的射线检查碰撞。
            if (target->CalculateCollisionPointOrigin(weapon, collisionPoint, collisionRange_m))
            {
                // 确保碰撞距离小于伤害距离。
                // assert(collisionRange_m < damageRange_m);
                damageRange_m = std::min(damageRange_m, collisionRange_m);
            }

            // 沿着“向上”的射线检查碰撞。
            if (target->CalculateCollisionPointDir(weapon, Vector3d(0, 1, 0), collisionPoint, collisionRange_m))
            {
                damageRange_m = std::min(damageRange_m, collisionRange_m);
            }
        }

        // 确保伤害距离不小于10米。
        damageRange_m = std::max(damageRange_m, 10.0f);

        // 计算水下爆炸的超压。
        damage.waterBlast_psi = CalculateWaterBlastOverpressure(damageRange_m, weaponDamage->blastCharge_kg);
#ifdef _DEBUG
        // 在调试模式下输出信息。
        fprintf(stdout, "Underwater explosion, %s, range: %.1f m, blast: %.1f PSI\n", target->mzClass.c_str(), damageRange_m, damage.waterBlast_psi);
#endif
        return; // 水下没有热辐射或碎片伤害
    }

    // 计算最小伤害距离。
    float minRange_m = std::min(0.05f * target->GetSpan(), 50.0f);
    minRange_m = std::max(minRange_m, 5.0f);

    // 确保距离不小于最小伤害距离。
    range_m = std::max(range_m, minRange_m);

    // 计算爆炸的超压。
    damage.blast_psi = CalculateBlastOverpressure(range_m, weaponDamage->blastCharge_kg);

    // 计算热辐射强度。
    damage.thermal_J_cm2 = CalculateRadiationIntensity(range_m, weaponDamage->radCharge_kg);

    // 如果武器有碎片伤害。
    if (weaponDamage->fragCharge_kg > 0)
    {
        // 设置碎片武器的参数。
        FragWeapon fragWeap;
        fragWeap.charge_kg = weaponDamage->fragCharge_kg;
        fragWeap.metal_kg = weaponDamage->fragMetal_kg;
        fragWeap.fragment_kg = weaponDamage->fragFragment_kg;
        fragWeap.spread_factor = weaponDamage->fragSpread;

        // 计算目标的半径和面积。
        float targetRadius_m = 0.5*target->GetSpan();
        float targetArea_m2 = 0.5 * C_PI * targetRadius_m * targetRadius_m; // approx for now, 0.5 for rect shape
        float fragRange_m = std::max(range_m, targetRadius_m);

        // 计算碎片对目标的冲击。
        tcDamageModel::FragHits fragHits =
            CalculateFragmentImpact(fragRange_m, target->mcKin.mfAlt_m, fragWeap, targetArea_m2);

        // 设置碎片命中数和能量。
        damage.fragHits = fragHits.hits;
        damage.fragEnergy_J = fragHits.ke_J;
    }

    return;
}
/**
* @return blast overpressure in PSI for underwater explosion
* @param range_m range in meters
* @param w_kg high explosive mass
*/
float tcDamageModel::CalculateWaterBlastOverpressure(float range_m, float w_kg) const
{
    if ((w_kg > 0) && (range_m > 0))
    {
		// Approximate blast scaling function
		// C. David Sulfredge, Robert H. Morris, and Robert L. Sanders, "Calculating the Effect of Surface or 
		//  Underwater Explosions on Submerged Equipment and Structures," Oak Ridge National Laboratory, Building 5700, MS-6085, 2001
        return 7592.2f * powf(w_kg, 0.376f) * powf(range_m, -1.13f); // 
    }
    else
    {
        return 0;
    }
}



const database::tcWeaponDamage* tcDamageModel::GetWeaponDamageModel(tcWeaponObject* weapon) const
{
    assert(weapon != 0);

    const database::tcWeaponDamage* weaponDamageData = weapon->GetDamageModel();
        
    if (weaponDamageData != 0)
    {
        return weaponDamageData;
    }
    else
    {
        assert(false); // should not happen, default returned by database
        return 0;
    }
}



tcDamageModel::tcDamageModel()
: database(0)
{
    database = tcDatabase::Get();
}


tcDamageModel::~tcDamageModel()
{
}
