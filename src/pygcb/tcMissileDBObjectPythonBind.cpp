#include"tcPythonBind.h"
#include <tcMissileDBObject.h>
#include <tcWaterDetectionDBObject.h>
#include <tcWeaponDBObject.h>
using namespace database;
void BindMissileDBObject(module &m)
{
    py::class_<tcMissileDBObject, std::shared_ptr<tcMissileDBObject>,tcWeaponDBObject, tcAirDetectionDBObject>(m, "tcMissileDBObject")
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
        .def_readwrite("maFlightProfile", &tcMissileDBObject::maFlightProfile)
        .def("CalculateParams",&tcMissileDBObject::CalculateParams);


}
