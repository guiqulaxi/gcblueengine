/**
**  @file tcTorpedoDBObject.h
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

#ifndef _TORPEDODBOBJECT_H_
#define _TORPEDODBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcWeaponDBObject.h"
#include "tcWaterDetectionDBObject.h"

#include <vector>


namespace database
{
    class tcSqlReader;
    class tcSonarDBObject;


    /**
    *
    */
    class tcTorpedoDBObject : public tcWeaponDBObject
    {
    public:
        enum {
            TORPEDO = 1,///鱼雷
            DEPTH_CHARGE = 2,///深水炸弹
            BOTTOM_MINE = 3, ///沉底水雷
            BOTTOM_MINE_CAPTOR = 4 ///底部地雷捕获器
        };

        // model parameters
        float maxTurnRate_degps;          ///< max turn rate
        float maxDepth_m;                 ///< maximum depth

        float battery_kJ;                 ///< battery charge
        float batteryRate_kW;             ///< battery rate at max thrust

        float maxSpeed_kts;               
        float acceleration_ktsps;         ///< for simple model only

        //float mfRange_km;                 ///< [km] nominal range (replaced with maxRange_km in tcWeaponDBObject

        // sensor info
        std::string sonarClass; 

        bool wireGuidance;                ///< true if wire guidance available
        float preEnableSpeed_kts;         ///< default pre-enable speed
        int weaponType;                   ///< used to expand modeling to other underwater weapons



        /// calculated parameters
        float maxTurnRate_radps;           ///< CALCULATED
        float batteryRate_kWpkt;            ///< [kW / kt] CALCULATED

        virtual const char* GetClassName() const override {return "Torpedo";} ///< returns class name of database object
         std::shared_ptr<tcSonarDBObject> GetSeekerDBObj() const;

        virtual void PrintToFile(tcFile& file) override;

        static void AddSqlColumns(std::string& columnString);
        void ReadSql(tcSqlReader& entry) override;
        void WriteSql(std::string& valueString) const override;
        void WritePythonValue(std::string& valueString) const override;
        void WritePython(std::string& valueString) const override;

        tcTorpedoDBObject();
        tcTorpedoDBObject(const tcTorpedoDBObject& obj); ///< copy constructor
        virtual ~tcTorpedoDBObject();
        virtual std::shared_ptr<tcGameObject>CreateGameObject() override;
        void CalculateParams()override;
        void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;


    private:


    };

}

#endif

