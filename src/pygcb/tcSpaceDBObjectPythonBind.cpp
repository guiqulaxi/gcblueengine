#include"tcPythonBind.h"

#include <tcSpaceDBObject.h>

using namespace database;
void BindSpaceDBObject(module &m)
{
    py::class_<tcSpaceDBObject,std::shared_ptr<tcSpaceDBObject>,tcPlatformDBObject>(m, "tcSpaceDBObject")
    .def(py::init<>())
        .def_readwrite("flightportClass", &tcSpaceDBObject::flightportClass);
}
