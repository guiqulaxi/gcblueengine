/**
**  @file tcShipDBObject.h
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

#ifndef _SHIPDBOBJECT_H_
#define _SHIPDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabaseObject.h"
#include "tcPlatformDBObject.h"
#include "tcAirDetectionDBObject.h"
#include "tcWaterDetectionDBObject.h"



namespace database
{

	class tcFlightportDBObject;
	class tcSqlReader;

    /**
    * Models a surface ship platform. Specialization of old tcGenericDBObject
    */
    class tcShipDBObject :  public tcPlatformDBObject, public tcAirDetectionDBObject, public tcWaterDetectionDBObject
    {
    public:
        float draft_m; ///< max navigational draft 最大航行吃水深度
        float length_m; ///< vessel Length at Waterline 船体水线长度
        float beam_m; ///< vessel Beam  船体宽度（即船宽）
        float PowerPlantType; ///< vessel powerplant type 船舶动力装置类型（注意：这里使用float可能不太合适，通常应该是一个枚举或整型来表示类型）
        float TotalShaft_HP; ///< vessel propulsion power 船舶推进总马力
        float ExhaustStacks; ///< vessel exhaust stacks 船舶排气烟囱数量（注意：这里同样使用float可能不太合适，应为整型
        float PropulsionShafts; ///< vessel drive shafts 船舶驱动轴数量（同样，float可能不是最佳选择）
        float PropulsiveEfficiency; ///< vessel power efficiency  船舶推进效率
        float CivilianPaintScheme; ///< vessel has civilian paint job  船舶是否具有民用涂装（这里使用float可能不恰当，应为布尔型或整型表示有/无
        float FlashyPaintScheme; ///< vessel has flashy paintjob 船舶是否具有醒目的涂装（同样，float可能不是最佳选择）
        std::string flightportClass; ///< database class name of flightport (or empty if none) 飞行港（或如果没有则为空）的数据库类名

		tcDatabaseObject* AsDatabaseObject();
        virtual const char* GetClassName() const {return "Ship";} ///< returns class name of database object
		tcFlightportDBObject* GetFlightport();
		virtual float GetFuelConsumptionConstant(float speed_kts = 0) const;

        virtual void PrintToFile(tcFile& file);
        
		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;

        void WritePythonValue(std::string& valueString) const;
        void WritePython(std::string& valueString) const;
        tcShipDBObject();
        tcShipDBObject(const tcShipDBObject& obj); ///< copy constructor
        virtual ~tcShipDBObject();
        virtual tcGameObject * CreateGameObject() override;
         void CalculateParams();
	private:


    };

}

#endif

