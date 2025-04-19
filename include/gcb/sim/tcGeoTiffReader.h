
#pragma once
/**
* Class to read geotiff
*/
#include <geotiff.h>
#include <geotiffio.h>
#include <proj.h>
#include <tiffio.h>
#include <xtiffio.h>
#include <geo_normalize.h>
#include <iostream>
class tcGeoTiffReader
{
public:
    enum
    {
        MISSING_DATA_VAL = -32383
    };
    tcGeoTiffReader();
    ~tcGeoTiffReader();
    float GetTerrainHeight(double afLon_deg, double afLat_deg);

private:
    //使用libgeotiff读取高程
    TIFF *mTif ;
    GTIF *mGtif ;
    PJ *mTrans;
    //图片大小
    int mnWidth, mnHeight;
    double mA  ;  // 左上角地理坐标X
    double mC  ;  // 左上角地理坐标Y
    double mB ;   // 东西向像素分辨率
    double mD  ;  // 南北向像素分辨率（取负号，因为Y轴向下）
    uint32_t nTileWidth, nTileHeight;//瓦片大小

    unsigned short mnSampleFormat, mnSamplesPerPixel, mnBitsPerSample;


};


