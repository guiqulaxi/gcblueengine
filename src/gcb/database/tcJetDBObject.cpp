/*
**  @file tcJetDBObject.cpp
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

#include "tcJetDBObject.h"
#include "tcPlatformDBObject.h"
#include <sstream>
#include "tcAero.h"
#include "strutil.h"
#include <cassert>
#include "tcAeroAirObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

namespace database
{
double tcJetDBObject::rho_sealevel = 1.225; // must match atmosphere.csv
double tcJetDBObject::inv_rho_sealevel = 0.8163265; // must match atmosphere.csv

std::vector<float> tcJetDBObject::tableAltitudes;

/**
	* Static function to initialize common table of altitude points (in meters)
	* Must be called once before starting simulation
	*/
void tcJetDBObject::InitializeTableAltitudes()
{
    assert(tableAltitudes.size() == 0);
    tableAltitudes.clear();

    tableAltitudes.push_back(2000.0f);
    tableAltitudes.push_back(4000.0f);
    tableAltitudes.push_back(6000.0f);
    tableAltitudes.push_back(8000.0f);
    tableAltitudes.push_back(10000.0f);
    tableAltitudes.push_back(12000.0f);
    tableAltitudes.push_back(16000.0f);
    tableAltitudes.push_back(20000.0f);
    tableAltitudes.push_back(25000.0f);
    tableAltitudes.push_back(30000.0f);
}

/**
    * Calculate private parameters. Should be called after
    * object is loaded.
    */
void tcJetDBObject::CalculateParams()
{
    // invMachRange
    if (mfMsupm <= mfMcm) // 如果马赫数上限小于等于临界马赫数
    {
        mfMsupm = 1.005f*mfMcm; // 将马赫数上限设置为临界马赫数的1.005倍
    }

    if (mfMsupm > mfMcm) // 如果马赫数上限大于临界马赫数
    {
        invMachRange = 1.0f / (mfMsupm - mfMcm); // 计算马赫数范围的倒数
    }
    else // 如果马赫数上限不大于临界马赫数
    {
        invMachRange = 0; // 马赫数范围的倒数设为0
    }

    Cdi = 0.333333 * mfCdpsub * (rho_sealevel * rho_sealevel) * powf(cruiseSpeed_mps, 4.0f); // 计算阻力系数Cdi
}

/**
    * @return cruise speed in m/s
    */
float tcJetDBObject::GetCruiseSpeedForAltitude(float alt_m) const
{
    // 计算空气密度
    float rho = Aero::GetAirDensity(alt_m);
    // 计算声速
    float vmach_mps = Aero::GetSoundSpeed(alt_m);

    // 计算因子，用于调整巡航速度
    float factor = powf(inv_rho_sealevel * rho, -0.5f);

    // 计算调整后的巡航速度
    float speed_mps = factor * cruiseSpeed_mps;

    // 返回调整后的巡航速度与临界马赫数乘以声速的较小值
    return std::min(speed_mps, mfMcm*vmach_mps);
}

/**
    * @return stall speed in m/s
    */
float tcJetDBObject::GetStallSpeedForAltitude(float alt_m) const
{
    float rho = Aero::GetAirDensity(alt_m);

    float factor = powf(inv_rho_sealevel * rho, -0.5f);

    float speed_mps = factor * stallSpeed_mps;

    return speed_mps;
}

void tcJetDBObject::GetCruiseAndStallSpeeds(float alt_m, float& cruise_mps, float& stall_mps) const
{
    float rho = Aero::GetAirDensity(alt_m);
    float vmach_mps = Aero::GetSoundSpeed(alt_m);

    float factor = powf(inv_rho_sealevel * rho, -0.5f);

    cruise_mps = factor * cruiseSpeed_mps;
    cruise_mps = std::min(cruise_mps, mfMcm*vmach_mps);

    stall_mps = factor * stallSpeed_mps;
}

/**
    * @param vmach Speed divided by speed of sound (mach number)
    * @return interpolated parasitic drag coeff
    *
    *
    * 计算给定马赫数下的寄生阻力系数
    * @param vmach 马赫数（速度除以声速）
    * @return 插值后的寄生阻力系数
    */
float tcJetDBObject::GetParasiticDragCoefficient(float vmach) const
{
    float K_dp;  // 寄生阻力系数
    float mcrit = mfMcm; // 临界马赫数
    float msup = mfMsupm; // 跨音速区域的中点
    float mtran = 0.5f*(mcrit + msup); // 超音速区域的起始点

    if (vmach <= mcrit)
    {
        K_dp = mfCdpsub; // 阻力系数包括0.5倍的面积因子
    }
    else if (vmach >= msup)
    {
        K_dp = mfCdpsup;
    }
    else if (vmach <= mtran)
    {
        // 在跨音速区域内插值计算阻力系数
        K_dp = 2.0f * (vmach - mcrit) * (mfCdptran - mfCdpsub) * invMachRange
               + mfCdpsub;
    }
    else // (vmach > mtran)&&(vmach < msup)
    {
        // 在超音速区域内插值计算阻力系数
        K_dp = 2.0f * (msup - vmach) * (mfCdptran - mfCdpsup) * invMachRange
               + mfCdpsup;
    }
    return K_dp;
}
/**
    * Placed here to allow better thrust decay model to be incorporated into
    * database without affecting air model
    */
void tcJetDBObject::GetThrustAndEfficiencyFactors(float alt_m, float& thrustFactor, float& fuelEfficiencyFactor) const
{
    // 初始化推力因子和燃油效率因子为1.0
    thrustFactor = 1.0f;
    fuelEfficiencyFactor = 1.0f;

    // 获取海拔高度表的大小
    size_t nAlt = tableAltitudes.size();

    // 如果给定的海拔高度小于表中的第一个值
    if (alt_m < tableAltitudes[0])
    {
        // 计算alpha值
        float alpha = 0.0005f * alt_m;
        assert(tableAltitudes[0] == 2000.0f);
        assert(alpha <= 1.0f);

        // 假设在0米处的推力因子始终为1.0
        fuelEfficiencyFactor = (1.0f - alpha) + alpha * fuelEfficiencyTable[0];
        thrustFactor = (1.0f - alpha) + alpha * thrustTable[0];
        return;
    }
    // 如果给定的海拔高度大于等于表中的最后一个值
    if (alt_m >= tableAltitudes[nAlt-1])
    {
        // 直接使用表中的最后一组推力因子和燃油效率因子
        thrustFactor = thrustTable[nAlt-1];
        fuelEfficiencyFactor = fuelEfficiencyTable[nAlt-1];
        return;
    }

    // 在表中查找位置并进行线性插值计算推力因子和燃油效率因子
    for (size_t idx=1; idx<nAlt; idx++)
    {
        float alt_low = tableAltitudes[idx-1];
        float alt_high = tableAltitudes[idx];
        if (alt_m <= alt_high)
        {
            float low_weight = (alt_high - alt_m) / (alt_high - alt_low);
            float high_weight = 1.0f - low_weight;
            thrustFactor = low_weight * thrustTable[idx-1] + high_weight * thrustTable[idx];
            fuelEfficiencyFactor = low_weight * fuelEfficiencyTable[idx-1] +
                                   high_weight * fuelEfficiencyTable[idx];
            return;
        }
    }

    // 错误处理，表损坏
    assert(false);
}


/**
    * Version that only returns thrust factor
    *
    * @return thrust factor
    */
float tcJetDBObject::GetThrustFactor(float alt_m) const
{
    float thrustFactor = 1.0f; // 初始化推力因子为1.0

    size_t nAlt = tableAltitudes.size(); // 获取海拔高度表的大小

    // 如果给定的海拔高度小于表中的第一个值
    if (alt_m < tableAltitudes[0])
    {
        float alpha = 0.0005f * alt_m; // 计算alpha值
        assert(tableAltitudes[0] == 2000.0f); // 确保表中的第一个值为2000.0
        assert(alpha <= 1.0f); // 确保alpha值不大于1.0

        // 假设在0米处的推力因子始终为1.0
        thrustFactor = (1.0f - alpha) + alpha * thrustTable[0]; // 计算推力因子
        return thrustFactor; // 返回推力因子
    }

    // 如果给定的海拔高度大于等于表中的最后一个值
    if (alt_m >= tableAltitudes[nAlt-1])
    {
        thrustFactor = thrustTable[nAlt-1]; // 直接使用表中的最后一组推力因子
        return thrustFactor; // 返回推力因子
    }

    // 在表中查找位置并进行线性插值计算推力因子
    for (size_t idx=1; idx<nAlt; idx++)
    {
        float alt_low = tableAltitudes[idx-1]; // 获取较低的海拔高度
        float alt_high = tableAltitudes[idx]; // 获取较高的海拔高度
        if (alt_m <= alt_high)
        {
            float low_weight = (alt_high - alt_m) / (alt_high - alt_low); // 计算较低海拔高度的权重
            float high_weight = 1.0f - low_weight; // 计算较高海拔高度的权重
            thrustFactor = low_weight * thrustTable[idx-1] + high_weight * thrustTable[idx]; // 计算推力因子
            return thrustFactor; // 返回推力因子
        }
    }

    assert(false); // 错误处理，表损坏
    return thrustFactor; // 返回推力因子
}

/**
    * Version that only returns fuel efficiency factor
    * 
    * @param inv_ias_mps = (1.0 / indicated air speed in m/s), used for fuel efficiency penalty when below cruise IAS
    * @return fuel efficiency factor, lower means burns less fuel
    */
/**
 * 仅返回燃油效率因子的版本
 *
 * @param alt_m = 海拔高度（米）
 * @param inv_ias_mps = (1.0 / indicated air speed in m/s), 用于在低于巡航速度时计算燃油效率惩罚
 * @return 燃油效率因子，越低表示燃烧的燃料越少
 */
float tcJetDBObject::GetFuelEfficiencyFactor(float alt_m, float inv_ias_mps) const
{
    float fuelEfficiencyFactor = 1.0f; // 初始化燃油效率因子为1.0

    float cruise_penalty = cruiseSpeed_mps * inv_ias_mps; // 计算巡航速度惩罚

    cruise_penalty = std::max(cruise_penalty, 1.0f); // 确保巡航速度惩罚不小于1.0

    size_t nAlt = tableAltitudes.size(); // 获取海拔高度表的大小

    if (alt_m < tableAltitudes[0]) // 如果海拔高度小于表中的第一个值
    {
        float alpha = 0.0005f * alt_m; // 计算alpha值
        assert(tableAltitudes[0] == 2000.0f); // 确保表中的第一个值为2000.0
        assert(alpha <= 1.0f); // 确保alpha值不大于1.0

        // 假设海拔高度为0时，燃油效率因子始终为1.0
        fuelEfficiencyFactor = (1.0f - alpha) + alpha * fuelEfficiencyTable[0];
        return fuelEfficiencyFactor; // 返回燃油效率因子
    }

    if (alt_m >= tableAltitudes[nAlt-1]) // 如果海拔高度大于等于表中的最后一个值
    {
        fuelEfficiencyFactor = cruise_penalty * fuelEfficiencyTable[nAlt-1]; // 计算燃油效率因子
        return fuelEfficiencyFactor; // 返回燃油效率因子
    }

    // 在表中查找位置并进行线性插值计算燃油效率因子
    for (size_t idx=1; idx<nAlt; idx++)
    {
        float alt_low = tableAltitudes[idx-1]; // 获取较低的海拔高度
        float alt_high = tableAltitudes[idx]; // 获取较高的海拔高度
        if (alt_m <= alt_high)
        {
            float low_weight = (alt_high - alt_m) / (alt_high - alt_low); // 计算较低海拔高度的权重
            float high_weight = 1.0f - low_weight; // 计算较高海拔高度的权重

            fuelEfficiencyFactor = low_weight * fuelEfficiencyTable[idx-1] +
                                   high_weight * fuelEfficiencyTable[idx]; // 计算燃油效率因子
            fuelEfficiencyFactor *= cruise_penalty; // 应用巡航速度惩罚
            return fuelEfficiencyFactor; // 返回燃油效率因子
        }
    }

    assert(false); // 错误处理，表损坏
    return fuelEfficiencyFactor; // 返回燃油效率因子
}


float tcJetDBObject::GetInducedDragCoefficient() const
{
    return Cdi;
}

/**
    * Adds sql column definitions to columnString. This is used for
    * SQL create table command
    */
void tcJetDBObject::AddSqlColumns(std::string& columnString)
{
    tcAirDBObject::AddSqlColumns(columnString);

    columnString += ",";

    columnString += "MilitaryThrust_N number(8),";
    columnString += "MilitaryThrustSpeedSlope number(8),";
    columnString += "ABThrust_N number(8),";
    columnString += "ABThrustSpeedSlope number(8),";
    columnString += "ABFuelRate_kgps number(8),";
    columnString += "Cdpsub number(8),";
    columnString += "Cdptran number(8),";
    columnString += "Cdpsup number(8),";
    columnString += "Mcm number(8),";
    columnString += "Msupm number(8),";
    columnString += "CruiseSpeed_mps number(8),";
    columnString += "StallSpeed_mps number(8)";

    if (tableAltitudes.size() == 0)
    {
        InitializeTableAltitudes();
    }

    for (size_t idx=0; idx<tableAltitudes.size(); idx++)
    {
        std::string s;
        s=strutil::format(",T%d number(5)", int(0.001f*tableAltitudes[idx]));
        columnString += s.c_str();
    }

    for (size_t idx=0; idx<tableAltitudes.size(); idx++)
    {
        std::string s;
        s=strutil::format(",FE%d number(5)", int(0.001f*tableAltitudes[idx]));
        columnString += s.c_str();
    }

}

void tcJetDBObject::ReadSql(tcSqlReader& entry)
{
    tcAirDBObject::ReadSql(entry);

    militaryThrust_N = entry.GetDouble("MilitaryThrust_N");
    militaryThrustSpeedSlope = entry.GetDouble("MilitaryThrustSpeedSlope");
    mfAfterburnThrust_N = entry.GetDouble("ABThrust_N");
    abThrustSpeedSlope = entry.GetDouble("ABThrustSpeedSlope");
    mfAfterburnFuelRate_kgps = entry.GetDouble("ABFuelRate_kgps");
    mfCdpsub = entry.GetDouble("Cdpsub");
    mfCdptran = entry.GetDouble("Cdptran");
    mfCdpsup = entry.GetDouble("Cdpsup");
    mfMcm = entry.GetDouble("Mcm");
    mfMsupm = entry.GetDouble("Msupm");
    cruiseSpeed_mps = entry.GetDouble("CruiseSpeed_mps");
    stallSpeed_mps = entry.GetDouble("StallSpeed_mps");

    thrustTable.clear();
    for (size_t idx=0; idx<tableAltitudes.size(); idx++)
    {
        std::string s;
        s=strutil::format("T%d", int(0.001f*tableAltitudes[idx]));
        float thrustFactor = entry.GetDouble(s.c_str());
        thrustTable.push_back(thrustFactor);
    }

    fuelEfficiencyTable.clear();
    for (size_t idx=0; idx<tableAltitudes.size(); idx++)
    {
        std::string s;
        s=strutil::format("FE%d", int(0.001f*tableAltitudes[idx]));
        float fuelEfficiency = entry.GetDouble(s.c_str());
        fuelEfficiencyTable.push_back(fuelEfficiency);
    }


    CalculateParams();
}

void tcJetDBObject::WriteSql(std::string& valueString) const
{
    tcAirDBObject::WriteSql(valueString);

    std::stringstream s;

    s << ",";

    s << militaryThrust_N << ",";
    s << militaryThrustSpeedSlope << ",";
    s << mfAfterburnThrust_N << ",";
    s << abThrustSpeedSlope << ",";
    s << mfAfterburnFuelRate_kgps << ",";
    s << mfCdpsub << ",";
    s << mfCdptran << ",";
    s << mfCdpsup << ",";
    s << mfMcm << ",";
    s << mfMsupm << ",";
    s << cruiseSpeed_mps << ",";
    s << stallSpeed_mps;


    for (size_t idx=0; idx<tableAltitudes.size(); idx++)
    {
        s << ",";
        s << thrustTable[idx];
    }

    for (size_t idx=0; idx<fuelEfficiencyTable.size(); idx++)
    {
        s << ",";
        s << fuelEfficiencyTable[idx];
    }

    valueString += s.str();

}

void tcJetDBObject::WritePythonValue(std::string &valueString) const
{
    tcAirDBObject::WritePythonValue(valueString);
    valueString+="    "+std::string(mzClass.PyVarString())+".militaryThrust_N="+strutil::to_python_value(militaryThrust_N)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".militaryThrustSpeedSlope="+strutil::to_python_value(militaryThrustSpeedSlope)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfAfterburnThrust_N="+strutil::to_python_value(mfAfterburnThrust_N)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".abThrustSpeedSlope="+strutil::to_python_value(abThrustSpeedSlope)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfAfterburnFuelRate_kgps="+strutil::to_python_value(mfAfterburnFuelRate_kgps)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfCdpsub="+strutil::to_python_value(mfCdpsub)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfCdptran="+strutil::to_python_value(mfCdptran)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfCdpsup="+strutil::to_python_value(mfCdpsup)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfMcm="+strutil::to_python_value(mfMcm)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".mfMsupm="+strutil::to_python_value(mfMsupm)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".cruiseSpeed_mps="+strutil::to_python_value(cruiseSpeed_mps)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".stallSpeed_mps="+strutil::to_python_value(stallSpeed_mps)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".thrustTable="+strutil::to_python_value(thrustTable)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".fuelEfficiencyTable="+strutil::to_python_value(fuelEfficiencyTable)+"\n";
    valueString+="    "+std::string(mzClass.PyVarString())+".CalculateParams()"+"\n";

}

void tcJetDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObjec():\n";
    valueString+="    "+std::string(mzClass.PyVarString())+"=pygcb.tcJetDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    return "+std::string(mzClass.PyVarString())+"\n";;
}


tcJetDBObject::tcJetDBObject()
    : invMachRange(0)
{
    mnModelType = MTYPE_FIXEDWINGX;
    mnType = PTYPE_FIXEDWING; // functional classification

    if (tableAltitudes.size() == 0)
    {
        InitializeTableAltitudes();
    }
}

tcJetDBObject::tcJetDBObject(tcJetDBObject& obj)
    :   tcAirDBObject(obj),
    invMachRange(obj.invMachRange),
    Cdi(obj.Cdi),
    militaryThrust_N(obj.militaryThrust_N),
    militaryThrustSpeedSlope(obj.militaryThrustSpeedSlope),
    mfAfterburnThrust_N(obj.mfAfterburnThrust_N),
    abThrustSpeedSlope(obj.abThrustSpeedSlope),
    mfAfterburnFuelRate_kgps(obj.mfAfterburnFuelRate_kgps),
    mfCdpsub(obj.mfCdpsub),
    mfCdptran(obj.mfCdptran),
    mfCdpsup(obj.mfCdpsup),
    mfMcm(obj.mfMcm),
    mfMsupm(obj.mfMsupm),
    cruiseSpeed_mps(obj.cruiseSpeed_mps),
    stallSpeed_mps(obj.stallSpeed_mps)
{

    if (tableAltitudes.size() == 0)
    {
        InitializeTableAltitudes();
    }
}


tcJetDBObject::~tcJetDBObject()
{
}

tcGameObject* tcJetDBObject::CreateGameObject()
{
        return new tcAeroAirObject(this);
}


}
