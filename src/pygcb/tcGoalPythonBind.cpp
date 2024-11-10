#include "tcGoal.h"
#include "tcPythonBind.h"

void BindGoal(module &m)
{
    py::class_<tcGoal>(m,"Goal")
    .def_readwrite("goalState",&tcGoal::goalState)
        .def("SetScores",&tcGoal::SetScores)
        .def("GetId", &tcGoal::GetId)
        ;

    //PyDict_SetItemString(dictionary->ptr(), "goalx", GoalType.ptr());  // does not work right


    py::class_<tcCompoundGoal, tcGoal>(m,"CompoundGoal")
        .def(py::init<int>())
        .def_readwrite("logicType", &tcCompoundGoal::logicType)
        .def("AddGoal",&tcCompoundGoal::AddGoal)
        .def("RemoveGoal",&tcCompoundGoal::RemoveGoal)
        .def("SetLogic",&tcCompoundGoal::SetLogic)
        .def("GetSubGoalCount", &tcCompoundGoal::GetSubGoalCount)
        .def("GetSubGoal", &tcCompoundGoal::GetSubGoal)
        ;

    py::class_<tcTimeGoal, tcGoal>(m,"TimeGoal")
        .def_readwrite("failTimeout", &tcTimeGoal::failTimeout)
        .def_readwrite("passTimeout", &tcTimeGoal::passTimeout)
        .def("SetFailTimeout",&tcTimeGoal::SetFailTimeout)
        .def("SetPassTimeout",&tcTimeGoal::SetPassTimeout)
        ;


    py::class_<tcDestroyGoal, tcGoal >(m,"DestroyGoal" )
        .def(py::init<const std::string &>())
        .def("GetTargetCount", &tcDestroyGoal::GetTargetCount)
        .def("GetTargetName", &tcDestroyGoal::GetTargetName)
        .def("GetQuantity", &tcDestroyGoal::GetQuantity)
        .def("SetQuantity", &tcDestroyGoal::SetQuantity)
        .def("AddTarget", &tcDestroyGoal::AddTarget)
        .def("RemoveTarget", &tcDestroyGoal::RemoveTarget)
        ;


    py::class_<tcProtectGoal, tcGoal >(m,"ProtectGoal")
        .def(py::init<const std::string &>())
        .def("GetTargetCount", &tcProtectGoal::GetTargetCount)
        .def("GetTargetName", &tcProtectGoal::GetTargetName)
        .def("GetQuantity", &tcProtectGoal::GetQuantity)
        .def("SetQuantity", &tcProtectGoal::SetQuantity)
        .def("AddTarget", &tcProtectGoal::AddTarget)
        .def("RemoveTarget", &tcProtectGoal::RemoveTarget)
        ;


    py::class_<tcAreaGoal,tcGoal >(m,"AreaGoal")
        .def("AddPoint", &tcAreaGoal::AddPoint)
        .def("AddPointDeg", &tcAreaGoal::AddPointDeg)
        .def("SetEnterGoal", &tcAreaGoal::SetEnterGoal)
        .def("SetTargetList", &tcAreaGoal::SetTargetList)
        .def("AddToTargetList", &tcAreaGoal::AddToTargetList)
        .def("SetQuantity", &tcAreaGoal::SetQuantity)
        .def("GetQuantity", &tcAreaGoal::GetQuantity)
        .def("SetTimeObjective", &tcAreaGoal::SetTimeObjective)
        .def("GetTimeObjective", &tcAreaGoal::GetTimeObjective)
        .def("SetLogicAny", &tcAreaGoal::SetLogicAny)
        .def("IsLogicAny", &tcAreaGoal::IsLogicAny)
        ;


    py::class_<tcGoalWrap>(m,"GoalWrap")
        .def("GetId", &tcGoalWrap::GetId)
        .def("GetTypeString", &tcGoalWrap::GetTypeString)
        .def("AsCompoundGoal", &tcGoalWrap::AsCompoundGoal)
        .def("AsTimeGoal", &tcGoalWrap::AsTimeGoal)
        .def("AsDestroyGoal", &tcGoalWrap::AsDestroyGoal)
        .def("AsProtectGoal", &tcGoalWrap::AsProtectGoal)
        .def("AsAreaGoal", &tcGoalWrap::AsAreaGoal)
        ;


    py::class_<tcCompoundGoalWrap>(m,"CompoundGoalWrap")
        .def("AddGoal", &tcCompoundGoalWrap::AddGoal)
        .def("GetLogicType", &tcCompoundGoalWrap::GetLogicType)
        .def("SetLogicType", &tcCompoundGoalWrap::SetLogicType)
        .def("GetSubGoalCount", &tcCompoundGoalWrap::GetSubGoalCount)
        .def("GetSubGoal", &tcCompoundGoalWrap::GetSubGoal)
        .def("GetId", &tcCompoundGoalWrap::GetId)
        ;


    py::class_<tcTimeGoalWrap>(m,"TimeGoalWrap")
        .def("GetFailTimeout", &tcTimeGoalWrap::GetFailTimeout)
        .def("SetFailTimeout", &tcTimeGoalWrap::SetFailTimeout)
        .def("GetPassTimeout", &tcTimeGoalWrap::GetPassTimeout)
        .def("SetPassTimeout", &tcTimeGoalWrap::SetPassTimeout)
        .def("GetId", &tcTimeGoalWrap::GetId)
        ;


    py::class_<tcDestroyGoalWrap>(m,"DestroyGoalWrap")
        .def("AddTarget", &tcDestroyGoalWrap::AddTarget)
        .def("RemoveTarget", &tcDestroyGoalWrap::RemoveTarget)
        .def("SetQuantity", &tcDestroyGoalWrap::SetQuantity)
        .def("GetQuantity", &tcDestroyGoalWrap::GetQuantity)
        .def("GetTargetCount", &tcDestroyGoalWrap::GetTargetCount)
        .def("GetTargetName", &tcDestroyGoalWrap::GetTargetName)
        .def("GetId", &tcDestroyGoalWrap::GetId)
        ;


    py::class_<tcProtectGoalWrap>(m,"ProtectGoalWrap")
        .def("AddTarget", &tcProtectGoalWrap::AddTarget)
        .def("RemoveTarget", &tcProtectGoalWrap::RemoveTarget)
        .def("SetQuantity", &tcProtectGoalWrap::SetQuantity)
        .def("GetQuantity", &tcProtectGoalWrap::GetQuantity)
        .def("GetTargetCount", &tcProtectGoalWrap::GetTargetCount)
        .def("GetTargetName", &tcProtectGoalWrap::GetTargetName)
        .def("GetId", &tcProtectGoalWrap::GetId)
        ;


    py::class_<tcAreaGoalWrap>(m,"AreaGoalWrap")
        .def("GetTargetString", &tcAreaGoalWrap::GetTargetString)
        .def("SetTargetList", &tcAreaGoalWrap::SetTargetList)
        .def("AddToTargetList", &tcAreaGoalWrap::AddToTargetList)
        .def("SetQuantity", &tcAreaGoalWrap::SetQuantity)
        .def("GetQuantity", &tcAreaGoalWrap::GetQuantity)
        .def("GetId", &tcAreaGoalWrap::GetId)
        .def("Clear", &tcAreaGoalWrap::Clear)
        .def("AddPoint", &tcAreaGoalWrap::AddPoint)
        .def("AddPointDeg", &tcAreaGoalWrap::AddPointDeg)
        .def("SetEnterGoal", &tcAreaGoalWrap::SetEnterGoal)
        .def("GetEnterGoal", &tcAreaGoalWrap::GetEnterGoal)
        .def("SetTimeObjective", &tcAreaGoalWrap::SetTimeObjective)
        .def("GetTimeObjective", &tcAreaGoalWrap::GetTimeObjective)
        .def("SetLogicAny", &tcAreaGoalWrap::SetLogicAny)
        .def("IsLogicAny", &tcAreaGoalWrap::IsLogicAny)
        ;
}
