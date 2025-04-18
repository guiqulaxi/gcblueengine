/**
**  @file simmath.h
**
**  This file (and simmath.cpp) needs to be broken up into separate
**  file for better modularity.
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


#ifndef _SIMMATH_H_
#define _SIMMATH_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include <math.h>
#include "math_constants.h"
#include "randfn.h"
#include <string>
#include "tcFile.h"
#include "tcRect.h"
#include "tcString.h"
#include "gctypes.h"
// #include "tcDatabaseObject.h"
#include "tcTrack.h"
#include <Dense>
using Eigen::Vector3d;
#ifndef UINT8
typedef unsigned char UINT8;
#endif
#define C_EPSILON 0.000001

class tcStream;
class tcGameStream;
class tcUpdateStream;
// class tcGameObject;

class tcPoint 
{
public:
    float x;
    float y;
    float DistanceTo(const tcPoint& p) const {return (sqrtf((p.x-x)*(p.x-x)+(p.y-y)*(p.y-y)));}
    void Offset(float distance, float angle_rad);

    const tcPoint& operator+=(const tcPoint& rhs) {x+= rhs.x; y+= rhs.y; return *this;}
	const tcPoint& operator-=(const tcPoint& rhs) {x-= rhs.x; y-= rhs.y; return *this;}
    tcPoint operator+(const tcPoint& rhs) {return tcPoint(x+rhs.x, y+rhs.y);}
	tcPoint operator-(const tcPoint& rhs) {return tcPoint(x-rhs.x, y-rhs.y);}
    tcPoint() : x(0), y(0) {}
    tcPoint(float ax, float ay) : x(ax), y(ay) {}
    tcPoint(const tcPoint &p) : x(p.x), y(p.y) {}
};



/** tcRect with [-pi,pi) and [-pi/2,pi/2) range for longitude and latitude */
class tcGeoRect : public tcRect 
{
public:
    void ApplyBounds(tcGeoRect& r);
    bool IsOutOfBounds(tcGeoRect& r) const;
    void Offset(float dx, float dy);
    virtual bool ContainsPoint(float x, float y) const;
    void Set(float x1, float x2, float y1, float y2);
    void SetDegrees(float lon1_deg, float lon2_deg, float lat1_deg, float lat2_deg);
    float Width();
    float XCenter();

    bool operator==(const tcGeoRect& r);
    bool operator!=(const tcGeoRect& r);
};



class tcTerrainInfo 
{
public:
    float mfHeight_m;  ///< negative is water
	float lookAheadHeight_m; ///< height of terrain a short distance ahead of platform (e.g. for avoiding crashing into mountains)

    float mfLonDatum;  ///< location where terrain info recorded (used to see 
    float mfLatDatum;  ///< if object has moved enough to require update)

    void Clear();
    void Serialize(tcFile& file, bool abLoad);

    tcGameStream& operator>>(tcGameStream& stream);
    tcGameStream& operator<<(tcGameStream& stream);
};

class GeoPoint
{
public:
    double mfLon_rad;
    double mfLat_rad;
    float mfAlt_m;

    const GeoPoint& Offset(float distance_km, float bearing_rad);
    void Set(float x,float y) {mfLon_rad=x;mfLat_rad=y;}
    void Set(float x,float y,float z) {mfLon_rad=x;mfLat_rad=y;mfAlt_m=z;}
	bool IsZero() const {return ((mfLon_rad == 0) && (mfLat_rad == 0));}
    tcStream& operator<<(tcStream& buffer);
    tcStream& operator>>(tcStream& buffer);

    GeoPoint();
    GeoPoint(double lon_rad, double lat_rad, float alt_m);
    virtual ~GeoPoint();
};

/**
* Class to hold kinematic state information
*
* heading and climb angle define motion vector, 
* yaw, pitch, roll define orientation
*/
class tcKinematics 
{
public:
    double mfLon_rad;              ///< longitude [rad]
    double mfLat_rad;              ///< latitude [rad]
    float mfAlt_m;                 ///< altitude, negative is subsurface depth [m]
    float mfHeading_rad;           ///< relative to north [rad] 顺时针
    float mfClimbAngle_rad;        ///< climb angle defines vertical motion vector [rad]
    float mfYaw_rad;               ///< orientation in azimuthal plane
    float mfPitch_rad;             ///< orientation in elevation plane
    float mfRoll_rad;			   ///< orienation about roll axis
    float mfSpeed_kts;             ///< [kts]
    void LLToXYm(double& x, double& y) const;//返回经纬度的XY坐标 以本初子午线与赤道交点为原点 单位米
    float CalculateCollisionPoint(const tcKinematics& collider, float& dxi, float& dyi, float& dzi);
	float CalculateGroundImpactPoint(float terrainHeight_m, double& lon_rad, double& lat_rad);

    void Clear() {mfLon_rad=0;mfLat_rad=0;mfAlt_m=0;
    mfHeading_rad=0;mfClimbAngle_rad=0;mfSpeed_kts=0;
    mfYaw_rad=0;mfPitch_rad=0;mfRoll_rad=0;}

	void PredictPosition(float dt_s, double& lon_rad, double& lat_rad, float& alt_m) const;
    void Extrapolate(float dt_s);
    float BearingRateTo(float range_km, float bearing_rad, float speed_kts, float heading_rad);
    float HeadingToTrack(const tcTrack& track);
    float HeadingToGeoRad(const GeoPoint *apGeoPoint) const;
	float HeadingToGeoRad(float lon_rad, float lat_rad) const;
    float HeadingToRad(const tcKinematics& k) const;
    float RangeToKm(const GeoPoint *apGeoPoint) const;
    float RangeToKm(const tcKinematics& k) const;
    float RangeToKm(const tcTrack& track) const;
	float RangeToKm(float lon_rad, float lat_rad) const;
    float RangeToM(float lon_rad, float lat_rad) const;
    float RangeToKmAlt(const tcKinematics& k) const;
    float RangeToKmAlt(const tcTrack& track) const;
    float RangeToKmAlt(float lon_rad, float lat_rad, float alt_m) const;
    // float RangeToKmAlt(std::shared_ptr<const tcGameObject> obj) const;

    //float InterceptHeadingToTrack(tcTrack& track, float& afTimeToIntercept);
    void GetInterceptData2D(const tcTrack& track, float& rfHeading_rad, 
        float& rfTimeToIntercept);
    void GetInterceptData3D(const tcTrack& track, float& rfHeading_rad,
        float& rfClimbAngle_rad, float& rfTimeToIntercept, float& rfRange_km);
    float CalculateRangeRate(const tcKinematics& k) const;
    void Serialize(tcFile& file, bool abLoad);
    void SetRelativeGeo(GeoPoint& rpGeoPoint, float afBearing_rad, float afRange_km);

    tcUpdateStream& operator<<(tcUpdateStream& stream);
    tcUpdateStream& operator>>(tcUpdateStream& stream);

    tcGameStream& operator<<(tcGameStream& stream);
    tcGameStream& operator>>(tcGameStream& stream);
};


void ConformLonLatRad(float& lon_rad, float& lat_rad);
void ConformLonLatRad(double& lon_rad, double& lat_rad);

void ConformLonLatDeg(float& lon_deg, float& lat_deg);
void ConformLonLatDeg(double& lon_deg, double& lat_deg);

void LonLatToString(float afLon_deg, float afLat_deg, tcString& s);
void LonLatToStringB(float afLon_deg, float afLat_deg, std::string& s);
int AngleWithinRange(float afAngle_rad, float afAngle1_rad, float afAngle2_rad);

float BearingTo(GeoPoint g1, GeoPoint g2);
float RangeToKm(GeoPoint g1, GeoPoint g2);

int GeoWithinRegion(GeoPoint p, const tcRect *pRegion);

float Add_dB(float x_dB, float y_dB);

bool TriangulateBearings(const tcPoint& p1, float bearing1_rad, const tcPoint& p2, float bearing2_rad,
        tcPoint& result);

inline float& degtoplusminus180(float& afDeg) {
    if (afDeg > 180.0f) {
        afDeg -= 360.0f;
    }
    else if (afDeg < -180.0f) {
        afDeg += 360.0f;
    }
    return afDeg;
}

inline float& radtoplusminuspi(float& afRad) {
    if (afRad >= C_PI) {
        afRad -= C_TWOPI;
    }
    else if (afRad < -C_PI) {
        afRad += C_TWOPI;
    }
    return afRad;
}

/**
 * @brief 计算线与面相交的点
 * @param point 线上的点
 * @param plane_a plane_b plane_c 面上的点
 * @return c_point 交点
 * @return false 线与面平行或同处于一个平面不考虑
**/
bool LineIntersectPlane (const Vector3d& point,const Vector3d& direction,
                         const Vector3d& plane_a,
                         const Vector3d& plane_b,
                         const Vector3d& plane_c,
                         Vector3d& c_point);


/**
 * @brief 计算线与面相交的点
 * @param point 线上的点
 * @param plane_a plane_b plane_c 面上的点
 * @return c_point 交点
 * @return false 线与面平行或同处于一个平面不考虑
**/
bool RayIntersectPlane (const Vector3d& point,const Vector3d& direction,
                        const Vector3d& plane_a,
                        const Vector3d& plane_b,
                        const Vector3d& plane_c,
                        Vector3d& c_point);
/**
 * @brief 计算点是否在三维多边形内
 * @param point 与多边形是否相同
 * @param rect_a rect_b rect_c rect_d 三维矩形上的点
 * @return
**/
bool PointInPolygon (const Vector3d& point,const std::vector<Vector3d>&Polygon);

/**
 * @brief 射线与多边形平面相交
 * @param point
 * @param direction
 * @param Polygon
 * @return
 */
bool RayIntersectPolygon (const Vector3d& point,const Vector3d& direction,

                          const std::vector<Vector3d>&polygon);

/**
 * @brief 计算两条直线是否相交
 * @param 线上的点
 * @return interp 交点
**/
bool LineIntersectLine (const Vector3d& l1p1,const Vector3d& l1p2,
                     const Vector3d& l2p1,const Vector3d& l2p2,Vector3d& interp);

/**
 * @brief 计算射线与直线是否相交
 * @param l1p1 开始位置，l1p1->l1p2为射线方向
 * @return interp 交点
**/
bool RayIntersectLine (const Vector3d& l1p1,const Vector3d& l1p2,
                     const Vector3d& l2p1,const Vector3d& l2p2,Vector3d& interp);

/**
 * @brief 计算射线与线段是否相交
 * @param l1p1 开始位置，l1p1->l1p2为射线方向
 * @return interp 交点
**/
bool RayIntersectSegment (const Vector3d& l1p1,const Vector3d& l1p2,
                     const Vector3d& l2p1,const Vector3d& l2p2,Vector3d& interp);



/**
 * @brief 计算点是否在线段ab上
 * @param p
 * @param a
 * @param b
 * @return
 */
bool PointOnSegment(const Vector3d& p,const Vector3d& a,const Vector3d& b);

/**
 * @brief 计算点是否在平面内
 * @param p
 * @param a 平面点
 * @param b 平面点
 * @param c 平面点
 * @return
 */
bool PointInPlane(const Vector3d& p,const Vector3d& a,const Vector3d& b,const Vector3d& c);



/**
 * 判断是否相等
 */
template <typename T>
bool IsEqual(const T& a, const T& b) {
    if constexpr (std::is_floating_point_v<T>) {
        // 对于浮点数类型
        const T epsilon = C_EPSILON; // 使用类型的epsilon
        return std::fabs(a - b) < epsilon;
    } else {
        // 对于其他类型
        return a == b;
    }
}
#endif

