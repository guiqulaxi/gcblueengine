/**
**  @file tcWaterDetectionDBObject.h
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

#ifndef _WATERDETECTIONDBOBJECT_H_
#define _WATERDETECTIONDBOBJECT_H_

#include "tcAcousticModel.h"
#include "tcSignatureModel.h"
#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include <string>
#include <memory>
#include "tcComponentDBObject.h"
namespace database
{
	class tcSqlReader;
    class tcSignatureModel;
    class tcAcousticModel;

    /**
    * Describes detectability of object through water with sonar
    */
    class tcWaterDetectionDBObject: public tcComponentDBObject
    {
    public:
        float TS;                           ///< Target strength for active sonar detection // 主动声纳探测的目标强度
        std::string TS_Model;               ///< aspect variation model for acoustic backscatter 声学反向散射的方位变化模型
        std::string acousticModel;          ///< acoustic model for SL vs speed 声级（SL）与速度之间的声学模型
        std::string SL_Model;               ///< aspect variation model for radiated noise 辐射噪声的方位变化模型

        
		static void AddSqlColumns(std::string& columnString);
		void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString) const;
        void WritePythonValue(const std::string &mzClass, std::string& valueString) const;
        void WritePython(const std::string& mzClass,std::string& valueString) const;

        float GetSourceLevel(float speed_mps, float depth_m, float az_deg) const;
        float GetTargetStrength(float az_deg) const;
        
        float GetCavitationSpeedKts(float depth_m) const;
        float GetMinNonCavitatingDepth(float speed_kts) const;
        float GetCavitatingSourceLevel() const;
        float GetSnorkelingSourceLevel() const;

        float GetNoiseLevelForSpeed(float speed_mps) const;
        float GetNoiseLevelForSpeedKts(float speed_kts) const;

        tcWaterDetectionDBObject();
        tcWaterDetectionDBObject(const tcWaterDetectionDBObject& obj); ///< copy constructor
        virtual ~tcWaterDetectionDBObject();
        void BindSignatureModels();
    private:
        tcSignatureModel TS_pattern;
        tcSignatureModel SL_pattern;
        tcAcousticModel acousticNoise;


        
    };

}

#endif

