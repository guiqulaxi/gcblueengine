/**
** @file tcWeaponObject.cpp
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
#include "tcWeaponObject.h"
#include "tcGameObject.h"
#include "tcMissileObject.h"
#include "tcTorpedoObject.h"
#include "tcBallisticWeapon.h"
#include "tcAirCM.h"
#include "tcWeaponDBObject.h"
#include "tcSensorMap.h"
#include "tcSimState.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "database/tcDamageEffect.h"
#include "tcDamageModel.h"
////#include "tcMessageInterface.h"
//#include "tc3DModel.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



/**
* Load state from update stream
*/
tcUpdateStream& tcWeaponObject::operator<<(tcUpdateStream& stream)
{
    tcGameObject::operator<<(stream);

    stream >> intendedTarget;

    return stream;
}

/**
* Save state to update stream
*/
tcUpdateStream& tcWeaponObject::operator>>(tcUpdateStream& stream)
{
    tcGameObject::operator>>(stream);

    stream << intendedTarget;

    return stream;
}


/**
* Load state from game stream
*/
tcGameStream& tcWeaponObject::operator<<(tcGameStream& stream)
{
    tcGameObject::operator<<(stream);

    stream >> intendedTarget;
    stream >> fuseHasTriggered;
    stream >> directHitTargetId;
	stream >> fuseDelay;
    stream >> payloadDeployed;
    stream >> malfunctionChecked;

    stream >> launchingPlatform;
    stream >> datalinkActive;

    int val;
    stream >> val;
    fuseMode = (FuseMode)val;

    return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcWeaponObject::operator>>(tcGameStream& stream)
{
    tcGameObject::operator>>(stream);

    stream << intendedTarget;
    stream << fuseHasTriggered;
    stream << directHitTargetId;
	stream << fuseDelay;
    stream << payloadDeployed;
    stream << malfunctionChecked;

    stream << launchingPlatform;
    stream << datalinkActive;

    int val = (int)fuseMode;
    stream << val;

    return stream;
}


/**
* @return damage fraction for new damage, 0 means no new damage
*/
float tcWeaponObject::ApplyAdvancedDamage(const Damage& damage, std::shared_ptr<tcGameObject> damager)
{
    // 初始化不同类型的伤害值为0
    float impactDamage = 0; // 冲击伤害
    float internalDamage = 0; // 内部伤害
    float blastDamage = 0; // 爆炸伤害
    float waterBlastDamage = 0; // 水下爆炸伤害
    float thermalDamage = 0; // 热辐射伤害
    float fragDamage = 0; // 破片伤害

    // 如果当前损伤等级已满（1表示完全损坏），则不再接受新伤害
    if (mfDamageLevel >= 1) return 0;

    // 保存当前损伤等级，用于后续计算
    float priorDamage = mfDamageLevel;

    // 从数据库中获取当前对象的伤害效果数据
    const database::tcDamageEffect* damageEffect =
        database->GetDamageEffectData(mpDBObject->damageEffect);

    // 如果没有找到伤害效果数据，则输出错误信息并断言失败
    if (damageEffect == 0)
    {
        fprintf(stderr, "tcWeaponObject::ApplyAdvancedDamage -- NULL damageEffect for %s\n",
                mzClass.c_str());
        assert(false);
        return 0;
    }

    // 根据动能计算冲击伤害
    impactDamage = damageEffect->GetFragmentDamageFactor(damage.kinetic_J);
    // 如果穿透成功且冲击伤害大于一定值，则计算内部伤害
    if (damage.isPenetration && (impactDamage > 0.02f))
    {
        internalDamage = damageEffect->GetInternalDamageFactor(damage.explosive_kg);
    }
    // 根据爆炸压力计算爆炸伤害
    blastDamage = damageEffect->GetBlastDamageFactor(damage.blast_psi);
    // 根据水下爆炸压力计算水下爆炸伤害
    waterBlastDamage = damageEffect->GetWaterBlastDamageFactor(damage.waterBlast_psi);
    // 根据热辐射能量计算热辐射伤害
    thermalDamage = damageEffect->GetRadiationDamageFactor(damage.thermal_J_cm2);
    // 根据破片数量和能量计算破片伤害
    fragDamage = sqrtf(damage.fragHits) * damageEffect->GetFragmentDamageFactor(damage.fragEnergy_J);

    // 计算总伤害值
    float cumulativeDamage = impactDamage + internalDamage + blastDamage + waterBlastDamage + thermalDamage + fragDamage;

    // 构建伤害描述字符串
    std::string damageDescription;
    if (impactDamage > 0) damageDescription.append("K"); // 冲击
    if (internalDamage > 0) damageDescription.append("X"); // 内部
    if (blastDamage > 0) damageDescription.append("B"); // 爆炸
    if (waterBlastDamage > 0) damageDescription.append("U"); // 水下爆炸
    if (thermalDamage > 0) damageDescription.append("T"); // 热辐射
    if (fragDamage > 0) damageDescription.append("F"); // 破片
    SetLastDamageDescription(damageDescription); // 设置最后的伤害描述

    // 如果总伤害值小于等于0，则没有伤害，直接返回
    if (cumulativeDamage <= 0) return 0;

    // 计算新的伤害值，使用随机数使伤害值在一定范围内波动
    // 这里使用了一个范围调整，使得伤害值在70%到130%的累计伤害值之间
    float newDamage = (0.7 + (randf() * 0.6)) * cumulativeDamage;

    // 更新当前对象的损伤等级
    mfDamageLevel += newDamage;

    // 确保损伤等级不超过1
    mfDamageLevel = std::min(mfDamageLevel, 1.0f);

    // 根据伤害更新分数
    UpdateScoreForDamage(damager, priorDamage);

    // 如果损伤等级达到或超过1，标记对象被摧毁
    if (mfDamageLevel >= 1.0f)
    {
        simState->mcSensorMap.MarkObjectDestroyed(tcGameObject::shared_from_this());
    }

    // 返回新造成的伤害值
    return newDamage;
}


/**
* Create payload and add to simState
*/
void tcWeaponObject::DeployPayload()
{
    std::shared_ptr<tcDatabaseObject> payloadData = database->GetObject(mpDBObject->payloadClass);
    if (payloadData == 0)
    {
        payloadDeployed = true;
        fprintf(stderr, "tcWeaponObject::DeployPayload - Invalid payload (%s)\n",
            mpDBObject->payloadClass.c_str());
        return;
    }


	for (unsigned int n=0; n<mpDBObject->payloadQuantity; n++)
	{
		std::shared_ptr<tcGameObject> payload = simState->CreateGameObject(payloadData);
		if (payload == 0)
		{
			fprintf(stderr, "tcWeaponObject::DeployPayload - Failed to create payload (%s)\n",
				mpDBObject->payloadClass.c_str());
			return;
		}

		LaunchPayload(payload);
	}

   
    payloadDeployed = true;
}



/**
* ??
* Called when weapon detonates
*/
void tcWeaponObject::Detonate(float delay_s)
{
    ///msg:武器爆炸
	fuseHasTriggered = true;
	fuseDelay = delay_s;
    //????
    TestForDud();
    //???
	if (goodDetonation)
	{
        if (std::shared_ptr<tcBallisticWeapon> ballistic =  std::dynamic_pointer_cast<tcBallisticWeapon>(tcGameObject::shared_from_this()))
        {
            if (ballistic->IsAutocannon()) return;
        }

		std::shared_ptr<tcGameObject> target = simState->GetObject(intendedTarget);
		if (target != 0)
		{
            Vector3d pos;
            Vector3d vel;
            target->GetRelativeStateWorld(tcGameObject::shared_from_this(), pos, vel);
            //target->GetModel()->AddExplosion(pos);
		}
	}
}

float tcWeaponObject::GetDamage() const
{
	return mpDBObject->mfDamage;
}

float tcWeaponObject::GetDamageEffectRadius() const
{
	if (const database::tcWeaponDamage* weaponDamage = GetDamageModel())
	{
		return weaponDamage->maxRange_m;
	}
	else
	{
		return 0;
	}
}

const database::tcWeaponDamage* tcWeaponObject::GetDamageModel() const
{
    const database::tcWeaponDamage* weaponDamageData = database->GetWeaponDamageData(mpDBObject->damageModel);

    return weaponDamageData;
}

std::shared_ptr<const tcWeaponDBObject> tcWeaponObject::GetDBObject() const
{
    return mpDBObject;
       
}

float tcWeaponObject::GetDetonationDelay() const
{
	return fuseDelay;
}

int tcWeaponObject::GetDirectHitTargetId() const
{
    return directHitTargetId;
}

const Vector3d& tcWeaponObject::GetImpactPoint() const
{
    return impactPoint;
}

int tcWeaponObject::GetIntendedTarget() const
{
	return intendedTarget;
}

float tcWeaponObject::GetMassKg() const
{
    return mpDBObject->weight_kg;
}

/**
 * 处理对象在极地附近经度超过±90度的情况（即纬度跨越极点）
 * 与tcPlatformObject::Move函数中的处理方式相同
 */
void tcWeaponObject::HandlePoleWrap()
{
    // 判断经度是否小于-π（即西半球超过-90度经线，但这里用浮点数表示布尔值可能不是最佳实践）
    float wrapLow = float(mcKin.mfLon_rad < -C_PI);

    // 判断经度是否大于等于π（即东半球超过90度经线）
    float wrapHigh = float(mcKin.mfLon_rad >= C_PI);

    // 根据经度是否跨越-π或π来调整经度，确保经度在[-π, π)范围内
    // 如果经度小于-π，则加上2π；如果经度大于等于π，则减去2π（但由于wrapLow和wrapHigh是互斥的，所以实际上只会执行其中一个操作）
    mcKin.mfLon_rad += (wrapLow - wrapHigh) * C_TWOPI;

    // 检查是否跨越了极点
    if (fabsf(mcKin.mfLat_rad) >= C_PIOVER2) // fabsf计算浮点数的绝对值，C_PIOVER2表示π/2
    {
        // 如果纬度大于等于π/2（即北半球极点附近）
        if (mcKin.mfLat_rad >= C_PIOVER2)
        {
            // 将纬度调整为南半球对称的位置（用π减去原纬度）
            mcKin.mfLat_rad = C_PI - mcKin.mfLat_rad;
        }
        else // 如果纬度小于-π/2（即南半球极点附近）
        {
            // 将纬度调整为北半球对称的位置（用-π减去原纬度）
            mcKin.mfLat_rad = -C_PI - mcKin.mfLat_rad;
        }

        // 调整航向，确保在跨越极点后航向正确（用π减去原航向）
        mcKin.mfHeading_rad = C_PI - mcKin.mfHeading_rad;
    }
}

/**
* Handles case where object has wrapped over +/- 90 latitude at pole
* Same as what tcPlatformObject::Move is doing
*/
void tcWeaponObject::HandlePoleWrap(tcKinematics& kin)
{
    float wrapLow = float(kin.mfLon_rad < -C_PI);
    float wrapHigh = float(kin.mfLon_rad >= C_PI);

    kin.mfLon_rad += (wrapLow - wrapHigh) * C_TWOPI;

    // check for pole crossing
    if (fabsf(kin.mfLat_rad) >= C_PIOVER2)
    {
        if (kin.mfLat_rad >= C_PIOVER2)
        {
            kin.mfLat_rad = C_PI - kin.mfLat_rad;
        }
        else
        {
            kin.mfLat_rad = -C_PI - kin.mfLat_rad;
        }
        kin.mfHeading_rad = C_PI - kin.mfHeading_rad;
    }
}

bool tcWeaponObject::HasPayload() const
{
	return (mpDBObject->payloadClass.size() > 0);
}


bool tcWeaponObject::IsDatalinkActive() const
{
    return datalinkActive;
}

/**
 * Serialize weapon-specific fields to JSON. Calls base class serialization
 * to include common fields.
 */
void tcWeaponObject::SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const
{
    tcGameObject::SerializeToJson(obj, allocator);

    obj.AddMember(rapidjson::Value("intendedTarget", allocator).Move(), (int)intendedTarget, allocator);
    obj.AddMember(rapidjson::Value("directHitTargetId", allocator).Move(), (int)directHitTargetId, allocator);
    obj.AddMember(rapidjson::Value("fuseDelay", allocator).Move(), fuseDelay, allocator);
    obj.AddMember(rapidjson::Value("fuseMode", allocator).Move(), (int)fuseMode, allocator);
    obj.AddMember(rapidjson::Value("datalinkActive", allocator).Move(), datalinkActive, allocator);
    obj.AddMember(rapidjson::Value("launchingPlatform", allocator).Move(), (int)launchingPlatform, allocator);
    obj.AddMember(rapidjson::Value("payloadDeployed", allocator).Move(), payloadDeployed, allocator);
    obj.AddMember(rapidjson::Value("massKg", allocator).Move(), GetMassKg(), allocator);

    // impact point
    rapidjson::Value impactObj(rapidjson::kObjectType);
    impactObj.AddMember("x", impactPoint.x(), allocator);
    impactObj.AddMember("y", impactPoint.y(), allocator);
    impactObj.AddMember("z", impactPoint.z(), allocator);
    obj.AddMember(rapidjson::Value("impactPoint", allocator).Move(), impactObj, allocator);
}

/**
* @return true if weapon has detonated
*/
bool tcWeaponObject::IsDetonated()
{
	return fuseHasTriggered;
}

bool tcWeaponObject::IsDirectHit() const
{
    return (directHitTargetId != -1);
}

bool tcWeaponObject::IsGoodDetonation() const
{
    return goodDetonation;
}

bool tcWeaponObject::IsGroundFused() const
{
    return (fuseMode == GROUND_FUSE);
}

bool tcWeaponObject::IsIntendedTarget(int id)
{
    if (id == -1) return false;
    return intendedTarget == id;
}

/**
* Initialize state of payload to be launched and call LaunchFrom method
* Possibly move this method higher and combine with tcSimState::AddLaunchedPlatform
* Watch out for side effects from adding to sim objects while they are being updated
*
* @see tcSimState::AddLaunchedPlatform
*/
void tcWeaponObject::LaunchPayload(std::shared_ptr<tcGameObject> payload)
{
    assert(payload != 0);

    payload->LaunchFrom(tcGameObject::shared_from_this(), 0);

 //   if (std::shared_ptr<tcTorpedoObject> torpedo = std::dynamic_pointer_cast<tcTorpedoObject>>(payload))
	//{
	//	torpedo->LaunchFrom(this, 0);
	//}
	//else if (std::shared_ptr<tcMissileObject> missile =  std::dynamic_pointer_cast<tcMissileObject>>(payload))
 //   {
 //       missile->LaunchFrom(this, 0);
 //   }
 //   else if (std::shared_ptr<tcBallisticWeapon> ballistic =  std::dynamic_pointer_cast<tcBallisticWeapon>>(payload))
 //   {
 //       ballistic->LaunchFrom(this, 0);
 //   }
 //   else if (std::shared_ptr<tcAirCM> airCM =  std::dynamic_pointer_cast<tcAirCM>>(payload))
 //   {
 //       airCM->LaunchFrom(this, 0);
 //   }
 //   else
	//{
	//	fprintf(stderr, "tcWeaponObject::LaunchPayload - Invalid payload type (%s)\n",
 //           payload->mpDBObject->GetClassName());
	//}
}

/**
 * 武器故障检查函数
 * 如果已经检查过故障，则直接返回。否则，检查是否存在故障，并在发现故障时执行自毁操作。
 */
void tcWeaponObject::MalfunctionCheck()
{
    // 如果已经检查过故障，则直接返回，避免重复检查
    if (malfunctionChecked) return;

    // 标记为已检查过故障，避免后续重复检查
    malfunctionChecked = true;

    // 使用随机数生成函数randf()生成一个随机数，并与无故障概率probNoFaults比较
    // 如果随机数大于无故障概率，则认为存在故障
    bool malfunction = (randf() > mpDBObject->probNoFaults);

    // 如果检测到故障
    if (malfunction)
    {
        // 执行自毁操作，销毁当前武器对象
        SelfDestruct(); // 自毁函数，具体实现可能包括释放资源、更新状态等

        // 以下代码仅在调试模式下编译和执行
#ifdef _DEBUG
        // 向标准输出打印故障信息，包括武器类别、单位标识和无故障概率
        fprintf(stdout, "%s %s malfunctioned (pr_nf:%.2f)\n", mzClass.c_str(), mzUnit.c_str(), mpDBObject->probNoFaults);

        // 构造故障信息字符串，并通过消息接口输出到控制台
        std::string msg = strutil::format("WPN MALFUNCTION (%s)", mzClass.c_str());
        tcMessageInterface::Get()->ConsoleMessage(msg);
#endif
    }

}


void tcWeaponObject::SetDetonationDelay(float delay_s)
{
	fuseDelay = delay_s;
}


void tcWeaponObject::SetDirectHitTargetId(int id)
{
    directHitTargetId = id;
}

/**
* @param pos world coordinates (east, up, north) of collision point relative to target origin
*/
void tcWeaponObject::SetImpactPoint(const Vector3d& pos)
{
    impactPoint = pos;
}

void tcWeaponObject::SetFuseMode(FuseMode mode)
{
    fuseMode = mode;
}

void tcWeaponObject::SetIntendedTarget(int targetId)
{
    if (intendedTarget == targetId) return;

    intendedTarget = targetId;
    if (targetId == -1) return;
    std::shared_ptr<tcSensorMapTrack>smtrack = 
        simState->mcSensorMap.GetSensorMapTrack(targetId, GetAlliance());
    if (smtrack != 0)
    {
		smtrack->AddEngagement(tcGameObject::mnID);
    }
	else
	{
        // check if this is a friendly
        if (std::shared_ptr<tcGameObject> target = simState->GetObject(targetId))
        { 
            if (target->GetAlliance() != GetAlliance())
            {
                fprintf(stderr, "tcWeaponObject::SetIntendedTarget - targetId %d not found in sensor map and is not a friendly" 
                    "(%s %s)\n", targetId, mzClass.c_str(), mzUnit.c_str());
            }
        }
        else
        {
            fprintf(stderr, "tcWeaponObject::SetIntendedTarget - targetId %d not found in sensor map or simState" 
                "(%s %s)\n", targetId, mzClass.c_str(), mzUnit.c_str());
        }
	}
}

/**
* ????
* Should be called exactly once after detonation
* Do random test for dud based on probDetonate in weapon damage model
* If no damage model then set not dud
*/
void tcWeaponObject::TestForDud()
{
    assert(IsDetonated());

    if (const database::tcWeaponDamage* damageModel = GetDamageModel())
    {
        goodDetonation = (randf() <= damageModel->probDetonate);
    }
    else
    {
        goodDetonation = true;
    }
}



void tcWeaponObject::UpdateDatalinkStatus()
{
    if ((launchingPlatform == -1) || (!mpDBObject->acceptsUserCommands))
    {
        datalinkActive = false;
        return;
    }

    if (std::shared_ptr<tcGameObject> source = simState->GetObject(launchingPlatform))
    {
        assert(source != 0);
        float range_km = mcKin.RangeToKmAlt(source->mcKin);
        // float range_km = mcKin.RangeToKmAlt(source);

        float radioHorizon_km = C_RADARHOR * (sqrtf(mcKin.mfAlt_m) + sqrtf(std::max(source->mcKin.mfAlt_m, source->GetZmax()-3.0f)));

        datalinkActive = (range_km <= mpDBObject->datalinkRange_km) && (range_km <= radioHorizon_km);
    }
    else
    {
        launchingPlatform = -1;
        datalinkActive = false;
    }

}


bool tcWeaponObject::WasLaunchedBy(int id) const
{
	return (launchingPlatform == id);
}


/**
 *
 */
tcWeaponObject::tcWeaponObject() 
: fuseHasTriggered(false), fuseDelay(0), intendedTarget(-1),
  mpDBObject(0),
  fuseMode(GROUND_FUSE),
  directHitTargetId(-1),
  impactPoint(0, 0, 0),
  goodDetonation(false),
  payloadDeployed(false),
  malfunctionChecked(false)
{

}

/**
 * Copy constructor.
 */
tcWeaponObject::tcWeaponObject(const tcWeaponObject& o) 
{
    assert(false); // not supported
}

/**
* Constructor that initializes using info from database entry.
*/
tcWeaponObject::tcWeaponObject(std::shared_ptr<tcWeaponDBObject> obj)
: tcGameObject(obj), 
  fuseHasTriggered(false), fuseDelay(0), intendedTarget(-1),
  mpDBObject(obj),
  fuseMode(GROUND_FUSE),
  directHitTargetId(-1),
  impactPoint(0, 0, 0),
  goodDetonation(false),
  payloadDeployed(false),
  malfunctionChecked(false),
  launchingPlatform(-1),
  datalinkActive(false)
{
    assert(simState);
}

/**
 *
 */
tcWeaponObject::~tcWeaponObject() 
{
}

