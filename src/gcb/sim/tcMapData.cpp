/**  
**  @file tcMapData.cpp
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

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcMapData.h"
#include "aerror.h"
#include "math.h"
#include "tcFile.h"
#include "tcString.h"
#include "tcGeoTiffReader.h"
//#include "tcTexture2D.h"
//#include "tcTVEngine.h"
#include "tcTime.h"
#include "nsNav.h"
#include "strutil.h"
#include <cassert>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

using std::max;
using std::min;

tcMapData* tcMapData::Get()
{
	static tcMapData instance;

	return &instance;
}


/**
* returns coordinate near (lon,lat) within altitude range. If
* a random point cannot be found within the altitude range after
* the max number of attempts, the last point with an invalid altitude
* is returned.
* @param lon reference intitude in degrees
* @param lat ref latitude in deg
* @param r peak-to-peak random variation in deg for lon and lat
* @param minAlt minimum altitude in meters
* @param maxAlt maximum altitude in meters
*/
GeoPoint tcMapData::GetRandomPointNear(float lon, float lat, 
										 float r, float minAlt, float maxAlt)
{
	enum {MAX_TRIALS = 100};
	GeoPoint p;

	int trial = 0;
	float randomLon = 0;
	float randomLat = 0;
	float alt = 0;
	while (trial++ < MAX_TRIALS)
	{
		randomLon = lon + randfc(r);
		randomLat = lat + randfc(r);
		alt = GetTerrainHeight(randomLon, randomLat, 0);
		if ((alt >= minAlt)&&(alt <= maxAlt))
		{
			p.mfAlt_m = alt;
			p.mfLon_rad = C_PIOVER180*randomLon;
			p.mfLat_rad = C_PIOVER180*randomLat;
			return p;
		}
	}
	fprintf(stderr, "GetRandomPointNear couldn't find valid point. (%.2f,%.2f) [%.0f,%.0f] %f\n",
		lon,lat,minAlt,maxAlt,r);
	p.mfAlt_m = alt;
	p.mfLon_rad = C_PIOVER180*randomLon;
	p.mfLat_rad = C_PIOVER180*randomLat;
	return p;
}

bool tcMapData::GetFarthestClearPoint(float lon1_rad, float lat1_rad, float lon2_rad, float lat2_rad, float maxTerrain_m,
        double& lon_rad, double& lat_rad)
{
    float lonb_rad;
    float latb_rad;

    bool result = GetFarthestClearPoint(lon1_rad, lat1_rad, lon2_rad, lat2_rad, maxTerrain_m, lonb_rad, latb_rad);
    lon_rad = (double)lonb_rad;
    lat_rad = (double)latb_rad;
    return result;
}

/**
* Get farthest point (lon,lat) aint path from (lon1,lat1) to (lon2,lat2) such that path up to point has
* terrain less than maxTerrain_m at all points up to (lon,lat).
* Used for path finding
* @return true if clear aint entire path
*/
bool tcMapData::GetFarthestClearPoint(float lon1_rad, float lat1_rad, float lon2_rad, float lat2_rad, float maxTerrain_m,
        float& lon_rad, float& lat_rad)
{
    GeoPoint p1(lon1_rad, lat1_rad, 0);
    GeoPoint p2(lon2_rad, lat2_rad, 0);

    //float heading_rad = nsNav::GCHeadingApprox_rad(p1, p2);
    float dist_km = C_RADTOKM * nsNav::GCDistanceApprox_rad(p1, p2);

    size_t nSteps = size_t(ceilf(0.5f * dist_km));
    if (nSteps == 0)
    {
        lon_rad = lon2_rad;
        lat_rad = lat2_rad;
        return false;
    }
    
    float inv_nsteps = 1.0f / float(nSteps);

    float dlon_rad = lon2_rad - lon1_rad;
    if (dlon_rad > C_PI) dlon_rad -= C_TWOPI;
    if (dlon_rad < -C_PI) dlon_rad += C_TWOPI;
 
    float dlat_rad = lat2_rad - lat1_rad;


    float dlonCoarse_rad = dlon_rad * inv_nsteps;   
    float dlatCoarse_rad = dlat_rad * inv_nsteps;

    float dlonFine_rad = 0.125f * dlonCoarse_rad;
    float dlatFine_rad = 0.125f * dlatCoarse_rad;

    lon_rad = lon1_rad;
    lat_rad = lat1_rad;
    float lonTest_rad = lon_rad;
    float latTest_rad = lat_rad;

    float lonStep_rad = dlonFine_rad;
    float latStep_rad = dlatFine_rad;

    bool searching = true;
    unsigned int iterations = 0;
    while (searching && (iterations++ < 100000))
    {
        float terrain_m = GetTerrainHeightHighRes(C_180OVERPI*lonTest_rad, C_180OVERPI*latTest_rad);

        if (terrain_m < maxTerrain_m)
        {
            lon_rad = lonTest_rad;
            lat_rad = latTest_rad;
        }
        else
        {
            return false;
        }

        // set adaptive step size
        if (terrain_m < (maxTerrain_m - 15.0f))
        {
            lonStep_rad = dlonCoarse_rad;
            latStep_rad = dlatCoarse_rad;
        }
        else
        {
            lonStep_rad = dlonFine_rad;
            latStep_rad = dlatFine_rad;
        }

        lonTest_rad = lon_rad + lonStep_rad;
        latTest_rad = lat_rad + latStep_rad;

        if (lonStep_rad >= 0)
        {
            lonTest_rad = std::min(lonTest_rad, lon2_rad);
        }
        else
        {
            lonTest_rad = std::max(lonTest_rad, lon2_rad);
        }

        if (latStep_rad >= 0)
        {
            latTest_rad = std::min(latTest_rad, lat2_rad);
        }
        else
        {
            latTest_rad = std::max(latTest_rad, lat2_rad);
        }


        searching = (lon_rad != lon2_rad) && (lat_rad != lat2_rad);

    }

    // entire path is clear
    return true;
}


/**
* Uses the high res map to get the terrain height. This does
* not use the 0.5 x 0.5 tiles and will not load tiles to cache
* map data.
* @see tcMapData::GetTerrainHeight
* @see tcMapData::GetTerrainHeightLowRes
*
* @return terrain height based on high resolution world map
*/
float tcMapData::GetTerrainHeightHighRes(double afLon_deg, double afLat_deg) 
{
    return GetTerrainHeight(afLon_deg,afLat_deg,0);
}


/**
* @return terrain height based on low resolution world map
*/
float tcMapData::GetTerrainHeightLowRes(float afLon_deg, float afLat_deg) 
{
    return GetTerrainHeight(afLon_deg,afLat_deg,0);
}
/**
* Gets high resolution terrain height
* @see
*/
float tcMapData::GetTerrainHeight(double afLon_deg, double afLat_deg, double afStatusTime) 
{

    return mGeoTiffReader->GetTerrainHeight(afLon_deg,afLat_deg);
}



/********************************************************************/
/********************************************************************/




/********************************************************************/
void tcMapData::ReportMapDataError(UINT32 anError) 
{

	switch (anError) 
	{
	case ME_TILE_STRUCTURE:
		{
			static bool bReported = false;
			if (!bReported) 
			{
				fprintf(stderr, "MapData error: bad tile structure");
				bReported = true;
			}
		}
		break;
	case ME_GENERIC:
	default:
		{
			static bool bReported = false;
			if (!bReported) 
			{
				fprintf(stderr, "MapData error: generic");
				bReported = true;
			}
		}
		break;
	}
}

/********************************************************************/
tcMapData::tcMapData()
{
	mpOptions = NULL;
	tcString s;
	WTL(s.GetBuffer());
    mGeoTiffReader =new tcGeoTiffReader;
}
/********************************************************************/
tcMapData::~tcMapData() 
{

}
/********************************************************************/
