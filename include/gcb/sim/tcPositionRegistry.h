/**
**  @file tcPositionRegistry.h
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


#ifndef _POSITIONREGISTRY_H_
#define _POSITIONREGISTRY_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include <map>
#include <vector>

/**
* Provides fast lookup of platforms within region
*/
class tcPositionRegistry
{
public:
    std::vector<int>& GetAllWithinRegion(double lon_west, double lon_east, 
        double lat_south, double lat_north);
    void RemoveAll();
    void RemoveId(int id);
    void UpdatePosition(int id, double lon, double lat);

    tcPositionRegistry();
    ~tcPositionRegistry();

private:
    /// lookup of id map by bin location code
    std::map<int, std::map<int, bool> > positionMap;
    
    /// lookup for bin location by id
    std::map<int, int> entryLookup;
    
    const double pi;
    const double twopi;
    const double piovertwo;
    const double binWidth; ///< size of bin in radians
    double invBinWidth; ///< 1.0 / binWidth
    double nLatBins; ///< number of latitude bins from -90 S to 90 N
    
    void AddIdToBin(int id, int bin);
    void RemoveIdFromBin(int id, int bin);
    
    void AppendBinContents(std::vector<int>& v, int bin);
    void ConformLonLat(double& lon_west, double& lon_east, 
        double& lat_south, double& lat_north);
        
    int LatToIndex(double lat);
    int LonToIndex(double lon);       
    int LonLatToBinLocation(double lon, double lat);

    
};


















#endif