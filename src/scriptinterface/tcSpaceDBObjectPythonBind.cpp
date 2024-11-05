#include"tcPythonBind.h"

#include <tcSpaceDBObject.h>

using namespace database;
void BindSpaceDBObject(module &m)
{
    py::class_<tcSpaceDBObject,tcPlatformDBObject>(m, "tcSpaceDBObject")
    .def(py::init<>());
}
