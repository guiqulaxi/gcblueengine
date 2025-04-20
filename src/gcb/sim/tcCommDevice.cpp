#include "tcCommDevice.h"
#include "tcCommPlatform.h"
#include "tcSimState.h"
#include "tcDatabase.h"
#include "tcGameObject.h"
#include "tcLOS.h"
#include <algorithm>
#include <cmath>
#include "tcDamageModel.h"
#include "tcCommDeviceDBObject.h"
#include <cassert>
namespace database {
    class tcCommDeviceDBObject;
}

using database::tcCommDeviceDBObject;

// 静态成员初始化
tcSimState* tcCommDevice::simState = nullptr;
tcDatabase* tcCommDevice::database = 0;
tcLOS* tcCommDevice::los = 0;
/**
 * 默认构造函数
 */
tcCommDevice::tcCommDevice()
    : mbActive(false),
    mnCurrentConnections(0),
    mfEffectiveRange_km(0),
    mfCurrentLatency_ms(0),
    mfCurrentPacketLoss(0),
    mfLastUpdateTime(0)
{
}

/**
 * 通过数据库对象构造
 */
tcCommDevice::tcCommDevice(std::shared_ptr<tcCommDeviceDBObject> dbObj)
    : mbActive(false),
    mpDBObj(dbObj),
    mnCurrentConnections(0),
    mfEffectiveRange_km(dbObj ? dbObj->mfMaxRange_km : 0),
    mfCurrentLatency_ms(dbObj ? dbObj->mfLatency_ms : 0),
    mfCurrentPacketLoss(0),
    mfLastUpdateTime(0)
{
}

tcCommDevice::~tcCommDevice() = default;

/**
 * 从数据库初始化设备
 */
bool tcCommDevice::InitFromDatabase(long key) {
    assert(database);

    mpDBObj =  std::dynamic_pointer_cast<tcCommDeviceDBObject>(database->GetObject(key));
    if (mpDBObj == NULL)
    {
        fprintf(stderr, "Error - tcSensorState::InitFromDatabase - Not found in db or bad class for key\n");
        return false;
    }
    mnDBKey = key;
    mbActive = false;
    isHidden = false;
    mfLastUpdateTime = randf(mpDBObj->mfLatency_ms);
    return true;
}
bool tcCommDevice::IsActive() const
{
    return mbActive != 0;
}

bool tcCommDevice::IsDamaged() const
{
    return isDamaged;
}

bool tcCommDevice::IsHidden() const
{
    return isHidden;
}
/**
* @return true if sensor is damaged
*/
bool tcCommDevice::ApplyAdvancedDamage(const Damage& damage)
{
    if (IsDamaged()) return false; // already damaged;

    const database::tcDamageEffect* damageEffect =
        database->GetDamageEffectData(mpDBObj->damageEffect);

    if (damageEffect == 0)
    {
        fprintf(stderr, "tcSensorState::ApplyAdvancedDamage -- NULL damageEffect for %s\n",
                mpDBObj->mzClass.c_str());
        assert(false);
        return false;
    }


    float blastDamage = damageEffect->GetBlastDamageFactor(damage.blast_psi);
    float waterBlastDamage = damageEffect->GetWaterBlastDamageFactor(damage.waterBlast_psi);
    float thermalDamage = damageEffect->GetRadiationDamageFactor(damage.thermal_J_cm2);

    // arbitrarily declare nFragments x 5% chance of fragment hitting this sensor
    bool fragmentHits = (randf() < 0.05*damage.fragHits);

    float fragDamage = fragmentHits ? damageEffect->GetFragmentDamageFactor(damage.fragEnergy_J) : 0;

    blastDamage = std::min(blastDamage, 1.0f);
    waterBlastDamage = std::min(blastDamage, 1.0f);
    thermalDamage = std::min(blastDamage, 1.0f);
    fragDamage = std::min(blastDamage, 1.0f);

    float pFail = 1.0f - ((1.0f-blastDamage) * (1.0f-waterBlastDamage) * (1.0f-thermalDamage) * (1.0f-fragDamage));

    if (randf() < pFail)
    {
        SetDamaged(true);
        return true;
    }
    else
    {
        return false;
    }

}
/**
 * 增强版通信链路可行性判断
 */
bool tcCommDevice::CanEstablishLink(std::shared_ptr<const tcGameObject> target, float& effectiveRange_km) {
    if (!mbActive || !mpDBObj || !parent || !target) return false;

    // 获取目标通信设备（假设目标平台有通信设备）
     if ( std::shared_ptr<const tcPlatformObject>pPlatformObj = std::dynamic_pointer_cast<const tcPlatformObject>(target))
    {

        bool bEstablishLink = false; //
        unsigned nComms = pPlatformObj->GetComponent<tcCommPlatform>()->GetCommCount(); // 获取平台对象的通信设备数量
        for (unsigned n=0; (n<nComms) && (!bEstablishLink); n++) //
        {
            std::shared_ptr<const tcCommDevice> comm = pPlatformObj->GetComponent<tcCommPlatform>()->GetComm(n); // 获取当前传感器状态
            CanEstablishLink(comm,effectiveRange_km);
        }

        return bEstablishLink; // 返回是否检测到
    }
     return false;
}

bool tcCommDevice::CanEstablishLink(std::shared_ptr<const tcCommDevice> targetComm, float& effectiveRange_km)
{
    if (!targetComm || !targetComm->IsActive()) return false;

    // 协议兼容性检查
    if (mpDBObj->commProtocol != targetComm->mpDBObj->commProtocol) return false;

    // 频率重叠检查
    const float thisFreqStart = mpDBObj->mfMinFrequency_MHz;
    const float thisFreqEnd = mpDBObj->mfMaxFrequency_MHz;
    const float targetFreqStart = targetComm->mpDBObj->mfMinFrequency_MHz;
    const float targetFreqEnd = targetComm->mpDBObj->mfMaxFrequency_MHz;
    if ((thisFreqEnd < targetFreqStart) || (thisFreqStart > targetFreqEnd)) return false;

    // // 方向性覆盖检查
    // if (mpDBObj->mfCoverageAngle_deg < 360.0f) {
    //     const float relBearing_deg = parent->CalculateRelativeBearingTo(target->GetGeoPoint());
    //     if (fabs(relBearing_deg) > mpDBObj->mfCoverageAngle_deg * 0.5f) return false;
    // }

    // 加密等级兼容性（需双方加密等级匹配或更高）
    if (mpDBObj->mfEncryptionLevel != targetComm->mpDBObj->mfEncryptionLevel) return false;

    // 信号强度计算
    const float txPower_dBm = mpDBObj->mfSignalStrength_dBm;
    const float rxSensitivity_dBm = targetComm->mpDBObj->mfSignalStrength_dBm; // 假设接收灵敏度存储在相同字段
    const float powerMargin_dB = txPower_dBm - rxSensitivity_dBm;

    // 基础距离计算（自由空间路径损耗模型简化版）
    const float refDistance_km = mpDBObj->mfRefRange_km;
    const float maxTheoreticalRange_km = refDistance_km * pow(10.0f, powerMargin_dB / 20.0f);

    // 环境因素计算
    const float distance_km = parent->mcKin.RangeToKm(    targetComm->parent->mcKin);
    const float weatherAtten = CalculateWeatherImpact();
    const float terrainAtten = CalculateTerrainAttenuation();
    const float totalAttenuation = weatherAtten + terrainAtten;

    // 有效通信距离
    effectiveRange_km = maxTheoreticalRange_km * (1.0f - totalAttenuation);

    return (distance_km <= effectiveRange_km);
}

/**
 * 增强版有效距离计算
 */
void tcCommDevice::UpdateEffectiveRange() {
    if (!mpDBObj) return;

    // 信号强度计算
    const float txPower_dBm = mpDBObj->mfSignalStrength_dBm;
    const float rxSensitivity_dBm = -90.0f; // 假设标准接收灵敏度
    const float powerMargin_dB = txPower_dBm - rxSensitivity_dBm;

    // 理论最大距离
    const float maxTheoreticalRange_km = mpDBObj->mfRefRange_km * pow(10.0f, powerMargin_dB / 20.0f);

    // 环境衰减
    const float weatherAtten = CalculateWeatherImpact();
    const float terrainAtten = CalculateTerrainAttenuation();

    mfEffectiveRange_km = maxTheoreticalRange_km * (1.0f - (weatherAtten + terrainAtten));
}

/**
 * 增强版链路质量更新
 */
void tcCommDevice::UpdateLinkQuality() {
    if (!mpDBObj || !parent) return;

    // 基础延迟（含加密处理延迟）
    const float encryptionDelay = mpDBObj->mfEncryptionLevel * 2.0f; // 加密等级每级增加2ms
    mfCurrentLatency_ms = mpDBObj->mfLatency_ms + encryptionDelay;

    // 距离导致的延迟增加（每100km增加1ms）
    const float distanceFactor = parent->mcKin.mfAlt_m / 100000.0f; // 假设高度近似代表通信距离
    mfCurrentLatency_ms += distanceFactor * 1.0f;

    // 天气影响延迟
    mfCurrentLatency_ms *= (1.0f + CalculateWeatherImpact());

    // 抗干扰丢包率计算
    const float jammingEffect =  mpDBObj->mfAntiJammingFactor;
    mfCurrentPacketLoss = std::min(1.0f,
                                   mpDBObj->mfPacketLossRate + jammingEffect + CalculateWeatherImpact());
}

/**
 * 网络节点连接扩展
 */
bool tcCommDevice::RequestConnection(long deviceId) {
    if (!mpDBObj->isNetworkNode && (mnCurrentConnections >= mpDBObj->mnMaxConnections)) {
        return false;
    }

    // 网络节点允许超额连接（作为中继）
    if (std::find(connectedDevices.begin(), connectedDevices.end(), deviceId) == connectedDevices.end()) {
        connectedDevices.push_back(deviceId);
        if (!mpDBObj->isNetworkNode) mnCurrentConnections++;
        return true;
    }
    return false;
}









/**
 * 释放连接
 */
bool tcCommDevice::ReleaseConnection(long deviceId) {
    auto it = std::find(connectedDevices.begin(), connectedDevices.end(), deviceId);
    if (it != connectedDevices.end()) {
        connectedDevices.erase(it);
        mnCurrentConnections--;
        return true;
    }
    return false;
}

/**
 * 主状态更新函数
 */
void tcCommDevice::Update(double t) {
    if (!mbActive) return;

    const double dt = t - mfLastUpdateTime;
    if (dt < 0.1) return; // 100ms更新间隔

    UpdateEffectiveRange();
    UpdateLinkQuality();

    mfLastUpdateTime = t;
}

void tcCommDevice::AttachLOS()
{
    los = tcLOS::Get();
}


/**
* @return true if sensor has line of sight to target
*/
bool tcCommDevice::HasLOS(std::shared_ptr<const tcGameObject> target)
{
    assert(parent != 0);
    assert(target != 0);

    long key = 0;
    GeoPoint p1;
    GeoPoint p2;

    if (parent->mnID > target->mnID)
    {
        key = ((parent->mnID & 0x00FF) << 16) + (target->mnID & 0x00FF);
        p1.Set(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m);
        p2.Set(target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfAlt_m);
    }
    else
    {
        key = ((target->mnID & 0x00FF) << 16) + (parent->mnID & 0x00FF);
        p1.Set(target->mcKin.mfLon_rad, target->mcKin.mfLat_rad, target->mcKin.mfAlt_m);
        p2.Set(parent->mcKin.mfLon_rad, parent->mcKin.mfLat_rad, parent->mcKin.mfAlt_m);
    }

    return los->HasLOS(key, mfLastUpdateTime, p1, p2);
}

void tcCommDevice::SetMountAz(float lookAz_rad)
{
    mountAz_rad=lookAz_rad;
}

std::shared_ptr<tcCommDevice> tcCommDevice::Clone()
{

        std::shared_ptr<tcCommDevice> pNew=std::make_shared<tcCommDevice>();
        *pNew = *this;
        return pNew;
}

// 序列化实现
tcUpdateStream& tcCommDevice::operator<<(tcUpdateStream& stream) {

    return stream;
}

tcUpdateStream& tcCommDevice::operator>>(tcUpdateStream& stream) {

    return stream;
}

void tcCommDevice::SetActive(bool active)
{
    if (mbActive == (int)active) return;

    mbActive = active;
}

void tcCommDevice::SetDamaged(bool state)
{
    isDamaged = state;

}

void tcCommDevice::SetParent(std::shared_ptr<tcGameObject> obj)
{
    parent = obj;

}

tcGameStream& tcCommDevice::operator<<(tcGameStream& stream) {
    return stream;
}

tcGameStream& tcCommDevice::operator>>(tcGameStream& stream) {
    return stream;
}

/**
 * 计算天气影响因子
 */
float tcCommDevice::CalculateWeatherImpact() const {
    if (!simState || !mpDBObj) return 0.0f;
    // 假设simState提供当前天气强度（0~1）
    const float weatherIntensity = 1;
    return mpDBObj->mfWeatherImpact * weatherIntensity;
}

/**
 * 计算地形衰减
 */
float tcCommDevice::CalculateTerrainAttenuation() const {
    if (!simState || !parent || !mpDBObj) return 0.0f;
    // 假设simState提供地形遮挡系数
    return 0;
}

// /**
//  * 视线检测
//  */
// bool tcCommDevice::CheckLineOfSight(std::shared_ptr<const tcGameObject> target) const {
//     if (!simState || !parent || !target) return true; // 默认允许

//     // 使用LOS模块检测两点间视线
//     return simState->CheckLineOfSight(parent->GetGeoPoint(), target->GetGeoPoint());
// }
