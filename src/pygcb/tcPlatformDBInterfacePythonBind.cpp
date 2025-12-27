#include "tcPythonBind.h"
#include "tcPlatformDBInterface.h"
using namespace scriptinterface ;
void BindPlatformDBInterface(module &m)
{
    py::class_<tcPlatformDBInterface>(m,"UnitDBInfoClass")
    .def(py::init<>())
        // navigation related commands
        .def("IsValid", &tcPlatformDBInterface::IsValid)
        .def("GetClassName", &tcPlatformDBInterface::GetClassName)
        .def("SetClassName", &tcPlatformDBInterface::SetClassName)
        // Static database queries
        .def_static("PlatformDBObjectExists", &tcPlatformDBInterface::PlatformDBObjectExists)
        .def_static("GetPlatformObject", &tcPlatformDBInterface::GetPlatformObject);
        ;
}
