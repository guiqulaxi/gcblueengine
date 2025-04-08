#include "tcCommDeviceDBObject.h"
#include "strutil.h"
using namespace database ;
void tcCommDeviceDBObject::WritePythonValue(std::string &valueString) const
{
    // 基础通信参数
    valueString+="    dbObj.mfRefRange_km="+strutil::to_python_value(mfRefRange_km)+"\n";
    valueString+="    dbObj.mfCoverageAngle_deg="+strutil::to_python_value(mfCoverageAngle_deg)+"\n";
    valueString+="    dbObj.mfBandwidth_Mbps="+strutil::to_python_value(mfBandwidth_Mbps)+"\n";
    valueString+="    dbObj.mfLatency_ms="+strutil::to_python_value(mfLatency_ms)+"\n";
    // 信号与抗干扰
    valueString+="    dbObj.mfMinFrequency_MHz="+strutil::to_python_value(mfMinFrequency_MHz)+"\n";
    valueString+="    dbObj.mfMaxFrequency_MHz="+strutil::to_python_value(mfMaxFrequency_MHz)+"\n";
    valueString+="    dbObj.mfSignalStrength_dBm="+strutil::to_python_value(mfSignalStrength_dBm)+"\n";
    valueString+="    dbObj.mfAntiJammingFactor="+strutil::to_python_value(mfAntiJammingFactor)+"\n";
    valueString+="    dbObj.mfEncryptionLevel="+strutil::to_python_value(mfEncryptionLevel)+"\n";
    // 环境与可靠性
    valueString+="    dbObj.mfTerrainAttenuation="+strutil::to_python_value(mfTerrainAttenuation)+"\n";
    valueString+="    dbObj.mfWeatherImpact="+strutil::to_python_value(mfWeatherImpact)+"\n";
    valueString+="    dbObj.mfPacketLossRate="+strutil::to_python_value(mfPacketLossRate)+"\n";
    // 系统参数
    valueString+="    dbObj.databaseClass="+strutil::to_python_value(mnMaxConnections)+"\n";
    valueString+="    dbObj.commProtocol="+strutil::to_python_value(commProtocol.c_str())+"\n";
    valueString+="    dbObj.isNetworkNode="+strutil::to_python_value(isNetworkNode)+"\n";
    valueString+="    dbObj.CalculateEffectiveParams()\n";
}

void tcCommDeviceDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcCommDeviceDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    return dbObj";
}

std::shared_ptr<tcCommDevice> tcCommDeviceDBObject::CreateComm(std::shared_ptr<tcGameObject> parent)
{
    std::shared_ptr<tcCommDevice> comm = std::make_shared<tcCommDevice>(dynamic_pointer_cast<tcCommDeviceDBObject>(tcDatabaseObject::shared_from_this()));
    comm->SetParent(parent);
    return comm;
}

tcCommDeviceDBObject::tcCommDeviceDBObject():tcDatabaseObject(),
    // 基础通信参数
 mfMaxRange_km(0.0f),        ///< [km] 最大理论通信距离（理想条件下）
 mfRefRange_km(0.0f),        ///< [km] 标准参考距离（如晴天对0dB增益天线的有效距离）
 mfCoverageAngle_deg(0.0f),   ///< [degrees] 信号覆盖角度（0=全向，30=定向扇形）
 mfBandwidth_Mbps(0.0f),      ///< [Mbps] 数据传输带宽（理论最大值）
 mfLatency_ms(0.0f),          ///< [ms] 基础通信延迟（未计入干扰和距离）
// 信号与抗干扰
 mfMinFrequency_MHz(0.0f),    ///< [MHz] 最低工作频率
 mfMaxFrequency_MHz(0.0f),    ///< [MHz] 最高工作频率
 mfSignalStrength_dBm(0.0f),  ///< [dBm] 发射功率强度
 mfAntiJammingFactor(0.0f),   ///< 抗干扰系数（0=完美抗扰，1=默认，>1=易受干扰）
 mfEncryptionLevel(0.0f),     ///< 加密等级（0=无加密，1=基础，2=军用级）
// 环境与可靠性
 mfTerrainAttenuation(0.0f),  ///< 地形衰减系数（0=无衰减，1=完全阻隔）
 mfWeatherImpact(0.0f),       ///< 天气影响系数（雨雪导致的信号衰减比例）
 mfPacketLossRate(0.0f),      ///< 基础数据丢包率（0~1，0=无丢包）
// 系统参数
 mnMaxConnections(0.0f),        ///< 最大同时连接设备数
commProtocol("Undefined"),    ///< 通信协议类型（"UHF"、"SATCOM"、"量子"等）
 isNetworkNode(true)          ///< 是否为网络节点（可中继信号）
{}

tcCommDeviceDBObject::tcCommDeviceDBObject(const tcCommDeviceDBObject &obj):
    // 基础通信参数
    mfMaxRange_km(obj.mfMaxRange_km),        ///< [km] 最大理论通信距离（理想条件下）
    mfRefRange_km(obj.mfRefRange_km),        ///< [km] 标准参考距离（如晴天对0dB增益天线的有效距离）
    mfCoverageAngle_deg(obj.mfCoverageAngle_deg),   ///< [degrees] 信号覆盖角度（0=全向，30=定向扇形）
    mfBandwidth_Mbps(obj.mfBandwidth_Mbps),      ///< [Mbps] 数据传输带宽（理论最大值）
    mfLatency_ms(obj.mfLatency_ms),          ///< [ms] 基础通信延迟（未计入干扰和距离）
    // 信号与抗干扰
    mfMinFrequency_MHz(obj.mfMinFrequency_MHz),    ///< [MHz] 最低工作频率
    mfMaxFrequency_MHz(obj.mfMaxFrequency_MHz),    ///< [MHz] 最高工作频率
    mfSignalStrength_dBm(obj.mfSignalStrength_dBm),  ///< [dBm] 发射功率强度
    mfAntiJammingFactor(obj.mfAntiJammingFactor),   ///< 抗干扰系数（0=完美抗扰，1=默认，>1=易受干扰）
    mfEncryptionLevel(obj.mfEncryptionLevel),     ///< 加密等级（0=无加密，1=基础，2=军用级）
    // 环境与可靠性
    mfTerrainAttenuation(obj.mfTerrainAttenuation),  ///< 地形衰减系数（0=无衰减，1=完全阻隔）
    mfWeatherImpact(obj.mfWeatherImpact),       ///< 天气影响系数（雨雪导致的信号衰减比例）
    mfPacketLossRate(obj.mfPacketLossRate),      ///< 基础数据丢包率（0~1，0=无丢包）
    // 系统参数
    mnMaxConnections(obj.mnMaxConnections),        ///< 最大同时连接设备数
    commProtocol(obj.commProtocol),    ///< 通信协议类型（"UHF"、"SATCOM"、"量子"等）
    isNetworkNode(obj.isNetworkNode)          ///< 是否为网络节点（可中继信号）
{

}

tcCommDeviceDBObject::~tcCommDeviceDBObject()
{

}

void tcCommDeviceDBObject::CalculateEffectiveParams()
{

}
