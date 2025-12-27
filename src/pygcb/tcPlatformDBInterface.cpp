#include "tcPlatformDBInterface.h"

#include "tcPlatformDBInterface.h"
#include "tcDatabase.h"
#include "tcPlatformObject.h"
#include "tcStringArray.h"
#include <pybind11-global/pybind11/pybind11.h>

namespace scriptinterface {

py::object tcPlatformDBInterface::GetPlatformDBInterface() {
    py::module pybind11_module = py::module::import("pygcb");
    // 获取Python类的引用
    py::object  InterfaceType = pybind11_module.attr("UnitDBInfoClass");
    return InterfaceType;
}

tcPlatformDBInterface::tcPlatformDBInterface() {
}

tcPlatformDBInterface::~tcPlatformDBInterface() {}

bool tcPlatformDBInterface::IsValid() const {
    return databaseObject != nullptr;
}

std::string tcPlatformDBInterface::GetClassName() const {
    return className;
}
void tcPlatformDBInterface::SetClassName( const std::string & className)
{
    databaseObject=  std::dynamic_pointer_cast<database::tcPlatformDBObject>(database::tcDatabase::Get()->GetObject(className));
    if (databaseObject) {
        this->className=className;
    }
}

std::shared_ptr<database::tcPlatformDBObject> tcPlatformDBInterface::GetPlatformDBObject() const {
    return databaseObject;
}


bool tcPlatformDBInterface::PlatformDBObjectExists(const std::string& className) {
    auto obj = database::tcDatabase::Get()->GetObject(className);
    return obj != nullptr ;
}


std::shared_ptr<database::tcPlatformDBObject> tcPlatformDBInterface::GetPlatformObject(const std::string& platformClass) {
    auto obj = database::tcDatabase::Get()->GetObject(platformClass);
    return std::dynamic_pointer_cast<database::tcPlatformDBObject>(obj);
}



} // namespace scriptinterface
