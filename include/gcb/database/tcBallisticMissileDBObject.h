/**
**  @file tcBallisticMissileDBObject.h
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

#ifndef _BALLISTICMISSILEDBOBJ_H_
#define _BALLISTICMISSILEDBOBJ_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcWeaponDBObject.h"
#include "tcAirDetectionDBObject.h"
#include <vector>

namespace database
{
    class tcSqlReader;


    class tcBallisticMissileDBObject : public tcWeaponDBObject
    {
    public:
        float gmax; ///< 最大过载（Gs），表示导弹能承受的最大加速度与重力加速度的比值

        // 飞行模型参数
        float timeStage1_s; ///< 第一阶段飞行时间（单位：秒），导弹发射后的初始加速阶段
        float accelStage1_mps2; ///< 第一阶段加速度（单位：米/秒²），表示导弹在第一阶段受到的推力产生的加速度
        float bcStage1; ///< 第一阶段弹道系数，等于导弹质量M与阻力系数Cd和参考面积A的乘积的倒数（M/(CdA)），用于计算导弹在飞行中的阻力

        float timeStage2_s; ///< 第二阶段飞行时间（单位：秒）
        float accelStage2_mps2; ///< 第二阶段加速度（单位：米/秒²）
        float bcStage2; ///< 第二阶段弹道系数

        float timeStage3_s; ///< 第三阶段飞行时间（单位：秒）
        float accelStage3_mps2; ///< 第三阶段加速度（单位：米/秒²）
        float bcStage3; ///< 第三阶段弹道系数

        float timeStage4_s; ///< 第四阶段飞行时间（单位：秒），通常是导弹的末段飞行或制导阶段
        float accelStage4_mps2; ///< 第四阶段加速度（单位：米/秒²）
        float bcStage4; ///< 第四阶段弹道系数

        // 计算得到的参数
        float inv_bcStage1; ///< 第一阶段弹道系数的倒数，用于简化阻力计算
        float inv_bcStage2; ///< 第二阶段弹道系数的倒数
        float inv_bcStage3; ///< 第三阶段弹道系数的倒数
        float inv_bcStage4; ///< 第四阶段弹道系数的倒数
        float thrustShutoffTime_s; ///< 推力关闭时间（单位：秒），表示导弹最后一个带有推力的飞行阶段结束的时间点

        virtual teWeaponLaunchMode GetLaunchMode() const;

        static void AddSqlColumns(std::string& columnString);
        void ReadSql(tcSqlReader& entry);
        void WriteSql(std::string& valueString);
        void WritePythonValue(std::string& valueString) const;
        void WritePython(std::string &valueString) const;

        void CalculateParams();

        tcBallisticMissileDBObject();
        tcBallisticMissileDBObject(const tcBallisticMissileDBObject& obj); ///< copy constructor
        virtual ~tcBallisticMissileDBObject();
        virtual std::shared_ptr<tcGameObject>CreateGameObject() override;
        virtual void SetAirDetectionDBObject(std::shared_ptr<tcAirDetectionDBObject> obj)
        {
            airDetectionDBObject=obj;
        }
    protected:

        std::shared_ptr<tcAirDetectionDBObject> airDetectionDBObject;

    };

}

#endif

