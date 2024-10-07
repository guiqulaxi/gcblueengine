#include "tcGameInterface.h"
namespace scriptinterface
{
tcSimState* tcGameInterface::mpSimState = nullptr;
tcGameInterface::tcGameInterface()
{

}

void tcGameInterface::SetEditMode(bool state)
{
    tcGameObject::SetEditMode(state);
}

void tcGameInterface::SetTimeAccel(long accel)
{
     assert(mpSimState);
    mpSimState->SetTimeAcceleration(accel);
}

pybind11::object tcGameInterface::GetInterface()
{
    py::module pybind11_module = py::module::import("gcblue");
    // 获取Python类的引用
    py::object  InterfaceType = pybind11_module.attr("GameInterface");
    return InterfaceType;
}
void tcGameInterface::ClearScenario()
{
    assert(mpSimState);

    mpSimState->Clear();

    // clear db if using dynamic load so that only units from scenario are in memory
    tcDatabase* database = tcDatabase::Get();
    if (database->IsUsingDynamicLoad() && (!mpSimState->IsMultiplayerClient()))
    {
        database->ClearForNewScenario(); // (let server clear database for multiplayer client mode)
    }

    //    director->ClearEvents();
    //    overlay->ClearMapObjects();
}

/**
* Loads scenario from Python script file. File should have
* method "CreateScenario(scenario_manager)".
*
* @param filePath complete file path, e.g. "scenario\\fastattack.txt"
*        filePath is only used for information when logging error
* @param fileName just the file name, e.g. "fastattack.txt"
*/
void tcGameInterface::LoadScenario(const std::string &filePath)
{
    assert(mpSimState);
    //    assert(director);
    //    assert(overlay);

    // start with clear state for new scenario
    ClearScenario();

    std::string cmdText;
    std::string errText;

    if (filePath.length() < 2) return; // work-around to support clear only

    std::string fileNameWx(filePath);
    if (strutil::contains(fileNameWx,".py"))
    {
        // remove .py extension from fileName
        int findIdx = fileNameWx.find(".py");
        fileNameWx = fileNameWx.substr(0, findIdx);
        printf( "tcSimPythonInterface -- Loading scenario %s\n", fileNameWx.c_str());
    }
    std::string pythonMoudlePath=fileNameWx;
    strutil::replace_all(pythonMoudlePath,"/",".");
    strutil::replace_all(pythonMoudlePath,"\\",".");



    //    try {
    py::exec(strutil::format("from %s import *",pythonMoudlePath.c_str()));
    py::exec("CreateScenario(ScenarioManager)\n");
    //    }catch (const pybind11::error_already_set& e) {
    //        mpSimState->Clear();
    //        return;
    //    }
}


}
