#include"tcPythonBind.h"
#include "tcScenarioInterface.h"
#include "tcPlatformInterface.h"
using namespace scriptinterface;
void BindScenario(module &m)
{
    py::class_<tcScenarioInterface>(m,"ScenarioInterface")
    .def(py::init<>())
        .def("AddUnitToAlliance",&tcScenarioInterface::AddUnitToAlliance)
        .def("AddUnitToFlightDeck",&tcScenarioInterface::AddUnitToFlightDeck)
        .def("AddUnitTask", &tcScenarioInterface::AddUnitTask)
        .def("AddToUnitMagazine",&tcScenarioInterface::AddToUnitMagazine)
        .def("GetUnitInterface", &tcScenarioInterface::GetUnitInterface)
        .def("GetUnitNameById", &tcScenarioInterface::GetUnitNameById)
        .def("GetUnitIdByName", &tcScenarioInterface::GetUnitIdByName)
        .def("SetUnitLauncherItem",&tcScenarioInterface::SetUnitLauncherItem)
        .def("SetFlightDeckUnitLoadout", &tcScenarioInterface::SetFlightDeckUnitLoadout)
        .def("SetUnitAlwaysVisibleState", &tcScenarioInterface::SetUnitAlwaysVisibleState)

        .def("AllianceExists", &tcScenarioInterface::AllianceExists)
        .def("CreateAlliance",&tcScenarioInterface::CreateAlliance)
        .def("SetAllianceRelationship", &tcScenarioInterface::SetAllianceRelationship)
        .def("GetAllianceRelationship", &tcScenarioInterface::GetAllianceRelationship)
        .def("SetAllianceDefaultCountry", &tcScenarioInterface::SetAllianceDefaultCountry)
        .def("GetAllianceCountry", &tcScenarioInterface::GetAllianceCountry)
        .def("SetAlliancePlayable", &tcScenarioInterface::SetAlliancePlayable)
        .def("IsAlliancePlayable", &tcScenarioInterface::IsAlliancePlayable)
        .def("GetAllianceROE", &tcScenarioInterface::GetAllianceROE)
        .def("SetAllianceROE", &tcScenarioInterface::SetAllianceROE)
        .def("SetAllianceROEByType", &tcScenarioInterface::SetAllianceROEByType)
        .def("GetDefaultUnit",&tcScenarioInterface::GetDefaultUnit)
        .def("GetRandomDatum",&tcScenarioInterface::GetRandomDatum)
        .def("GetRandomPlatformName", &tcScenarioInterface::GetRandomPlatformName)
        .def("GetParsedUnitName", &tcScenarioInterface::GetParsedUnitName)
        .def("GetUserAlliance", &tcScenarioInterface::GetUserAlliance)
        .def("SaveGame", &tcScenarioInterface::SaveGame)
        .def("SetAllianceGoal",&tcScenarioInterface::SetAllianceGoal)
        .def("GetAllianceGoal",&tcScenarioInterface::GetAllianceGoal)
        .def("GetGoalById",&tcScenarioInterface::GetGoalById)
        .def("AddChildGoalToId", &tcScenarioInterface::AddChildGoalToId)
        .def("DeleteGoalById", &tcScenarioInterface::DeleteGoalById)
        .def("SetDateTime",&tcScenarioInterface::SetDateTime)
        .def("SetDateTimeByString",&tcScenarioInterface::SetDateTimeByString)
        .def("GetScenarioDateAsString",&tcScenarioInterface::GetScenarioDateAsString)
        .def("SetPerfectScore",&tcScenarioInterface::SetPerfectScore)
        .def("SetScenarioDescription",&tcScenarioInterface::SetScenarioDescription)
        .def("SetScenarioLoaded",&tcScenarioInterface::SetScenarioLoaded)
        .def("SetScenarioName",&tcScenarioInterface::SetScenarioName)
        .def("SetScenarioLocked", &tcScenarioInterface::SetScenarioLocked)
        .def("DuplicateUnitTasking", &tcScenarioInterface::DuplicateUnitTasking)
        .def("IsUsingNATONames", &tcScenarioInterface::IsUsingNATONames)
        .def("GetDisplayName", &tcScenarioInterface::GetDisplayName)
        .def("GetUnitList", &tcScenarioInterface::GetUnitList)

        .def("SetStartTheater", &tcScenarioInterface::SetStartTheater)
        .def("SetUserAlliance",&tcScenarioInterface::SetUserAlliance)
        // time/mode events
        //                  .def("ClearEvents",&tcScenarioInterface::ClearEvents)
        //                  .def("HookPlatform",&tcScenarioInterface::HookPlatform)
        //                  .def("Pause",&tcScenarioInterface::Pause)
        //                  .def("Resume",&tcScenarioInterface::Resume)
        //                  .def("Set3DMode",&tcScenarioInterface::Set3DMode)
        //                  .def("SetBriefingMode",&tcScenarioInterface::SetBriefingMode)
        //                  .def("SetEventTime",&tcScenarioInterface::SetEventTime)
        //                  // audio events
        //                  .def("PauseAudio",&tcScenarioInterface::PauseAudio)
        //                  .def("PlayAudio",&tcScenarioInterface::PlayAudio)
        //                  .def("PlayEffect",&tcScenarioInterface::PlayEffect)
        //                  .def("SeekAudio",&tcScenarioInterface::SeekAudio)
        // send command
        //            .def("SendCommand", &tcScenarioInterface::SendCommand)
        // text console and map events
        //                  .def("ChangeMapView",&tcScenarioInterface::ChangeMapView)
        //                  .def("ChangeWorldMapView",&tcScenarioInterface::ChangeWorldMapView)
        //                  .def("SetStartView",&tcScenarioInterface::SetStartView)
        //                .def("ChangeMapTheater",&tcScenarioInterface::ChangeMapTheater)
        //                  .def("ConsoleText",&tcScenarioInterface::ConsoleText)
        //                  .def("ChannelMessage", &tcScenarioInterface::ChannelMessage)
        //                  .def("MapText",&tcScenarioInterface::MapText)
        //                  // overlay graphics
        //                  .def("OverlayText", &tcScenarioInterface::OverlayText)
        //                  .def("OverlayTextInteractive", &tcScenarioInterface::OverlayTextInteractive)
        //                  // camera and 3D viewer events
        //                  .def("FlybyCamera",&tcScenarioInterface::FlybyCamera)
        //                  .def("TrackCamera",&tcScenarioInterface::TrackCamera)
        //                  .def("Text3D",&tcScenarioInterface::Text3D)
        // goal creation workaround
        .def("CompoundGoal",&tcScenarioInterface::CompoundGoal)
        .def("TimeGoal",&tcScenarioInterface::TimeGoal)
        .def("DestroyGoal",&tcScenarioInterface::DestroyGoal)
        .def("ProtectGoal",&tcScenarioInterface::ProtectGoal)
        .def("AreaGoal",&tcScenarioInterface::AreaGoal)
        // simple briefing text
        .def("SetSimpleBriefing", &tcScenarioInterface::SetSimpleBriefing)
        // database query
        .def("GetPlatformListByClass", &tcScenarioInterface::GetPlatformListByClass)
        .def("SetFilterByYear", &tcScenarioInterface::SetFilterByYear)
        .def("GetFilterByYear", &tcScenarioInterface::GetFilterByYear)
        .def("SetFilterByCountry", &tcScenarioInterface::SetFilterByCountry)
        .def("GetFilterByCountry", &tcScenarioInterface::GetFilterByCountry)
        .def("QueryDatabase", &tcScenarioInterface::QueryDatabase)

        // database management
        .def("LoadDatabaseMod", &tcScenarioInterface::LoadDatabaseMod)
        .def("RestoreDefaultDatabase", &tcScenarioInterface::RestoreDefaultDatabase)

        // more scenario edit commands, started Oct 2008
        .def("SetAirGroupName", &tcScenarioInterface::SetAirGroupName)
        .def("GetAirGroupName", &tcScenarioInterface::GetAirGroupName)
        .def("GetAirUnitId", &tcScenarioInterface::GetAirUnitId)
        .def("SetAirGroupCount", &tcScenarioInterface::SetAirGroupCount)
        .def("GetAirGroupCount", &tcScenarioInterface::GetAirGroupCount)
        .def("SetMagazineAddCount", &tcScenarioInterface::SetMagazineAddCount)
        .def("GetMagazineAddCount", &tcScenarioInterface::GetMagazineAddCount)

        // scenario randomization commands
        .def("SetIncludeProbability", &tcScenarioInterface::SetIncludeProbability)
        .def("IncludeUnit", &tcScenarioInterface::IncludeUnit)
        .def("AddRandomBox", &tcScenarioInterface::AddRandomBox)

        // sonar
        .def("SetSeaState", &tcScenarioInterface::SetSeaState)
        .def("GetSeaState", &tcScenarioInterface::GetSeaState)
        .def("SetSVP", &tcScenarioInterface::SetSVP)
        .def("SetSonarTemplate", &tcScenarioInterface::SetSonarTemplate)
        .def("GetSonarTemplate", &tcScenarioInterface::GetSonarTemplate)
        .def("GetNumberSonarTemplates", &tcScenarioInterface::GetNumberSonarTemplates)
        .def("GetTemplateName", &tcScenarioInterface::GetTemplateName)
        .def("SetEditMode", &tcScenarioInterface::SetEditMode)
        .def("SetTimeAccel", &tcScenarioInterface::SetTimeAccel)
        .def("ClearScenario", &tcScenarioInterface::ClearScenario)
        .def("LoadScenario", &tcScenarioInterface::LoadScenario)
        ;
}
