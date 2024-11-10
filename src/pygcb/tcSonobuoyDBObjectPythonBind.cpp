#include"tcPythonBind.h"
#include <tcSonobuoyDBObject.h>
#include <tcTorpedoDBObject.h>
#include <tcWaterDetectionDBObject.h>
#include <tcWeaponDBObject.h>
using namespace database;
void BindSonobuoyDBObject(module &m)
{
    py::class_<tcSonobuoyDBObject,tcDatabaseObject,  tcSensorPlatformDBObject,  tcWaterDetectionDBObject>(m, "tcSonobuoyDBObject")
    .def(py::init<>())
        .def_readwrite("batteryLife_s", &tcSonobuoyDBObject::batteryLife_s)
        .def_readwrite("commRange_km", &tcSonobuoyDBObject::commRange_km);
}
