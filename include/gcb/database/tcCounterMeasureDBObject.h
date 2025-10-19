/**
**  @file tcCounterMeasureDBObject.h
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

#ifndef _COUNTERMEASUREDBOBJECT_H_
#define _COUNTERMEASUREDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcDatabaseObject.h"
#include "tcAirDetectionDBObject.h"
#include "tcWaterDetectionDBObject.h"


namespace database
{

	class tcSqlReader;

    /**
    * Database object to support simple countermeasure model for chaff and flares
    * doesn't model subsurface CM like noisemakers
    */
    class tcCounterMeasureDBObject : public tcDatabaseObject
	{
	public:
        std::string subType; ///< type of countermeasure, "Chaff", "Flare"
        float lifeSpan_s; ///< duration that CM is active
        float effectiveness; ///< generic factor for CM effectiveness
        float maxSpeed_mps; ///< drop speed for chaff and flare (terminal velocity in fall at sea level)
        
        float GetAirDragFactor() const;
		bool IsFlare() const;

		virtual const char* GetClassName() const {return "CounterMeasure";} ///< returns class name of database object
		virtual void PrintToFile(tcFile& file);
		
		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;
        void WritePythonValue(std::string& valueString) const;
        void WritePython(std::string &valueString) const;

		tcCounterMeasureDBObject();
		tcCounterMeasureDBObject(const tcCounterMeasureDBObject& obj);
		virtual ~tcCounterMeasureDBObject();
        virtual std::shared_ptr<tcGameObject>CreateGameObject() override;
         void CalculateParams();
        void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

        // virtual void SetAirDetectionDBObject(std::shared_ptr<tcAirDetectionDBObject> obj)
        // {
        //     airDetectionDBObject=obj;
        // }
        // virtual void setWaterDetectionDBObject(std::shared_ptr<tcWaterDetectionDBObject> obj )
        // {
        //     waterDetectionDBObject=obj;
        // }
        // virtual std::shared_ptr<tcAirDetectionDBObject> GetAirDetectionDBObject()const
        // {
        //     return airDetectionDBObject;
        // }
        // virtual std::shared_ptr<tcWaterDetectionDBObject> GetWaterDetectionDBObject( )const
        // {
        //     return waterDetectionDBObject;
        // }
    private:
        // calculated parameters
        float airDragFactor; ///< accel [m/s^2] = dragFactor * v_mps^2
		bool isFlare;

    // protected:

    //     std::shared_ptr<tcAirDetectionDBObject> airDetectionDBObject;
    //     std::shared_ptr<tcWaterDetectionDBObject> waterDetectionDBObject;

	};

} // namespace database

#endif

