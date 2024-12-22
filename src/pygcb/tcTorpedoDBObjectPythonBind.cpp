#include"tcPythonBind.h"
#include <tcTorpedoDBObject.h>
#include <tcWaterDetectionDBObject.h>
#include <tcWeaponDBObject.h>
using namespace database;


void BindTorpedoDBObject(module &m)
{
    py::class_<tcTorpedoDBObject,std::shared_ptr<tcTorpedoDBObject>, tcWeaponDBObject, tcWaterDetectionDBObject>(m, "tcTorpedoDBObject")
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
        .def_readwrite("batteryRate_kWpkt", &tcTorpedoDBObject::batteryRate_kWpkt)
        .def("CalculateParams",&tcTorpedoDBObject::CalculateParams);

}
