
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
#include <list>
#include <unordered_map>
#include <vector>




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
    //缓存 用于缓存
    void *mDataBuf;


    struct PairHash {
        size_t operator()(const std::pair<int, int>& p) const noexcept {
            return static_cast<size_t>(p.first) * 31 + p.second; // 更好的哈希组合方式
        }
    };
    class LRUCache {
    public:
        explicit LRUCache(size_t max_size) : max_size(max_size) {
            cache_map.reserve(max_size * 2);  // 预分配内存
        }

        bool Get(int x_tile, int y_tile, std::vector<float>& data) {
            auto key = std::make_pair(x_tile, y_tile);
            auto it = cache_map.find(key);
            if (it == cache_map.end()) return false;

            lru_list.splice(lru_list.begin(), lru_list, it->second.second);
            data = it->second.first;
            return true;
        }

        void Put(int x_tile, int y_tile, const std::vector<float>& data) {
            auto key = std::make_pair(x_tile, y_tile);

            if (auto it = cache_map.find(key); it != cache_map.end()) {
                lru_list.splice(lru_list.begin(), lru_list, it->second.second);
                it->second.first = data;
                return;
            }

            lru_list.emplace_front(key);
            cache_map[key] = {data, lru_list.begin()};

            if (cache_map.size() > max_size) {
                cache_map.erase(lru_list.back());
                lru_list.pop_back();
            }
        }

        void SetCapacity(size_t capacity) {
            max_size = capacity;
            while (cache_map.size() > max_size) {
                cache_map.erase(lru_list.back());
                lru_list.pop_back();
            }
        }

    private:
        size_t max_size;
        std::list<std::pair<int, int>> lru_list;
        std::unordered_map<
            std::pair<int, int>,
            std::pair<std::vector<float>, std::list<std::pair<int, int>>::iterator>,
            PairHash
            > cache_map;
    };

    LRUCache mCache;
};


