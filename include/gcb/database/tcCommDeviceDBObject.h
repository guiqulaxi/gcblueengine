#ifndef TCCOMMDEVICEDBOBJECT_H
#define TCCOMMDEVICEDBOBJECT_H
#include "tcCommDevice.h"
#include "tcDatabaseObject.h"
namespace database {

class tcCommDeviceDBObject : public tcDatabaseObject
{
public:
    // 基础通信参数
    float mfMaxRange_km;        ///< [km] 最大理论通信距离（理想条件下）
    float mfRefRange_km;        ///< [km] 标准参考距离（如晴天对0dB增益天线的有效距离）
    float mfCoverageAngle_deg;  ///< [degrees] 信号覆盖角度（0=全向，30=定向扇形）
    float mfBandwidth_Mbps;     ///< [Mbps] 数据传输带宽（理论最大值）
    float mfLatency_ms;         ///< [ms] 基础通信延迟（未计入干扰和距离）

    // 信号与抗干扰
    float mfMinFrequency_MHz;   ///< [MHz] 最低工作频率
    float mfMaxFrequency_MHz;   ///< [MHz] 最高工作频率
    float mfSignalStrength_dBm; ///< [dBm] 发射功率强度
    float mfAntiJammingFactor;  ///< 抗干扰系数（0=完美抗扰，1=默认，>1=易受干扰）
    float mfEncryptionLevel;    ///< 加密等级（0=无加密，1=基础，2=军用级）

    // 环境与可靠性
    float mfTerrainAttenuation; ///< 地形衰减系数（0=无衰减，1=完全阻隔）
    float mfWeatherImpact;      ///< 天气影响系数（雨雪导致的信号衰减比例）
    float mfPacketLossRate;     ///< 基础数据丢包率（0~1，0=无丢包）

    // 系统参数
    int mnMaxConnections;       ///< 最大同时连接设备数
    std::string commProtocol;   ///< 通信协议类型（"UHF"、"SATCOM"、"量子"等）
    bool isNetworkNode;         ///< 是否为网络节点（可中继信号）

    std::string damageEffect;  ///< damage susceptibility model 损伤敏感性模型

    // 数据库交互
    // static void AddSqlColumns(std::string& columnString);
    // void ReadSql(tcSqlReader& entry);
    // void WriteSql(std::string& valueString) const;
    void WritePythonValue(std::string& valueString) const;
    void WritePython(std::string& valueString) const;
    virtual  std::shared_ptr<tcCommDevice> CreateComm(std::shared_ptr<tcGameObject> parent); ///< factory method

    // 构造与析构
    tcCommDeviceDBObject();
    tcCommDeviceDBObject(const tcCommDeviceDBObject& obj);
    virtual ~tcCommDeviceDBObject();

    // 参数计算（例如将角度转为弧度、计算实际通信距离）
    void CalculateEffectiveParams();
    virtual void SerializeToJson(rapidjson::Value& obj, rapidjson::Document::AllocatorType& allocator) const override;

protected:
    // 可扩展的保护成员（例如内部缓存机制）
    float mfCachedWeatherImpact; ///< 当前天气影响的缓存值
};

} // namespace database


#endif // TCCOMMDEVICEDBOBJECT_H
