/**
**  @file tcAirDBObject.h
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

#ifndef _AIRDBOBJECT_H_
#define _AIRDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabaseObject.h"
#include "tcPlatformDBObject.h"
#include "tcAirDetectionDBObject.h"
#include "tcWaterDetectionDBObject.h"

namespace database
{
	class tcSqlReader;

    /**
    * Models a simple air platform (fixed wing or helo). Specialization of
	* old tcGenericDBObject.
    *
    * Added tcWaterDetectionDBObject parent to support dipping sonar
    */
    class tcAirDBObject :  public tcPlatformDBObject, public tcAirDetectionDBObject, public tcWaterDetectionDBObject
    {
    public:
        // float maxTakeoffWeight_kg;          ///< [kg] maximum weight at takeoff
        // float maxAltitude_m;                ///< [m] operating ceiling
        // float climbRate_mps;                ///< [m/s]
        // float gmax;                         ///< max Gs
        // float minimumRunway_m;              ///< minimum runway length required (with no arrestor)
        // bool isCarrierCompatible;           ///< 1 - can land on aircraft carriers, 0 - otherwise
        // int outFuelPods;                    ///< number of aircraft that this aircraft can refuel simultaneously
        // float fuelOut_kgps;                 ///< fuel output for each pod in kg/s
        // float fuelIn_kgps;                  ///< amount of fuel this a/c can receive in kg/s, use 0 for no A/A refueling
        // float maintenanceMin_s;             ///< minimum amount of random maintenance time required after landing
        // float maintenanceMax_s;             ///< maximum amount of random maintenance time required after landing
        float maxTakeoffWeight_kg;          ///< [kg] 最大起飞重量
            // 注释：此变量表示飞机能够安全起飞的最大重量，单位为千克。
        float maxAltitude_m;                ///< [m] 操作上限（飞行高度）
            // 注释：此变量表示飞机的最高操作高度（或称为飞行上限），单位为米。
        float climbRate_mps;                ///< [m/s] 爬升率
            // 注释：此变量表示飞机的爬升速度，即每秒上升的高度，单位为米每秒。
        float gmax;                         ///< 最大过载（G力）
            // 注释：此变量表示飞机在飞行中能够承受的最大过载，通常用G力表示。
        float minimumRunway_m;              ///< 所需最小跑道长度（无阻拦索）
            // 注释：此变量表示飞机在无需阻拦索的情况下起飞或着陆所需的最小跑道长度，单位为米。
        bool isCarrierCompatible;           ///< 1 - 可在航母上起降，0 - 否则
            // 注释：此布尔变量表示飞机是否能够在航空母舰上起降。1表示可以，0表示不可以。
        int outFuelPods;                    ///< 可同时加油的飞机数量
            // 注释：此变量表示该飞机能够同时为多少架其他飞机进行空中加油。
        float fuelOut_kgps;                 ///< 每个加油吊舱的燃油输出量（kg/s）
            // 注释：此变量表示该飞机每个加油吊舱每秒能够输出的燃油量，单位为千克每秒。
        float fuelIn_kgps;                  ///< 该飞机可接受空中加油的燃油量（kg/s），若不支持空中加油则为0
            // 注释：此变量表示该飞机每秒能够接受多少千克的空中加油燃油量。如果不支持空中加油，则设置为0。
        float maintenanceMin_s;             ///< 着陆后所需的最小随机维护时间（秒）
            // 注释：此变量表示飞机着陆后所需的最小随机维护时间，单位为秒。
        float maintenanceMax_s;             ///< 着陆后所需的最大随机维护时间（秒）
        // 注释：此变量表示飞机着陆后所需的最大随机维护时间，单位为秒。
		tcDatabaseObject* AsDatabaseObject();
        virtual const char* GetClassName() const {return "Air";} ///< returns class name of database object

		virtual float GetFuelConsumptionConstant(float speed_kts = 0) const;
		float GetRandomMaintenanceTime() const;

        bool IsCarrierCompatible() const;

        void ValidateLoadouts();

        virtual void PrintToFile(tcFile& file);

		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;

        tcAirDBObject();
        tcAirDBObject(const tcAirDBObject& obj); ///< copy constructor
        virtual ~tcAirDBObject();
	private:

		void CalculateParams();

    };

}

#endif

