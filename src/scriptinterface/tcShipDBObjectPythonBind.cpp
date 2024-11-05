#include"tcPythonBind.h"
#include <tcShipDBObject.h>
#include <tcTorpedoDBObject.h>
#include <tcWaterDetectionDBObject.h>
#include <tcWeaponDBObject.h>
using namespace database;
void BindShipDBObject(module &m)
{

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
}
