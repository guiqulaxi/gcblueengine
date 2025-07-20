#ifndef TCSPACEOBJECT_H
#define TCSPACEOBJECT_H
#include "tcPlatformObject.h"
#include "tcCommandObject.h"
#include "tcFile.h"
#include "tcEngagementData.h"
#include "tcPlatformObject.h"
#include <deque>

class tcGameStream;

namespace database
{
class tcSpaceDBObject;
}

/**
* Represents a platform that resides on the water's surface.
*
* @see tcSpaceObject
*/
class tcSpaceObject : public tcPlatformObject
{
public:
    std::shared_ptr<tcSpaceDBObject>mpDBObject;

      virtual void SetKinematics(
            double fLon_rad,              ///< longitude [rad]
            double fLat_rad,               ///< latitude [rad]
            float fAlt_m,                  ///< altitude, negative is subsurface depth [m]
            float fHeading_rad,           ///< relative to north [rad] 顺时针
            float fYaw_rad,                ///< orientation in azimuthal plane
            float fPitch_rad,              ///< orientation in elevation plane
            float fRoll_rad, 			   ///< orienation about roll axis
            float fSpeed_kts             ///< [kts])
    ) override;
    virtual void Clear();

    virtual bool IsDestroyed();
    virtual void Update(double afStatusTime);
    virtual void UpdateHeading(float dt_s);
    virtual void Move(float dt_s);
    void PrintToFile(tcFile& file);
    void SaveToFile(tcFile& file) override;
    void LoadFromFile(tcFile& file);
    virtual void Serialize(tcFile& file, bool mbLoad);

    const std::deque<tcPoint>& GetPositionHistory() const;

    virtual tcGameStream& operator>>(tcGameStream& stream);
    virtual tcGameStream& operator<<(tcGameStream& stream);

    tcSpaceObject();
    tcSpaceObject(tcSpaceObject&);
    tcSpaceObject(std::shared_ptr<tcSpaceDBObject>obj);
    ~tcSpaceObject();

    //根据经纬度高度速度构造轨道参数
    void SetOrbit(double fLat_rad, double fLon_rad, double fAlt_m, double fSpeed_kts, double fHeading_rad);
    // 访问器和修改器，用于获取和设置轨道参数
    double GetA(void) const  {return m_a;}     // 获取半长轴
    void   SetA(double a)  {m_a = a;}       // 设置半长轴
    double Gete(void) const {return m_e;}     // 获取偏心率
    void   Sete(double e)  {m_e = e;}       // 设置偏心率
    double GetI(void) const  {return m_i;}     // 获取轨道倾角
    void   SetI(double i) {m_i = i;}       // 设置轨道倾角
    double GetOmega(void) const {return m_Omega;} // 获取升交点经度
    void   SetOmega(double Om) {m_Omega = Om;}  // 设置升交点经度
    double Getomega(void) const {return m_omega;} // 获取近地点幅角
    void   Setomega(double om) {m_omega = om;}  // 设置近地点幅角
    double GetN(void) const   {return std::sqrt(m_mu/std::pow(m_a, 3.0));}     // 获取平均角速度（根据开普勒第三定律计算）
    double GetV(void) const  {return m_v;}     // 获取速度（注意：此实现可能依赖于其他方法或数据）
    double GetE(void) const    {return m_E;}     // 获取偏近点角（注意：此实现可能未直接给出）
    double GetM(void) const {return m_M;}     // 获取平近点角
    void   SetM(double M);       // 设置平近点角
    double GetTp(void) const{return m_tp;}    // 获取过近地点时间
    void   SetTp(double tp)   {m_tp = tp;}     // 设置过近地点时间

    // 获取远地点和近地点的距离
    double GetRa(void) const  {return m_a*(1.0+m_e);} // 远地点距离
    double GetRp(void) const {return m_a*(1.0-m_e);} // 近地点距离
    // 获取当前位置的极坐标点
    GeoPoint GetPositionPoint() const;

    // 根据真近点角M获取轨道上的点
    GeoPoint GetPointAt(double M) const;

    double GetOrbitalVelocity() const;
    virtual void Construct() override;
protected:
    enum {MAX_HISTORY = 64};
    double lastHistoryUpdate; ///< time that positionHistory was last updated

    double m_a;             // 半长轴 千米 输入
    double m_e;             // 偏心率  输入
    double m_i;             // 轨道倾角 输入
    double m_Omega;         // 升交点经度 输入
    double m_omega;         // 近地点幅角 输入

    // 卫星运动参数
    double m_v;             // 真近点角
    double m_E;             // 偏近点角（注意：此变量在构造函数中可能未初始化）
    double m_M;             // 初始平近点角 输入

    // 初始常量
    double m_tp;            // 过近地点时间 输入
    double m_mu;            // 中心天体的引力常数（km^3/s^2

    double m_r;             //卫星到中心天体的距离

    std::deque<tcPoint> positionHistory; ///< deque of (lon_rad,lat_rad) platform position, front is most recent


    virtual void ApplyRestrictions(void);
    virtual void UpdateClimb(float dt_s) {} // do nothing for surface objs
    virtual void UpdateDestroyed(double t);
    virtual void UpdateHistory(double t);
};



#endif // TCSPACEOBJECT_H
