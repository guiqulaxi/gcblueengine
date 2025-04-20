/**
**  @file tcLOS.cpp
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

//#include "stdwx.h"

#include "tcLOS.h"
#include "tcOptions.h"
#include "tcMapData.h"
#include "nsNav.h"
#include "strutil.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif


tcLOS* tcLOS::Get()
{
    static tcLOS instance;
    return &instance;
}




void tcLOS::Clear()
{
    rayCache.clear();

    lastUpdateTime = 0;
}

size_t tcLOS::GetRayCount() const
{
    return rayCache.size();
}


const std::string& tcLOS::GetRayTestData(const GeoPoint& p1, const GeoPoint& p2)
{
    static std::string s;

    s.clear();

    std::string text = strutil::format("p1: lat %.4f, lon %.4f, alt %.0f m\n", 
        C_180OVERPI*p1.mfLat_rad, C_180OVERPI*p1.mfLon_rad, p1.mfAlt_m);
    text += strutil::format("p2: lat %.4f, lon %.4f, alt %.0f m\n", 
        C_180OVERPI*p2.mfLat_rad, C_180OVERPI*p2.mfLon_rad, p2.mfAlt_m);

    RayData testRay;
    testRay.p1 = p1;
    testRay.p2 = p2;
    testRay.t_update = 0;
    testRay.terrainClearance_m = 98765.0f;

    UpdateRay(testRay);

    // text += strutil::format("   min LOS clearance: %.0f m (%d rays in cache, %d map tiles)\n", testRay.terrainClearance_m,
    //     GetRayCount(), mapData->GetTilesUsedCount());
    text += strutil::format("   min LOS clearance: %.0f m (%d rays in cache)\n", testRay.terrainClearance_m,
                            GetRayCount());

    s = text;

    return s;
}

/**
* @return true if unobstructed path exists along line-of-sight between p1 and p2
* 检查点p1和p2之间是否存在无障碍的视线路径
*/
bool tcLOS::HasLOS(long key, double t, const GeoPoint& p1, const GeoPoint& p2)
{
    // 如果配置中关闭了视线计算，则使用简单方法检查视线
    if (tcOptions::Get()->calcLineOfSight == 0)
    {
        return HasLOSSimple(key, t, p1, p2);
    }

    // 在射线缓存中查找是否存在该key的射线数据
    std::map<long, RayData>::iterator iter = rayCache.find(key);
    // 如果缓存中不存在，则创建新的射线数据并插入缓存
    if (iter == rayCache.end())
    {
        RayData rayData;

        rayData.t_update = t; // 更新时间
        rayData.terrainClearance_m = 0; // 地形间隙（高度差），初始化为0

        rayCache[key] = rayData; // 插入缓存
        iter = rayCache.find(key); // 重新查找以获取迭代器
    }

    // 确保迭代器有效
    assert(iter != rayCache.end());

    RayData& ray = iter->second; // 获取射线数据引用

    // 计算p1和缓存中p1的粗略距离差，用于判断是否需要更新射线数据
    // 粗略距离是纬度差和经度差（转换为米）加上两倍的高度差
    float d1 = C_RADTOM*(fabsf(ray.p1.mfLat_rad - p1.mfLat_rad) + fabsf(ray.p1.mfLon_rad - p1.mfLon_rad)) +
               2.0*fabsf(ray.p1.mfAlt_m - p1.mfAlt_m);
    // 注意：这里d2的计算与d1完全相同，可能是代码冗余或错误，正常情况下只需要d1即可
    float d2 = C_RADTOM*(fabsf(ray.p2.mfLat_rad - p2.mfLat_rad) + fabsf(ray.p2.mfLon_rad - p2.mfLon_rad)) +
               2.0*fabsf(ray.p2.mfAlt_m - p2.mfAlt_m);

    // 如果距离差大于阈值（200米），则更新射线数据
    if ((d1 + d2) > 200.0f)
    {
        ray.p1 = p1; // 更新起点
        ray.p2 = p2; // 更新终点
        ray.t_update = t; // 更新时间

        UpdateRay(ray); // 更新射线数据
    }

    // 如果射线数据中的地形间隙大于等于0，则存在无障碍视线路径
    if (ray.terrainClearance_m >= 0)
    {
        return true;
    }
    else
    {
        return false; // 否则，不存在无障碍视线路径
    }

}
bool tcLOS::HasLOSSimple(long key, double t, const GeoPoint& p1, const GeoPoint& p2)
{
    return true;
}


/**
* Remove stale rays from rayCache
*/
void tcLOS::Update(double t)
{
    if (t - lastUpdateTime < 31.0) return;
    lastUpdateTime = t;

    std::map<long, RayData> temp;

    std::map<long, RayData>::iterator iter = rayCache.begin();
    for (;iter != rayCache.end(); ++iter)
    {
        if ((t - iter->second.t_update) < 60.0)
        {
            temp.insert(*iter);
        }
    }

    rayCache = temp;
}


/**
* 此函数存在使用地球曲率近似进行雷达地平线计算，然后假设地球为平板进行地形遮蔽的基本问题，
* 但它仍然是一个起点。
*/
void tcLOS::UpdateRay(RayData& ray)
{
    // 计算两点之间的经度、纬度和高度差
    float dLon_deg = C_180OVERPI * (ray.p2.mfLon_rad - ray.p1.mfLon_rad); // 经度差，转换为度
    // 处理经度差越界情况，确保其在-180到180度之间
    dLon_deg = dLon_deg + 360 * (dLon_deg < -180) - 360 * (dLon_deg >= 180);

    float dLat_deg = C_180OVERPI * (ray.p2.mfLat_rad - ray.p1.mfLat_rad); // 纬度差，转换为度
    float dAlt_m = ray.p2.mfAlt_m - ray.p1.mfAlt_m; // 高度差，单位：米

    // 计算两点之间的大致距离，单位：公里
    float range_km = C_RADTOKM * nsNav::GCDistanceApprox_rad(ray.p1, ray.p2);

    // 根据距离计算需要检查的点数，每0.25公里一个点，至少3个点
    unsigned int nPoints = (unsigned int)ceilf(range_km * 0.25);
    nPoints = std::max(nPoints, (unsigned int)3);

    // 计算每个步骤的缩放比例
    float step_scale = 1.0f / float(nPoints + 1);

    // 计算经度、纬度和高度的每一步增量
    float lon_step = dLon_deg * step_scale;
    float lat_step = dLat_deg * step_scale;
    float alt_step = dAlt_m * step_scale;

    // 初始化起点坐标
    float lon_n = C_180OVERPI * ray.p1.mfLon_rad; // 经度，转换为度
    float lat_n = C_180OVERPI * ray.p1.mfLat_rad; // 纬度，转换为度
    float alt_n = ray.p1.mfAlt_m; // 高度，单位：米

    // 初始化最小间隙和对应的索引
    float minimumClearance_m = 99999.9f; // 初始化为一个很大的数
    unsigned int minIdx = 1; // 索引，初始化为1（这里的选择可能不是最优的，但暂时使用）

    // 粗搜索每个点，找到最小间隙
    for (unsigned int n = 0; n < nPoints; n++)
    {
        lon_n += lon_step; // 更新经度
        lat_n += lat_step; // 更新纬度
        alt_n += alt_step; // 更新高度

        // 处理经度越界情况
        lon_n = lon_n + 360 * (lon_n < -180) - 360 * (lon_n >= 180);

        // 获取当前位置的地形高度
        float terrain_m = mapData->GetTerrainHeight(lon_n, lat_n, ray.t_update);

        // 计算当前点与地形之间的间隙
        float clearance_m = alt_n - terrain_m;
        // 如果当前间隙小于最小间隙，则更新最小间隙和索引
        if (clearance_m < minimumClearance_m)
        {
            minimumClearance_m = clearance_m;
            minIdx = n;
        }
    }

    // 在最小间隙附近进行精细搜索
    lon_n = C_180OVERPI * ray.p1.mfLon_rad; // 重新初始化起点经度
    lat_n = C_180OVERPI * ray.p1.mfLat_rad; // 重新初始化起点纬度
    alt_n = ray.p1.mfAlt_m; // 重新初始化起点高度

    // 计算精细搜索的起始偏移量
    float startOffset = float(minIdx + 1) - 0.75f;
    lon_n += lon_step * startOffset; // 更新经度
    lat_n += lat_step * startOffset; // 更新纬度
    alt_n += alt_step * startOffset; // 更新高度

    // 精细搜索7个点，找到更精确的最小间隙
    for (unsigned int n = 0; n < 7; n++)
    {
        // 处理经度越界情况
        lon_n = lon_n + 360 * (lon_n < -180) - 360 * (lon_n >= 180);

        // 获取当前位置的地形高度
        float terrain_m = mapData->GetTerrainHeight(lon_n, lat_n, ray.t_update);

        // 计算当前点与地形之间的间隙
        float clearance_m = alt_n - terrain_m;
        // 如果当前间隙小于最小间隙，则更新最小间隙
        if (clearance_m < minimumClearance_m)
        {
            minimumClearance_m = clearance_m;
        }

        // 更新下一步的经度、纬度和高度
        lon_n += 0.25f * lon_step;
        lat_n += 0.25f * lat_step;
        alt_n += 0.25f * alt_step;
    }

    // 更新射线数据中的地形间隙
    ray.terrainClearance_m = minimumClearance_m;
}


/**
*
*/
tcLOS::tcLOS()
: lastUpdateTime(0)
{
    mapData = tcMapData::Get();
}


/**
*
*/
tcLOS::~tcLOS() 
{
}
