#include "tcPythonBind.h"
#include "tcDatabaseObject.h"
#include "tcECMDBObject.h"
#include "tcESMDBObject.h"
#include "tcOpticalDBObject.h"
#include "tcRadarDBObject.h"
#include "tcSonarDBObject.h"
#include "tcTorpedoDBObject.h"

using namespace database;
void BindSensorDBObject(module &m)
{
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
}
