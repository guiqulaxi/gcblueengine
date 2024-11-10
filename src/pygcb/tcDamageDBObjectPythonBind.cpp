#include "tcPythonBind.h"
#include "tcTableObject.h"
#include "tcWeaponDamage.h"
#include "tcDamageEffect.h"

using namespace database;
void BindDamageDBObject(module &m)
{
    py::class_<tcTableObject>(m, "tcTableObject")
    .def(py::init<>())
        .def_readwrite("databaseClass", &tcTableObject::databaseClass);

    py::class_<tcWeaponDamage, tcTableObject>(m, "tcWeaponDamage")
        .def(py::init<>())
        .def_readwrite("maxRange_m", &tcWeaponDamage::maxRange_m)
        .def_readwrite("probDetonate", &tcWeaponDamage::probDetonate)
        .def_readwrite("isPenetration", &tcWeaponDamage::isPenetration)
        .def_readwrite("blastCharge_kg", &tcWeaponDamage::blastCharge_kg)
        .def_readwrite("fragCharge_kg", &tcWeaponDamage::fragCharge_kg)
        .def_readwrite("radCharge_kg", &tcWeaponDamage::radCharge_kg)
        .def_readwrite("fragMetal_kg", &tcWeaponDamage::fragMetal_kg)
        .def_readwrite("fragFragment_kg", &tcWeaponDamage::fragFragment_kg)
        .def_readwrite("fragSpread", &tcWeaponDamage::fragSpread);

    py::class_<tcDamageEffect::DamagePoint>(m, "DamagePoint")
        .def(py::init<>())
        .def_readwrite("effectLevel", &tcDamageEffect::DamagePoint::effectLevel)
        .def_readwrite("damageFactor", &tcDamageEffect::DamagePoint::damageFactor);
    py::class_<tcDamageEffect,tcTableObject>(m, "tcDamageEffect")
        .def(py::init<>())
        .def_readwrite("blastEffect", &tcDamageEffect::blastEffect)
        .def_readwrite("waterBlastEffect", &tcDamageEffect::waterBlastEffect)
        .def_readwrite("fragEffect", &tcDamageEffect::fragEffect)
        .def_readwrite("radEffect", &tcDamageEffect::radEffect)
        .def_readwrite("internalEffect", &tcDamageEffect::internalEffect);

}
