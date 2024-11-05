/** 
**  @file tcBallisticMissile.h
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

#if _MSC_VER > 1000
#pragma once
#endif

#ifndef _TCBALLISTICMISSILE_H_
#define _TCBALLISTICMISSILE_H_

#include "tcAero.h"
#include "tcWeaponObject.h"
#include "tcBallisticMissileDBObject.h"

class tcUpdateStream;
class tcGameStream;

/**
 * A class that represents a missle.
 *
 * @see tcGameObject
 */
class tcBallisticMissile : public tcWeaponObject
{
public:
    void Clear();
	virtual void LaunchFrom(tcGameObject* obj, unsigned nLauncher);

    virtual void Update(double t);
//    virtual void UpdateEffects();
    virtual void UpdateGuidance(double t);

    const GeoPoint& GetTargetDatum() const;

    virtual tcUpdateStream& operator<<(tcUpdateStream& stream);
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream);

    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

    tcBallisticMissile(const tcBallisticMissile& obj);
    tcBallisticMissile(tcBallisticMissileDBObject* obj);
    ~tcBallisticMissile();

private:
    tcBallisticMissileDBObject* mpDBObject;

    bool subSurfaceLaunch; ///< true during subsurface launch phase for sub-launched missiles

    double lastGuidanceUpdateTime; ///< 上次制导更新时间（单位：秒）
    double guidanceUpdateInterval; ///< 制导更新间隔（单位：秒）

    float flightTime_s; ///< 飞行时间（单位：秒）

    float thrustShutoffTime_s; ///< allows for early shutoff of thrust for closer range target 推力关闭时间（单位：秒），允许针对近距离目标提前关闭推力

    GeoPoint targetDatum; ///< 目标位置数据（地理坐标）

    // ECEF parameters 地心坐标
    double x; ///< 在ECEF坐标系中的X坐标（单位：米）
    double y; ///< 在ECEF坐标系中的Y坐标（单位：米）
    double z; ///< 在ECEF坐标系中的Z坐标（单位：米）
    float vx; ///< 在ECEF坐标系中的X方向速度（单位：米/秒）
    float vy; ///< 在ECEF坐标系中的Y方向速度（单位：米/秒）
    float vz; ///< 在ECEF坐标系中的Z方向速度（单位：米/秒）

    double xt; ///< 目标位置在ECEF坐标系中的X坐标（单位：米）
    double yt; ///< 目标位置在ECEF坐标系中的Y坐标（单位：米）
    double zt; ///< 目标位置在ECEF坐标系中的Z坐标（单位：米）
    double rt; ///< 目标位置到ECEF原点的距离（单位：米）

    float gx; ///< ECEF目标速度的单位向量X分量，由制导系统更新
    float gy; ///< ECEF目标速度的单位向量Y分量，由制导系统更新
    float gz; ///< ECEF目标速度的单位向量Z分量，由制导系统更新

    float speed_mps;
    float speed2_mps2;//速度的平方
    double r_ecef; // distance from ECEF origin [m] 到ECEF原点的距离

    
    void CalculateECEF();
    void CalculateLLA();
    /**
     * @brief 经纬度上速度转东北天速度
     * @param lat_rad 所处的经纬度
     * @param lon_rad 所处的经纬度
     * @param ke 东向速度
     * @param kn 北向速度
     * @param ku 上速度
     * @param kx
     * @param ky
     * @param kz
     */
    void Enu2ecef(float lat_rad, float lon_rad, float ke, float kn, float ku, float& kx, float& ky, float& kz);
    /**
     * @brief 东北速度转经纬度上速度
     * @param lat_rad
     * @param lon_rad
     * @param kx
     * @param ky
     * @param kz
     * @param ke
     * @param kn
     * @param ku
     */
    void Ecef2enu(float lat_rad, float lon_rad, float kx, float ky, float kz, float& ke, float& kn, float& ku);

    void UpdateDetonation();
    void UpdateSubsurface(double t);
    void UpdateFlight(float dt_s);

    float GlimitedTurnRate() const;
    void CalculateSecondFocus(float xa, float ya, float xb, float yb, float ae, float& xf, float& yf);
};

#endif
