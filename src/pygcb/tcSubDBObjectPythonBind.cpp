#include"tcPythonBind.h"

#include <tcSubDBObject.h>
using namespace database;
void BindSubDBObject(module &m)
{
    py::class_<tcSubDBObject,std::shared_ptr<tcSubDBObject>,tcPlatformDBObject>(m, "tcSubDBObject")
    .def(py::init<>())
        .def_readwrite("draft_m", &tcSubDBObject::draft_m)
        .def_readwrite("surfaceSpeed_kts", &tcSubDBObject::surfaceSpeed_kts)
        .def_readwrite("mfMaxDepth_m", &tcSubDBObject::mfMaxDepth_m)
        .def_readwrite("isDieselElectric", &tcSubDBObject::isDieselElectric)
        .def_readwrite("batteryCapacity_kJ", &tcSubDBObject::batteryCapacity_kJ)
        .def_readwrite("batteryRate_kW", &tcSubDBObject::batteryRate_kW)
        .def_readwrite("batteryCharge_kW", &tcSubDBObject::batteryCharge_kW)
        .def("CalculateParams", &tcSubDBObject::CalculateParams);

}

