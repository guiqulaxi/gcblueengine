
#include"tcPythonBind.h"
#include <tcPlatformDBObject.h>
using namespace database;
void BindPlatformDBObject(module &m)
{
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
}
