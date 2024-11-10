#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>
#include "Game.h"
namespace py = pybind11;
using namespace py;
//内嵌模块


PYBIND11_MODULE(pygame, m) {


    // 绑定tcGame类
    py::class_<tcGame>(m, "tcGame")
        .def(py::init<>()) // 绑定默认构造函数
        .def("EndGame", &tcGame::EndGame)
        .def("Finish", &tcGame::Finish)
        .def("Init", &tcGame::Init)
        .def("InitSim", &tcGame::InitSim)
        .def("CheckGoals", &tcGame::CheckGoals)
        .def("CheckMultiplayerEndGame", &tcGame::CheckMultiplayerEndGame)
        .def("HookRandomFriendly", &tcGame::HookRandomFriendly)
        .def("ProcessCommandList", &tcGame::ProcessCommandList)
        .def("ProcessTextCommand", &tcGame::ProcessTextCommand, py::arg("cmd_info"))
        .def("AddCommand", &tcGame::AddCommand, py::arg("cmd"))
        .def("SetScenarioEdit", &tcGame::SetScenarioEdit, py::arg("state"))
        .def("SetTheater", &tcGame::SetTheater, py::arg("lat_deg"), py::arg("lon_deg"))
        .def("SetTimeAccel", &tcGame::SetTimeAccel, py::arg("accel"))
        .def("NextTimeAccelVal", &tcGame::NextTimeAccelVal, py::arg("current"), py::arg("goFaster"))
        .def("ShiftTime", &tcGame::ShiftTime, py::arg("delta_s"))
        .def("SynchTimeAcceleration", &tcGame::SynchTimeAcceleration)
        .def("UninitGame", &tcGame::UninitGame)
        .def("UpdateFrame", &tcGame::UpdateFrame)
        .def("UpdateStart", &tcGame::UpdateStart)
        .def("UpdateOptions", &tcGame::UpdateOptions)
        .def("GetClientSyncFactor", &tcGame::GetClientSyncFactor)
        .def("ValidateHooked", &tcGame::ValidateHooked)
        .def("SetInGame", &tcGame::SetInGame, py::arg("state"))
        .def("LoadDatabase", &tcGame::LoadDatabase, py::arg("filePath"))
        .def("LoadScenario", &tcGame::LoadScenario, py::arg("filePath"), py::arg("caption"), py::arg("startInEditMode"))
        .def("GetOutSimData", &tcGame::GetOutSimData);

}


