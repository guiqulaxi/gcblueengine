#include "tcPythonBind.h"

#include "tcDatabaseObject.h"
#include "tcAcousticModel.h"
#include "tcSensorPlatformDBObject.h"
#include "tcPlatformDBObject.h"
#include "tcSignatureModel.h"
#include "tcAirDetectionDBObject.h"
#include "tcWeaponDBObject.h"
#include "tcBallisticDBObject.h"
#include "tcBallisticMissileDBObject.h"
#include "tcCounterMeasureDBObject.h"
#include "tcCountryData.h"

#include "tcFlightportDBObject.h"
#include "tcFuelTankDBObject.h"
#include "tcGroundDBObject.h"
#include "tcJetDBObject.h"
#include "tcLauncherDBObject.h"
#include "tcMissileDBObject.h"
#include "tcShipDBObject.h"

#include "tcSpaceDBObject.h"
#include "tcStoresDBObject.h"


#include "tcItemDBObject.h"
using namespace database;

void BindDBObject(module &m)
{
    // py::class_<tcDBString>(m, "tcDBString")
    // .def(py::init<>(), "默认构造函数")
    //     .def(py::init<const char*>(), "接受C风格字符串的构造函数", py::arg("buff"))
    //     .def(py::init<const std::string&>())
    //     .def(py::init<const tcDBString&>(), "复制构造函数", py::arg("src"))
    //     .def("AssignRandomString", &tcDBString::AssignRandomString, "分配一个随机字符串")
    //     .def("AssignRandomStringB", &tcDBString::AssignRandomStringB, "分配另一个随机字符串（可能是不同的实现）")
    //     .def("AssignRandomSuffix", &tcDBString::AssignRandomSuffix, "向现有字符串添加随机后缀")
    //     .def("c_str", &tcDBString::c_str, py::return_value_policy::copy, "返回C风格字符串的副本")
    //     .def("size", &tcDBString::size, "返回字符串的大小")
    //     // 绑定赋值操作符
    //     .def("__setitem__", [](tcDBString& self, const std::string& index, const std::string& value) {
    //         if (index.empty()) { // 假设我们不支持索引赋值，只支持整体赋值
    //             self = tcDBString(value.c_str());
    //         } else {
    //             throw std::runtime_error("tcDBString不支持索引赋值");
    //         }
    //     }, "不支持索引赋值，只支持整体赋值")
    //     .def("__eq__", [](const tcDBString& self, const std::string& other) {
    //         return self == other.c_str();
    //     }, py::is_operator(), "与C风格字符串的比较操作符")
    //     .def("__eq__", [](const tcDBString& self, const tcDBString& other) {
    //         return self == other;
    //     }, py::is_operator(), "与另一个tcDBString的比较操作符")
    //     .def("__str__", [](const tcDBString& self) {
    //         return std::string(self.c_str()); // 返回Python字符串
    //     }, "返回字符串的Python表示");

    py::class_<tcDatabaseObject>(m, "tcDatabaseObject")
        .def(pybind11::init<>()) // 绑定默认构造函数
        .def_readwrite("mzClass", &tcDatabaseObject::mzClass)
        .def_readwrite("natoClass", &tcDatabaseObject::natoClass)
        .def_readwrite("mnKey", &tcDatabaseObject::mnKey)
        .def_readwrite("mnType", &tcDatabaseObject::mnType)
        .def_readwrite("mnModelType", &tcDatabaseObject::mnModelType)
        .def_readwrite("cost", &tcDatabaseObject::cost)
        .def_readwrite("weight_kg", &tcDatabaseObject::weight_kg)
        .def_readwrite("volume_m3", &tcDatabaseObject::volume_m3)
        .def_readwrite("initialYear", &tcDatabaseObject::initialYear)
        .def_readwrite("finalYear", &tcDatabaseObject::finalYear)
        .def_readwrite("length_m", &tcDatabaseObject::length_m)
        .def_readwrite("width_m", &tcDatabaseObject::width_m)
        .def_readwrite("height_m", &tcDatabaseObject::height_m)
        .def_readwrite("country", &tcDatabaseObject::country)
        .def_readwrite("designation", &tcDatabaseObject::designation)
        .def_readwrite("imageList", &tcDatabaseObject::imageList)
        .def_readwrite("iconFileName", &tcDatabaseObject::iconFileName) // 如果tcDBString是std::string的别名
        .def_readwrite("mz3DModelFileName", &tcDatabaseObject::mz3DModelFileName) // 同上
        .def_readwrite("mzDescription", &tcDatabaseObject::mzDescription)
        .def_readwrite("notes", &tcDatabaseObject::notes)
        .def("CalculateParams", &tcDatabaseObject::CalculateParams);

    pybind11::class_<tcAcousticModel>(m, "tcAcousticModel")
        .def(pybind11::init<>()) // 绑定默认构造函数
        .def_readwrite("databaseClass", &tcAcousticModel::databaseClass)
        .def_readwrite("xSpeed_kts", &tcAcousticModel::xSpeed_kts)
        .def_readwrite("ySL_dB", &tcAcousticModel::ySL_dB)
        .def_readwrite("speedMinNL_kts", &tcAcousticModel::speedMinNL_kts)
        .def_readwrite("NL_min", &tcAcousticModel::NL_min)
        .def_readwrite("speedMaxNL_kts", &tcAcousticModel::speedMaxNL_kts)
        .def_readwrite("NL_max", &tcAcousticModel::NL_max)
        .def_readwrite("cavitationOffset_kts", &tcAcousticModel::cavitationOffset_kts)
        .def_readwrite("cavitationSlope_ktsperft", &tcAcousticModel::cavitationSlope_ktsperft)
        .def_readwrite("cavitationSL_dB", &tcAcousticModel::cavitationSL_dB)
        .def_readwrite("snorkelingSL_dB", &tcAcousticModel::snorkelingSL_dB);
    py::class_<tcSignatureModel>(m, "tcSignatureModel")
        .def(pybind11::init<>())
        .def_readwrite("mzClass", &tcSignatureModel::mzClass)
        .def_readwrite("aspectModifier_dB", &tcSignatureModel::aspectModifier_dB)
        .def_readwrite("topModifier_dB", &tcSignatureModel::topModifier_dB)
        .def_readwrite("bottomModifier_dB", &tcSignatureModel::bottomModifier_dB)
        .def("GetModifier", &tcSignatureModel::GetModifier, "az_deg"_a, "el_deg"_a);
    pybind11::class_<tcSensorPlatformDBObject>(m, "tcSensorPlatformDBObject")
        .def(pybind11::init<>()) // 绑定默认构造函数
        .def_readwrite("sensorClass", &tcSensorPlatformDBObject::sensorClass)
        .def_readwrite("sensorId", &tcSensorPlatformDBObject::sensorId)
        .def_readwrite("sensorAz", &tcSensorPlatformDBObject::sensorAz);
    // .def_static("MAXSENSORS", (int)tcSensorPlatformDBObject::MAXSENSORS, "Maximum number of sensor entries supported in database");
    BindPlatformDBObject(m);

    pybind11::class_<tcAirDetectionDBObject>(m, "tcAirDetectionDBObject")
        .def(pybind11::init<>())
        .def_readwrite("RCS_dBsm", &tcAirDetectionDBObject::RCS_dBsm)
        .def_readwrite("RCS_Model", &tcAirDetectionDBObject::RCS_Model)
        .def_readwrite("opticalCrossSection_dBsm", &tcAirDetectionDBObject::opticalCrossSection_dBsm)
        .def_readwrite("irSignature_dB", &tcAirDetectionDBObject::irSignature_dB)
        .def_readwrite("IR_ModelA", &tcAirDetectionDBObject::IR_ModelA)
        .def_readwrite("IR_ModelB", &tcAirDetectionDBObject::IR_ModelB)
        .def_readwrite("IR_ModelC", &tcAirDetectionDBObject::IR_ModelC)
        .def_readwrite("effectiveHeight_m", &tcAirDetectionDBObject::effectiveHeight_m)
        .def_readwrite("radarSignature", &tcAirDetectionDBObject::radarSignature)
        .def_readwrite("irSignatureA", &tcAirDetectionDBObject::irSignatureA)
        .def_readwrite("irSignatureB", &tcAirDetectionDBObject::irSignatureB)
        .def_readwrite("irSignatureC", &tcAirDetectionDBObject::irSignatureC)
        .def("BindSignatureModels",&tcAirDetectionDBObject::BindSignatureModels);

    py::class_<tcWeaponDBObject, tcDatabaseObject>(m, "tcWeaponDBObject")
        .def(py::init<>())
        .def_readwrite("mfDamage", &tcWeaponDBObject::mfDamage)
        .def_readwrite("damageModel", &tcWeaponDBObject::damageModel)
        .def_readwrite("damageEffect", &tcWeaponDBObject::damageEffect)
        .def_readwrite("launchSpeed_mps", &tcWeaponDBObject::launchSpeed_mps)
        .def_readwrite("targetFlags", &tcWeaponDBObject::targetFlags)
        .def_readwrite("minLaunchAlt_m", &tcWeaponDBObject::minLaunchAlt_m)
        .def_readwrite("maxLaunchAlt_m", &tcWeaponDBObject::maxLaunchAlt_m)
        .def_readwrite("minRange_km", &tcWeaponDBObject::minRange_km)
        .def_readwrite("maxRange_km", &tcWeaponDBObject::maxRange_km)
        .def_readwrite("probNoFaults", &tcWeaponDBObject::probNoFaults)
        .def_readwrite("payloadClass", &tcWeaponDBObject::payloadClass)
        .def_readwrite("payloadQuantity", &tcWeaponDBObject::payloadQuantity)
        .def_readwrite("datalinkRange_km", &tcWeaponDBObject::datalinkRange_km)
        .def_readwrite("acceptsUserCommands", &tcWeaponDBObject::acceptsUserCommands)
        .def_readwrite("detonationRange_m", &tcWeaponDBObject::detonationRange_m)
        .def("CalculateParams",&tcWeaponDBObject::CalculateParams);

    py::class_<tcBallisticDBObject, tcWeaponDBObject>(m, "tcBallisticDBObject")
        .def(py::init<>()) // 假设tcBallisticDBObject有一个默认构造函数
        .def_readwrite("ballisticType", &tcBallisticDBObject::ballisticType)
        .def_readwrite("angleError_rad", &tcBallisticDBObject::angleError_rad)
        .def_readwrite("burstCount", &tcBallisticDBObject::burstCount)
        .def_readwrite("burstDuration_s", &tcBallisticDBObject::burstDuration_s)
        .def_readwrite("clusterCount", &tcBallisticDBObject::clusterCount)
        .def_readwrite("clusterEffectRadius_m", &tcBallisticDBObject::clusterEffectRadius_m)
        .def_readwrite("sensorClass", &tcBallisticDBObject::sensorClass)
        .def_readwrite("smartMaxClimb_rad", &tcBallisticDBObject::smartMaxClimb_rad)
        .def_readwrite("smartError_m", &tcBallisticDBObject::smartError_m)
        .def_readwrite("lockOnAfterLaunch", &tcBallisticDBObject::lockOnAfterLaunch)
        .def_readwrite("sensorKey", &tcBallisticDBObject::sensorKey)
        .def_readwrite("one_over_launchSpeed", &tcBallisticDBObject::one_over_launchSpeed)
        .def_readwrite("launchSpeed2", &tcBallisticDBObject::launchSpeed2);



    py::class_<tcWaterDetectionDBObject>(m, "tcWaterDetectionDBObject")
        .def(py::init<>())
        .def_readwrite("TS", &tcWaterDetectionDBObject::TS)
        .def_readwrite("TS_Model", &tcWaterDetectionDBObject::TS_Model)
        .def_readwrite("acousticModel", &tcWaterDetectionDBObject::acousticModel)
        .def_readwrite("SL_Model", &tcWaterDetectionDBObject::SL_Model)
        .def("BindSignatureModels",&tcWaterDetectionDBObject::BindSignatureModels);
    py::class_<tcCounterMeasureDBObject,
               tcDatabaseObject, tcAirDetectionDBObject,
               tcWaterDetectionDBObject>(m, "tcCounterMeasureDBObject")
        .def(py::init<>()) // 假设有一个默认构造函数
        .def_readwrite("subType", &tcCounterMeasureDBObject::subType)
        .def_readwrite("lifeSpan_s", &tcCounterMeasureDBObject::lifeSpan_s)
        .def_readwrite("effectiveness", &tcCounterMeasureDBObject::effectiveness)
        .def_readwrite("maxSpeed_mps", &tcCounterMeasureDBObject::maxSpeed_mps)
        .def("CalculateParams",&tcCounterMeasureDBObject::CalculateParams);

    py::class_<tcCountryData>(m, "tcCountryData")
        .def(py::init<>())
        .def_readwrite("countryName", &tcCountryData::countryName)
        .def_readwrite("navalEnsign", &tcCountryData::navalEnsign);

    py::class_<tcFlightportDBObject,tcDatabaseObject>(m, "tcFlightportDBObject")
        .def(py::init<>())
        .def_readwrite("heloOnly", &tcFlightportDBObject::heloOnly)
        .def_readwrite("hangarCapacity", &tcFlightportDBObject::hangarCapacity)
        .def_readwrite("spotInfo", &tcFlightportDBObject::spotInfo)
        .def("CalculateParams",&tcFlightportDBObject::CalculateParams);

    py::class_<tcFlightportDBObject::spotDBInfo>(m, "spotDBInfo")
        .def(py::init<>())
        .def_readwrite("isLaunch", &tcFlightportDBObject::spotDBInfo::isLaunch)
        .def_readwrite("x", &tcFlightportDBObject::spotDBInfo::x)
        .def_readwrite("y", &tcFlightportDBObject::spotDBInfo::y)
        .def_readwrite("z", &tcFlightportDBObject::spotDBInfo::z)
        .def_readwrite("orientation_deg", &tcFlightportDBObject::spotDBInfo::orientation_deg)
        .def_readwrite("length", &tcFlightportDBObject::spotDBInfo::length);

    py::class_<tcFuelTankDBObject,tcDatabaseObject>(m, "tcFuelTankDBObject")
        .def(py::init<>())
        .def_readwrite("fuelCapacity_kg", &tcFuelTankDBObject::fuelCapacity_kg)
        .def("CalculateParams",&tcFuelTankDBObject::CalculateParams);

    py::class_<tcGroundDBObject,tcPlatformDBObject,tcAirDetectionDBObject>(m, "tcGroundDBObject")
        .def(py::init<>())
        .def_readwrite("flightportClass", &tcGroundDBObject::flightportClass)
        .def("CalculateParams",&tcFuelTankDBObject::CalculateParams);
    py::class_<tcAirDBObject,tcPlatformDBObject, tcAirDetectionDBObject, tcWaterDetectionDBObject>(m, "tcAirDBObject")
        .def(py::init<>())
        .def_readwrite("maxTakeoffWeight_kg", &tcAirDBObject::maxTakeoffWeight_kg)
        .def_readwrite("maxAltitude_m", &tcAirDBObject::maxAltitude_m)
        .def_readwrite("climbRate_mps", &tcAirDBObject::climbRate_mps)
        .def_readwrite("gmax", &tcAirDBObject::gmax)
        .def_readwrite("minimumRunway_m", &tcAirDBObject::minimumRunway_m)
        .def_readwrite("isCarrierCompatible", &tcAirDBObject::isCarrierCompatible)
        .def_readwrite("outFuelPods", &tcAirDBObject::outFuelPods)
        .def_readwrite("fuelOut_kgps", &tcAirDBObject::fuelOut_kgps)
        .def_readwrite("fuelIn_kgps", &tcAirDBObject::fuelIn_kgps)
        .def_readwrite("maintenanceMin_s", &tcAirDBObject::maintenanceMin_s)
        .def_readwrite("maintenanceMax_s", &tcAirDBObject::maintenanceMax_s)
        .def("CalculateParams",&tcAirDBObject::CalculateParams);
    py::class_<tcJetDBObject,tcAirDBObject>(m, "tcJetDBObject")
        .def(py::init<>())
        .def_readwrite("militaryThrust_N", &tcJetDBObject::militaryThrust_N)
        .def_readwrite("militaryThrustSpeedSlope", &tcJetDBObject::militaryThrustSpeedSlope)
        .def_readwrite("mfAfterburnThrust_N", &tcJetDBObject::mfAfterburnThrust_N)
        .def_readwrite("abThrustSpeedSlope", &tcJetDBObject::abThrustSpeedSlope)
        .def_readwrite("mfAfterburnFuelRate_kgps", &tcJetDBObject::mfAfterburnFuelRate_kgps)
        .def_readwrite("mfCdpsub", &tcJetDBObject::mfCdpsub)
        .def_readwrite("mfCdptran", &tcJetDBObject::mfCdptran)
        .def_readwrite("mfCdpsup", &tcJetDBObject::mfCdpsup)
        .def_readwrite("mfMcm", &tcJetDBObject::mfMcm)
        .def_readwrite("mfMsupm", &tcJetDBObject::mfMsupm)
        .def_readwrite("cruiseSpeed_mps", &tcJetDBObject::cruiseSpeed_mps)
        .def_readwrite("stallSpeed_mps", &tcJetDBObject::stallSpeed_mps)
        .def("CalculateParams",&tcJetDBObject::CalculateParams);

    py::class_<tcLauncherDBObject,tcDatabaseObject>(m, "tcLauncherDBObject")
        .def(py::init<>()) // Default constructor
        // Add other member functions if needed
        .def_readwrite("childClassList", &tcLauncherDBObject::childClassList)
        .def_readwrite("childCapacityList", &tcLauncherDBObject::childCapacityList)
        .def_readwrite("childLoadTime_s", &tcLauncherDBObject::childLoadTime_s)
        .def_readwrite("childCycleTime_s", &tcLauncherDBObject::childCycleTime_s)
        .def("CalculateParams",&tcLauncherDBObject::CalculateParams);

    py::class_<tsMissileFlightSegment>(m, "tsMissileFlightSegment")
        .def(py::init<>())
        .def_readwrite("mfRange_km", &tsMissileFlightSegment::mfRange_km)
        .def_readwrite("mfAltitude_m", &tsMissileFlightSegment::mfAltitude_m)
        .def_readwrite("meAltitudeMode", &tsMissileFlightSegment::meAltitudeMode)
        .def_readwrite("meGuidanceMode", &tsMissileFlightSegment::meGuidanceMode);
    py::enum_<teAltitudeMode>(m, "teAltitudeMode")
        .value("AM_ASL", teAltitudeMode::AM_ASL)
        .value("AM_AGL", teAltitudeMode::AM_AGL)
        .value("AM_INTERCEPT", teAltitudeMode::AM_INTERCEPT)
        .value("AM_DATUM", teAltitudeMode::AM_DATUM)
        .value("AM_INTERCEPT_HIGH", teAltitudeMode::AM_INTERCEPT_HIGH)
        .value("AM_ASL_LOFT", teAltitudeMode::AM_ASL_LOFT)
        .export_values();

    // 绑定 teGuidanceMode 枚举
    py::enum_<teGuidanceMode>(m, "teGuidanceMode")
        .value("GM_COMMAND", teGuidanceMode::GM_COMMAND)
        .value("GM_NAV", teGuidanceMode::GM_NAV)
        .value("GM_SENSOR1", teGuidanceMode::GM_SENSOR1)
        .value("GM_DEPLOY", teGuidanceMode::GM_DEPLOY)
        .export_values();


    BindMissileDBObject(m);

    BindShipDBObject(m);




    py::class_<tcStoresDBObject>(m, "tcStoresDBObject")
        .def(py::init<>())
        .def_readwrite("displayName", &tcStoresDBObject::displayName)
        .def_readwrite("capacity", &tcStoresDBObject::capacity)
        .def_readwrite("maxVolume_m3", &tcStoresDBObject::maxVolume_m3)
        .def_readwrite("maxWeight_kg", &tcStoresDBObject::maxWeight_kg)
        .def_readwrite("moveTime", &tcStoresDBObject::moveTime)
        .def_readwrite("compatibleItems", &tcStoresDBObject::compatibleItems);
    BindSonobuoyDBObject(m);
    BindSubDBObject(m);
    BindTorpedoDBObject(m);

    py::class_<tcItemDBObject , tcDatabaseObject>(m, "tcItemDBObject")
        .def(py::init<>());
}
