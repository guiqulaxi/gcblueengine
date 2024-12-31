#include "tcSpaceObject.h"
#include "Task.h"
#include "tcSpaceDBObject.h"
#include "Brain.h"
#include <cmath>
/**
* Save
*/
tcGameStream& tcSpaceObject::operator>>(tcGameStream& stream)
{
    tcPlatformObject::operator>>(stream);
    return stream;
}

/**
* Load
*/
tcGameStream& tcSpaceObject::operator<<(tcGameStream& stream)
{
    tcPlatformObject::operator<<(stream);
    return stream;
}

void tcSpaceObject::ApplyRestrictions()
{

    if (mfDamageLevel < 0.25f)
    {
        return;
    }
    else
    {
        mcGS.mfGoalSpeed_kts = std::min(mcGS.mfGoalSpeed_kts, (1.0f - 0.5f*mfDamageLevel)*mpDBObject->mfMaxSpeed_kts);
    }
}


const std::deque<tcPoint>& tcSpaceObject::GetPositionHistory() const
{
    return positionHistory;
}

void tcSpaceObject::Move(float dt_s)
{
    // 更新平近点角m_M，这里假设GetN()是获取某种速度或角速度的函数，dt_s是时间步长
    m_M += GetN() * dt_s;

    // 将m_M规范化到[0, 2π)范围内
    m_M = std::fmod(m_M, C_TWOPI);

    // 如果m_M小于0（由于浮点数精度问题可能发生），则将其调整到[0, 2π)范围内
    if (m_M < 0.0)
        m_M += C_TWOPI;

    // 使用二分法求解偏近点角m_E
    // 偏近点角E满足的方程是 E - e*sin(E) = 某个与m_M和轨道参数有关的常数（此处未直接计算）
    // 但由于我们关心的是E与m_M的关系，且E-e*sin(E)是增函数，因此可以使用二分法
    const double eps = 1.0e-6; // 设定二分法的精度
    double min = 0.0; // 搜索区间的下限
    double max = C_TWOPI; // 搜索区间的上限
    while((max-min) > eps) // 当搜索区间宽度大于精度时继续搜索
    {
        double mid = 0.5*(max+min); // 计算区间中点
        // 根据E - e*sin(E)与m_M的比较（这里简化为与mid的比较，实际需考虑常数项）调整搜索区间
        // 注意：这里的比较是简化的，实际中需要解方程或利用已知关系来确定搜索方向
        if (m_M < mid - m_e*std::sin(mid)) // 假设的比较，实际中可能不同
            max = mid;
        else
            min = mid;
    }
    m_E = min; // 当搜索区间足够小时，认为中点即为所求的E

    // 计算真近点角m_v
    // 使用开普勒方程（或几何关系）的近似解
    if(m_E <= M_PI) // 注意：这里应该是M_PI（π的宏定义），但原代码写成了m_PI，可能是笔误
        m_v = std::acos((std::cos(m_E) - m_e) / (1.0 - m_e * std::cos(m_E))); // 当E在[0, π]时
    else
        m_v = C_TWOPI - std::acos((std::cos(m_E) - m_e) / (1.0 - m_e * std::cos(m_E))); // 当E在(π, 2π)时
    GeoPoint p=GetPositionPoint();
    mcKin. mfLon_rad=p.mfLon_rad;              ///< longitude [rad]
    mcKin. mfLat_rad=p.mfLat_rad;              ///< latitude [rad]
    mcKin. mfAlt_m=p.mfAlt_m-C_REARTHM; ;                 ///< altitude, negative is subsurface depth [m]
    mcKin. mfHeading_rad=0;           ///< relative to north [rad] 顺时针
    mcKin. mfClimbAngle_rad=0;        ///< climb angle defines vertical motion vector [rad]
    mcKin. mfYaw_rad=0;               ///< orientation in azimuthal plane
    mcKin. mfPitch_rad=0;             ///< orientation in elevation plane
    mcKin. mfRoll_rad=0;			   ///< orienation about roll axis
    mcKin. mfSpeed_kts=GetOrbitalVelocity()*1000*C_MPSTOKTS;             ///< [kts]

    return;
}
void tcSpaceObject::UpdateHeading(float dt_s)
{
    float heading_start,heading_end,dh;

    float previous_roll = mcKin.mfRoll_rad;

    float new_roll = 0.03f*sinf((float)mfStatusTime*0.25f); // sinusoidal "wave roll"

    heading_start = mcKin.mfHeading_rad;

    tcPlatformObject::UpdateHeading(dt_s);

    heading_end = mcKin.mfHeading_rad;
    dh = heading_end - heading_start;


    if (dh != 0)
    {    // skip rest of function if no heading change
        if (dh > C_PI) {dh -= C_TWOPI;}
        else if (dh < -C_PI) {dh += C_TWOPI;}

        // crude version of induced by center of buoyancy / Cg moment
        new_roll += (dt_s > 0) ? 0.75f*dh/dt_s : 0;
    }
    float alpha = dt_s; // really dt_s*1.0f, falls apart for dt_s close to or > 1
    mcKin.mfRoll_rad = alpha*new_roll + (1-alpha)*previous_roll;
}

void tcSpaceObject::UpdateHistory(double t)
{
    const double updateInterval = 90.1;
    if (t < (lastHistoryUpdate + updateInterval)) return;
    lastHistoryUpdate = t;

    tcPoint p;
    p.x = mcKin.mfLon_rad;
    p.y = mcKin.mfLat_rad;
    positionHistory.push_front(p);

    if (positionHistory.size() > MAX_HISTORY)
    {
        positionHistory.pop_back();
    }
}

void tcSpaceObject::Update(double afStatusTime)
{
    const float min_update_s = 0.0f;
    float dt_s = (float)(afStatusTime - mfStatusTime);

    //UpdateEffects();

    if (parent != NULL) {return;} // captive, let parent update if applicable
    if ((dt_s <= min_update_s) && !tcGameObject::IsEditMode())
    {
        return;
    } // added for pause case


    if (mpDBObject == NULL) {return;}

    if (mfDamageLevel >= 1.0f)
    {
        UpdateDestroyed(afStatusTime);
        mfStatusTime = afStatusTime;
        //Update3D();
        return;
    }

    // UpdateFormationGuidance(); // formation heading/speed calculation

    // UpdateHeading(dt_s);

    // UpdateSpeed(dt_s);

    //UpdateClimb(dt_s);

    // ApplyRestrictions();

    Move(dt_s);

    // UpdateLauncherState(dt_s);

    UpdateSensors(afStatusTime);

    // UpdateAI(afStatusTime);

    UpdateMagazines(afStatusTime);

    //Update3D();

    UpdateHistory(afStatusTime);

    mfStatusTime = afStatusTime;
}

void tcSpaceObject::UpdateDestroyed(double t)
{

}



void tcSpaceObject::Clear()
{
    tcPlatformObject::Clear();
}



bool tcSpaceObject::IsDestroyed()
{
    return (mfDamageLevel >= 1.0f) ;
}




void tcSpaceObject::PrintToFile(tcFile& file)
{
    tcPlatformObject::PrintToFile(file);
}

void tcSpaceObject::SaveToFile(tcFile& file)
{
    tcPlatformObject::SaveToFile(file);
}


void tcSpaceObject::LoadFromFile(tcFile& file)
{
    tcPlatformObject::LoadFromFile(file);
}

void tcSpaceObject::Serialize(tcFile& file, bool mbLoad)
{
    if (mbLoad)
    {
        LoadFromFile(file);
    }
    else
    {
        SaveToFile(file);
    }
}

tcSpaceObject::tcSpaceObject()
{
    Clear();
    mpDBObject = NULL;
    mnModelType = MTYPE_SPACE;
    m_mu=398600.4415;
}

tcSpaceObject::tcSpaceObject(tcSpaceObject& o) : tcPlatformObject(o)
{
    mpDBObject = o.mpDBObject;
}

tcSpaceObject::tcSpaceObject(std::shared_ptr<tcSpaceDBObject>obj)
    : tcPlatformObject(obj)
{
    mpDBObject = obj;
    mnModelType = MTYPE_SPACE;
    mcGS.mfGoalAltitude_m = 0;
    m_mu=398600.4415;
    lastHistoryUpdate = 3.0f*randf();


}

/******************************************************************************/
tcSpaceObject::~tcSpaceObject()
{
}

void tcSpaceObject::SetM(double M)
{

    // Set M
    m_M      = M;
    m_M      = std::fmod(m_M, C_TWOPI);
    if (m_M < 0.0)
        m_M += C_TWOPI;

    // Set E and v

    // Compute E with dichotomy since E - e*sin(E) is crescent
    const double eps = 1.0e-6;
    double min = 0.0;
    double max = C_TWOPI;
    while((max-min) > eps)
    {
        double mid = 0.5*(max+min);
        if (m_M < mid - m_e*std::sin(mid))
            max = mid;
        else
            min = mid;
    }
    m_E = min;

    // Compute v
    if(m_E <= C_PI)
        m_v = std::acos((std::cos(m_E) - m_e) / (1.0 - m_e * std::cos(m_E)));
    else
        m_v = C_TWOPI- std::acos((std::cos(m_E) - m_e) / (1.0 - m_e * std::cos(m_E)));

    return;

}
GeoPoint tcSpaceObject::GetPositionPoint() const
{
// 径向距离（r）:
//     使用开普勒方程（简化为这里的形式）来计算天体相对于中心天体的径向距离。这个距离考虑了轨道的偏心率和当前位置
    double r     = m_a * (1.0 - m_e * std::cos(m_E));
    /*
    double theta = fmod(m_Omega + std::cos(m_i) * (m_omega + m_v), C_TWOPI);
    if (theta < 0.0)
        theta += C_TWOPI;
    */
    //double theta = fmod(m_Omega+std::atan(std::tan(m_omega+m_v)*std::cos(m_i)), C_TWOPI);
    // 经度（theta）:
    // 使用了 atan2 函数来计算，它根据给定的 y 和 x 坐标值计算角度，能正确处理所有四个象限，
    // 并返回角度的完整范围（-π 到 π）。这里， y 和 x 坐标是通过将 m_omega + m_v（当前位置的角度）和 m_i（轨道倾角）代入到转换公式中计算得到的，
    // 以确保考虑了轨道的倾斜
    double theta = fmod(m_Omega+std::atan2(
                            std::sin(m_omega+m_v)*std::cos(m_i)/std::sqrt(1.0-std::pow(std::sin(m_omega+m_v)*std::sin(m_i), 2.0)),
                            std::cos(m_omega+m_v)/std::sqrt(1.0-std::pow(std::sin(m_omega+m_v)*std::sin(m_i), 2.0))
                            ), C_TWOPI);
    if (theta < 0.0)
        theta += C_TWOPI;
// 纬度（phi）:
// 使用 asin 函数计算纬度（赤纬），这取决于轨道倾角 m_i 和当前位置相对于近地点的角度 m_omega + m_v。
// 同样，使用 fmod 函数和 C_TWOPI 将角度归一化，但这里实际上有些多余，
//因为 asin 的输出范围已经是 [-π/2, π/2]，而赤纬的范围也应该是这个范围。
 //不过，对于确保代码的一致性和未来的修改可能是有用的。
    double phi   = fmod(std::asin(std::sin(m_i)*std::sin(m_omega+m_v)), C_TWOPI);
    if (phi < 0.0)
        phi += C_TWOPI;

    return GeoPoint( theta, phi,r*1000);
}
double tcSpaceObject::GetOrbitalVelocity() const {
//径向距离（r）
    double r     = m_a * (1.0 - m_e * std::cos(m_E));

    // 计算角动量并据此计算速度
    double p = m_a * (1 - pow(m_e, 2)); // 焦距
    double h = sqrt(m_mu * p) * cos(m_i) / r; // 角动量

    // 计算卫星在惯性坐标系中的速度
    auto vx = h / r * (-sin(m_v) * cos(m_omega) - cos(m_v + m_omega) * sin(m_omega) * cos(m_i));
    auto vy = h / r * (-sin(m_v) * sin(m_omega) + cos(m_v + m_omega) * cos(m_omega) * cos(m_i));
    auto vz = h / r * (cos(m_v + m_omega) * sin(m_i));

    double total_speed = sqrt(vx * vx + vy * vy + vz * vz);

}

void tcSpaceObject::Construct()
{
    tcPlatformObject::Construct();

    if (addTasksOnCreate) brain->AddTaskDirectly("MissileWarning", 3.0, ai::Task::HIDDEN | ai::Task::PERMANENT);
    if (addTasksOnCreate) brain->AddTaskDirectly("PointDefense", 3.0, ai::Task::HIDDEN | ai::Task::PERMANENT);
}
// tcSpaceObject类的成员函数，用于根据给定的平近点角M计算天体的三维空间位置
GeoPoint tcSpaceObject::GetPointAt(double M) const
{
    // 将M规范化到[0, 2π)范围内
    M = std::fmod(M, C_TWOPI);
    if (M < 0.0)
        M += C_TWOPI;

    // 使用二分法求解偏近点角E
    // 偏近点角E满足的方程是 E - e*sin(E) = M + 某个常数（此处常数与平近点角M和轨道参数有关，但在此函数中未直接计算）
    // 由于E - e*sin(E)是增函数，可以使用二分法求解
    const double eps = 1.0e-6; // 设定二分法的精度
    double min = 0.0; // 搜索区间的下限
    double max = C_TWOPI; // 搜索区间的上限
    while((max-min) > eps) // 当搜索区间宽度大于精度时继续搜索
    {
        double mid = 0.5*(max+min); // 计算区间中点
        // 根据E - e*sin(E)与M的比较结果调整搜索区间
        if (M < mid - m_e*std::sin(mid))
            max = mid;
        else
            min = mid;
    }
    double E = min; // 当搜索区间足够小时，认为中点即为所求的E

    // 使用开普勒方程（此处通过几何关系近似求解）计算真近点角v
    double v = 0.0;
    // 根据E是否在[0, π]范围内选择适当的公式计算v
    if(E <= C_PI)
        v = std::acos((std::cos(E) - m_e) / (1.0 - m_e * std::cos(E)));
    else
        v = C_TWOPI - std::acos((std::cos(E) - m_e) / (1.0 - m_e * std::cos(E)));

    // 计算天体在轨道上的径向距离r
    double r = m_a * (1.0 - m_e * std::cos(E));

    // 计算经度theta（在赤道面上的投影角度）
    double theta = fmod(m_Omega+std::atan2(
                            // 使用atan2函数计算经度，考虑了轨道的倾斜和当前位置在赤道面上的投影
                            std::sin(m_omega+v)*std::cos(m_i)/std::sqrt(1.0-std::pow(std::sin(m_omega+v)*std::sin(m_i), 2.0)),
                            std::cos(m_omega+v)/std::sqrt(1.0-std::pow(std::sin(m_omega+v)*std::sin(m_i), 2.0))
                            ), C_TWOPI);
    if (theta < 0.0)
        theta += C_TWOPI; // 确保theta在[0, 2π)范围内

    // 计算纬度phi（赤纬）
    double phi = fmod(std::asin(std::sin(m_i)*std::sin(m_omega+v)), C_TWOPI);
    // 注意：这里的fmod对phi可能是多余的，因为asin的输出范围已经满足[-π/2, π/2]
    // 但为了与theta的处理保持一致，还是进行了取模操作
    if (phi < 0.0)
        phi += C_TWOPI; // 实际上，phi不会小于0，因为asin的输出不会为负

    // 返回天体的三维空间位置
    return GeoPoint(r, theta, phi);
}
