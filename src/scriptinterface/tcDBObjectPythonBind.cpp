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
#include "tcECMDBObject.h"
#include "tcESMDBObject.h"
#include "tcFlightportDBObject.h"
#include "tcFuelTankDBObject.h"
#include "tcGroundDBObject.h"
#include "tcJetDBObject.h"
#include "tcLauncherDBObject.h"
#include "tcMissileDBObject.h"
#include "tcOpticalDBObject.h"
#include "tcRadarDBObject.h"
#include "tcShipDBObject.h"
#include "tcSonarDBObject.h"
#include "tcSonobuoyDBObject.h"
#include "tcSpaceDBObject.h"
#include "tcStoresDBObject.h"
#include "tcSubDBObject.h"
#include "tcTorpedoDBObject.h"
#include "tcTableObject.h"
#include "tcWeaponDamage.h"
#include "tcDamageEffect.h"
#include "tcItemDBObject.h"
using namespace database;
void BindDBObject(module &m)
{
    py::class_<tcDBString>(m, "tcDBString")
    .def(py::init<>(), "默认构造函数")
        .def(py::init<const char*>(), "接受C风格字符串的构造函数", py::arg("buff"))
        .def(py::init<const tcDBString&>(), "复制构造函数", py::arg("src"))
        .def("AssignRandomString", &tcDBString::AssignRandomString, "分配一个随机字符串")
        .def("AssignRandomStringB", &tcDBString::AssignRandomStringB, "分配另一个随机字符串（可能是不同的实现）")
        .def("AssignRandomSuffix", &tcDBString::AssignRandomSuffix, "向现有字符串添加随机后缀")
        .def("c_str", &tcDBString::c_str, py::return_value_policy::copy, "返回C风格字符串的副本")
        .def("size", &tcDBString::size, "返回字符串的大小")
        // 绑定赋值操作符
        .def("__setitem__", [](tcDBString& self, const std::string& index, const std::string& value) {
            if (index.empty()) { // 假设我们不支持索引赋值，只支持整体赋值
                self = tcDBString(value.c_str());
            } else {
                throw std::runtime_error("tcDBString不支持索引赋值");
            }
        }, "不支持索引赋值，只支持整体赋值")
        .def("__eq__", [](const tcDBString& self, const std::string& other) {
            return self == other.c_str();
        }, py::is_operator(), "与C风格字符串的比较操作符")
        .def("__eq__", [](const tcDBString& self, const tcDBString& other) {
            return self == other;
        }, py::is_operator(), "与另一个tcDBString的比较操作符")
        .def("__str__", [](const tcDBString& self) {
            return std::string(self.c_str()); // 返回Python字符串
        }, "返回字符串的Python表示");

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
        .def_readwrite("notes", &tcDatabaseObject::notes);

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
    pybind11::class_<tcSensorPlatformDBObject>(m, "tcSensorPlatformDBObject")
        .def(pybind11::init<>()) // 绑定默认构造函数
        .def_readwrite("sensorClass", &tcSensorPlatformDBObject::sensorClass)
        .def_readwrite("sensorId", &tcSensorPlatformDBObject::sensorId)
        .def_readwrite("sensorAz", &tcSensorPlatformDBObject::sensorAz);
    // .def_static("MAXSENSORS", (int)tcSensorPlatformDBObject::MAXSENSORS, "Maximum number of sensor entries supported in database");
    pybind11::class_<tcPlatformDBObject, tcDatabaseObject, tcSensorPlatformDBObject>(m, "PlatformDBObject")
        .def(pybind11::init<>())
        .def_readwrite("mfMaxSpeed_kts", &tcPlatformDBObject::mfMaxSpeed_kts)
        .def_readwrite("mfAccel_ktsps", &tcPlatformDBObject::mfAccel_ktsps)
        .def_readwrite("mfTurnRate_degps", &tcPlatformDBObject::mfTurnRate_degps)
        .def_readwrite("mfFuelCapacity_kg", &tcPlatformDBObject::mfFuelCapacity_kg)
        .def_readwrite("mfFuelRate_kgps", &tcPlatformDBObject::mfFuelRate_kgps)
        .def_readwrite("mfToughness", &tcPlatformDBObject::mfToughness)
        .def_readwrite("damageEffect", &tcPlatformDBObject::damageEffect)
        .def_readwrite("mnNumLaunchers", &tcPlatformDBObject::mnNumLaunchers)
        .def_readwrite("mnNumMagazines", &tcPlatformDBObject::mnNumMagazines)
        .def_readwrite("maLauncherClass", &tcPlatformDBObject::maLauncherClass)
        .def_readwrite("maMagazineClass", &tcPlatformDBObject::maMagazineClass)
        .def_readwrite("magazineId", &tcPlatformDBObject::magazineId)
        .def_readwrite("launcherId", &tcPlatformDBObject::launcherId)
        .def_readwrite("launcherDescription", &tcPlatformDBObject::launcherDescription)
        .def_readwrite("launcherName", &tcPlatformDBObject::launcherName)
        .def_readwrite("launcherFOV_deg", &tcPlatformDBObject::launcherFOV_deg)
        .def_readwrite("launcherAz_deg", &tcPlatformDBObject::launcherAz_deg)
        .def_readwrite("launcherEl_deg", &tcPlatformDBObject::launcherEl_deg)
        .def_readwrite("launcherFireControl", &tcPlatformDBObject::launcherFireControl)
        .def_readwrite("launcherFireControl2", &tcPlatformDBObject::launcherFireControl2)
        .def_readwrite("launcherIsReloadable", &tcPlatformDBObject::launcherIsReloadable);/*
        .def_static("MAXLAUNCHERS", tcPlatformDBObject::MAXLAUNCHERS, "Maximum number of launchers")
        .def_static("MAXANIMATIONS", tcPlatformDBObject::MAXANIMATIONS, "Maximum number of animations")
        .def_static("MAXMAGAZINES", tcPlatformDBObject::MAXMAGAZINES, "Maximum number of magazines");*/

    py::class_<tcSignatureModel>(m, "tcSignatureModel")
        .def(pybind11::init<>())
        .def_readwrite("mzClass", &tcSignatureModel::mzClass)
        .def_readwrite("aspectModifier_dB", &tcSignatureModel::aspectModifier_dB)
        .def_readwrite("topModifier_dB", &tcSignatureModel::topModifier_dB)
        .def_readwrite("bottomModifier_dB", &tcSignatureModel::bottomModifier_dB)
        .def("GetModifier", &tcSignatureModel::GetModifier, "az_deg"_a, "el_deg"_a);
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
        .def_readwrite("irSignatureC", &tcAirDetectionDBObject::irSignatureC);

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
        .def_readwrite("detonationRange_m", &tcWeaponDBObject::detonationRange_m);


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

    py::class_<tcBallisticMissileDBObject, tcWeaponDBObject, tcAirDetectionDBObject>(m, "tcBallisticMissileDBObject")
        .def(py::init<>()) // 假设有一个默认构造函数
        .def_readwrite("gmax", &tcBallisticMissileDBObject::gmax)
        .def_readwrite("timeStage1_s", &tcBallisticMissileDBObject::timeStage1_s)
        .def_readwrite("accelStage1_mps2", &tcBallisticMissileDBObject::accelStage1_mps2)
        .def_readwrite("bcStage1", &tcBallisticMissileDBObject::bcStage1)
        .def_readwrite("inv_bcStage1", &tcBallisticMissileDBObject::inv_bcStage1)
        .def_readwrite("timeStage2_s", &tcBallisticMissileDBObject::timeStage2_s)
        .def_readwrite("accelStage2_mps2", &tcBallisticMissileDBObject::accelStage2_mps2)
        .def_readwrite("bcStage2", &tcBallisticMissileDBObject::bcStage2)
        .def_readwrite("inv_bcStage2", &tcBallisticMissileDBObject::inv_bcStage2)
        .def_readwrite("timeStage3_s", &tcBallisticMissileDBObject::timeStage3_s)
        .def_readwrite("accelStage3_mps2", &tcBallisticMissileDBObject::accelStage3_mps2)
        .def_readwrite("bcStage3", &tcBallisticMissileDBObject::bcStage3)
        .def_readwrite("inv_bcStage3", &tcBallisticMissileDBObject::inv_bcStage3)
        .def_readwrite("timeStage4_s", &tcBallisticMissileDBObject::timeStage4_s)
        .def_readwrite("accelStage4_mps2", &tcBallisticMissileDBObject::accelStage4_mps2)
        .def_readwrite("bcStage4", &tcBallisticMissileDBObject::bcStage4)
        .def_readwrite("inv_bcStage4", &tcBallisticMissileDBObject::inv_bcStage4)
        .def_readwrite("thrustShutoffTime_s", &tcBallisticMissileDBObject::thrustShutoffTime_s);

    py::class_<tcWaterDetectionDBObject>(m, "tcWaterDetectionDBObject")
        .def(py::init<>())
        .def_readwrite("TS", &tcWaterDetectionDBObject::TS)
        .def_readwrite("TS_Model", &tcWaterDetectionDBObject::TS_Model)
        .def_readwrite("acousticModel", &tcWaterDetectionDBObject::acousticModel)
        .def_readwrite("SL_Model", &tcWaterDetectionDBObject::SL_Model);
    py::class_<tcCounterMeasureDBObject,
               tcDatabaseObject, tcAirDetectionDBObject,
               tcWaterDetectionDBObject>(m, "tcCounterMeasureDBObject")
        .def(py::init<>()) // 假设有一个默认构造函数
        .def_readwrite("subType", &tcCounterMeasureDBObject::subType)
        .def_readwrite("lifeSpan_s", &tcCounterMeasureDBObject::lifeSpan_s)
        .def_readwrite("effectiveness", &tcCounterMeasureDBObject::effectiveness)
        .def_readwrite("maxSpeed_mps", &tcCounterMeasureDBObject::maxSpeed_mps);
    py::class_<tcCountryData>(m, "tcCountryData")
        .def(py::init<>())
        .def_readwrite("countryName", &tcCountryData::countryName)
        .def_readwrite("navalEnsign", &tcCountryData::navalEnsign);
    py::class_<tcSensorDBObject,tcDatabaseObject>(m, "tcSensorDBObject")
        .def(py::init<>())
        .def_readwrite("mfMaxRange_km", &tcSensorDBObject::mfMaxRange_km)
        .def_readwrite("mfRefRange_km", &tcSensorDBObject::mfRefRange_km)
        .def_readwrite("mfFieldOfView_deg", &tcSensorDBObject::mfFieldOfView_deg)
        .def_readwrite("minElevation_deg", &tcSensorDBObject::minElevation_deg)
        .def_readwrite("maxElevation_deg", &tcSensorDBObject::maxElevation_deg)
        .def_readwrite("mfScanPeriod_s", &tcSensorDBObject::mfScanPeriod_s)
        .def_readwrite("damageEffect", &tcSensorDBObject::damageEffect)
        .def_readwrite("rangeError", &tcSensorDBObject::rangeError)
        .def_readwrite("angleError_deg", &tcSensorDBObject::angleError_deg)
        .def_readwrite("elevationError_deg", &tcSensorDBObject::elevationError_deg)
        .def_readwrite("minFrequency_Hz", &tcSensorDBObject::minFrequency_Hz)
        .def_readwrite("maxFrequency_Hz", &tcSensorDBObject::maxFrequency_Hz)
        .def_readwrite("idThreshold_dB", &tcSensorDBObject::idThreshold_dB)
        .def_readwrite("counterMeasureFactor", &tcSensorDBObject::counterMeasureFactor)
        .def_readwrite("isSurveillance", &tcSensorDBObject::isSurveillance);
    py::class_<tcECMDBObject,tcSensorDBObject>(m, "tcECMDBObject")
        .def(py::init<>())
        .def_readwrite("ecmType", &tcECMDBObject::ecmType)
        .def_readwrite("ERP_dBW", &tcECMDBObject::ERP_dBW)
        .def_readwrite("effectivenessRating", &tcECMDBObject::effectivenessRating)
        .def_readwrite("isEffectiveVsSurveillance", &tcECMDBObject::isEffectiveVsSurveillance)
        .def_readwrite("isEffectiveVsSeeker", &tcECMDBObject::isEffectiveVsSeeker);
    py::class_< tcESMDBObject,tcSensorDBObject>(m, "tcESMDBObject")
        .def(py::init<>())
        .def_readwrite("ecmType", &tcESMDBObject::isRWR);
    py::class_<tcFlightportDBObject,tcDatabaseObject>(m, "tcFlightportDBObject")
        .def(py::init<>())
        .def_readwrite("heloOnly", &tcFlightportDBObject::heloOnly)
        .def_readwrite("hangarCapacity", &tcFlightportDBObject::hangarCapacity)
        .def_readwrite("spotInfo", &tcFlightportDBObject::spotInfo);

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
        .def_readwrite("fuelCapacity_kg", &tcFuelTankDBObject::fuelCapacity_kg);

    py::class_<tcGroundDBObject,tcPlatformDBObject,tcAirDetectionDBObject>(m, "tcGroundDBObject")
        .def(py::init<>())
        .def_readwrite("flightportClass", &tcGroundDBObject::flightportClass);
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
        .def_readwrite("maintenanceMax_s", &tcAirDBObject::maintenanceMax_s);
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
        .def_readwrite("stallSpeed_mps", &tcJetDBObject::stallSpeed_mps);

    py::class_<tcLauncherDBObject,tcDatabaseObject>(m, "tcLauncherDBObject")
        .def(py::init<>()) // Default constructor
        // Add other member functions if needed
        .def_readwrite("childClassList", &tcLauncherDBObject::childClassList)
        .def_readwrite("childCapacityList", &tcLauncherDBObject::childCapacityList)
        .def_readwrite("childLoadTime_s", &tcLauncherDBObject::childLoadTime_s)
        .def_readwrite("childCycleTime_s", &tcLauncherDBObject::childCycleTime_s);

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

    py::class_<tcMissileDBObject, tcWeaponDBObject, tcAirDetectionDBObject>(m, "tcMissileDBObject")
        .def(py::init<>())
        .def_readwrite("mfDragArea_sm", &tcMissileDBObject::mfDragArea_sm)
        .def_readwrite("mfGmax", &tcMissileDBObject::mfGmax)
        .def_readwrite("mfMaxTurnRate_degps", &tcMissileDBObject::mfMaxTurnRate_degps)
        .def_readwrite("mfCdpsub", &tcMissileDBObject::mfCdpsub)
        .def_readwrite("mfCdptran", &tcMissileDBObject::mfCdptran)
        .def_readwrite("mfCdpsup", &tcMissileDBObject::mfCdpsup)
        .def_readwrite("mfMcm", &tcMissileDBObject::mfMcm)
        .def_readwrite("mfMsupm", &tcMissileDBObject::mfMsupm)
        .def_readwrite("mfBoostThrust_N", &tcMissileDBObject::mfBoostThrust_N)
        .def_readwrite("mfBoostTime_s", &tcMissileDBObject::mfBoostTime_s)
        .def_readwrite("mfSustThrust_N", &tcMissileDBObject::mfSustThrust_N)
        .def_readwrite("mfSustTime_s", &tcMissileDBObject::mfSustTime_s)
        .def_readwrite("mfShutdownSpeed_mps", &tcMissileDBObject::mfShutdownSpeed_mps)
        .def_readwrite("maSensorClass", &tcMissileDBObject::maSensorClass)
        .def_readwrite("sensorKey", &tcMissileDBObject::sensorKey)
        .def_readwrite("needsFireControl", &tcMissileDBObject::needsFireControl)
        .def_readwrite("acceptsWaypoints", &tcMissileDBObject::acceptsWaypoints)
        .def_readwrite("fireAndForget", &tcMissileDBObject::fireAndForget)
        .def_readwrite("isARM", &tcMissileDBObject::isARM)
        .def_readwrite("seekerFOV_rad", &tcMissileDBObject::seekerFOV_rad)
        .def_readwrite("aczConstant_kts", &tcMissileDBObject::aczConstant_kts)
        .def_readwrite("invMass_kg", &tcMissileDBObject::invMass_kg)
        .def_readwrite("mnNumSegments", &tcMissileDBObject::mnNumSegments)
        .def_readwrite("maFlightProfile", &tcMissileDBObject::maFlightProfile);

    py::class_<tcOpticalDBObject,tcSensorDBObject>(m, "tcOpticalDBObject")
        .def(py::init<>()) // 默认构造函数
        .def_readwrite("maxFireControlTracks", &tcOpticalDBObject::maxFireControlTracks)
        .def_readwrite("isSemiactive", &tcOpticalDBObject::isSemiactive)
        .def_readwrite("isDesignator", &tcOpticalDBObject::isDesignator)
        .def_readwrite("mbDetectsSurface", &tcOpticalDBObject::mbDetectsSurface)
        .def_readwrite("mbDetectsAir", &tcOpticalDBObject::mbDetectsAir)
        .def_readwrite("mbDetectsMissile", &tcOpticalDBObject::mbDetectsMissile)
        .def_readwrite("mbDetectsGround", &tcOpticalDBObject::mbDetectsGround)
        .def_readwrite("isIR", &tcOpticalDBObject::isIR)
        .def_readwrite("nightFactor", &tcOpticalDBObject::nightFactor);
    py::class_<tcRadarDBObject, tcSensorDBObject>(m, "tcRadarDBObject")
        .def(py::init<>())
        .def_readwrite("ERPpeak_dBW", &tcRadarDBObject::ERPpeak_dBW)
        .def_readwrite("ERPaverage_dBW", &tcRadarDBObject::ERPaverage_dBW)
        .def_readwrite("maxFireControlTracks", &tcRadarDBObject::maxFireControlTracks)
        .def_readwrite("isSemiactive", &tcRadarDBObject::isSemiactive)
        .def_readwrite("blindSpeed_mps", &tcRadarDBObject::blindSpeed_mps)
        .def_readwrite("lookdownWater_dB", &tcRadarDBObject::lookdownWater_dB)
        .def_readwrite("lookdownLand_dB", &tcRadarDBObject::lookdownLand_dB)
        .def_readwrite("bandwidth_Hz", &tcRadarDBObject::bandwidth_Hz)
        .def_readwrite("azimuthBeamwidth_deg", &tcRadarDBObject::azimuthBeamwidth_deg)
        .def_readwrite("elevationBeamwidth_deg", &tcRadarDBObject::elevationBeamwidth_deg)
        .def_readwrite("effectiveSidelobes_dB", &tcRadarDBObject::effectiveSidelobes_dB)
        .def_readwrite("mbDetectsSurface", &tcRadarDBObject::mbDetectsSurface)
        .def_readwrite("mbDetectsAir", &tcRadarDBObject::mbDetectsAir)
        .def_readwrite("mbDetectsMissile", &tcRadarDBObject::mbDetectsMissile)
        .def_readwrite("mbDetectsGround", &tcRadarDBObject::mbDetectsGround)
        .def_readwrite("invBlindSpeed_mps", &tcRadarDBObject::invBlindSpeed_mps)
        .def_readwrite("antennaGain", &tcRadarDBObject::antennaGain)
        .def_readwrite("antennaGain_dBi", &tcRadarDBObject::antennaGain_dBi)
        .def_readwrite("invAzBeamwidth_deg", &tcRadarDBObject::invAzBeamwidth_deg)
        .def_readwrite("invElBeamwidth_deg", &tcRadarDBObject::invElBeamwidth_deg)
        .def_readwrite("cpi_s", &tcRadarDBObject::cpi_s)
        .def_readwrite("jamConstant_dB", &tcRadarDBObject::jamConstant_dB);


    py::class_<tcShipDBObject,tcPlatformDBObject,tcAirDetectionDBObject,tcWaterDetectionDBObject>(m, "tcShipDBObject")
        .def(py::init<>())
        .def_readwrite("draft_m", &tcShipDBObject::draft_m)
        .def_readwrite("length_m", &tcShipDBObject::length_m)
        .def_readwrite("beam_m", &tcShipDBObject::beam_m)
        .def_readwrite("PowerPlantType", &tcShipDBObject::PowerPlantType)
        .def_readwrite("TotalShaft_HP", &tcShipDBObject::TotalShaft_HP)
        .def_readwrite("ExhaustStacks", &tcShipDBObject::ExhaustStacks)
        .def_readwrite("PropulsionShafts", &tcShipDBObject::PropulsionShafts)
        .def_readwrite("PropulsiveEfficiency", &tcShipDBObject::PropulsiveEfficiency)
        .def_readwrite("CivilianPaintScheme", &tcShipDBObject::CivilianPaintScheme)
        .def_readwrite("FlashyPaintScheme", &tcShipDBObject::FlashyPaintScheme)
        .def_readwrite("flightportClass", &tcShipDBObject::flightportClass);

    py::class_<tcSonarDBObject,tcSensorDBObject>(m, "tcSonarDBObject")
        .def(py::init<>())
        .def_readwrite("SL", &tcSonarDBObject::SL)
        .def_readwrite("DI", &tcSonarDBObject::DI)
        .def_readwrite("minFrequency_Hz", &tcSonarDBObject::minFrequency_Hz)
        .def_readwrite("maxFrequency_Hz", &tcSonarDBObject::maxFrequency_Hz)
        .def_readwrite("isPassive", &tcSonarDBObject::isPassive)
        .def_readwrite("isActive", &tcSonarDBObject::isActive)
        .def_readwrite("isTowed", &tcSonarDBObject::isTowed)
        .def_readwrite("maxScope_m", &tcSonarDBObject::maxScope_m)
        .def_readwrite("isWakeHoming", &tcSonarDBObject::isWakeHoming)
        .def_readwrite("alpha", &tcSonarDBObject::alpha)
        .def_readwrite("averageFreq_Hz", &tcSonarDBObject::averageFreq_Hz);

    py::class_<tcSonobuoyDBObject,tcDatabaseObject,  tcSensorPlatformDBObject,  tcWaterDetectionDBObject>(m, "tcSonobuoyDBObject")
        .def(py::init<>())
        .def_readwrite("batteryLife_s", &tcSonobuoyDBObject::batteryLife_s)
        .def_readwrite("commRange_km", &tcSonobuoyDBObject::commRange_km);

    py::class_<tcSpaceDBObject,tcPlatformDBObject>(m, "tcSpaceDBObject")
        .def(py::init<>());
    py::class_<tcStoresDBObject>(m, "tcStoresDBObject")
        .def(py::init<>())
        .def_readwrite("displayName", &tcStoresDBObject::displayName)
        .def_readwrite("capacity", &tcStoresDBObject::capacity)
        .def_readwrite("maxVolume_m3", &tcStoresDBObject::maxVolume_m3)
        .def_readwrite("maxWeight_kg", &tcStoresDBObject::maxWeight_kg)
        .def_readwrite("moveTime", &tcStoresDBObject::moveTime)
        .def_readwrite("compatibleItems", &tcStoresDBObject::compatibleItems);

    py::class_<tcSubDBObject,tcPlatformDBObject,  tcAirDetectionDBObject,  tcWaterDetectionDBObject>(m, "tcSubDBObject")
        .def(py::init<>())
        .def_readwrite("draft_m", &tcSubDBObject::draft_m)
        .def_readwrite("surfaceSpeed_kts", &tcSubDBObject::surfaceSpeed_kts)
        .def_readwrite("mfMaxDepth_m", &tcSubDBObject::mfMaxDepth_m)
        .def_readwrite("isDieselElectric", &tcSubDBObject::isDieselElectric)
        .def_readwrite("batteryCapacity_kJ", &tcSubDBObject::batteryCapacity_kJ)
        .def_readwrite("batteryRate_kW", &tcSubDBObject::batteryRate_kW)
        .def_readwrite("batteryCharge_kW", &tcSubDBObject::batteryCharge_kW);

    py::class_<tcTorpedoDBObject, tcWeaponDBObject, tcWaterDetectionDBObject>(m, "tcTorpedoDBObject")
        .def(py::init<>())
        .def_readwrite("maxTurnRate_degps", &tcTorpedoDBObject::maxTurnRate_degps)
        .def_readwrite("maxDepth_m", &tcTorpedoDBObject::maxDepth_m)
        .def_readwrite("battery_kJ", &tcTorpedoDBObject::battery_kJ)
        .def_readwrite("batteryRate_kW", &tcTorpedoDBObject::batteryRate_kW)
        .def_readwrite("maxSpeed_kts", &tcTorpedoDBObject::maxSpeed_kts)
        .def_readwrite("acceleration_ktsps", &tcTorpedoDBObject::acceleration_ktsps)
        .def_readwrite("sonarClass", &tcTorpedoDBObject::sonarClass)
        .def_readwrite("wireGuidance", &tcTorpedoDBObject::wireGuidance)
        .def_readwrite("preEnableSpeed_kts", &tcTorpedoDBObject::preEnableSpeed_kts)
        .def_readwrite("weaponType", &tcTorpedoDBObject::weaponType)
        .def_readwrite("maxTurnRate_radps", &tcTorpedoDBObject::maxTurnRate_radps)
        .def_readwrite("batteryRate_kWpkt", &tcTorpedoDBObject::batteryRate_kWpkt);

    py::class_<tcTableObject>(m, "tcTableObject")
        .def(py::init<>())
        .def_readwrite("databaseClass", &tcTableObject::databaseClass);

    py::class_<tcWeaponDamage, tcTableObject>(m, "tcWeaponDamage")
        .def(py::init<>())
        .def_readwrite("maxRange_m", &tcWeaponDamage::maxRange_m)
        .def_readwrite("probDetonate", &tcWeaponDamage::probDetonate)
        .def_readwrite("isPenetration", &tcWeaponDamage::isPenetration)
        .def_readwrite("blastCharge_kg", &tcWeaponDamage::blastCharge_kg)
        .def_readwrite("fragCharge_kg", &tcWeaponDamage::fragCharge_kg)
        .def_readwrite("radCharge_kg", &tcWeaponDamage::radCharge_kg)
        .def_readwrite("fragMetal_kg", &tcWeaponDamage::fragMetal_kg)
        .def_readwrite("fragFragment_kg", &tcWeaponDamage::fragFragment_kg)
        .def_readwrite("fragSpread", &tcWeaponDamage::fragSpread);




    py::class_<tcDamageEffect::DamagePoint>(m, "DamagePoint")
        .def(py::init<>())
        .def_readwrite("effectLevel", &tcDamageEffect::DamagePoint::effectLevel)
        .def_readwrite("damageFactor", &tcDamageEffect::DamagePoint::damageFactor);
    py::class_<tcDamageEffect,tcTableObject>(m, "tcDamageEffect")
        .def(py::init<>())
        .def_readwrite("blastEffect", &tcDamageEffect::blastEffect)
        .def_readwrite("waterBlastEffect", &tcDamageEffect::waterBlastEffect)
        .def_readwrite("fragEffect", &tcDamageEffect::fragEffect)
        .def_readwrite("radEffect", &tcDamageEffect::radEffect)
        .def_readwrite("internalEffect", &tcDamageEffect::internalEffect);

    py::class_<tcItemDBObject , tcDatabaseObject>(m, "tcItemDBObject")
        .def(py::init<>());
}

