/**
**  @file tcAero.cpp
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

//#include "stdwx.h" // precompiled header file

#ifndef WX_PRECOMP
//#include "wx/wx.h"
#endif

#include "tcAero.h"
#include "tcMissileDBObject.h"
#include <cmath>
#include <fstream>
#include "common/tcStream.h"
#include "common/tcGameStream.h"
#include "strutil.h"
#include<iostream>
#include<cassert>
//#include "wx/textfile.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


std::vector<float> Aero::altitude_m;//高度
std::vector<float> Aero::rho_kgm3;//空气密度
std::vector<float> Aero::rho_relative;//空气相对密度（相对于海拔为0）
std::vector<float> Aero::c_mps;//声速
std::vector<float> Aero::T_K;//温度 开尔文
float Aero::inv_altitude_step_m = 1.0f;


/**
* Load state from stream
*/
tcStream& Aero::tsMissileKState::operator<<(tcStream& stream)
{
    stream >> mfFlightTime;
    //stream >> mfSpeed_mps;
    //stream >> mfGroundSpeed_mps;
    //stream >> mfPitch_rad;
    //stream >> mfHeading_rad;
    //stream >> mfAltitude_m;

    return stream;
}

/**
* Save state to stream
*/
tcStream& Aero::tsMissileKState::operator>>(tcStream& stream)
{
    stream << mfFlightTime;
    //stream << mfSpeed_mps;
    //stream << mfGroundSpeed_mps;
    //stream << mfPitch_rad;
    //stream << mfHeading_rad;
    //stream << mfAltitude_m;

    return stream;
}

/**
* Load state from stream
*/
tcGameStream& Aero::tsMissileKState::operator<<(tcGameStream& stream)
{
    stream >> mfFlightTime;
    stream >> mfSpeed_mps;
    stream >> mfGroundSpeed_mps;
    stream >> mfPitch_rad;
    stream >> mfHeading_rad;
    stream >> mfAltitude_m;

    return stream;
}

/**
* Save state to stream
*/
tcGameStream& Aero::tsMissileKState::operator>>(tcGameStream& stream)
{
    stream << mfFlightTime;
    stream << mfSpeed_mps;
    stream << mfGroundSpeed_mps;
    stream << mfPitch_rad;
    stream << mfHeading_rad;
    stream << mfAltitude_m;

    return stream;
}


void Aero::ClearTables()
{
    altitude_m.clear();
    rho_kgm3.clear();
    rho_relative.clear();
    c_mps.clear();
    T_K.clear();

    inv_altitude_step_m = 1.0f;
}

/**
* TODO look at replacing this with lookup table (or caching equation
* to table)
*/
float Aero::GetAirDensity(float alt_m) 
{
    size_t base_idx;
    float alpha = GetInterpolationParams(alt_m, base_idx);

    float density_kgm3 = (1.0f-alpha)*rho_kgm3[base_idx] + alpha*rho_kgm3[base_idx+1];

    return density_kgm3;
}

/**
* 获得指定海拔高度的想对空气密度
* @return air density relative to density at sea level
*/
float Aero::GetRelativeAirDensity(float alt_m) 
{
    size_t base_idx;
    float alpha = GetInterpolationParams(alt_m, base_idx);

    float densityRelative = (1.0f-alpha)*rho_relative[base_idx] + alpha*rho_relative[base_idx+1];

    return densityRelative;
}

/**
* @return alpha param and set base_idx such that interpolated_val = (1-alpha)*table[base_idx] + alpha*table[base_idx+1]
*/
float Aero::GetInterpolationParams(float alt_m, size_t& base_idx)
{
    float alpha = 0;
    alt_m = std::max(alt_m, 0.0f);

    float steps = inv_altitude_step_m * alt_m;
    size_t idx = size_t(steps);

    float steps_floor = float(idx);

    if ((idx + 1) < altitude_m.size())
    {
        base_idx = idx;
        alpha = steps - steps_floor;
    }
    else
    {
        base_idx = altitude_m.size() - 2;
        alpha = 1.0f;
    }

    return alpha;

}

/**
*
*/
float Aero::GetSoundSpeed(float alt_m) 
{
    size_t base_idx;
    float alpha = GetInterpolationParams(alt_m, base_idx);

    float soundSpeed_mps = (1.0f-alpha)*c_mps[base_idx] + alpha*c_mps[base_idx+1];

    return soundSpeed_mps;
}

/**
* Call once at startup to load atmosphere.csv table
*/
void Aero::LoadAtmosphereTable()
{
    ClearTables();


    std::ifstream file("database/atmosphere.csv"); // 打开名为example.txt的文件

    if (!file.is_open()) { // 检查文件是否成功打开
        std::cerr << "无法打开文件database/atmosphere.csv" << std::endl;
        return ;
    }

    std::string line;
    int n=0;
    while (std::getline(file, line))
    { // 使用getline函数读取文件中的每一行
        n++;
        if(n<=1) continue;//第一行不管
        auto datas=strutil::split(line,',');
        std::string s_alt = datas[0];
        std::string s_rho = datas[1];;
        std::string s_c =  datas[2];
        std::string s_T =  datas[3];;

        double val_altitude_m = 0;
        double val_rho_kgm3 = 0;
        double val_c_mps = 0;
        double val_T_K = 0;
        try{
            val_altitude_m=std::stod(s_alt);
            val_rho_kgm3=std::stod(s_rho);
            val_c_mps=std::stod(s_c);
            val_T_K=std::stod(s_T);


            altitude_m.push_back(val_altitude_m);
            rho_kgm3.push_back(val_rho_kgm3);
            c_mps.push_back(val_c_mps);
            T_K.push_back(val_T_K);
            rho_relative.push_back(val_rho_kgm3 / rho_kgm3[0]);

        }catch(...){
            std::string msg = strutil::format("Error in atmosphere table at line %d", n+1);
            std::cerr<<msg<<std::endl;
            file.close();
            return;
        }
    }


    //        if (!success)
    //        {
    //            std::string msg = strutil::format("Error in atmosphere table at line %d", n+1);
    //            //wxMessageBox(msg, "Data File Error");
    //            file.close();
    //            return;
    //        }


    //    std::ifstream inFile("database/atmosphere.csv");
    //    if (!inFile.good())
    //    {
    //        //wxMessageBox("Missing database/atmosphere.csv file", "File Missing");
    //        assert(false);
    //        return;
    //    }
    //    bool success = true;
    //    size_t nLines = inFile.GetLineCount(); // first line is header
    //    for (size_t n=1; n<nLines; n++)
    //    {
    //        std::string line = inFile.GetLine(n);

    //        std::string s_alt = line.BeforeFirst(',');
    //        line = line.AfterFirst(',');

    //        std::string s_rho = line.BeforeFirst(',');
    //        line = line.AfterFirst(',');

    //        std::string s_c = line.BeforeFirst(',');
    //        line = line.AfterFirst(',');

    //        std::string s_T = line;

    //        double val_altitude_m = 0;
    //        double val_rho_kgm3 = 0;
    //        double val_c_mps = 0;
    //        double val_T_K = 0;

    //        bool sucess1 = s_alt.ToDouble(&val_altitude_m);
    //        bool sucess2 = s_rho.ToDouble(&val_rho_kgm3);
    //        bool sucess3 = s_c.ToDouble(&val_c_mps);
    //        bool sucess4 = s_T.ToDouble(&val_T_K);
    //        success = success && sucess1 && sucess2 && sucess3 && sucess4;

    //        if (!success)
    //        {
    //            std::string msg = strutil::format("Error in atmosphere table at line %d", n+1);
    //            //wxMessageBox(msg, "Data File Error");
    //            inFile.Close();
    //            return;
    //        }

    //        altitude_m.push_back(val_altitude_m);
    //        rho_kgm3.push_back(val_rho_kgm3);
    //        c_mps.push_back(val_c_mps);
    //        T_K.push_back(val_T_K);

    //        rho_relative.push_back(val_rho_kgm3 / rho_kgm3[0]);

    //    }

    //    inFile.Close();


    file.close();
    float stepSize = altitude_m[1] - altitude_m[0];
    inv_altitude_step_m = 1.0f / stepSize;

    assert(altitude_m.size() > 20);
    if (altitude_m[0] != 0)
    {
        std::string msg = strutil::format("Atmosphere table must start with 0 m");
        //wxMessageBox(msg, "Data File Error");
        ClearTables();
        return;
    }

    for (size_t n=1; n<altitude_m.size(); n++)
    {
        float step_n = altitude_m[n]-altitude_m[n-1];
        if (fabsf(1.0f - (inv_altitude_step_m * step_n)) > 0.01f)
        {
            std::string msg = strutil::format("Atmosphere table must have uniform spacing in altitude");
            //wxMessageBox(msg, "Data File Error");
            ClearTables();
            return;
        }
    }
}



void Aero::UpdateMissileKState(tsMissileKState& k, const database::tcMissileDBObject *apMissileData, float afTimeStep)
{

    //rhv2: 密度与速度的平方的乘积，用于计算阻力。
    //vsound: 声速，根据给定的海拔高度计算。
    //vmach: 导弹的速度与声速的比值，用于判断导弹是否在亚音速、跨音速或超音速飞行。
    //mcrit, mtran, msup: 临界马赫数、过渡马赫数和超音速马赫数。
    //K_dp: 寄生阻力系数，根据导弹的速度和位置进行计算。
    float rhv2;
    float vmach, vsound, vz;
    float mcrit, mtran, msup, K_dp;
    float fDrag_N, fThrust_N;
    float fAccel_mps2;
    rhv2 = GetAirDensity(k.mfAltitude_m)*k.mfSpeed_mps*k.mfSpeed_mps;
    vsound = GetSoundSpeed(k.mfAltitude_m);//对应高度声速
    vmach = k.mfSpeed_mps/vsound;//速度转为马赫

    // parasitic drag coeff calculation
    mcrit = apMissileData->mfMcm; //
    msup = apMissileData->mfMsupm;//
    mtran = 0.5f*(mcrit + msup); // midpoint of transonic region


    if (vmach <= mcrit) {
        K_dp = apMissileData->mfCdpsub; // drag coeff includes 0.5*area factor
    }
    else if (vmach >= msup) {
        K_dp = apMissileData->mfCdpsup;
    }
    else if (vmach <= mtran) {
        K_dp = (vmach - mcrit)*(apMissileData->mfCdptran-apMissileData->mfCdpsub)/(mtran-mcrit)
                + apMissileData->mfCdpsub;
    }
    else { // (vmach > mtran)&&(vmach < msup)
        K_dp = (msup - vmach)*(apMissileData->mfCdptran-apMissileData->mfCdpsup)/(msup-mtran)
                + apMissileData->mfCdpsup;
    }

    fDrag_N = rhv2*K_dp;//阻力
    //   根据导弹的飞行时间决定推力。如果飞行时间在助推时间内，则使用助推推力；
    //   如果飞行时间在维持时间之内，则使用维持推力；否则推力为0。
    if (k.mfFlightTime <= apMissileData->mfBoostTime_s) {
        fThrust_N = apMissileData->mfBoostThrust_N;
    }
    else if (k.mfFlightTime <= (apMissileData->mfBoostTime_s + apMissileData->mfSustTime_s)) {
        fThrust_N = apMissileData->mfSustThrust_N;
    }
    else {
        fThrust_N = 0;
    }

    //k.mfPitch_rad = k.mfClimbControl; // +/- 1 radian
    //如果导弹有俯仰角，修正自身重量(质量)带来推力的影响
    if (k.mfPitch_rad != 0) {
        fThrust_N -= apMissileData->weight_kg*G_MPS2*sinf(k.mfPitch_rad);
    }

    fAccel_mps2 = apMissileData->invMass_kg * (fThrust_N - fDrag_N); // 计算加速度 removed divide 20091205
    k.mfSpeed_mps += fAccel_mps2*afTimeStep;
    k.mfGroundSpeed_mps = k.mfSpeed_mps*cosf(k.mfPitch_rad);//计算水平速度
    vz = k.mfSpeed_mps*sinf(k.mfPitch_rad);//计算垂直速度
    k.mfAltitude_m += vz*afTimeStep;//计算高度
    k.mfFlightTime += afTimeStep;//计算已经飞行的时间
}
