/**  
**  @file tcScenarioRandomizer.h
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

#ifndef _SCENARIORANDOMIZER_H_
#define _SCENARIORANDOMIZER_H_

#ifdef WIN32
#pragma once
#endif

#include <map>
#include <string>
#include <vector>
#include "tcRect.h"

/**
*
*/
namespace scriptinterface
{
// 前向声明 tcScenarioLogger 类
class tcScenarioLogger;

/**
     * 单例类，用于管理场景随机化数据。
     * 该类用于存储和管理场景中单位的随机化信息，包括随机位置模式和随机区域。
     */
class tcScenarioRandomizer
{
public:
    // 随机化信息结构体，用于存储每个单位的随机化配置
    struct RandInfo
    {
        // 随机位置模式枚举
        enum
        {
            NONE = 0, ///< 无随机位置模式
            BOX = 1   ///< 使用随机区域（矩形框）模式
        };
        int randomLocationMode; ///< 随机位置模式（NONE 或 BOX）
        float includeProbability; ///< 创建单位的概率（0 到 1 之间的值）
        std::vector<tcRect> randomBox; ///< 随机区域的矩形框列表
    };

    // 获取 tcScenarioRandomizer 单例实例
    static tcScenarioRandomizer* Get();

    // 获取指定单位的创建概率
    float GetIncludeProbability(const std::string& unit) const;

    // 设置指定单位的创建概率
    void SetIncludeProbability(const std::string& unit, float prob);

    // 获取指定单位的随机区域矩形框列表
    std::vector<tcRect> GetRandomBoxes(const std::string& unit) const;

    // 为指定单位添加一个随机区域矩形框
    void AddRandomBox(const std::string& unit, const tcRect& box);

    // 更新指定单位的随机区域矩形框
    void UpdateRandomBox(const std::string& unit, const tcRect& boxPrev, const tcRect& boxNew);

    // 删除指定单位的某个随机区域矩形框
    void DeleteRandomBox(const std::string& unit, const tcRect& box);

    // 删除指定单位的所有随机区域矩形框
    void DeleteAllRandomBoxes(const std::string& unit);

    // 检查指定单位的某个随机区域矩形框是否存在
    bool RandomBoxExists(const std::string& unit, const tcRect& box) const;

    // 重命名单位（更新随机化信息中的单位名称）
    void RenameUnit(const std::string& nameOld, const std::string& nameNew);

    // 删除指定单位的随机化信息
    void DeleteUnit(const std::string& unit);

    // 清除所有随机化信息
    void Clear();

    // 将随机化信息保存到 Python 脚本中
    void SaveToPython(scriptinterface::tcScenarioLogger& logger);

private:
    // 构造函数（私有，确保单例模式）
    tcScenarioRandomizer();

    // 析构函数（私有，确保单例模式）
    ~tcScenarioRandomizer();

    // 存储所有单位的随机化信息（单位名称 -> RandInfo）
    std::map<std::string, RandInfo> randomInfo;
};
}
#endif

