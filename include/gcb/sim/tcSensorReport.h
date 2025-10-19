/**
**  @file tcSensorReport.h
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


#ifndef _SENSORREPORT_H_ 
#define _SENSORREPORT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "simmath.h"
#include "tcFile.h"
#include <vector>
#include "tcAllianceInfo.h"

class tcSimState;
class tcUpdateStream;
class tcGameStream;

namespace database
{
	class tcDatabase;
}
using database::tcDatabase;


/**
 * 存储传感器用于监视目标的所有状态信息。
 * 该类用于表示传感器对目标的检测报告，包括目标的位置、速度、高度、航向等信息。
 */
class tcSensorReport
{
public:
    // 枚举类型，表示报告中的哪些字段是有效的
    enum {
        LONLAT_VALID = 0x0001, ///< 经度和纬度有效
        ALT_VALID = 0x0002,    ///< 高度有效
        SPEED_VALID = 0x0004,  ///< 速度有效
        HEADING_VALID = 0x0008, ///< 航向有效
        CLIMB_VALID = 0x0010   ///< 爬升角有效
    };

    double timeStamp; ///< 报告的时间戳
    double startTime; ///< 传感器开始跟踪目标的时间
    int platformID;  ///< 传感器的平台ID（如飞机、舰船等）
    int sensorID;    ///< 传感器的数据库ID
    unsigned int validFlags; ///< 有效标志位，表示哪些字段是有效的（使用枚举值进行位运算）

    std::vector<int> emitterList; ///< 目标的发射器列表（如雷达、通信设备等）
    unsigned int classification; ///< 目标的分类（如空中目标、潜艇等），0 表示未知
    unsigned char alliance; ///< 目标的阵营编号，0 表示未知
    int databaseID; ///< 目标在数据库中的具体ID，-1 表示未知

    // 目标的位置估计（经度、纬度）及其协方差
    float lonEstimate_rad; ///< 经度估计值（弧度）
    float latEstimate_rad; ///< 纬度估计值（弧度）
    float C11; ///< 协方差矩阵的 C11 项（经度方差）
    float C22; ///< 协方差矩阵的 C22 项（纬度方差）
    float C12; ///< 协方差矩阵的 C12 项（经度和纬度的协方差）

    // 目标的高度估计及其方差（假设与经度/纬度无相关性）
    float altEstimate_m;  ///< 高度估计值（米）
    float altVariance;    ///< 高度方差

    // 目标的速度估计及其方差
    float speedEstimate_mps; ///< 速度估计值（米/秒）
    float speedVariance;     ///< 速度方差

    // 目标的航向估计及其方差
    float headingEstimate_rad; ///< 航向估计值（弧度）
    float headingVariance;     ///< 航向方差

    // 目标的爬升角估计及其方差
    float climbEstimate_rad; ///< 爬升角估计值（弧度）
    float climbVariance;     ///< 爬升角方差
    //是否本地有效，通信没有通信智能报告给本地
    bool isLocal;

    // 获取目标的跟踪寿命（从开始跟踪到当前时间的时间差）
    double GetTrackLife() const;

    // 检查目标是否已被识别
    bool IsIdentified() const;

    // 检查目标是否是新的（即是否刚刚被检测到）
    bool IsNew() const;

    // 计算目标位置的不确定区域（基于协方差矩阵）
    float UncertaintyArea() const;

    // 序列化和反序列化操作符重载
    tcGameStream& operator<<(tcGameStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);

    // 赋值操作符重载
    const tcSensorReport& operator=(const tcSensorReport& obj);

    // 构造函数
    tcSensorReport();

    // 拷贝构造函数
    tcSensorReport(const tcSensorReport& obj);

    // 析构函数
    virtual ~tcSensorReport();
};





#endif 

