


#include "tcGeoTiffReader.h"
#include <cassert>
#include "strutil.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



void MyTIFFErrorHandler(const char* module, const char* fmt, va_list args) {
    // 格式化错误消息
    char buffer[1024];
    vsnprintf(buffer, sizeof(buffer), fmt, args);

    // 输出到标准错误（或日志文件）
    std::cerr << "[TIFF ERROR] Module: " << (module ? module : "unknown")
              << ", Message: " << buffer << std::endl;
}


tcGeoTiffReader::tcGeoTiffReader():
    mTif(NULL),
    mGtif(NULL),
    mTrans(NULL),
    mDataBuf(NULL),
    mCache(100)
{
    const char* file="maps/ETOPO_2022_v1_60s_N90W180_surface.tif";
    TIFFErrorHandler oldHandler = TIFFSetErrorHandler(MyTIFFErrorHandler);
    mTif = XTIFFOpen(file, "r");
    if (!mTif) {
        return ;
    }

    mGtif = GTIFNew(mTif);
    if (!mGtif) {
        GTIFFree(mGtif);
        XTIFFClose(mTif);
        mGtif=NULL;
        mTif=NULL;
        return  ;
    }
    TIFFGetField(mTif, TIFFTAG_SAMPLESPERPIXEL, &mnSamplesPerPixel);// 1: 无符号整数，2: 有符号整数，3: 浮点
    TIFFGetField(mTif, TIFFTAG_BITSPERSAMPLE, &mnBitsPerSample);
    TIFFGetField(mTif, TIFFTAG_SAMPLEFORMAT, &mnSampleFormat);

    if (mnSampleFormat != SAMPLEFORMAT_IEEEFP || mnBitsPerSample != 32 || mnSamplesPerPixel != 1) {
        GTIFFree(mGtif);
        XTIFFClose(mTif);
        mGtif=NULL;
        mTif=NULL;
        return  ;
    }

    TIFFGetField(mTif, TIFFTAG_TILEWIDTH, &nTileWidth);
    TIFFGetField(mTif, TIFFTAG_TILELENGTH, &nTileHeight);

    TIFFGetField(mTif, TIFFTAG_IMAGEWIDTH, &mnWidth);
    TIFFGetField(mTif, TIFFTAG_IMAGELENGTH, &mnHeight);

    short tiepointsize, pixscalesize;
    double* tiepoints;//[6];
    double* pixscale;//[3];
    if(!TIFFGetField(mTif, TIFFTAG_GEOTIEPOINTS,  &tiepointsize,
                      &tiepoints)||
        !TIFFGetField(mTif, TIFFTAG_GEOPIXELSCALE, &pixscalesize, &pixscale))
    {
        GTIFFree(mGtif);
        XTIFFClose(mTif);
        mGtif=NULL;
        mTif=NULL;
        return  ;
    }

    // 5. 计算经纬度对应的像素坐标
    mA = tiepoints[3];  // 左上角地理坐标X
    mC = tiepoints[4];  // 左上角地理坐标Y
    mB = pixscale[0];   // 东西向像素分辨率
    mD = -pixscale[1];  // 南北向像素分辨率（取负号，因为Y轴向下）

    // 3. 获取 GeoTIFF 定义
    GTIFDefn defn;
    if (!GTIFGetDefn(mGtif, &defn)) {
        std::cerr << "Could not parse GeoTIFF definition." << std::endl;
        GTIFFree(mGtif);
        XTIFFClose(mTif);
        mGtif=NULL;
        mTif=NULL;
        return  ;
    }

    // 4. 坐标转换（WGS84经纬度 -> 投影坐标系）
    char *target_crs = NULL;
    if (defn.Model == ModelTypeProjected && defn.PCS != KvUserDefined) {
        target_crs = (char *)malloc(16);
        snprintf(target_crs, 16, "EPSG:%d", defn.PCS);
    } else if (defn.Model == ModelTypeGeographic && defn.GCS != KvUserDefined) {
        target_crs = (char *)malloc(16);
        snprintf(target_crs, 16, "EPSG:%d", defn.GCS);
    } else {
        // 自定义坐标系处理（示例：UTM zone 50N）
        target_crs = "+proj=utm +zone=50 +north +datum=WGS84";
    }

    PJ_CONTEXT *ctx = proj_context_create();
    mTrans = proj_create_crs_to_crs(ctx, "EPSG:4326", target_crs, NULL);

    if (TIFFIsTiled(mTif)) {//块存储
         mDataBuf = _TIFFmalloc(TIFFTileSize(mTif));
    }
    else
    {
       mDataBuf = _TIFFmalloc(TIFFScanlineSize(mTif));
    }

}

tcGeoTiffReader::~tcGeoTiffReader()
{
    GTIFFree(mGtif);
    XTIFFClose(mTif);
    proj_destroy(mTrans);
    if(mDataBuf)
    {
        _TIFFfree(mDataBuf);
    }
}


float tcGeoTiffReader::GetTerrainHeight(double afLon_deg, double afLat_deg)
{

    PJ_COORD proj = proj_trans(mTrans, PJ_FWD, proj_coord(afLon_deg, afLat_deg, 0, 0));



    int x_pixel = (proj.xy.x - mA) / mB;
    int y_pixel = (proj.xy.y - mC) / mD;
    // 5. 读取数据
    double value=MISSING_DATA_VAL;
    if (TIFFIsTiled(mTif))
    {//块存储
        if(mnBitsPerSample == 32)
        {
            int x_tile = x_pixel / nTileWidth;
            int y_tile = y_pixel / nTileHeight;
            std::vector<float> tile_data;
            bool cache_hit = mCache.Get(x_tile, y_tile, tile_data);
            if (cache_hit)
            {
                uint32_t offset_x = x_pixel % nTileWidth;
                uint32_t offset_y = y_pixel % nTileHeight;
                value = tile_data[offset_y * nTileWidth + offset_x];
            }
            else
            {
                if (TIFFReadTile(mTif, mDataBuf, x_pixel, y_pixel, 0, 0) == -1) {
                    return MISSING_DATA_VAL;
                }
                size_t tile_size = nTileWidth * nTileHeight;
                tile_data.resize(tile_size);
                memcpy(tile_data.data(), mDataBuf, tile_size * sizeof(float));

                mCache.Put(x_tile, y_tile, tile_data);
                uint32_t offset_x = x_pixel % nTileWidth;
                uint32_t offset_y = y_pixel % nTileHeight;
                value = tile_data[offset_y * nTileWidth + offset_x];
            }

        }



        // TIFFReadTile(mTif, mDataBuf, x_pixel, y_pixel, 0, 0);
        // // TIFFReadTile(tif, buf1,x_pixel+1, y_pixel, 0, 0);//即使偏移buf也是一样的 因为是按块读取

        // if (mnBitsPerSample == 32) {

        //     float* floatData = (float*)mDataBuf;
        //     uint32_t offset_x = x_pixel % nTileWidth;
        //     uint32_t offset_y = y_pixel % nTileHeight;
        //     value = floatData[offset_y * nTileWidth + offset_x];

        //     // float* floatData1 = (float*)buf1;
        //     // float value1 = (floatData1)[offset_y * tile_width + offset_x];
        //     // int  a=0;
        //     // 处理32位浮点数据...

        // } else if (mnBitsPerSample == 64) {
        //     double* doubleData = (double*)mDataBuf;
        //     int a=0;
        //     // 处理64位浮点数据...
        // }
        // else if (mnBitsPerSample == 16) {
        //     uint16_t* shortData = (uint16_t*)mDataBuf;
        // }

        //读取所有
        // for (uint32_t y = 0; y < height; y += tileHeight) {
        //     for (uint32_t x = 0; x < width; x += tileWidth) {
        //         TIFFReadTile(tif, buf, x, y, 0, 0);
        //         if(y>=3437&&x>18042)
        //         {
        //             int a=0;
        //         }
        //         if (bitsPerSample == 32) {
        //             float* floatData = (float*)buf;
        //             int a=0;
        //             // 处理32位浮点数据...
        //         } else if (bitsPerSample == 64) {
        //             double* doubleData = (double*)buf;
        //             int a=0;
        //             // 处理64位浮点数据...
        //         }
        //         else if (bitsPerSample == 16) {
        //             uint16_t* shortData = (uint16_t*)buf;

        //         }

        //     }
        // }
    }
    else
    {
        for (int i = 0; i < mnHeight; i++) {
            if (TIFFReadScanline(mTif, mDataBuf, (unsigned int)i, 0) == -1) {
                return value;
            }

        }

    }
    return value;
}
