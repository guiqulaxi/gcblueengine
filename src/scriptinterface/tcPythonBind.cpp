#include "tcPythonBind.h"

#include <ScriptedTaskInterface.h>
#include "tcFlightPortInterface.h"
#include "tcPlatformInterface.h"
#include "tcMissionInterface.h"
#include "tcGroupInterface.h"
#include "tcTrackInterface.h"
#include "BlackboardInterface.h"
#include "tcWeaponInterface.h"
#include "tcScenarioInterface.h"
#include "BlackboardItem.h"
using namespace scriptinterface;
//内嵌模块
PYBIND11_EMBEDDED_MODULE(gcblue, m) {
    BindDBObject(m);
    BindDatabase(m);
    BindFlightPort(m);
    BindSensorDBObject(m);
    BindTrack(m);

    py::class_<tcMissionInterface>(m,"MissionInterface")

        .def("IsValid", &tcMissionInterface::IsValid)
        .def("GetAirborneAircraftCount", &tcMissionInterface::GetAirborneAircraftCount)
        .def("GetAirborneAircraftId", &tcMissionInterface::GetAirborneAircraftId)
        .def("GetMissionAircraftCount", &tcMissionInterface::GetMissionAircraftCount)
        .def("GetSmallestWaypointIndex", &tcMissionInterface::GetSmallestWaypointIndex)
        .def("GetLocalObj", &tcMissionInterface::GetLocalObj)
        ;
    class_<BlackboardInterface>(m,"BlackboardInterface")
        .def_readonly("author", &BlackboardInterface::author)
        .def_readonly("priority", &BlackboardInterface::priority)
        .def("Erase", &BlackboardInterface::Erase)
        .def("KeyExists", &BlackboardInterface::KeyExists)
        .def("Read", &BlackboardInterface::Read)
        .def("ReadAuthor", &BlackboardInterface::ReadAuthor)
        .def("ReadMessage", &BlackboardInterface::ReadMessage)
        .def("ReadPriority", &BlackboardInterface::ReadPriority)
        .def("Write", &BlackboardInterface::Write)
        .def("WriteGlobal", &BlackboardInterface::WriteGlobal)
        ;

    BindPlatform(m);

    py::class_<tcFormationPosition>(m,"FormationPosition")
        .def_readwrite("range_km",&tcFormationPosition::range_km)
        .def_readwrite("span_km",&tcFormationPosition::span_km)
        .def_readwrite("bearing_rad",&tcFormationPosition::bearing_rad)
        .def_readwrite("span_rad",&tcFormationPosition::span_rad)
        ;

    py::class_<GeoPoint>(m,"GeoPoint")
        .def_readonly("Alt",&GeoPoint::mfAlt_m)
        .def_readonly("Lon",&GeoPoint::mfLon_rad)
        .def_readonly("Lat",&GeoPoint::mfLat_rad)
        ;

    py::class_<tcLauncherInfo>(m,"LauncherInfo")
        .def_readonly("Launcher",&tcLauncherInfo::mnLauncher)   // index of launcher, or -1 for none
        .def_readonly("Quantity",&tcLauncherInfo::mnQuantity)
        .def_readonly("TargetFlags",&tcLauncherInfo::mnTargetFlags) // 0x01 - surface, 0x02 - air, 0x04 - land
        .def_readonly("Range_km",&tcLauncherInfo::mfRange_km)
        .def_readonly("MinLaunchAlt_m", &tcLauncherInfo::minLaunchAlt_m)
        .def_readonly("MaxLaunchAlt_m", &tcLauncherInfo::maxLaunchAlt_m)
        .def_readonly("MinRange_km", &tcLauncherInfo::minRange_km)
        .def_readonly("MaxRange_km", &tcLauncherInfo::maxRange_km)
        .def_readonly("LaunchMode",&tcLauncherInfo::mnLaunchMode)  // 0 - datum, 1 - handoff
        .def_readonly("MaxDepth_m",&tcLauncherInfo::maxDepth_m)
        .def_readonly("Speed_mps", &tcLauncherInfo::speed_mps)
        .def_readonly("SectorCenter", &tcLauncherInfo::sectorCenter)
        .def_readonly("SectorWidth", &tcLauncherInfo::sectorWidth)
        .def_readonly("FireControlTracks", &tcLauncherInfo::fireControlTracks)
        .def_readonly("MaxFireControlTracks", &tcLauncherInfo::maxFireControlTracks)
        .def_readonly("IsNuclear", &tcLauncherInfo::isNuclear)
        .def_readonly("IsLoading", &tcLauncherInfo::isLoading)
        .def_readonly("AcceptsWaypoints", &tcLauncherInfo::acceptsWaypoints)
        .def_readonly("LifeTime_s", &tcLauncherInfo::lifeTime_s)
        .def_readonly("Status", &tcLauncherInfo::launcherStatus)
        .def("IsValid", &tcLauncherInfo::IsValid)
        ;

    py::class_<tcSensorInfo>(m,"SensorInfo")
        .def_readonly("isActive",&tcSensorInfo::isActive)
        .def_readonly("type",&tcSensorInfo::type)
        .def("IsPassive", &tcSensorInfo::IsPassive)
        ;

    py::class_<tcFireControlInfo>(m,"FireControlInfo")
        .def_readonly("radarGuidanceActive", &tcFireControlInfo::radarGuidanceActive)
        .def_readonly("maxLeft_deg", &tcFireControlInfo::maxLeft_deg)
        .def_readonly("maxRight_deg", &tcFireControlInfo::maxRight_deg)
        .def_readonly("weaponsOut", &tcFireControlInfo::weaponsOut)
        ;

    py::class_<EmitterInfo>(m,"EmitterInfo")
        .def_readonly("EmitterID", &EmitterInfo::mnEmitterID)
        .def_readonly("Timestamp", &EmitterInfo::mfTimestamp)
        .def_readonly("Mode", &EmitterInfo::mnMode)
        .def("GetEmitterName", &EmitterInfo::GetEmitterName)
        ;

    py::class_<tcGroupInterface>(m,"GroupInterfaceClass")
        .def(py::init<>())
        .def("GetPlatformInterface", &tcGroupInterface::GetPlatformInterface)
        .def("GetWeaponInterface", &tcGroupInterface::GetWeaponInterface)
        .def("GetUnitCount", &tcGroupInterface::GetUnitCount)
        .def("GetUnitId", &tcGroupInterface::GetUnitId)
        .def("IsPlatform", &tcGroupInterface::IsPlatform)
        .def("IsWeapon", &tcGroupInterface::IsWeapon)
        .def("GetTankerList", &tcGroupInterface::GetTankerList)
        .def("LookupUnit", &tcGroupInterface::LookupUnit)
        .def("LookupUnitIdx", &tcGroupInterface::LookupUnitIdx)
        .def("TakeControl", &tcGroupInterface::TakeControl)
        .def("ReleaseControl", &tcGroupInterface::ReleaseControl)
        .def("GetUserInput", &tcGroupInterface::GetUserInput)
        .def("GetScenarioInterface", &tcGroupInterface::GetScenarioInterface);

    py::class_<tcSubInterface>(m,"SubInterfaceClass")
        .def("GetBatteryFraction", &tcSubInterface::GetBatteryFraction)
        .def("GetMaxDepth", &tcSubInterface::GetMaxDepth)
        .def("GoToPeriscopeDepth", &tcSubInterface::GoToPeriscopeDepth)
        .def("IsAtPeriscopeDepth", &tcSubInterface::IsAtPeriscopeDepth)
        .def("IsDieselElectric", &tcSubInterface::IsDieselElectric)
        .def("IsPeriscopeRaised", &tcSubInterface::IsPeriscopeRaised)
        .def("IsRadarMastRaised", &tcSubInterface::IsRadarMastRaised)
        .def("IsSnorkeling", &tcSubInterface::IsSnorkeling)
        .def("IsValid", &tcSubInterface::IsValid)
        .def("LowerPeriscope", &tcSubInterface::LowerPeriscope)
        .def("LowerRadarMast", &tcSubInterface::LowerRadarMast)
        .def("RaisePeriscope", &tcSubInterface::RaisePeriscope)
        .def("RaiseRadarMast", &tcSubInterface::RaiseRadarMast)
        .def("SetSnorkelState", &tcSubInterface::SetSnorkelState)
        .def("GetCavitatingSpeed", &tcSubInterface::GetCavitatingSpeed)
        ;


    py::class_<tcTrackInterface>(m,"TrackInterfaceClass")
        .def(py::init<>())
        .def("DeclareHostile", &tcTrackInterface::DeclareHostile)
        .def("DeclareNeutral", &tcTrackInterface::DeclareNeutral)
        .def("DeclareFriendly", &tcTrackInterface::DeclareFriendly)
        .def("DropTrack", &tcTrackInterface::DropTrack)
        .def("UpdateAmbiguityList", &tcTrackInterface::UpdateAmbiguityList)
        ;
    py::class_<tcWeaponInterface>(m,"WeaponInterface")
        .def(py::init<>())
        .def("IsValid", &tcWeaponInterface::IsValid)
        .def("GetWeaponType", &tcWeaponInterface::GetWeaponType)
        .def("IsLinkActive", &tcWeaponInterface::IsLinkActive)
        .def("UpdateTargetPosition", &tcWeaponInterface::UpdateTargetPosition)
        .def("DisplayMessage", &tcWeaponInterface::DisplayMessage)
        .def("GetPlatformName", &tcWeaponInterface::GetPlatformName)
        .def("GetPlatformClass", &tcWeaponInterface::GetPlatformClass)
        .def("GetPlatformAlliance", &tcWeaponInterface::GetPlatformAlliance)
        .def("GetLongitude", &tcWeaponInterface::GetLongitude)
        .def("GetLatitude", &tcWeaponInterface::GetLatitude)
        .def("GetAltitude", &tcWeaponInterface::GetAltitude)
        .def("GetHeading", &tcWeaponInterface::GetHeading)
        .def("GetSpeed", &tcWeaponInterface::GetSpeed)
        .def("DeletePlatform", &tcWeaponInterface::DeletePlatform)
        .def("MovePlatform", &tcWeaponInterface::MovePlatform)
        .def("RenamePlatform", &tcWeaponInterface::RenamePlatform)
        .def("GetScenarioInterface", &tcWeaponInterface::GetScenarioInterface)
        .def("GetLocalObj", &tcWeaponInterface::GetLocalObj)
        ;


    py::class_<tcDatum>(m,"Datum")
        .def_readwrite("lat",&tcDatum::lat)
        .def_readwrite("lon",&tcDatum::lon)
        .def_readwrite("alt",&tcDatum::alt)
        ;

    py::class_<tcScenarioUnit>(m,"ScenarioUnit")
        .def_readwrite("className",&tcScenarioUnit::className)
        .def_readwrite("unitName",&tcScenarioUnit::unitName)
        .def_readwrite("lat",&tcScenarioUnit::lat)
        .def_readwrite("lon",&tcScenarioUnit::lon)
        .def_readwrite("alt",&tcScenarioUnit::alt)
        .def_readwrite("heading",&tcScenarioUnit::heading)
        .def_readwrite("speed",&tcScenarioUnit::speed)
        .def_readwrite("throttle",&tcScenarioUnit::throttle)
        .def_readwrite("cost",&tcScenarioUnit::cost)
        .def("SetPosition",&tcScenarioUnit::SetPosition)
        .def("SetOrbit",&tcScenarioUnit::SetOrbit)
        ;

    py::class_<tcStringArray>(m,"StringArray")
        .def("Size", &tcStringArray::Size)
        .def("GetString", &tcStringArray::GetString)
        .def("PushBack", &tcStringArray::PushBack)
        ;

    py::class_<tcStringTable>(m,"StringTable")
        .def("Size", &tcStringTable::Size)
        .def("GetStringArray", &tcStringTable::GetStringArray)
        .def("GetRow", &tcStringTable::GetStringArray)
        .def("GetString", &tcStringTable::GetString)
        .def("PushBack", &tcStringTable::PushBack)
        ;

    py::class_<tcParsedUnitName>(m,"ParsedUnitName")
        .def_readwrite("isValid", &tcParsedUnitName::isValid)
        .def_readwrite("root", &tcParsedUnitName::root)
        .def_readwrite("separator", &tcParsedUnitName::separator)
        .def_readwrite("id", &tcParsedUnitName::id)
        ;

    py::class_<tcAllianceROEInfo>(m,"AllianceROEInfo")
        .def_readwrite("AirROE", &tcAllianceROEInfo::airROE)
        .def_readwrite("SurfaceROE", &tcAllianceROEInfo::surfaceROE)
        .def_readwrite("SubROE", &tcAllianceROEInfo::subROE)
        .def_readwrite("LandROE", &tcAllianceROEInfo::landROE)
        ;


    BindScenario(m);

    py::class_<ScriptedTaskInterface>(m,"ScriptedTaskInterface")
        .def(py::init<>())
        .def("EndTask", &ScriptedTaskInterface::EndTask)
        .def("GetBlackboardInterface", &ScriptedTaskInterface::GetBlackboardInterface)
        .def("GetPlatformInterface", &ScriptedTaskInterface::GetPlatformInterface)
        .def("SetUpdateInterval", &ScriptedTaskInterface::SetUpdateInterval)
        .def("SetTaskAttributes", &ScriptedTaskInterface::SetTaskAttributes)
        .def("GetMemoryText", &ScriptedTaskInterface::GetMemoryText)
        .def("SetMemoryText", &ScriptedTaskInterface::SetMemoryText)
        .def("GetMemoryValue", &ScriptedTaskInterface::GetMemoryValue)
        .def("SetMemoryValue", &ScriptedTaskInterface::SetMemoryValue)
        ;
    BindGoal(m);
    BindDamageDBObject(m);


}


