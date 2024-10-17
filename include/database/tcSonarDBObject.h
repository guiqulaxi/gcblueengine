/**
**  @file tcSonarDBObject.h
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

#ifndef _SONARDBOBJECT_H_
#define _SONARDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcSensorDBObject.h"


namespace database
{
    class tcSqlReader;

    /**
    *
    */
    class tcSonarDBObject : public tcSensorDBObject 
    {
    public:
        float SL;                   ///< [dB] source level (active only) [dB] 源级（仅主动模式有效）
        float DI;                   ///< [dB] receive directivity index (includes processing gain) [dB] 接收指向性指数（包括处理增益）
        float minFrequency_Hz;      ///< 最小频率（赫兹）
        float maxFrequency_Hz;      ///< 最大频率（赫兹）
        bool isPassive;             ///< 是否为被动模式
        bool isActive;              ///< both isActive and isPassive indicate selectable at launch
        bool isTowed;               ///< 是否为拖曳阵列
        float maxScope_m;           ///< towed array scope or dipping sonar "scope"  拖曳阵列范围或潜望声纳“范围”（米）
        bool isWakeHoming;          ///< wake homing vs. surface only 是否为尾流制导（相对于仅表面制导

        float alpha;                ///< CALCULATED attenuation coefficent in dB/km 计算得到的衰减系数
        float averageFreq_Hz;   ///< CALCULATED  计算得到的平均频率

        virtual tcSensorState* CreateSensor(tcGameObject* parent); ///< factory method
        virtual const char* GetClassName() const {return "Sonar";} ///< returns class name of database object
        virtual void PrintToFile(tcFile& file);

        const char* GetTypeDescription() const;

        static void AddSqlColumns(std::string& columnString);
        void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString);

        tcSonarDBObject();
        tcSonarDBObject(tcSonarDBObject& obj); ///< copy constructor
        virtual ~tcSonarDBObject();

    private:
        void CalculateParams();
    };

} // namespace database

#endif

