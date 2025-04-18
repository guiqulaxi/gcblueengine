/**
**  @file simmath.cpp
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

#pragma warning (disable : 4996) // 'strdup' was declared deprecated
#include <cassert>
#include "simmath.h"
#include "nsNav.h"
#include "tcMapData.h"
#include "common/tcStream.h"
#include "tcGameStream.h"
#include "tcGameObject.h"
#include "tcFloatCompressor.h"
#include "common/tcObjStream.h"
#include <cassert>


float Add_dB(float x_dB, float y_dB)
{
    if (fabsf(x_dB - y_dB) > 17.0f)
    {
        return (x_dB > y_dB) ? x_dB : y_dB;
    }
    else
    {
        return 10.0f*log10f(powf(10.0f, 0.1f*x_dB) + powf(10.0f, 0.1f*y_dB));
    }
}

void ConformLonLatRad(float& lon_rad, float& lat_rad) 
{
    lon_rad += C_TWOPI * (float(lon_rad < -C_PI) - float(lon_rad >= C_PI));

    //if (lon_rad < -C_PI) {lon_rad += C_TWOPI;}
    //else if (lon_rad >= C_PI) {lon_rad -= C_TWOPI;}

    if (lat_rad > C_PIOVER2) {lat_rad = C_PIOVER2;}
    else if (lat_rad < - C_PIOVER2) {lat_rad = -C_PIOVER2;}
}

void ConformLonLatRad(double& lon_rad, double& lat_rad) 
{
    lon_rad += C_TWOPI * (double(lon_rad < -C_PI) - double(lon_rad >= C_PI));
    //if (lon_rad < -C_PI) {lon_rad += C_TWOPI;}
    //else if (lon_rad >= C_PI) {lon_rad -= C_TWOPI;}

    if (lat_rad > C_PIOVER2) {lat_rad = C_PIOVER2;}
    else if (lat_rad < - C_PIOVER2) {lat_rad = -C_PIOVER2;}
}

void ConformLonLatDeg(float& lon_deg, float& lat_deg) 
{
    lon_deg += 360.0f * (float(lon_deg < -180.0f) - float(lon_deg >= 180.0f));
    //if (lon_deg < -180.0f) {lon_deg += 360.0f;}
    //else if (lon_deg >= 180.0f) {lon_deg -= 360.0f;}

    if (lat_deg > 90.0f) {lat_deg = 90.0f;}
    else if (lat_deg < -90.0f) {lat_deg = -89.9999f;}
}

void ConformLonLatDeg(double& lon_deg, double& lat_deg) 
{
    lon_deg += 360.0 * (double(lon_deg < -180.0) - double(lon_deg >= 180.0));
    //if (lon_deg < -180.0) {lon_deg += 360.0;}
    //else if (lon_deg >= 180.0) {lon_deg -= 360.0;}

    if (lat_deg > 90.0) {lat_deg = 90.0;}
    else if (lat_deg < -90.0) {lat_deg = -89.99999;}
}

void LonLatToStringB(float afLon_deg, float afLat_deg, std::string& s) 
{
    char zBuff[128];
    float deg,min,sec;

    deg = floorf(afLat_deg);
    min = floorf(60.0f*(afLat_deg-deg));
    sec = floorf(60.0f*(60.0f*(afLat_deg-deg)-min));
    sprintf(zBuff,"%03.f:%02.f:%02.f ",deg,min,sec);
    s = zBuff;

    float abs_lon = fabsf(afLon_deg);
    float sign_lon = (afLon_deg < 0) ? -1.0f : 1.0f;

    deg = floorf(abs_lon);
    min = floorf(60.0f*(abs_lon-deg));
    sec = floorf(60.0f*(60.0f*(abs_lon-deg)-min));
    sprintf(zBuff,"%03.f:%02.f:%02.f ",sign_lon*deg,min,sec);
    s += zBuff;
}

void LonLatToString(float afLon_deg, float afLat_deg, tcString& s) 
{
    tcString stemp;
    float deg,min,sec;
    deg = floorf(afLat_deg);
    min = floorf(60.0f*(afLat_deg-deg));
    sec = floorf(60.0f*(60.0f*(afLat_deg-deg)-min));
    s.Format("%03.f:%02.f:%02.f ",deg,min,sec);

    float abs_lon = fabsf(afLon_deg);
    float sign_lon = (afLon_deg < 0) ? -1.0f : 1.0f;

    deg = floorf(abs_lon);
    min = floorf(60.0f*(abs_lon-deg));
    sec = floorf(60.0f*(60.0f*(abs_lon-deg)-min));
    stemp.Format("%03.f:%02.f:%02.f ",sign_lon*deg,min,sec);
    s += stemp;
}


// assumes lon is within [-pi,pi) and lat [-pi/2,pi/2]
int GeoWithinRegion(GeoPoint p, const tcRect *pRegion) 
{ 
    if ((p.mfLat_rad > pRegion->top)||(p.mfLat_rad < pRegion->bottom))
    {
        return 0;
    }

    if (pRegion->left <= pRegion->right)
    {
        return ((p.mfLon_rad >= pRegion->left)&&(p.mfLon_rad <= pRegion->right));
    }
    else
    {
        return ((p.mfLon_rad >= pRegion->left)||(p.mfLon_rad <= pRegion->right));
    }
}

int AngleWithinRange(float afAngle_rad, float afAngle1_rad, float afAngle2_rad) 
{
    // map angles to -180 to 180, assumes angles are in [-540,540]
    if (afAngle_rad < -C_PI) afAngle_rad += C_TWOPI;
    else if (afAngle_rad >= C_PI) afAngle_rad -= C_TWOPI;

    if (afAngle1_rad < -C_PI) afAngle1_rad += C_TWOPI;
    else if (afAngle1_rad > C_PI) afAngle1_rad -= C_TWOPI;

    if (afAngle2_rad < -C_PI) afAngle2_rad += C_TWOPI;
    else if (afAngle2_rad > C_PI) afAngle2_rad -= C_TWOPI;

    // check if region is wrapped and calc result
    if (afAngle1_rad <= afAngle2_rad)
    {
        return ((afAngle_rad >= afAngle1_rad)&&(afAngle_rad <= afAngle2_rad));
    }
    else
    {
        return ((afAngle_rad >= afAngle1_rad)||(afAngle_rad <= afAngle2_rad));
    }
}


/**
* operates in radian longitude, latitude, bearing
*/
bool TriangulateBearings(const tcPoint& p1, float bearing1_rad, const tcPoint& p2, float bearing2_rad,
                         tcPoint& result)
{
    result.x = 0;
    result.y = 0;

    // use point 1 as origin
    float dx = p2.x - p1.x;
    float dy = p2.y - p1.y;

    float sin_brg1 = sinf(bearing1_rad);
    float cos_brg1 = cosf(bearing1_rad);
    float sin_brg2 = sinf(bearing2_rad);
    float cos_brg2 = cosf(bearing2_rad);

    float lon_distortion1 = 1.0f / cosf(0.5f*(p1.y+p2.y));
    float lon_distortion2 = lon_distortion1;

    float bx1 = sin_brg1*lon_distortion1;
    float by1 = cos_brg1;

    float bx2 = sin_brg2*lon_distortion2;
    float by2 = cos_brg2;

    float num1 = by2*dx - bx2*dy;
    float num2 = by1*dx - bx1*dy;
    float den = bx1*by2 - bx2*by1;

    //float num2 = (dx*by1 - dy*bx1);
    //float den2 = (bx1*by2 - bx2*by1);


    if (den == 0) return false; // parallel

    float ua = num1 / den; // ua will be negative if bad triangulation (point behind p1)
    
    result.x = p1.x + ua*bx1;
    result.y = p1.y + ua*by1;

    // refine estimate with more accurate lon distortion
    lon_distortion1 = 1.0f / cosf(0.5f*(p1.y+result.y));
    lon_distortion2 = 1.0f / cosf(0.5f*(p2.y+result.y));

    bx1 = sin_brg1*lon_distortion1;
    bx2 = sin_brg2*lon_distortion2;

    num1 = by2*dx - bx2*dy;
    num2 = by1*dx - bx1*dy;
    den = bx1*by2 - bx2*by1;

    ua = num1 / den; // ua will be negative if bad triangulation (point behind p1)
    
    result.x = p1.x + ua*bx1;
    result.y = p1.y + ua*by1;

    bool valid1 = ((num1 > 0) && (den > 0)) || ((num1 < 0) && (den < 0));
    bool valid2 = ((num2 > 0) && (den > 0)) || ((num2 < 0) && (den < 0));

    return valid1 && valid2;
}

/************ tcPoint ********************/
/**
* Offsets point where angle 0 is +y, angle pi/2 is +x
*/
void tcPoint::Offset(float distance, float angle_rad)
{
    x += distance * sinf(angle_rad);
    y += distance * cosf(angle_rad);
}



/******************************* tcGeoRect ********************************/

/**
* @param x longitude in radians
* @param y latitude in radians
* @return true if point (lon,lat) in radians is within
* @return region.
*/
bool tcGeoRect::ContainsPoint(float x, float y) const
{
    GeoPoint p;
    p.Set(x, y, 0);
    return GeoWithinRegion(p, this) != 0;
}

float tcGeoRect::Width() {
    if (right > left) {return right-left;}
    else {return right - left + C_TWOPI;}
}

float tcGeoRect::XCenter() {
    float fAvg;
    if (right > left) {return 0.5f*(right+left);}
    else {
        fAvg = 0.5f*(right + left + C_TWOPI);
        if (fAvg >= C_PI) {fAvg -= C_TWOPI;}
        return fAvg;
    }
}

void tcGeoRect::Offset(float dx, float dy) {
    if (top+dy > C_PIOVER2) {dy=0;}
    else if (bottom+dy <= -C_PIOVER2) {dy=0;}
    Set(left+dx,right+dx,bottom+dy,top+dy);
}

/**
* radian units
*/
void tcGeoRect::Set(float x1,float x2,float y1,float y2) {
    if (x1 < -C_PI) {x1 += C_TWOPI;}
    else if (x1 >= C_PI) {x1 -= C_TWOPI;}
    if (x2 < -C_PI) {x2 += C_TWOPI;}
    else if (x2 >= C_PI) {x2 -= C_TWOPI;}

    if (y1 <= -C_PIOVER2) {
        y2 = (y2-y1) - C_PIOVER2M;
        y1 = -C_PIOVER2M;
    }
    else if (y1 > C_PIOVER2) {
        y1 = C_PIOVER2 - (y2-y1);
        y2 = C_PIOVER2;
    }
    if (y2 <= -C_PIOVER2) {
        y2 = (y2-y1) - C_PIOVER2M;
        y1 = -C_PIOVER2M;
    }
    else if (y2 > C_PIOVER2) {
        y1 = C_PIOVER2 - (y2-y1);
        y2 = C_PIOVER2;
    }
    left = x1;
    right = x2;
    bottom = y1;
    top = y2;
}

/**
* accepts longitude and latitude arguments in degrees units
*/
void tcGeoRect::SetDegrees(float lon1_deg, float lon2_deg, float lat1_deg, float lat2_deg)
{
    tcGeoRect::Set(C_PIOVER180*lon1_deg, C_PIOVER180*lon2_deg,
                   C_PIOVER180*lat1_deg, C_PIOVER180*lat2_deg);
}

// forces r to be within tcGeoRect, assumes dimensions of r don't exceed tcGeoRect
// dimensions
void tcGeoRect::ApplyBounds(tcGeoRect& r) 
{
    // first handle top and bottom
    if (r.top > top)
    {
        r.Offset(0, top - r.top);
    }
    else if (r.bottom < bottom)
    {
        r.Offset(0, bottom - r.bottom);
    }

    // left and right need to handle wrapped case

    float width = Width();
    float rWidth = r.Width();

    float xLeft = (r.left > left) ? r.left - left : r.left - left + C_TWOPI;
    if (xLeft > width)
    {
        r.left = left;
        r.right = left + rWidth;
        if (r.right >= C_PI) r.right -= C_TWOPI;
    }

    float xRight = (r.right > left) ? r.right - left : r.right - left + C_TWOPI;
    if (xRight > width)
    {
        r.right = right;
        r.left = right - rWidth;
        if (r.left < -C_PI) r.left += C_TWOPI;
    }
}



/// @returns true if any part of r is outside of this rect
bool tcGeoRect::IsOutOfBounds(tcGeoRect& r) const
{
    bool boundsAreWrapped = left > right;

    if (!boundsAreWrapped)
    {
        return (r.top > top) || (r.bottom < bottom) || (r.left < left) || (r.left > right) || (r.right > right) || (r.right < left);
    }
    else
    {
        bool leftIn = (r.left >= left)||(r.left <= right);
        bool rightIn = (r.right >= left)||(r.right <= right);

        return (r.top > top) || (r.bottom < bottom) || (!leftIn) || (!rightIn);
    }
}



bool tcGeoRect::operator==(const tcGeoRect& r)
{
    return ((left == r.left)&&(right == r.right)&&
            (top == r.top)&&(bottom == r.bottom));
}

bool tcGeoRect::operator!=(const tcGeoRect& r)
{
    return !(operator==(r));
}

/******************************* tcTerrainInfo *******************************/
void tcTerrainInfo::Clear() 
{
    mfHeight_m = 0;
    lookAheadHeight_m = 0;
    mfLatDatum = 0;
    mfLonDatum = 0;
}

void tcTerrainInfo::Serialize(tcFile& file, bool abLoad) 
{
    assert(false);
    if (abLoad)
    {
        file.Read(&mfHeight_m,sizeof(mfHeight_m));
        file.Read(&mfLonDatum,sizeof(mfLonDatum));
        file.Read(&mfLatDatum,sizeof(mfLatDatum));
    }
    else
    {
        file.Write(&mfHeight_m,sizeof(mfHeight_m));
        file.Write(&mfLonDatum,sizeof(mfLonDatum));
        file.Write(&mfLatDatum,sizeof(mfLatDatum));
    }
}

tcGameStream& tcTerrainInfo::operator>>(tcGameStream& stream)
{
    stream << mfHeight_m;
    stream << lookAheadHeight_m;
    stream << mfLonDatum;
    stream << mfLatDatum;

    return stream;
}

tcGameStream& tcTerrainInfo::operator<<(tcGameStream& stream)
{
    stream >> mfHeight_m;
    stream >> lookAheadHeight_m;
    stream >> mfLonDatum;
    stream >> mfLatDatum;

    return stream;
}

/********************** GeoPoint *************************************/
/**
* Load state from stream
*/
tcStream& GeoPoint::operator<<(tcStream& stream)
{
    stream >> mfLon_rad;
    stream >> mfLat_rad;
    stream >> mfAlt_m;

    return stream;
}

/**
* Save state to stream
*/
tcStream& GeoPoint::operator>>(tcStream& stream)
{
    stream << mfLon_rad;
    stream << mfLat_rad;
    stream << mfAlt_m;

    return stream;
}

const GeoPoint& GeoPoint::Offset(float distance_km, float bearing_rad)
{
    float dist_rad = C_KMTORAD * distance_km;

    mfLon_rad += dist_rad * sinf(bearing_rad) / cosf(mfLat_rad);
    mfLat_rad += dist_rad * cosf(bearing_rad);

    ConformLonLatRad(mfLon_rad, mfLat_rad);

    return *this;
}


GeoPoint::GeoPoint()
    : mfLon_rad(0),
      mfLat_rad(0),
      mfAlt_m(0)
{
}


GeoPoint::GeoPoint(double lon_rad, double lat_rad, float alt_m)
    : mfLon_rad(lon_rad),
      mfLat_rad(lat_rad),
      mfAlt_m(alt_m)
{
}

GeoPoint::~GeoPoint()
{
}


/******************************* tcKinematics *******************************/
void tcKinematics::LLToXYm(double& x, double& y) const
{
    // 计算X和Y坐标
    x = C_RADTOM*cos(mfLat_rad)*(mfLon_rad);
    y = C_RADTOM*(mfLon_rad);
}
/**
* 计算碰撞体与由tcKinematics表示的对象之间的最近距离时间点。
* @param dx 世界坐标系中东方向的距离差（米）
* @param dy 世界坐标系中北方向的距离差（米）
* @param dz 世界坐标系中垂直方向的距离差（米）
* @return 碰撞发生时的最近时间（秒），负值表示已过去
*/

float tcKinematics::CalculateCollisionPoint(const tcKinematics& collider, float& dxi, float& dyi, float& dzi)
{
    // 计算经度差和纬度差（弧度）
    double dlon = mfLon_rad - collider.mfLon_rad;
    double dlat = mfLat_rad - collider.mfLat_rad;

    // 根据经度差和纬度差计算东西方向和南北方向上的距离差（米）
    float dx = C_RADTOM*cosf(mfLat_rad)*((float)dlon); // C_RADTOM 是弧度到米的转换系数
    float dy = C_RADTOM*((float)dlat);
    // 计算垂直方向上的距离差（米）
    float dz = mfAlt_m - collider.mfAlt_m;

    // 将速度（节）转换为速度（米/秒）
    float v = C_KTSTOMPS*mfSpeed_kts; // C_KTSTOMPS 是节到米/秒的转换系数
    float vc = C_KTSTOMPS*collider.mfSpeed_kts;
    // 计算垂直方向上的速度差
    float dvz = v*sinf(mfPitch_rad) - vc*sinf(collider.mfPitch_rad);
    // 计算俯仰角的余弦值
    float cospitch = cosf(mfPitch_rad);
    float cospitchc = cosf(collider.mfPitch_rad);
    // 计算东西方向和南北方向上的速度差
    float dvx = v*cospitch*sinf(mfHeading_rad) - vc*cospitchc*sinf(collider.mfHeading_rad);
    float dvy = v*cospitch*cosf(mfHeading_rad) - vc*cospitchc*cosf(collider.mfHeading_rad);

    // 断言确保速度差不为零，避免除以零错误
    assert(dvx*dvx + dvy*dvy + dvz*dvz != 0);

// 相对运动: 当两个物体以不同的速度移动时，可以想象其中一个物体是静止的，而另一个物体以它们之间的相对速度移动。这简化了问题，使得我们可以使用一维或三维空间中的直线运动方程。
// 直线运动方程: 对于一维直线运动，物体从初始位置x0​以速度v移动，其位置随时间t的变化可以表示为x=x0​+vt。如果两个物体分别从x1​(0)和x2​(0)开始，以速度v1​和v2​移动，则它们之间的相对位置随时间的变化为xrel​(t)=(x1​(0)−x2​(0))+(v1​−v2​)t。
// 碰撞时间: 碰撞发生的时间tclosest​是当相对位置xrel​(t)等于0的时间点。将上述方程设置为0并解出t，我们得到tclosest​=−v1​−v2​x1​(0)−x2​(0)​。
// 三维情况: 对于三维情况，我们只需将上述一维方程扩展到三个维度。相对位置随时间的变化可以表示为rrel​(t)=r1​(0)−r2​(0)+(v1​−v2​)t，其中r和v分别是位置和速度的向量。碰撞发生的时间是当rrel​(t)=0的时间点，即解方程r1​(0)−r2​(0)+(v1​−v2​)t=0。
// 解方程: 在三维空间中，上述方程可以分解为三个独立的方程（每个维度一个）。
// 但更简洁地，我们可以使用向量的点积来求解。将方程两边同时点乘(v1​−v2​)，得到(r1​(0)−r2​(0))⋅(v1​−v2​)+(v1​−v2​)⋅(v1​−v2​)t=0。
// 解这个方程得到tclosest​=−(v1​−v2​)⋅(v1​−v2​)(r1​(0)−r2​(0))⋅(v1​−v2​)​。
  // 计算最近的碰撞时间（秒）
    float tclosest = -(dx*dvx + dy*dvy + dz*dvz) /
                     (dvx*dvx + dvy*dvy + dvz*dvz);

    // 计算碰撞发生时的距离差（米）
    dxi = dx + dvx*tclosest;
    dyi = dy + dvy*tclosest;
    dzi = dz + dvz*tclosest;

    // 返回最近的碰撞时间
    return tclosest;
}

/**
* Calculates the ground impact point (lon_rad, lat_rad)
* assuming constant velocity motion to impact.
* This has not been tested.
* 
* @param terrainHeight_m assumed terrain height in meters
* @param lon_rad longitude in radians of impact point
* @param lat_rad latitude in radians of impact point
* @return time of impact in seconds, negative indicates past
*/
float tcKinematics::CalculateGroundImpactPoint(float terrainHeight_m, 
                                               double& lon_rad, double& lat_rad)
{

    float dz =  terrainHeight_m - mfAlt_m;
    float v = C_KTSTOMPS*mfSpeed_kts;
    float vz = v*sinf(mfPitch_rad);

    float timpact = dz / vz;

    float cospitch = cosf(mfPitch_rad);
    float k = C_MTORAD * timpact * v * cospitch;
    float dlon = k * sinf(mfHeading_rad) / cosf(mfLat_rad);
    float dlat = k * cosf(mfHeading_rad);

    lon_rad = mfLon_rad + dlon;
    lat_rad = mfLat_rad + dlat;

    return timpact;
}

/**
 * @brief 计算相对速度
 * @return range rate in m/s between this tcKinematics and k
 * 3-D calculation
*/
float tcKinematics::CalculateRangeRate(const tcKinematics& k) const
{
    float speed1_mps = C_KTSTOMPS * mfSpeed_kts;
    float vz1 = sinf(mfClimbAngle_rad) * speed1_mps;
    float vxy1 = cosf(mfClimbAngle_rad) * speed1_mps;
    float vx1 = sinf(mfHeading_rad) * vxy1;
    float vy1 = cosf(mfHeading_rad) * vxy1;

    float speed2_mps = C_KTSTOMPS * k.mfSpeed_kts;
    float vz2 = sinf(k.mfClimbAngle_rad) * speed2_mps;
    float vxy2 = cosf(k.mfClimbAngle_rad) * speed2_mps;
    float vx2 = sinf(k.mfHeading_rad) * vxy2;
    float vy2 = cosf(k.mfHeading_rad) * vxy2;

    float dvx = vx1 - vx2;
    float dvy = vy1 - vy2;
    float dvz = vz1 - vz2;

    return sqrtf(dvx*dvx + dvy*dvy + dvz*dvz);
}


/**
*  Extrapolates position ahead in time by dt_s (or behind if dt_s < 0)
*  预测推断目标的位置dt_s 秒
*/
void tcKinematics::Extrapolate(float dt_s)
{
    double lon_rad;
    double lat_rad;
    float alt_m;

    PredictPosition(dt_s, lon_rad, lat_rad, alt_m);

    mfLon_rad = lon_rad;
    mfLat_rad = lat_rad;
    mfAlt_m = alt_m;
}

/**
* Predicts position ahead by dt_s seconds
*/
void tcKinematics::PredictPosition(float dt_s, 
                                   double& lon_rad, double& lat_rad, float& alt_m) const
{
    float v = C_KTSTOMPS*mfSpeed_kts;

    float vz, cospitch;
    if (mfPitch_rad == 0)
    {
        vz = 0;
        cospitch = 1.0f;
    }
    else
    {
        vz = v*sinf(mfPitch_rad);
        cospitch = cosf(mfPitch_rad);
    }

    float k = C_MTORAD * dt_s * v * cospitch;
    float dlon = k * sinf(mfHeading_rad) / cosf(mfLat_rad);
    float dlat = k * cosf(mfHeading_rad);

    lon_rad = mfLon_rad + dlon;
    lat_rad = mfLat_rad + dlat;
    alt_m = mfAlt_m + vz * dt_s;

}

/**
* @return bearing rate to track in radians per second
* Ignores altitude difference
* @param range_km range to target
* @param bearing_rad bearing to target
* @param speet_kts target speed
* @param heading_rad target heading
*/
float tcKinematics::BearingRateTo(float range_km, float bearing_rad, float speed_kts, float heading_rad)
{
    float inv_range = 1.0f / range_km;
    float dx = sinf(bearing_rad) * inv_range;
    float dy = cosf(bearing_rad) * inv_range;

    float dvx = C_KTSTOKMPS * (sinf(heading_rad) * speed_kts -
                               sinf(mfHeading_rad) * mfSpeed_kts);
    float dvy = C_KTSTOKMPS * (cosf(heading_rad) * speed_kts -
                               cosf(mfHeading_rad) * mfSpeed_kts);

    return ((dy * dvx) - (dx * dvy));
}


/**
* @returns radian heading to track
*/
float tcKinematics::HeadingToTrack(const tcTrack& track) {
    return nsNav::GCHeadingApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                      (float)track.mfLat_rad,(float)track.mfLon_rad);
}
/**
* @returns radian heading to (lat,lon) point
*/
float tcKinematics::HeadingToGeoRad(const GeoPoint *apGeoPoint) const
{
    return nsNav::GCHeadingApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                      (float)apGeoPoint->mfLat_rad,(float)apGeoPoint->mfLon_rad);
}

/**
* @returns radian heading to (lat,lon) point
*/
float tcKinematics::HeadingToGeoRad(float lon_rad, float lat_rad) const
{
    return nsNav::GCHeadingApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                      lat_rad, lon_rad);
}

/**
* @returns radian heading to (lat,lon) point of kinematics object
*/
float tcKinematics::HeadingToRad(const tcKinematics& k) const
{
    return nsNav::GCHeadingApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                      k.mfLat_rad, k.mfLon_rad);
}

/**
* @returns range in km
*/
float tcKinematics::RangeToKm(const tcKinematics& k) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   (float)k.mfLat_rad,(float)k.mfLon_rad);
}
/**
 * @brief 计算距离包括高度
 * @param k
 * @return range in km including range due to altitude difference
 */
float tcKinematics::RangeToKmAlt(const tcKinematics& k) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   (float)k.mfLat_rad,(float)k.mfLon_rad,
                                                   mfAlt_m,k.mfAlt_m);
}

float tcKinematics::RangeToKmAlt(const tcTrack& track) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   (float)track.mfLat_rad,(float)track.mfLon_rad,
                                                   mfAlt_m,track.mfAlt_m);
}


float tcKinematics::RangeToKmAlt(float lon_rad, float lat_rad, float alt_m) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   (float)lat_rad,(float)lon_rad,
                                                   mfAlt_m, alt_m);
}

// float tcKinematics::RangeToKmAlt(std::shared_ptr<const tcGameObject> obj) const
// {
//     assert(obj != 0);
//     return RangeToKmAlt(obj->mcKin);
// }


float tcKinematics::RangeToKm(const GeoPoint *apGeoPoint) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   apGeoPoint->mfLat_rad,apGeoPoint->mfLon_rad);
}


/**
* @return approximate range in km, altitude difference is neglected
*/
float tcKinematics::RangeToKm(const tcTrack& track) const
{
    float lat_rad = (float)track.mfLat_rad;
    float lon_rad = (float)track.mfLon_rad;
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   lat_rad,lon_rad);
}

/**
* @return approximate range in km, altitude difference is neglected
*/
float tcKinematics::RangeToKm(float lon_rad, float lat_rad) const
{
    return C_RADTOKM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                   lat_rad, lon_rad);
}

/**
* @return approximate range in m, altitude difference is neglected
*/
float tcKinematics::RangeToM(float lon_rad, float lat_rad) const
{
    return C_RADTOM * nsNav::GCDistanceApprox_rad((float)mfLat_rad,(float)mfLon_rad,
                                                  lat_rad, lon_rad);
}


/**
* Load state from stream 
* No compression for game stream
*/
tcGameStream& tcKinematics::operator<<(tcGameStream& stream)
{
    stream >> mfLon_rad;
    stream >> mfLat_rad;
    stream >> mfAlt_m;
    stream >> mfHeading_rad;
    stream >> mfClimbAngle_rad;
    stream >> mfYaw_rad;
    stream >> mfPitch_rad;
    stream >> mfRoll_rad;
    stream >> mfSpeed_kts;

    return stream;
}

/**
* Save state to stream
* No compression for game stream
*/
tcGameStream& tcKinematics::operator>>(tcGameStream& stream)
{
    stream << mfLon_rad;
    stream << mfLat_rad;
    stream << mfAlt_m;
    stream << mfHeading_rad;
    stream << mfClimbAngle_rad;
    stream << mfYaw_rad;
    stream << mfPitch_rad;
    stream << mfRoll_rad;
    stream << mfSpeed_kts;

    return stream;
}

/**
* Load state from stream, compression used for update stream
*/
tcUpdateStream& tcKinematics::operator<<(tcUpdateStream& stream)
{
    stream >> mfLon_rad;
    stream >> mfLat_rad;
    stream >> mfAlt_m;
    tcAngleCompressor headingc(mfHeading_rad);
    stream >>headingc;
    tcAngleCompressor climbAnglec(mfClimbAngle_rad);
    stream >>climbAnglec;
    tcAngleCompressor yawc(mfYaw_rad);
    stream >>yawc;
    tcAngleCompressor pitchc(mfPitch_rad);
    stream >>pitchc;
    tcAngleCompressor rollc(mfRoll_rad);
    stream >>rollc;
    tcIntervalCompressor speedc(mfSpeed_kts, 0, 4000.0f);
    stream >>speedc;

    //    stream >> tcAngleCompressor(mfHeading_rad);
    //    stream >> tcAngleCompressor(mfClimbAngle_rad);
    //    stream >> tcAngleCompressor(mfYaw_rad);
    //    stream >> tcAngleCompressor(mfPitch_rad);
    //    stream >> tcAngleCompressor(mfRoll_rad);
    //    stream >> tcIntervalCompressor(mfSpeed_kts, 0, 4000.0f);

    return stream;
}

/**
* Save state to update stream, compression used for update stream
*/
tcUpdateStream& tcKinematics::operator>>(tcUpdateStream& stream)
{
    stream << mfLon_rad;
    stream << mfLat_rad;
    stream << mfAlt_m;
    stream << tcAngleCompressor(mfHeading_rad);
    stream << tcAngleCompressor(mfClimbAngle_rad);
    stream << tcAngleCompressor(mfYaw_rad);
    stream << tcAngleCompressor(mfPitch_rad);
    stream << tcAngleCompressor(mfRoll_rad);
    stream << tcIntervalCompressor(mfSpeed_kts, 0, 4000.0f);

    return stream;
}

void tcKinematics::Serialize(tcFile& file, bool abLoad) {
    if (abLoad) {
        file.Read(&mfLon_rad,sizeof(mfLon_rad));
        file.Read(&mfLat_rad,sizeof(mfLat_rad));
        file.Read(&mfAlt_m,sizeof(mfAlt_m));
        file.Read(&mfHeading_rad,sizeof(mfHeading_rad));
        file.Read(&mfClimbAngle_rad,sizeof(mfClimbAngle_rad));
        file.Read(&mfYaw_rad,sizeof(mfYaw_rad));
        file.Read(&mfPitch_rad,sizeof(mfPitch_rad));
        file.Read(&mfRoll_rad,sizeof(mfRoll_rad));
        file.Read(&mfSpeed_kts,sizeof(mfSpeed_kts));
    }
    else {
        file.Write(&mfLon_rad,sizeof(mfLon_rad));
        file.Write(&mfLat_rad,sizeof(mfLat_rad));
        file.Write(&mfAlt_m,sizeof(mfAlt_m));
        file.Write(&mfHeading_rad,sizeof(mfHeading_rad));
        file.Write(&mfClimbAngle_rad,sizeof(mfClimbAngle_rad));
        file.Write(&mfYaw_rad,sizeof(mfYaw_rad));
        file.Write(&mfPitch_rad,sizeof(mfPitch_rad));
        file.Write(&mfRoll_rad,sizeof(mfRoll_rad));
        file.Write(&mfSpeed_kts,sizeof(mfSpeed_kts));
    }
}

/**
* 2009 OCT 03 - Modified this to use GetInterceptData3D code with altitude difference = 0
* Something appeared wrong with previous code when checked in matlab
*/
void tcKinematics::GetInterceptData2D(const tcTrack& track, 
                                      float& rfHeading_rad, float& rfTimeToIntercept)
{
    float dx,dy,dx2,dy2;
    float vtx,vty,vtx2,vty2; // track velocity components
    float vx,vy,v2;
    float fTrackSpeed_radps, fSpeed_radps;
    float a,b,c,det,k; // quadratic equation coefficients

    dx = (track.mfLon_rad - (float)mfLon_rad)*cosf((float)mfLat_rad);
    dy = track.mfLat_rad - (float)mfLat_rad;

    dx2 = dx*dx;
    dy2 = dy*dy;

    //rfRange_rad = sqrtf(dx2+dy2);

    fTrackSpeed_radps = track.mfSpeed_kts*C_KTSTORADPS;

    float vtgroundspeed = fTrackSpeed_radps;
    vtx = vtgroundspeed*sinf(track.mfHeading_rad);
    vty = vtgroundspeed*cosf(track.mfHeading_rad);
    vtx2 = vtx*vtx;
    vty2 = vty*vty;

    fSpeed_radps = mfSpeed_kts*C_KTSTORADPS; // ownship speed
    v2 = fSpeed_radps*fSpeed_radps;
    a = dx2 + dy2;
    b = 2.0f*(dx*vtx + dy*vty);
    c = vtx2 + vty2 - v2;
    det = (b*b - 4.0f*a*c);
    if (det >= 0)
    {
        k = (-b + sqrtf(det))/(2.0f*a); // may need to check negative sol'n too

        if (k > 0)
        {
            vx = vtx + k*dx;
            vy = vty + k*dy;

            //float vground = sqrtf(vx*vx + vy*vy);
            // negative solution is evasion course

            rfHeading_rad = atan2f(vx,vy);
            //rfHeading_rad = atan2f(dx,dy);
            rfTimeToIntercept = (fabsf(dy)>=fabsf(dx)) ? dy/(vy-vty) : dx/(vx-vtx);
            return;
        }
    }

    // no intercept solution exists, just head toward target
    rfHeading_rad = atan2f(dx,dy);
    rfTimeToIntercept = 9999.0f;
    return;

}

/**
 * @brief 函数旨在计算我方（一个动态对象，可能是一架飞机或导弹）为了拦截一个目标（另一个动态对象，如敌方飞机或导弹）所需的数据
 * @param track
 * @param rfHeading_rad 拦截时的航向角
 * @param rfClimbAngle_rad 拦截时的爬升角，以弧度为单位
 * @param rfTimeToIntercept 预计的拦截时间
 * @param rfRange_km 目标与我方之间的直线距离
 */
void tcKinematics::GetInterceptData3D(const tcTrack& track, float& rfHeading_rad,
                                      float& rfClimbAngle_rad, float& rfTimeToIntercept, float& rfRange_km)
{
    // 定义用于计算的中间变量
    float dx,dy,dz,dx2,dy2,dz2; // 目标与我方在经度、纬度和高度上的差值及其平方
    float vtx,vty,vtz,vtx2,vty2,vtz2; // 目标速度分量
    float vx,vy,vz,v2; // 我方拦截时的速度分量及速度的平方
    float fTrackSpeed_radps, fSpeed_radps; // 目标速度和我方速度，单位：弧度/秒
    float a,b,c,det,k; // 二次方程系数及判别式

    // 计算目标与我方在经度、纬度和高度上的差值

    double dlon = mfLon_rad - track.mfLon_rad;
    double dlat = mfLat_rad - track.mfLat_rad;

    dx = C_RADTOM*cosf(mfLat_rad)*((float)dlon);
    dy = C_RADTOM*((float)dlat);
    dz = (track.mfAlt_m - mfAlt_m)*C_MTORAD; // 高度差转换为弧度（C_MTORAD为米转弧度的常数）
    // dx = (track.mfLon_rad - (float)mfLon_rad)*cosf((float)mfLat_rad); // 考虑纬度对经度差的影响
    // dy = track.mfLat_rad - (float)mfLat_rad;
    // dz = (track.mfAlt_m - mfAlt_m)*C_MTORAD; // 高度差转换为弧度（C_MTORAD为米转弧度的常数）

    // 计算差值的平方
    dx2 = dx*dx;
    dy2 = dy*dy;
    dz2 = dz*dz;

    // 计算目标与我方的直线距离（以弧度为单位，实际上这里应该是直线距离但单位用了弧度，可能是个错误或者特定上下文中的用法）
    rfRange_km = sqrtf(dx2+dy2+dz2)*0.001;

    // 将目标速度从节转换为弧度/秒
    fTrackSpeed_radps = track.mfSpeed_kts*C_KTSTORADPS;

    // 计算目标速度在垂直和水平方向上的分量
    vtz = sinf(track.mfClimbAngle_rad)*fTrackSpeed_radps;
    float vtgroundspeed = cosf(track.mfClimbAngle_rad)*fTrackSpeed_radps;
    vtx = vtgroundspeed*sinf(track.mfHeading_rad);
    vty = vtgroundspeed*cosf(track.mfHeading_rad);

    // 计算速度分量的平方
    vtx2 = vtx*vtx;
    vty2 = vty*vty;
    vtz2 = vtz*vtz;

    // 将我方速度从节转换为弧度/秒，并计算其平方
    fSpeed_radps = mfSpeed_kts*C_KTSTORADPS; // ownship speed
    v2 = fSpeed_radps*fSpeed_radps;

    // 构建二次方程的系数a, b, c，用于求解拦截时间
    a = dx2 + dy2 + dz2;
    b = 2.0f*(dx*vtx + dy*vty + dz*vtz);
    c = vtx2 + vty2 + vtz2 - v2;

    // 计算判别式
    det = (b*b - 4.0f*a*c);

    // 如果判别式小于0，则假设我方速度稍快一些以得到一个解（这里的方法可能不是最准确的）
    if (det < 0) {
        det = b*b + 4.0f*a*0.1f*v2; // assume slightly faster
    }

    // 解二次方程得到拦截时间k（可能还需要检查负解）
    k = (-b + sqrtf(det))/(2.0f*a); // may need to check negative sol'n too, check for k < 0?? 3 OCT

    // 计算拦截时的速度分量
    vx = vtx + k*dx;
    vy = vty + k*dy;
    vz = vtz + k*dz;

    // 计算拦截时的地面速度
    float vground = sqrtf(vx*vx + vy*vy);

    // 计算拦截时的航向角和爬升角
    rfHeading_rad = atan2f(vx,vy); // 拦截时的航向角
    //rfHeading_rad = atan2f(dx,dy); // 这行被注释掉了，可能是之前的尝试或错误

    // 计算拦截时间（这里的方法可能不精确，因为它没有考虑加速度和三维空间中的复杂运动）
    // 注意：这个计算方法在很多情况下可能不准确，特别是当目标和我方都在移动时
    rfTimeToIntercept = (fabsf(dy)>=fabsf(dx)) ? dy/(vy-vty) : dx/(vx-vtx);

    // 计算拦截时的爬升角
    rfClimbAngle_rad = atanf(vz/vground);
}

/**
* Set rpGeoPoint to point at afBearing_deg and afRange_km relative to
* current location of this tcKinematics object
* altitude isn't changed, has issues off of equator like everything else :<
*/
void  tcKinematics::SetRelativeGeo(GeoPoint& rpGeoPoint, float afBearing_rad, float afRange_km) {
    nsNav::OffsetApprox(mfLat_rad, mfLon_rad, rpGeoPoint.mfLat_rad, rpGeoPoint.mfLon_rad,
                        afBearing_rad,afRange_km*C_KMTORAD);
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
                         Vector3d& c_point)
{
    //需要知道直线上一点和其方向向量，平面一点及其法向量
    Vector3d plane = (plane_a - plane_b).cross(plane_b - plane_c);//平面两个向量叉乘就是法向量

    double den = plane.dot(direction);//面法向量乘线方向向量
    if(0==den)//线与面平行或同处于一个平面不考虑
    {
        return false;
    }
    double t = plane.dot(plane_a - point) / den;//plane_a是面上一点
    c_point = point + direction * t;//这里线上的点用的N，也可以用M，只要上面求t的时候也是用的M就可以
    return true;
}
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
                        Vector3d& c_point)
{

    if(!LineIntersectPlane(point,direction,plane_a,plane_b,plane_c,c_point))
    {
        return false;
    }
    Vector3d dir=c_point-point;
    if(dir.dot(direction)<0)
    {
        return false;
    }
    else
    {
        return true;
    }
}




bool PointOnSegment(const Eigen::Vector3d &p, const Eigen::Vector3d &a, const Eigen::Vector3d &b)
{
    Eigen::Vector3d ap=p-a;
    Eigen::Vector3d bp=p-b;
//    double aa=ap.dot(bp);
//    double aas=ap.norm()*bp.norm();
    //如果点在线段上，ap.bp=-|ab||bp| 方向相反（点积为负数）
    if(IsEqual(ap.dot(bp),-(ap.norm()*bp.norm())))
    {
        return true;
    }else
    {
        return false;
    }

}
bool LineIntersectLine(const Eigen::Vector3d &l1p1, const Eigen::Vector3d &l1p2, const Eigen::Vector3d &l2p1, const Eigen::Vector3d &l2p2, Eigen::Vector3d &interp)
{
    Vector3d d1=(l1p1-l1p2);
    Vector3d d2=(l2p1-l2p2);
    Vector3d  v1=d1/d1.norm();//线的方向单位向量
    Vector3d  v2=d2/d2.norm();//线的方向单位向量
    if (IsEqual(abs(v1.dot(v2)),1.0))
    {
        // 两线平行
        return false;
    }
    Vector3d startPointSeg = l2p1 - l1p1;
    Vector3d vecS1 = v1.cross( v2);            // 有向面积1
    Vector3d vecS2 = startPointSeg.cross( v2); // 有向面积2
    double num = startPointSeg.dot(vecS1);



    // 判断两这直线是否共面
    if (!IsEqual(num,0.0))
    {
        return false;
    }

    // 有向面积比值，利用点乘是因为结果可能是正数或者负数
    float num2 = vecS2.dot( vecS1) / vecS1.norm()/vecS1.norm();
    interp = l1p1 + v1 * num2;
    return true;
}
bool RayIntersectSegment(const Eigen::Vector3d &l1p1, const Eigen::Vector3d &l1p2, const Eigen::Vector3d &l2p1, const Eigen::Vector3d &l2p2, Eigen::Vector3d &interp)
{
    bool ret=LineIntersectLine(l1p1,  l1p2, l2p1, l2p2, interp);
    if(!ret )
    {
        return false;
    }

      //判断射线方向、射线起点与交点连线是否同向，即点乘大于0
    double d=(l1p2-l1p1).dot(interp-l1p1);
     if(d<0)//方向相反
     {
        return false;
     }
    //判断交点是否在线段上
    return PointOnSegment(interp,l2p1,l2p2);
}
bool PointInPolygon(const Eigen::Vector3d &p, const std::vector<Eigen::Vector3d> &polygon)
{
    //判断点是否在多边形边上
    for(size_t i=0;i<polygon.size()-1;i++)
    {
        if(PointOnSegment(p,polygon[i],polygon[i+1]))
        {
            return true;
        }
    }

    //额外取平面上的一个点
    Vector3d dir=polygon[1]-polygon[0];//取第一个点和第二个点的方向
    Vector3d dst=polygon[1]+dir;//沿着直线方向再扩充一倍 取一个点
    Vector3d interp;
    int count=0;
    for(size_t i=0;i<polygon.size();i++)
    {
         if(RayIntersectSegment(p,dst,polygon[i],polygon[(i+1)%polygon.size()],interp))
         {
             count++;
         }
    }
    if(count%2==1)//奇数个说明在多边形内
    {
      return true;
    }else
    {
        return false;
    }
}





bool RayIntersectLine(const Eigen::Vector3d &l1p1, const Eigen::Vector3d &l1p2, const Eigen::Vector3d &l2p1, const Eigen::Vector3d &l2p2, Eigen::Vector3d &interp)
{
     bool ret=LineIntersectLine(l1p1,  l1p2, l2p1, l2p2, interp);
     if(!ret )
     {
         return false;
     }
     //判断射线方向与 射线起点与交点连线是方向否相同,即两个向量点积大于0，
     //更精确来说，(l1p2-l1p1).dot(interp-l1p1)=|l1p2-l1p1|*|interp-l1p1|
     double d=(l1p2-l1p1).dot(interp-l1p1);
     if(d>0)
     {
         return true;
     }
     else{
     return false;
     }
}

bool PointInPlane(const Vector3d& p,const Vector3d& a,const Vector3d& b,const Vector3d& c)
{
    Vector3d ab=b-a;
    Vector3d bc=c-b;
    Vector3d ap=p-a;
    //先求法向量再求，法向量是否与ap垂直
   double d=(ab.cross(bc)).dot(ap);
   return IsEqual(d,0.0);
}


bool RayIntersectPolygon(const Eigen::Vector3d &point, const Eigen::Vector3d &direction, const std::vector<Eigen::Vector3d> &polygon)
{
    if(polygon.size()<3) return false;
    Vector3d c_point;
    if(RayIntersectPlane ( point,direction,
                            polygon[0],polygon[1],polygon[2],c_point))
    {
           if(PointInPolygon(c_point,polygon))
           {
               return  true;
           }
    }
    return false;
}
