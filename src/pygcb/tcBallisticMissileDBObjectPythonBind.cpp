#include"tcPythonBind.h"

#include <tcBallisticMissileDBObject.h>

using namespace database;
void BindBallisticMissileDBObject( module&m ){

        py::class_<tcBallisticMissileDBObject,std::shared_ptr<tcBallisticMissileDBObject>,tcWeaponDBObject>(m, "tcBallisticMissileDBObject")
            .def(py::init<>()) // 假设有一个默认构造函数
            .def_readwrite("gmax", &tcBallisticMissileDBObject::gmax)
            .def_readwrite("timeStage1_s", &tcBallisticMissileDBObject::timeStage1_s)
            .def_readwrite("accelStage1_mps2", &tcBallisticMissileDBObject::accelStage1_mps2)
            .def_readwrite("bcStage1", &tcBallisticMissileDBObject::bcStage1)
            .def_readwrite("inv_bcStage1", &tcBallisticMissileDBObject::inv_bcStage1)
            .def_readwrite("timeStage2_s", &tcBallisticMissileDBObject::timeStage2_s)
            .def_readwrite("accelStage2_mps2", &tcBallisticMissileDBObject::accelStage2_mps2)
            .def_readwrite("bcStage2", &tcBallisticMissileDBObject::bcStage2)
            .def_readwrite("inv_bcStage2", &tcBallisticMissileDBObject::inv_bcStage2)
            .def_readwrite("timeStage3_s", &tcBallisticMissileDBObject::timeStage3_s)
            .def_readwrite("accelStage3_mps2", &tcBallisticMissileDBObject::accelStage3_mps2)
            .def_readwrite("bcStage3", &tcBallisticMissileDBObject::bcStage3)
            .def_readwrite("inv_bcStage3", &tcBallisticMissileDBObject::inv_bcStage3)
            .def_readwrite("timeStage4_s", &tcBallisticMissileDBObject::timeStage4_s)
            .def_readwrite("accelStage4_mps2", &tcBallisticMissileDBObject::accelStage4_mps2)
            .def_readwrite("bcStage4", &tcBallisticMissileDBObject::bcStage4)
            .def_readwrite("inv_bcStage4", &tcBallisticMissileDBObject::inv_bcStage4)
            .def_readwrite("thrustShutoffTime_s", &tcBallisticMissileDBObject::thrustShutoffTime_s);
}
