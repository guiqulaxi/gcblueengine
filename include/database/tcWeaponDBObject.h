/**
**  @file tcWeaponDBObject.h
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

#ifndef _WEAPONDBOBJECT_H_
#define _WEAPONDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabaseObject.h"



namespace database
{

#define SURFACE_TARGET 0x0001
#define AIR_TARGET 0x0002
#define LAND_TARGET 0x0004
#define MISSILE_TARGET 0x0008
#define SUBSURFACE_TARGET 0x0010
#define AEW_TARGET 0x1000 ///< virtual "target" for AEW mission type

	class tcSqlReader;

	class tcWeaponDBObject : public tcDatabaseObject 
	{
	public:
		float mfDamage;
        std::string damageModel;    ///< advanced damage model for dealing damage  武器造成的伤害值
        std::string damageEffect;   ///< advanced damage model for receiving damage 高级伤害模型，用于造成伤害
        float launchSpeed_mps;      ///< initial speed at launch, use zero to use plat speed 发射时的初始速度，若为零则使用平台速度 [米/秒]
        int targetFlags;            ///< 0x01 surf, 0x02 air, 0x04 land, 0x08 missile, 0x10 sub 目标标志：0x01 水面，0x02 空中，0x04 陆地，0x08 导弹，0x10 潜艇
        float minLaunchAlt_m;       ///< minimum altitude (negative is depth) at which missile can be launched [m] 导弹可发射的最小高度（负值表示深度） [米]
        float maxLaunchAlt_m;       ///< maximum altitude at which missile can be launched [m] 导弹可发射的最大高度 [米]
        float minRange_km;          ///< minimum standoff range from target 对目标的最小保持距离 [公里]
        float maxRange_km;          ///< maximum standoff range (what AI and range circle will use) 对目标的最大保持距离（AI和射程圈将使用的范围） [公里]
        float probNoFaults;         ///< probability that weapon will operate successfully to reach target area 武器成功到达目标区域的概率
        std::string payloadClass;   ///< payload to deploy (weapon shuts down after payload deployed) 要部署的有效载荷（部署有效载荷后武器关闭）
        unsigned int payloadQuantity; ////< number of payload types to deploy 要部署的有效载荷类型数量
        float datalinkRange_km;     ///< range for datalink to weapon from launching platform 从发射平台到武器的数据链范围 [公里]
        bool acceptsUserCommands;   ///< true if user midcourse guidance accepted through datalink 如果接受用户中途制导指令（通过数据链），则为真
        float detonationRange_m;    ///< detonate when this close to target, 0 means on impact 当接近目标这个距离时引爆，0表示撞击时引爆 [米]

		virtual const char* GetClassName() const {return "Weapon";} ///< returns class name of database object
		virtual void PrintToFile(tcFile& file);

		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
		void WriteSql(std::string& valueString);

        bool IsNuclear() const;

	protected:
		tcWeaponDBObject();
		tcWeaponDBObject(const tcWeaponDBObject& obj); ///< copy constructor
		virtual ~tcWeaponDBObject();
	};

} // namespace database

#endif

