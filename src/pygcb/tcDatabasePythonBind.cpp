#include "tcPythonBind.h"
#include "tcDatabaseInterface.h"
using namespace scriptinterface ;
void BindDatabase(module &m)
{
    py::class_<tcDatabaseInterface>(m, "tcDatabaseInterface")
        .def(py::init<>())
        .def("Clear", &tcDatabaseInterface::Clear)
        .def("ClearForNewScenario", &tcDatabaseInterface::ClearForNewScenario)
        // .def("CreateObjectCopy", &tcDatabaseInterface::CreateObjectCopy)
        .def("DeleteObject", &tcDatabaseInterface::DeleteObject)
        .def("GetRandomKey", &tcDatabaseInterface::GetRandomKey)
        .def("GetRandomOfType", &tcDatabaseInterface::GetRandomOfType, py::return_value_policy::reference_internal) // 可能需要调整返回策略
        .def("GetPlatformNames", &tcDatabaseInterface::GetPlatformNames, py::return_value_policy::copy)
        // .def("GetPlatformNamesByDate", &tcDatabaseInterface::GetPlatformNamesByDate, py::return_value_policy::copy)
        // .def("GetPlatformHulls", &tcDatabaseInterface::GetPlatformHulls, py::return_value_policy::copy)
        .def("GetDisplayName", &tcDatabaseInterface::GetDisplayName, py::return_value_policy::copy)
        // .def("CheckForErrors", &tcDatabaseInterface::CheckForErrors)
        // .def("CheckTableReferences", &tcDatabaseInterface::CheckTableReferences)
        .def("GetSize", &tcDatabaseInterface::GetSize)
        .def("GetObjectByKey", &tcDatabaseInterface::GetObjectByKey,py::return_value_policy::reference_internal)
        .def("GetObjectByClassName", &tcDatabaseInterface::GetObjectByClassName,py::return_value_policy::reference_internal)
        .def("GetObjectClassName", &tcDatabaseInterface::GetObjectClassName, py::return_value_policy::copy)
        .def("WildcardSearch", &tcDatabaseInterface::WildcardSearch, py::return_value_policy::copy)
        .def("WildcardSearchLoaded", &tcDatabaseInterface::WildcardSearchLoaded, py::return_value_policy::copy)
        .def("GetObjectClass", &tcDatabaseInterface::GetObjectClass)
        .def("GetNextObjectOfSameClass", &tcDatabaseInterface::GetNextObjectOfSameClass)
        .def("GetPrevObjectOfSameClass", &tcDatabaseInterface::GetPrevObjectOfSameClass)
        .def("GetKey", &tcDatabaseInterface::GetKey)
        .def("GetVersion", &tcDatabaseInterface::GetVersion, py::arg("v1"), py::arg("v2"), py::arg("v3"))
        .def("GetCountryList", &tcDatabaseInterface::GetCountryList, py::return_value_policy::copy)
        .def("AddOrUpdateObject", &tcDatabaseInterface::AddOrUpdateObject, "rpobj"_a, py::return_value_policy::copy);
}
