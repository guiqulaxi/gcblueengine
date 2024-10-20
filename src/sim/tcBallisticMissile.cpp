/**
**  @file tcBallisticMissile.cpp
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
#include "tcBallisticMissile.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcGameStream.h"
#include "database/tcPlatformDBObject.h"

////#include "tc3DModel.h"
//#include "tcParticleEffect.h"
#include "tcLauncher.h"
#include "tcSimState.h"
#include "tc3DPoint.h"
#include "tcSubObject.h"
#include "tcTorpedoObject.h"
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define IGNORE_GOAL_ALTITUDE -999.0f

/**
* Load state from update stream
*/
tcUpdateStream& tcBallisticMissile::operator<<(tcUpdateStream& stream)
{
	tcWeaponObject::operator<<(stream);

	return stream;
}

/**
* Save state to update stream
*/
tcUpdateStream& tcBallisticMissile::operator>>(tcUpdateStream& stream)
{
	tcWeaponObject::operator>>(stream);

	return stream;
}




/**
* Load state from game stream
*/
tcGameStream& tcBallisticMissile::operator<<(tcGameStream& stream)
{
	tcWeaponObject::operator<<(stream);

    stream >> subSurfaceLaunch;

    stream >> lastGuidanceUpdateTime;
    stream >> guidanceUpdateInterval;
    stream >> flightTime_s;
    stream >> thrustShutoffTime_s;

    targetDatum << stream;

    stream >> x;
    stream >> y;
    stream >> z;
    stream >> vx;
    stream >> vy;
    stream >> vz;
    stream >> xt;
    stream >> yt;
    stream >> zt;
    stream >> rt;

    stream >> gx;
    stream >> gy;
    stream >> gz;

    stream >> speed_mps;
    stream >> speed2_mps2;
    stream >> r_ecef;

    stream.ReadCheckValue(6223);

	return stream;
}

/**
* Save state to game stream
*/
tcGameStream& tcBallisticMissile::operator>>(tcGameStream& stream)
{
	tcWeaponObject::operator>>(stream);

    stream << subSurfaceLaunch;

    stream << lastGuidanceUpdateTime;
    stream << guidanceUpdateInterval;
    stream << flightTime_s;
    stream << thrustShutoffTime_s;

    targetDatum >> stream;

    stream << x;
    stream << y;
    stream << z;
    stream << vx;
    stream << vy;
    stream << vz;
    stream << xt;
    stream << yt;
    stream << zt;
    stream << rt;

    stream << gx;
    stream << gy;
    stream << gz;

    stream << speed_mps;
    stream << speed2_mps2;
    stream << r_ecef;

    stream.WriteCheckValue(6223);

	return stream;
}




/**
* Initializes missile state for launch from game object.
* Adds self to simulation
*
* @param obj launching game object
* @param launcher index of launcher
*/
void tcBallisticMissile::LaunchFrom(tcGameObject* obj, unsigned nLauncher)
{
    tcLauncher virtualLauncher; // for missile deployment
	tcLauncher* pLauncher = &virtualLauncher;

    if (tcPlatformObject* platObj = dynamic_cast<tcPlatformObject*>(obj))
	{
		tc3DPoint launcherPos = platObj->mpDBObject->GetLauncherPosition(nLauncher);
		GeoPoint pos = obj->RelPosToLatLonAlt(launcherPos.x, launcherPos.y,
			launcherPos.z);
		mcKin.mfLon_rad = pos.mfLon_rad;
		mcKin.mfLat_rad = pos.mfLat_rad;
		mcKin.mfAlt_m = pos.mfAlt_m;
        if (tcSubObject* sub = dynamic_cast<tcSubObject*>(obj))
        {
            subSurfaceLaunch = true;
        }

        pLauncher = obj->GetLauncher(nLauncher);
	}
	else
	{
        fprintf(stderr, "tcBallisticMissile::LaunchFrom - Bad launch platform type\n");
        return;
	}

	mcKin.mfSpeed_kts = C_MPSTOKTS * mpDBObject->launchSpeed_mps;
	mcKin.mfHeading_rad = obj->mcKin.mfHeading_rad + pLauncher->pointingAngle;
	mcKin.mfPitch_rad = obj->mcKin.mfPitch_rad + pLauncher->GetPointingElevation();
	mcKin.mfClimbAngle_rad = mcKin.mfPitch_rad;

    CalculateECEF();

    // calculate target ECEF coordinates
    targetDatum = pLauncher->msDatum;
    const double Rearth_m = double(C_REARTHM);
    rt = Rearth_m + targetDatum.mfAlt_m;
    zt = rt * sin(targetDatum.mfLat_rad);
    double R_cos_lat = rt * cos(targetDatum.mfLat_rad);
    xt = R_cos_lat * cos(targetDatum.mfLon_rad);
    yt = R_cos_lat * sin(targetDatum.mfLon_rad);

    thrustShutoffTime_s = mpDBObject->thrustShutoffTime_s; // start with full thrust profile

	mfStatusTime = obj->mfStatusTime;


    std::string s = strutil::format("BM %d-%d", obj->mnID, launchedCounter++);
  
	/* Workaround, for some reason duplicate names were appearing with missiles
	** despite statistical unlikelihood. E.g. Missile 11-133 showed up three times!?
	** Changed from 3 to 4 digit random suffix and added test and second chance to 
	** get a unique object name.
	*/
	if (simState->GetObjectByName(s))
	{
        assert(false); // checkpoint to see if this ever happens
        launchedCounter += 1000;
        s = strutil::format("BM %d-%d", obj->mnID, launchedCounter++);
	}

    mzUnit = s.c_str();   

	SetAlliance(obj->GetAlliance());     

	simState->AddPlatform(static_cast<tcGameObject*>(this));

	// Set intended target (has to be done after alliance and id is set).
	// This is a tcWeaponObject method
	SetIntendedTarget(pLauncher->mnTargetID);

}



/**
*
*/
void tcBallisticMissile::Update(double t)
{
	float dt_s = (float)(t - mfStatusTime);

	assert(mpDBObject != NULL);
    
    if (subSurfaceLaunch)
    {
        UpdateSubsurface(t);
        return;
    }
   
	mfStatusTime = t;

    if (!clientMode)
    {
        UpdateGuidance(t);

        UpdateFlight(dt_s);

        //UpdateEffects();

        //Update3D();
    }
    else // MP client mode
    {
        UpdateFlight(dt_s);
        //UpdateEffects();
        //Update3D();
        return;
    }


    guidanceUpdateInterval = (flightTime_s < (thrustShutoffTime_s - 1.0f)) ? 1.0f : 0.01f;

    

    UpdateDetonation();

    

	/*** check for crash ***/
    bool underWater = (mcKin.mfAlt_m <= 0.0f);
    bool seaSurfaceCrash = (!subSurfaceLaunch) && underWater;

    // clear subSurfaceLaunch once weapon breaks surface
    if (!underWater) subSurfaceLaunch = false;


	if ((mcTerrain.mfHeight_m >= mcKin.mfAlt_m) || seaSurfaceCrash || payloadDeployed)
    {
        ApplyGeneralDamage(1.0f, 0);

        if (!payloadDeployed)
        {
            tcString s;
            s.Format("Object %s crashed at time %.1f lon %.3f, lat %.3f",
                mzUnit.c_str(), t, mcKin.mfLon_rad*C_180OVERPI, mcKin.mfLat_rad*C_180OVERPI);
            WTL(s.GetBuffer());
        }
	}


}
/**
 * @brief 在水下以2m/s，角度1.55（89度）上浮
 * @param t
 */
void tcBallisticMissile::UpdateSubsurface(double t)
{
    // 确保导弹是在水下发射的
    assert(subSurfaceLaunch);

    // 计算从上一次状态更新到现在的时间差（秒）
    float dt_s = (float)(t - mfStatusTime);

    // 将速度从节（kts）转换为米每秒（mps），C_KTSTOMPS是节到米每秒的转换常数
    float speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts;

    // alpha是一个随时间变化的因子，用于平滑过渡速度
    float alpha = dt_s;
    // 将速度平滑过渡到2米每秒
    speed_mps = (1-alpha)*speed_mps + alpha*2.0f;
    // 将速度从米每秒转换回节
    mcKin.mfSpeed_kts = speed_mps*(float)C_MPSTOKTS;

    // 将爬升角度平滑过渡到1.55弧度（约89度），表示导弹接近垂直向上
    mcKin.mfClimbAngle_rad = (1-alpha)*mcKin.mfClimbAngle_rad + alpha*1.55f;
    // 俯仰角与爬升角相同
    mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;

    // 获取导弹当前的航向角（弧度）
    float heading_rad = mcKin.mfHeading_rad;

    // 计算导弹在这段时间内移动的距离（米）
    float distance_m = speed_mps * dt_s;
    // 将距离转换为弧度，用于后续计算经纬度变化，C_MTORAD是米到弧度的转换常数
    double distance_rad = (double)distance_m * C_MTORAD;
    // 更新经度，考虑纬度的余弦修正，因为地球表面在纬度方向上的长度随纬度变化?????
    mcKin.mfLon_rad += distance_rad*(double)(sinf(heading_rad)/cosf((float)mcKin.mfLat_rad));
    // 更新纬度
    mcKin.mfLat_rad += distance_rad*(double)cosf(heading_rad);
    // 更新高度，考虑爬升角度
    mcKin.mfAlt_m += distance_m * sinf(mcKin.mfClimbAngle_rad);

    // 处理经度越过极点的情况
    HandlePoleWrap();

    // 判断导弹是否仍在水下
    bool underWater = (mcKin.mfAlt_m <= 0.0f);

    // 如果导弹已经浮出水面，则清除subSurfaceLaunch标志，并执行相关操作
    if (!underWater)
    {
        // 计算导弹在地球中心地固坐标系（ECEF）中的位置
        CalculateECEF();
        // 清除水下发射标志
        subSurfaceLaunch = false;
    }

    // 更新上一次状态更新的时间
    mfStatusTime = t;

    // 以下两行代码被注释掉，可能是因为它们在当前上下文中不是必需的或需要进一步优化
    // UpdateEffects(); // 更新导弹的视觉效果
    // Update3D(); // 更新导弹的3D模型
}


void tcBallisticMissile::UpdateDetonation()
{    
    const float tminDet_s = 0.05f;

    if ((mcKin.mfClimbAngle_rad > 0) || (mcKin.mfAlt_m > 30e3)) return;

    float terrainHeight_m = std::max(mcTerrain.mfHeight_m, 0.0f);
    // interpret detonation range parameter as altitude of detonation
    // if payloadClass is non-empty then use this altitude to deploy payload

    float triggerAlt_m = mpDBObject->detonationRange_m;

    float dz_m = mcKin.mfAlt_m - (terrainHeight_m + triggerAlt_m); // height above ground or sea level

    float vz_mps = C_KTSTOMPS * sinf(mcKin.mfClimbAngle_rad) * mcKin.mfSpeed_kts;

    float dt_impact = -dz_m / vz_mps;//计算导弹到达地面或海平面所需的时间。

    if (dt_impact > tminDet_s) return; // defer to future time step

    if (mpDBObject->payloadClass.size() == 0)
    {
        Detonate(dt_impact);
    }
    else
    {
        DeployPayload();
    }
}


//void tcBallisticMissile::UpdateEffects()
//{
////	if (model)
////	{
////        if (mcKin.mfAlt_m > 0)
////        {
////		    model->SetSmokeMode(tc3DModel::MISSILE);
////        }
////        else
////        {
////            model->SetSmokeMode(tc3DModel::BUBBLES);
////        }
////		model->UpdateEffects();
////	}
//}



void tcBallisticMissile::UpdateFlight(float dt_s)
{
    // 如果时间增量小于等于0，则直接返回，不进行更新
    if (dt_s <= 0) return;

    // 根据飞行时间确定当前所处的飞行阶段
    float t1 = mpDBObject->timeStage1_s; // 第一阶段时间
    float t2 = t1 + mpDBObject->timeStage2_s; // 第二阶段时间
    float t3 = t2 + mpDBObject->timeStage3_s; // 第三阶段时间
    float t4 = t3 + mpDBObject->timeStage4_s; // 第四阶段时间

    // 通过比较飞行时间与各阶段时间来确定当前阶段
    // 使用了一种巧妙的整数运算方式来确定阶段编号
    int stage = int(flightTime_s < t1) * int(1) +
                int((flightTime_s >= t1) && (flightTime_s < t2)) * int(2) +
                int((flightTime_s >= t2) && (flightTime_s < t3)) * int(3) +
                int((flightTime_s >= t3) && (flightTime_s < t4)) * int(4) +
                int(flightTime_s >= t4) * int(5);
    // 确保阶段编号在有效范围内
    assert((stage >= 1) && (stage <= 5));

    // 更新总飞行时间
    flightTime_s += dt_s;

    // 根据飞行阶段计算推力加速度和弹道系数倒数
    float thrustAccel_mps2 = 0; // 推力加速度
    float invBC = 0; // 弹道系数倒数
    switch (stage)
    {
    case 1:
        thrustAccel_mps2 = mpDBObject->accelStage1_mps2;
        invBC = mpDBObject->inv_bcStage1;
        break;
    case 2:
        thrustAccel_mps2 = mpDBObject->accelStage2_mps2;
        invBC = mpDBObject->inv_bcStage2;
        break;
    case 3:
        thrustAccel_mps2 = mpDBObject->accelStage3_mps2;
        invBC = mpDBObject->inv_bcStage3;
        break;
    case 4:
        thrustAccel_mps2 = mpDBObject->accelStage4_mps2;
        invBC = mpDBObject->inv_bcStage4;
        break;
    default:
        thrustAccel_mps2 = 0;
        invBC = mpDBObject->inv_bcStage4; // 假设第五阶段（如果有）使用第四阶段的弹道系数倒数
        break;
    }

    // 假设speed_mps（速度）和speed2_mps2（速度的平方）是有效的

    // 如果存在推力加速度，则进行以下计算
    if (thrustAccel_mps2 > 0)
    {
        // 应用“导向”来调整ECEF速度向量的方向，受最大过载限制
        // 可能使用旋转会更优，但这里采用另一种方式
        float dvx = speed_mps*gx - vx; // x方向速度变化量（考虑重力分量）
        float dvy = speed_mps*gy - vy; // y方向速度变化量
        float dvz = speed_mps*gz - vz; // z方向速度变化量

        // 移除与速度方向相同的分量，得到垂直分量
        float a_proj = (dvx*vx + dvy*vy + dvz*vz) / speed2_mps2;
        dvx -= a_proj*vx;
        dvy -= a_proj*vy;
        dvz -= a_proj*vz;

        // 计算速度变化量的模
        float dv = sqrtf(dvx*dvx + dvy*dvy + dvz*dvz);
        // 计算允许的最大速度变化量
        float max_dv = dt_s * C_G * mpDBObject->gmax; // C_G可能是重力加速度到推力加速度的转换系数

        // 在推力关闭前一秒允许完美导向（作弊）
        bool allowPerfectSteering = (flightTime_s > (thrustShutoffTime_s - 1.0f));
        // 如果速度变化量超过限制且不允许完美导向，则进行限制
        if ((dv > max_dv) && (!allowPerfectSteering))
        {
            float a_limit = (max_dv / dv);
            dvx *= a_limit;
            dvy *= a_limit;
            dvz *= a_limit;
        }

        // 更新速度分量
        vx += dvx;
        vy += dvy;
        vz += dvz;
    }

    // 根据弹道系数、高度和速度计算阻力加速度
    float rhov2 = Aero::GetAirDensity(mcKin.mfAlt_m) * speed2_mps2; // 空气密度与速度平方的乘积
    float dragAccel_mps2 = (stage < 5) ? rhov2 * invBC : 0; // 如果不是最终阶段，则计算阻力加速度

    // 如果推力已经关闭，则推力加速度为0
    thrustAccel_mps2 = (flightTime_s > thrustShutoffTime_s) ? 0 : thrustAccel_mps2;

    // 更新速度
    speed_mps += dt_s * (thrustAccel_mps2 - dragAccel_mps2); // 考虑推力和阻力加速度

    // 调整速度向量的模以匹配更新后的速度，同时去除导向带来的微小速度变化
    float a_rescale = speed_mps / sqrtf(vx*vx + vy*vy + vz*vz);
    vx *= a_rescale;
    vy *= a_rescale;
    vz *= a_rescale;

    // 应用重力加速度
    float a_grav = dt_s * C_GM / (r_ecef * r_ecef * r_ecef); // C_GM可能是地球引力常数与质量的乘积
    vx -= a_grav * x; // 更新x方向速度
    vy -= a_grav * y; // 更新y方向速度
    vz -= a_grav * z; // 更新z方向速度

    // 更新速度的平方和速度本身
    speed2_mps2 = vx*vx + vy*vy + vz*vz;
    speed_mps = sqrtf(speed2_mps2);

    // 根据速度更新导弹位置
    x += dt_s * vx;
    y += dt_s * vy;
    z += dt_s * vz;

    // 更新导弹到地心的距离
    r_ecef = sqrt(x*x + y*y + z*z);

    // 根据ECEF坐标更新经纬度高度（LLA）
    CalculateLLA();

    // 如果尚未检查过故障且导弹处于第三阶段或之后，则进行故障检查
    if (!tcWeaponObject::malfunctionChecked && (stage >= 3))
    {
        MalfunctionCheck(); // 调用基类中的故障检查函数
    }

}


/**
 * 更新导弹的目标航向和俯仰控制
 */
void tcBallisticMissile::UpdateGuidance(double t)
{
    // 如果当前时间与上次更新指导的时间之差小于指导更新间隔，则直接返回
    if ((t - lastGuidanceUpdateTime) < guidanceUpdateInterval)
    {
        return;
    }
    // 更新上次指导更新的时间
    lastGuidanceUpdateTime = t;

    // 计算目标位置与导弹当前位置在ECEF坐标系下的差值（x, y, z方向）
    float dx = float(xt - x);
    float dy = float(yt - y);
    float dz = float(zt - z);

    // 初始化东、北、上方向的差值变量
    float ke = 0;
    float kn = 0;
    float ku = 0;
    // 将ECEF坐标系下的差值转换为ENU（东-北-天）坐标系下的差值
    Ecef2enu(mcKin.mfLat_rad, mcKin.mfLon_rad, dx, dy, dz, ke, kn, ku); // 指向目标数据的ENU向量

    // 仅保留东-北分量，并将其归一化为1
    float ken_norm = sqrtf(ke*ke + kn*kn);
    float inv_ken_norm = 1.0f / ken_norm;
    ke *= inv_ken_norm;
    kn *= inv_ken_norm;
    ku = 0; // 将上方向分量置为0

    // 如果飞行时间小于30秒，则采用特定的爬升角度和速度比例
    if (flightTime_s < 30.0f)
    {
        ku = 0.98544973f; // 约80度的爬升角
        ke *= 0.1700f; // 东方向速度比例
        kn *= 0.1700f; // 北方向速度比例

        // 将ENU坐标系下的速度分量转换为ECEF坐标系下的速度分量
        Enu2ecef(mcKin.mfLat_rad, mcKin.mfLon_rad, ke, kn, ku, gx, gy, gz);
        return;
    }

    // 以下代码块用于计算导弹在二维u-v平面上的投影和相关参数
    // 计算导弹到目标的直线距离
    double dst = sqrt((xt-x)*(xt-x)+ (yt-y)*(yt-y) + (zt-z)*(zt-z));

    // 计算导弹与目标的连线与导弹当前位置的切线之间的夹角（余弦值和正弦值）
    double cos_gamma_rad = (r_ecef*r_ecef + rt*rt - dst*dst) / (2*r_ecef*rt);
    double sin_gamma_rad = sqrt(1 - cos_gamma_rad*cos_gamma_rad);
    // 导弹当前位置的u-v坐标
    float us = r_ecef;
    float vs = 0;
    // 目标位置的u-v坐标
    float ut = rt * cos_gamma_rad;
    float vt = rt * sin_gamma_rad;

    // 计算与导弹当前位置相关的轨道半长轴
    float two_over_r = 2.0f / r_ecef;
    float a_orbit = 1.0f / (two_over_r - (speed2_mps2 * C_GMINV)); // 轨道椭圆的半长轴

    // 计算第二焦点的u-v坐标
    float uf;
    float vf;
    CalculateSecondFocus(us, vs, ut, vt, a_orbit, uf, vf);

    // 计算导弹当前位置、第二焦点和目标位置之间的距离
    float aa2 = us*us + vs*vs;
    float aa = sqrtf(aa2);  // 导弹当前位置到原点的距离
    float bb2 = (us-uf)*(us-uf) + (vs-vf)*(vs-vf);
    float bb = sqrtf(bb2); // 第二焦点到导弹当前位置的距离
    float cc2 = uf*uf + vf*vf; // 第二焦点到原点的距离的平方（未直接使用）

    // 计算导弹爬升角（在局部LLA框架中）的余弦值
    float acos_arg = (aa2 + bb2 - cc2) / (2*aa*bb);
    // 如果余弦值的参数在有效范围内，则计算爬升角
    if ((acos_arg >= -1.0f) && (acos_arg <= 1.0f))
    {
        float beta_rad = 0.5f * acosf((aa2 + bb2 - cc2) / (2*aa*bb)); // 爬升角的一半

        float cos_beta = cosf(beta_rad); // 爬升角的余弦值
        float sin_beta = sinf(beta_rad); // 爬升角的正弦值

        ku = sin_beta; // 更新上方向的速度分量
        ke *= cos_beta; // 更新东方向的速度分量
        kn *= cos_beta; // 更新北方向的速度分量
    }
    else
    {
        // 如果参数无效，则采用默认的45度爬升角
        ku = 0.707107f; // 45度爬升角的正弦值
        ke *= 0.707107f; // 东方向速度比例
        kn *= 0.707107f; // 北方向速度比例
    }

    // 将ENU坐标系下的速度分量转换为ECEF坐标系下的速度分量
    Enu2ecef(mcKin.mfLat_rad, mcKin.mfLon_rad, ke, kn, ku, gx, gy, gz);

    // 如果导弹速度足够大，能够舒适地到达目标，则提前关闭推力，以减少飞行时间
    float a_orbit_min = 0.25*(dst + r_ecef +  rt); // 计算最小轨道半长轴
    float min_speed_mps = sqrtf(C_GM * (two_over_r - (1.0f/a_orbit_min))); // 计算达到最小轨道所需的最小速度
    if (speed_mps > (min_speed_mps + 300.0f)) // 如果当前速度大于最小速度加上一个安全余量
    {
        thrustShutoffTime_s = std::min(thrustShutoffTime_s, flightTime_s + 2.0f); // 更新推力关闭时间
    }

}

/**
* Update ECEF parameters based on mcKin
*/
void tcBallisticMissile::CalculateECEF()
{
    const double Rearth_m = double(C_REARTHM);
    r_ecef = Rearth_m + double(mcKin.mfAlt_m);

    z = r_ecef * sin(mcKin.mfLat_rad);
    double R_cos_lat = r_ecef * cos(mcKin.mfLat_rad);
    x = R_cos_lat * cos(mcKin.mfLon_rad);
    y = R_cos_lat * sin(mcKin.mfLon_rad);

    speed_mps = C_KTSTOMPS * mcKin.mfSpeed_kts;
    speed2_mps2 = speed_mps * speed_mps;

    float vu = speed_mps * sinf(mcKin.mfClimbAngle_rad);//垂直速度
    float vh = speed_mps * cosf(mcKin.mfClimbAngle_rad);//水平速度
    float ve = vh * sinf(mcKin.mfHeading_rad);//东速度
    float vn = vh * cosf(mcKin.mfHeading_rad);//北速度

    Enu2ecef(mcKin.mfLat_rad, mcKin.mfLon_rad, ve, vn, vu, vx, vy, vz);
}

/**
* Update mcKin based on ECEF parameters
*/
void tcBallisticMissile::CalculateLLA()
{
    const double Rearth_m = double(C_REARTHM);

    mcKin.mfLat_rad = asin(z / r_ecef);
    mcKin.mfLon_rad = atan2(y, x);
    mcKin.mfAlt_m = float(r_ecef - Rearth_m);


    mcKin.mfSpeed_kts = C_MPSTOKTS * speed_mps;

    float ve = 0;
    float vn = 0;
    float vu = 0;
    Ecef2enu(mcKin.mfLat_rad, mcKin.mfLon_rad, vx, vy, vz, ve, vn, vu);

    mcKin.mfHeading_rad = atan2(ve, vn);
    mcKin.mfClimbAngle_rad = asin(vu / speed_mps);
    mcKin.mfPitch_rad = mcKin.mfClimbAngle_rad;
}

/**
* Calculates second focus of ellipse (xf, yf) with one focus assumed at (0, 0) and given
* two points on the ellipse (xa, ya) and (xb, yb), and semimajor axis ae
* 计算椭圆的第二个焦点（xf, yf），假设其中一个焦点位于（0, 0），
* 并给定椭圆上的两个点（xa, ya）和（xb, yb），
* 以及椭圆的半长轴 ae
*/
void tcBallisticMissile::CalculateSecondFocus(float xa, float ya, float xb, float yb, float ae, float& xf, float& yf)
{
    // 计算点(xa, ya)到原点(0, 0)的距离
    float da = sqrtf(xa*xa + ya*ya);
    // 计算点(xb, yb)到原点(0, 0)的距离
    float db = sqrtf(xb*xb + yb*yb);
    // 计算点(xa, ya)和点(xb, yb)之间的距离
    float d = sqrtf((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb));
    // 计算d的倒数
    float inv_d = 1.0f / d;

    // 椭圆的长轴长度
    float major_axis = 2.0f * ae;
    // 点(xa, ya)到椭圆长轴另一端的距离（假设椭圆长轴通过原点）
    float ra = major_axis - da;
    // 点(xb, yb)到椭圆长轴另一端的距离（假设椭圆长轴通过原点）
    float rb = major_axis - db;

    // 计算ra的平方
    float ra2 = ra*ra;
    // 计算rb的平方
    float rb2 = rb*rb;
    // 计算d的平方
    float d2 = d*d;

    // 根据椭圆焦点公式计算a的值，a是与椭圆中心、两个焦点和椭圆上一点相关的几何量
    float a = 0.5f * inv_d * (ra2 - rb2 + d2);
    // 计算h的值，h是垂直于椭圆中心到椭圆上一点的连线，并且经过椭圆另一焦点的线段长度
    float h = sqrtf(ra2 - a*a);

    // 计算a除以d的值
    float a_over_d = a * inv_d;
    // 计算椭圆上两点连线的中点m的x坐标
    float xm = xa + a_over_d * (xb - xa);
    // 计算椭圆上两点连线的中点m的y坐标
    float ym = ya + a_over_d * (yb - ya);

    // 计算h除以d的值
    float h_over_d = h * inv_d;

    // 根据几何关系计算第二个焦点xf的x坐标
    xf = xm + h_over_d * (yb - ya);
    // 根据几何关系计算第二个焦点yf的y坐标
    yf = ym - h_over_d * (xb - xa);
}


/**
*
*/
void tcBallisticMissile::Clear()  
{  
	tcGameObject::Clear();

	guidanceUpdateInterval = 1.0f; // 1 second default
	lastGuidanceUpdateTime = 0.0f;
}



void tcBallisticMissile::Enu2ecef(float lat_rad, float lon_rad, float ke, float kn, float ku, float& kx, float& ky, float& kz)
{
    float sin_lat = sinf(lat_rad);
    float cos_lat = cosf(lat_rad);
    float sin_lon = sinf(lon_rad);
    float cos_lon = cosf(lon_rad);

    kx = (-sin_lon*ke) + (-sin_lat*cos_lon*kn) + (cos_lat*cos_lon*ku);
    ky = (cos_lon*ke) + (-sin_lat*sin_lon*kn) + (cos_lat*sin_lon*ku);
    kz = (cos_lat*kn) + (sin_lat*ku);
}

void tcBallisticMissile::Ecef2enu(float lat_rad, float lon_rad, float kx, float ky, float kz, float& ke, float& kn, float& ku)
{
    float sin_lat = sinf(lat_rad);
    float cos_lat = cosf(lat_rad);
    float sin_lon = sinf(lon_rad);
    float cos_lon = cosf(lon_rad);

    ke = (-sin_lon*kx) + (cos_lon*ky);
    kn = (-sin_lat*cos_lon*kx) + (-sin_lat*sin_lon*ky) + (cos_lat*kz);
    ku = (cos_lat*cos_lon*kx) + (cos_lat*sin_lon*ky) + (sin_lat*kz);
}

const GeoPoint& tcBallisticMissile::GetTargetDatum() const
{
    return targetDatum;
}


/**
* @return g-limited turn rate in radians/s
*/
float tcBallisticMissile::GlimitedTurnRate() const
{
    const float C_NUM = 19.0691f; // = (9.81 m/s2) / (kts to mps constant)

    return (C_NUM * mpDBObject->gmax) / (mcKin.mfSpeed_kts + 0.1f);
}




/**
* Copy constructor.
*/
tcBallisticMissile::tcBallisticMissile(const tcBallisticMissile& obj) 
: tcWeaponObject(obj),
    mpDBObject(obj.mpDBObject),
    subSurfaceLaunch(obj.subSurfaceLaunch),
    lastGuidanceUpdateTime(obj.lastGuidanceUpdateTime),
    guidanceUpdateInterval(obj.guidanceUpdateInterval),
    flightTime_s(obj.flightTime_s),
    thrustShutoffTime_s(obj.thrustShutoffTime_s),
    targetDatum(obj.targetDatum),
    x(obj.x),
    y(obj.y),
    z(obj.z),
    vx(obj.vx),
    vy(obj.vy),
    vz(obj.vz),
    xt(obj.xt),
    yt(obj.yt),
    zt(obj.zt),
    rt(obj.rt),
    gx(obj.gx),
    gy(obj.gy),
    gz(obj.gz),
    speed_mps(obj.speed_mps),
    speed2_mps2(obj.speed2_mps2),
    r_ecef(obj.r_ecef)
{
	mnModelType = MTYPE_BALLISTICMISSILE;
}

/**
* Constructor that initializes using info from database entry.
*/
tcBallisticMissile::tcBallisticMissile(tcBallisticMissileDBObject *obj)
:   tcWeaponObject(obj),
	mpDBObject(obj),
    subSurfaceLaunch(false),
    lastGuidanceUpdateTime(0),
    guidanceUpdateInterval(0.5),
    flightTime_s(0),
    thrustShutoffTime_s(0),
    x(0),
    y(0),
    z(0),
    vx(0),
    vy(0),
    vz(0),
    xt(0),
    yt(0),
    zt(0),
    rt(0),
    gx(0),
    gy(0),
    gz(0),
    speed_mps(0),
    speed2_mps2(0),
    r_ecef(0)
{
	mnModelType = MTYPE_BALLISTICMISSILE;

    targetDatum.Set(0, 0, 0);
}


tcBallisticMissile::~tcBallisticMissile() 
{
}

