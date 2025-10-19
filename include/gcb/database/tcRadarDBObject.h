/**
**  @file tcRadarDBObject.h
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

#ifndef _RADARDBOBJECT_H_
#define _RADARDBOBJECT_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "tcSensorDBObject.h"



namespace database
{
class tcSqlReader;

class tcRadarDBObject : public tcSensorDBObject
{
public:
    float ERPpeak_dBW;         ///< [dBW] effective radiated power, peak 有效辐射功率，峰值
    float ERPaverage_dBW;      ///< average ERP 平均ERP
    unsigned int maxFireControlTracks; ///< max number of simultaneous fire control tracks 同时进行的最大火控跟踪数
    bool isSemiactive;         ///< set true if this is a semiactive radar 如果这是半主动雷达则设为true
    float blindSpeed_mps;      ///< targets under this radial speed suffer large detection penalty, 0 for no blind speed 径向速度低于此值的目标会受到较大的探测惩罚，0表示无盲速
    float lookdownWater_dB;    ///< adjustment for look-down performance over water, negative is penalty 水面下视性能的调整，负值为惩罚
    float lookdownLand_dB;     ///< adjustment for look-down performance over land, negative is penalty 陆地下视性能的调整，负值为惩罚
    float bandwidth_Hz;        ///< instantaneous bandwidth used for jamming calculations 用于干扰计算的瞬时带宽
    float azimuthBeamwidth_deg;
    float elevationBeamwidth_deg;   ///< beamwidth in elevation used for lookdown calculations, gain calcs  波束宽度 用于下视计算和增益计算的仰角
    float effectiveSidelobes_dB;    ///< effective SLL considering adaptive cancellation, relative to peak, always negative 考虑自适应取消的有效旁瓣电平，相对于峰值，始终为负
    bool mbDetectsSurface;     ///< set true if detects surface targets
    bool mbDetectsAir;         ///< set true if detects airborne targets
    bool mbDetectsMissile;	   ///< set true if detects missiles
    bool mbDetectsGround;      ///< set true if detects ground targets

    /// calculated parameters
    float invBlindSpeed_mps;    ///< 1.0f / blindSpeed_mps;
    float antennaGain;          ///< calculated from az and el beamwidth 根据方位和仰角波束宽度计算得出
    float antennaGain_dBi;      ///< calculated from az and el beamwidth 根据方位和仰角波束宽度计算得出
    float invAzBeamwidth_deg;   ///< 1.0f / azimuthBeamwidth_deg
    float invElBeamwidth_deg;   ///< 1.0f / elevationBeamwidth_deg
    float cpi_s;                ///< CPI or dwell time calculated based on coverage angle and revisit period 据覆盖角度和回访周期计算出的CPI或驻留时间
    float jamConstant_dB;       ///< convert dB-W/m2 jam power density to J/N, assuming matched bandwidth and mainlobe

    virtual std::shared_ptr<tcSensorState> CreateSensor(std::shared_ptr<tcGameObject> parent); ///< factory method
    virtual const char* GetClassName() const {return "Radar";} ///< returns class name of database object
    virtual void PrintToFile(tcFile& file);

    static void AddSqlColumns(std::string& columnString);
    void ReadSql(tcSqlReader& entry);
    void WriteSql(std::string& valueString) const;
    void WritePythonValue(std::string& valueString) const;
    void WritePython(std::string &valueString) const;

    float EstimateDetectionRange(float rcs_dBsm, bool overWater, bool overLand) const;
    virtual const char* GetTypeDescription() const;
    float CalculateFL(float& lambda2);

    tcRadarDBObject();
    tcRadarDBObject(const tcRadarDBObject& obj); ///< copy constructor
    virtual ~tcRadarDBObject();
    void CalculateParams();
    void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

private:

};

} // namespace database

#endif

