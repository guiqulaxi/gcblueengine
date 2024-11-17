/**
**  @file tcPlatformDBObject.h
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

#ifndef _PLATFORMDBOBJECT_H_
#define _PLATFORMDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabaseObject.h"
#include "tcSensorPlatformDBObject.h"
#include <vector>
////#include "tv_types.h"
#include "tc3DPoint.h"
#include "tcLoadoutData.h"
#include <Dense>
//#include <tc3DModel.h>
using Eigen::Vector2d;
struct animationDBInfo;
class tcGameObject;

namespace database
{
	class tcSqlReader;

    /**
    * Models a generic platform that has weapon launchers and
    * sensors and basic movement restrictions. This can be used
    * for a simple surface ship or aircraft model.
    */
    class tcPlatformDBObject : public tcDatabaseObject, public tcSensorPlatformDBObject
    {
    public:
        enum 
        { 
            MAXLAUNCHERS = 24,
            MAXANIMATIONS = 4,
            MAXMAGAZINES = 5
        };
        float mfMaxSpeed_kts;               ///< max speed, [kts] 最大速度，单位：[节]
        float mfAccel_ktsps;                ///< [kts/s] acceleration, simple model 加速度，单位：[节/秒]，简化模型
        float mfTurnRate_degps;             ///< [deg/s] 转弯率，单位：[度/秒]
        float mfFuelCapacity_kg;            ///< [kg], 0 is infinite fuel 燃料容量，单位：[千克]，0 表示无限燃料
        float mfFuelRate_kgps;              ///< [kg/s] at max thrust, simple model for now 最大推力下的燃料消耗率，单位：[千克/秒]，目前为简化模型
        float mfToughness;                  ///< 0 - 100 for now, survivability 坚固度，目前范围：0 - 100，表示生存能力
        std::string damageEffect;           ///< advanced damage model "toughness" 高级损伤模型中的“坚固度”效果描述

        int mnNumLaunchers; //发射器数量
        int mnNumMagazines;//弹仓数量
        std::vector<std::string> maLauncherClass;  //发射器类别
        std::vector<std::string> maMagazineClass;//弹仓类别
        std::vector<unsigned int> magazineId; // id for each magazine 每个弹仓的ID
        std::vector<unsigned int> launcherId; // id for each launcher 每个发射器的ID
        
        std::vector<std::string> launcherDescription; ///发射器描述
        std::vector<std::string> launcherName; ///< display names of launchers, e.g. "Tube 1" 发射器显示名称
        std::vector<float> launcherFOV_deg;/// 发射器视野角度，单位：[度]
        std::vector<float> launcherAz_deg; ///发射器方位角，单位：[度]
        std::vector<float> launcherEl_deg; //发射器仰角，单位：[度]
        std::vector<std::string> launcherFireControl; ///< fire control sensors for launchers (empty for none) 发射器的火控传感器（无则为空）
        std::vector<std::string> launcherFireControl2; ///< fire control sensors for launchers, second option (empty for none) 发射器的第二个火控传感器选项（无则为空）
        std::vector<bool> launcherIsReloadable; ///< true if launcher is reloadable 如果发射器可重新装填则为true

//        std::vector<animationDBInfo> animationInfo;

		tcDatabaseObject* AsDatabaseObject();
        virtual const char* GetClassName() const {return "Generic";} ///< returns class name of database object

		virtual float GetFuelConsumptionConstant(float speed_kts = 0) const;
        Vector2d GetLauncherAttitude(unsigned n) const;
        float GetLauncherFOV_deg(unsigned n) const;
		tc3DPoint GetLauncherPosition(unsigned n);
        size_t GetItemCapacityForLauncher(size_t launcherIdx, const std::string& item);
        int GetLauncherIndex(unsigned int id) const;
        tcLoadoutData* GetLoadout(const std::string& setupName);
        const std::vector<tcLoadoutData>& GetLoadoutList(float searchYear);

		float GetInternalFuelCapacity() const;
		bool HasInfiniteFuel() const;

        void ReorderMagazines();

        virtual void PrintToFile(tcFile& file);
        
		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;
        void WritePythonValue(std::string& valueString) const;
        void WritePython(std::string& valueString) const;

        tcPlatformDBObject();
        tcPlatformDBObject(const tcPlatformDBObject& obj); ///< copy constructor
        virtual ~tcPlatformDBObject();
        void CalculateParams();
	protected:
		float fuelConsumptionConstant; ///< = (fuel rate / max speed)
		float invMaxSpeed; ///< 1/max_speed



    };

}

#endif

