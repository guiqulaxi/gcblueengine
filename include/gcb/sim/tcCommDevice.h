
/**
**  @file tcCommDevice.h
**  @brief 通信设备运行时状态类，管理通信链路的动态行为
*/
#ifndef TCCOMMDEVICE_H
#define TCCOMMDEVICE_H

#include "tcGameObject.h"
#include "tcDatabaseObject.h"
#include "tcGameStream.h"
#include <memory>

namespace database {
    class tcCommDeviceDBObject;
}

class tcSimState;
class tcGameSerializer;

class tcSimState;
class tcGameObject;
class tcUpdateStream;
class tcGameStream;
class tcSensorPlatform;
class tcSensorReport;
class tcLOS;
struct Damage;
class tcSensorMapTrack;
/**
 * 通信设备的运行时状态类，处理连接管理、信号质量计算等动态行为
 */
class tcCommDevice : public std::enable_shared_from_this<tcCommDevice> {
    friend class tcGameSerializer;
public:


    // 基本状态
    bool mbActive;                  ///< 设备是否激活
    long mnDBKey;
    std::shared_ptr<tcGameObject> parent; ///< 所属平台对象
    std::shared_ptr<database::tcCommDeviceDBObject> mpDBObj; ///< 关联的数据库对象

    // 动态参数
    int mnCurrentConnections;       ///< 当前连接数
    float mfEffectiveRange_km;      ///< 实际有效通信距离（考虑环境因素）
    float mfCurrentLatency_ms;      ///< 当前通信延迟（含环境叠加）
    float mfCurrentPacketLoss;      ///< 当前丢包率（0~1）
    double mfLastUpdateTime;        ///< 上次状态更新时间

    // 网络节点功能
    std::vector<long> connectedDevices; ///< 已连接的设备ID列表（若为网络节点）

    float mountAz_rad;       ///< mounted azimuth of boresight relative to nose/bow of platform 安装方位角，这是瞄准镜安装后的方位角，相对于平台的机头/船头。
    float mfCommHeight_m;     ///< height of comm relative to platform altitude 传感器高度，即传感器相对于平台高度的高度差


    // 静态依赖
    static void AttachSimState(tcSimState* ss) { simState = ss; }

    // 核心功能方法
    bool CanEstablishLink(std::shared_ptr<const tcGameObject> target, float& effectiveRange_km);
    bool CanEstablishLink(std::shared_ptr<const tcCommDevice> target, float& effectiveRange_km);

    void UpdateEffectiveRange();    ///< 根据环境参数计算有效通信距离
    void UpdateLinkQuality();       ///< 更新链路质量（延迟、丢包率）


    // 连接管理
    bool RequestConnection(long deviceId);
    bool ReleaseConnection(long deviceId);
    bool IsConnected(long deviceId) const;

    // 序列化
    virtual tcUpdateStream& operator<<(tcUpdateStream& stream);
    virtual tcUpdateStream& operator>>(tcUpdateStream& stream);
    virtual tcGameStream& operator<<(tcGameStream& stream);
    virtual tcGameStream& operator>>(tcGameStream& stream);

    // 状态控制
    void SetActive(bool active);
    void SetDamaged(bool state);
    void SetParent(std::shared_ptr<tcGameObject> obj);
    virtual void Update(double t);  ///< 主状态更新方法

    // 数据库初始化
    virtual bool InitFromDatabase(long key);
    bool IsActive() const;
    bool IsDamaged() const;
    bool IsHidden() const;
    bool ApplyAdvancedDamage(const Damage& damage);
    // 构造与拷贝
    tcCommDevice();
    tcCommDevice(std::shared_ptr<database::tcCommDeviceDBObject> dbObj);
    virtual ~tcCommDevice();

    void AttachLOS();
    bool HasLOS(std::shared_ptr<const tcGameObject> target);
    void SetMountAz(float lookAz_rad);

    std::shared_ptr<tcCommDevice> Clone(void);

protected:
    static tcSimState* simState;    ///< 模拟环境状态引用
    static tcDatabase* database;
    static tcLOS* los;
    bool isHidden; ///< hidden sensors are not displayed in object control view
    bool isDamaged;
    // 环境计算工具方法
    float CalculateWeatherImpact() const;
    float CalculateTerrainAttenuation() const;

};

#endif
