/**
**  @file tcSimPythonInterface.cpp
*/
/*
**  Copyright (c) 2014, GCBLUE PROJECT
**  All rights reserved.
**
**  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
**
**  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
**
**  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the 
**     documentation and/or other materials provided with the distribution.
**
**  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from 
**     this software without specific prior written permission.
**
**  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
**  NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
**  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
**  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
**  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
**  IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

//#include "stdwx.h" // precompiled header file

#ifndef WX_PRECOMP
//#include "wx/wx.h"
#endif // WX_PRECOMP

#include "tcSimPythonInterface.h"
#include "simmath.h"
#include "tcSimState.h"
//#include "tcMapOverlay.h"
//#include "tcMenu.h"
#include "tcTrackInterface.h"
#include "tcPlatformInterface.h"
#include "tcScenarioInterface.h"
#include "tcMissionInterface.h"

//#include "tcSoundConsole.h"
//#include "tcDirector.h"
////#include "tcMessageInterface.h"
#include "tcTime.h"
// #include "network/tcMultiplayerInterface.h"

#include "ScriptedTaskInterface.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include "common/tcOptions.h"



#ifdef _DEBUG
#define new DEBUG_NEW
#endif 

#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>

#include <tcDatabaseInterface.h>


namespace py = pybind11;
using namespace py;

//using namespace boost::python;
using namespace ai;
// using namespace network;

namespace scriptinterface 
{
/**
* Singleton accessor
*/
tcSimPythonInterface* tcSimPythonInterface::Get()
{
    static tcSimPythonInterface instance;

    return &instance;
}



/**
* Loads state from command stream
* MetaString of stream must be set to player name for control validation
*/
tcCommandStream& tcSimPythonInterface::operator<<(tcCommandStream& stream)
{
    assert(!mpSimState->IsMultiplayerClient());

    const std::string& playerName = stream.GetMetaString();

    //    tcMultiplayerInterface* multiplayerInterface = tcMultiplayerInterface::Get();
    //    int connId = multiplayerInterface->GetPlayerConnectionId(playerName);
    //    if (connId == -1)
    //    {
    //        fprintf(stderr, "tcSimPythonInterface::operator<< - Bad playername (%s)\n",
    //            playerName.c_str());
    //        return stream;
    //    }
    //    tcPlayerStatus playerStatus = multiplayerInterface->GetPlayerStatus(connId);
    // tcPlayerStatus playerStatus;
    // playerStatus.alliance=1;
    // tcAllianceSensorMap* playerSensorMap = mpSimState->GetSensorMap()->GetMap(playerStatus.alliance);
    tcAllianceSensorMap* playerSensorMap = mpSimState->GetSensorMap()->GetMap(1);

    if (playerSensorMap == 0)
    {
        //        fprintf(stderr, "tcSimPythonInterface::operator<< - Player has no sensor map, bad alliance? (%s, %d)\n",
        //            playerName.c_str(), playerStatus.alliance);
        return stream;
    }
    tcAllianceSensorMap* previousSensorMap = tcTrackInterface::GetSensorMap(); // save current map
    tcTrackInterface::SetSensorMap(playerSensorMap);

    unsigned char prevAlliance = mpSimState->mpUserInfo->GetOwnAlliance();
    mpSimState->mpUserInfo->SetOwnAlliance(1);

    unsigned char nCommands;
    stream >> nCommands;

    for (unsigned char n=0; n<nCommands; n++)
    {
        char menuMode;
        stream >> menuMode;

        unsigned char nId;
        stream >> nId;

        std::vector<long> idList;
        for (unsigned char n=0; n<nId; n++)
        {
            long id;
            stream >> id;
            idList.push_back(id);
        }

        std::string command;
        stream >> command;

        if (command.size() < 128)
        {
            bool playerHasControl = true;
            for (unsigned int n=0; (n<idList.size()) && playerHasControl; n++)
            {
                tcGameObject* obj = mpSimState->GetObject(idList[n]);
                playerHasControl = (obj != 0) ? obj->IsControlledBy(playerName) : false;
                if (obj == 0)
                {
                    fprintf(stderr, "tcSimPythonInterface::operator<< - bad idList passed, menuMode: %d\n",
                            int(menuMode));
                }
            }

            bool trackMode = menuMode == TRACK_MENU;

            if (!trackMode)
            {
                if (playerHasControl)
                {
#ifdef _DEBUG
                    long id0 = (idList.size() > 0) ? idList[0] : -1;
                    fprintf(stdout, "Script cmd (%d/%d): %s\n", id0, idList.size(), command.c_str());
#endif
                    ProcessCallbackString(command, idList);
                }
                else
                {
                    fprintf(stderr, "Script command issued for obj that player does not control, "
                                    "player: %s\n", playerName.c_str());
                }
            }
            else // track mode
            {
                if (!playerHasControl)
                {
#ifdef _DEBUG
                    long id0 = (idList.size() > 0) ? idList[0] : -1;
                    fprintf(stdout, "Script track cmd (%d/%d): %s\n", id0, idList.size(), command.c_str());
#endif
                    ProcessCallbackString(command, idList);
                }
                else
                {
                    fprintf(stderr, "Script track command issued for obj that player controls, "
                                    "player: %s\n", playerName.c_str());
                }
            }
        }
        else
        {
            fprintf(stderr, "Overlength command string received from client\n");
            assert(false);
        }
    }

    tcTrackInterface::SetSensorMap(previousSensorMap); // restore sensor map
    mpSimState->mpUserInfo->SetOwnAlliance(prevAlliance);

    return stream;
}


/**
* Saves state to command stream
*/
tcCommandStream& tcSimPythonInterface::operator>>(tcCommandStream& stream)
{
    assert(mpSimState->IsMultiplayerClient());

    assert(clientCommands.size() < 16);

    unsigned char nCommands = clientCommands.size();
    stream << nCommands;

    for (unsigned char n=0; n<nCommands; n++)
    {
        ClientCommand& cmd = clientCommands[n];

        stream << cmd.menuMode;

        assert(cmd.idList.size() < 256);
        unsigned char nId = cmd.idList.size();
        stream << nId;

        for (unsigned char n=0; n<nId; n++)
        {
            long id = cmd.idList[n];
            stream << id;
        }

        stream << cmd.commandText;
    }

    return stream;
}

void tcSimPythonInterface::ClearNewCommand()
{
    clientCommands.clear();
}

bool tcSimPythonInterface::HasNewCommand() const
{
    return (clientCommands.size() > 0);
}

void tcSimPythonInterface::InitCommandBypass()
{
    assert(commandBypass.size() == 0);

    commandBypass["TakeControl"] = true;
    commandBypass["TakeControlGroup"] = true;
    commandBypass["EnableFormationEdit"] = true;
    commandBypass["DisableFormationEdit"] = true;
    commandBypass["ShowFlightPanel"] = true;
    commandBypass["ShowPlatformPanel"] = true;
    commandBypass["ReleaseControlGroup"] = true;
}


// write apObj
void tcSimPythonInterface::SetUnitInfo(tcPlatformObject *apObj) {
    tcPlatformInterface::SetObj(apObj);
}



/**
* Task script for ai
* @return false if error with task
*/
bool tcSimPythonInterface::CallTaskScript(ScriptedTask* task, const char* azCommand) 
{
    assert(taskInterface);

    taskInterface->SetTask(task);

    try 
    {   
        //        handle<>( PyRun_String(azCommand
        //            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
        py::exec(azCommand);
        return true;
    }
    catch (error_already_set) 
    {
        // handle the exception in some way
        fprintf(stderr,"Exception occured in CallTaskScript\n");
        //        PyErr_Print();
        return false;
    }
}

tcPlatformObject* tcSimPythonInterface::GetHookedObj() const
{
    return mpHookedObj;
}

tcFlightPort* tcSimPythonInterface::GetHookedObjFlightPort()
{
    tcFlightOpsObject* flightOps = dynamic_cast<tcFlightOpsObject*>(mpHookedObj);
    if (flightOps == 0) return 0;
    return flightOps->GetFlightPort();
}

//void tcSimPythonInterface::AttachCommandQueue(tcCommandQueue *cq)
//{
////    tcPlatformInterface::AttachCommandQueue(cq);
////    tcGroupInterface::AttachCommandQueue(cq);
////    tcScenarioInterface::AttachCommandQueue(cq);
//}

//void tcSimPythonInterface::AttachConsole(tcSoundConsole *apConsole)
//{
//    tcPlatformInterface::AttachConsole(apConsole);
//    mpConsole = apConsole;
//}

//void tcSimPythonInterface::AttachDirector(tcDirector *dir)
//{
//    tcScenarioInterface::AttachDirector(dir);
//    director = dir;
//}

void tcSimPythonInterface::AttachMapData(tcMapData *md)
{
    tcPlatformInterface::AttachMapData(md);
    tcScenarioInterface::AttachMapData(md);
}

//void tcSimPythonInterface::AttachMapOverlay(tcMapOverlay* mo)
//{
//    overlay = mo;
//    tcScenarioInterface::AttachMapOverlay(mo);
//    tcFlightPortInterface::AttachMapOverlay(mo);
//}

void tcSimPythonInterface::AttachSimState(tcSimState *apSimState) 
{
    tcPlatformInterface::AttachSimState(apSimState);
    tcScenarioInterface::AttachSimState(apSimState);
    tcFlightPortInterface::AttachSimState(apSimState);
    mpSimState=apSimState;
}

//void tcSimPythonInterface::AttachTacticalMap(tcTacticalMapView* mv)
//{
//    tcPlatformInterface::AttachTacticalMap(mv);
//}


//void tcSimPythonInterface::BuildEditMenu()
//{
//	CallPython("Menu.BuildEditMenu(UserMenu, ScenarioManager)",
//		"Exception occured in BuildEditMenu");
//}

///**
//* Creates menu customized to selected group of units
//*/
//void tcSimPythonInterface::BuildGroupMenu()
//{
//    try
//	{
//        handle<>( PyRun_String("Menu.BuildGroupMenu(UserMenu, GroupInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildGroupMenu\n");
//        PyErr_Print();
//    }
//}

///**
//* creates platform menu customized to selected unit
//*/
//void tcSimPythonInterface::BuildPlatformMenu()
//{
//	//assert(mpHookedObj != 0);
//	if (mpHookedObj == 0) return; // occurs normally when missile is hooked

//    try
//	{
//        handle<>( PyRun_String("Menu.BuildUnitMenu(UserMenu, HookedUnitInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildPlatformMenu\n");
//        PyErr_Print();
//    }
//}

///**
//* Version for mission editor mode
//*/
//void tcSimPythonInterface::BuildPlatformEditMenu()
//{
//    try
//	{
//        handle<>( PyRun_String("Menu.BuildUnitEditMenu(UserMenu, HookedUnitInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildPlatformEditMenu\n");
//        PyErr_Print();
//    }
//}

///**
//* Version for mission editor mode
//*/
//void tcSimPythonInterface::BuildGroupEditMenu()
//{
//    try
//	{
//        handle<>( PyRun_String("Menu.BuildGroupEditMenu(UserMenu, GroupInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildGroupEditMenu\n");
//        PyErr_Print();
//    }
//}

//void tcSimPythonInterface::BuildWeaponMenu()
//{
//    try
//	{
//        handle<>( PyRun_String("Menu.BuildWeaponMenu(UserMenu, WeaponInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildWeaponMenu\n");
//        PyErr_Print();
//    }
//}

//void tcSimPythonInterface::BuildWeaponEditMenu()
//{
//    try
//	{
//        handle<>( PyRun_String("Menu.BuildWeaponEditMenu(UserMenu, WeaponInfo)"
//            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
//    }
//    catch(error_already_set)
//	{
//        fprintf(stderr,"Exception occured in BuildWeaponEditMenu\n");
//        PyErr_Print();
//    }
//}

///* If menu platform has a flightport, get a pointer to it and pass the
//** pointer to the FlightPortInterface python object.
//** Then pass PanelInterface, FlightPortInterface, and UnitInfo to python
//** script to build the panel object.
//*/
//void tcSimPythonInterface::BuildFlightPortPanel()
//{

//    tcFlightPort* flightport = GetHookedObjFlightPort();
//    if (flightport == NULL)
//    {
//        /*
//        tcFlightPortInterface::SetObj(NULL);
//        FlightPortInterface.attr("GetLocalObj")(); // load through this call
//        */
//        flightPortInterface->SetFlightPort(NULL);
//        tcPanelInterface::Reset();// sets to "no data available" state
//        return;
//    }
//    flightPortInterface->SetFlightPort(flightport);
//    /*
//    tcFlightPortInterface::SetObj(flightport);
//    FlightPortInterface.attr("GetLocalObj")(); // load through this call
//    */
//    CallPython("Menu.BuildFlightPortPanel(UserPanel, FlightPortInfo, HookedUnitInfo)",
//                "Exception occured in BuildFlightPortMenu\n");
//}

//// creates platform menu customized to object
//void tcSimPythonInterface::BuildTrackMenu() {
//    CallPython("Menu.BuildTrackMenu(UserMenu, HookedTrackInfo)",
//                "Exception occured in BuildTrackMenu\n");
//}

/**
* @return true if this command should be executed on client instead of sending to server
* Multiplayer method
*/
bool tcSimPythonInterface::BypassClientCommand(const std::string& command) const
{
    std::map<std::string, bool>::const_iterator iter = 
        commandBypass.find(command);
    return (iter != commandBypass.end());
}

/**
** Executes command line in command text in embedded Python
** using PyRun_String. If there is an exception an error message
** is output to various destinations. 
** @return 0 on success, non-zero for error
*/
int tcSimPythonInterface::CallPython(const char *commandtext, const char *errortext)
{
    try 
    {   
        py::exec(commandtext);
        //        handle<> ignored( PyRun_String(commandtext
        //            , Py_file_input, main_namespace.ptr(), main_namespace.ptr()) );
        return 0;
    }
    catch (error_already_set) 
    {
        ReportError(errortext);
        //PyErr_Print();
        return 1;
    }   
}

/* Copies name of python global object to pass to python function.
** It might be better to encode the object type into the command itself,
** vs. relying on the meMenuMode. The HotKey case doesn't have an active
** menu. */
void tcSimPythonInterface::GetObjectStringByMode(char *str)
{
    switch (meMenuMode)
    {
    case UNIT_MENU:
        strcpy(str, "HookedUnitInfo");
        return;
    case GROUP_MENU:
        strcpy(str, "GroupInfo");
        return;
    case TRACK_MENU:
        strcpy(str, "HookedTrackInfo");
        return;
    case FLIGHT_MENU:
        strcpy(str, "FlightPortInfo");
        return;
    case GAME_MENU:
        strcpy(str, "ScenarioManager");
        return;
    case WEAPON_MENU:
        strcpy(str, "WeaponInfo");
        return;
    }
}

tcScenarioInterface* tcSimPythonInterface::GetScenarioInterface() const
{
    assert(scenarioInterface);
    
    return scenarioInterface;
}


void tcSimPythonInterface::ClearScenario()
{
    assert(mpSimState);
    //    assert(director);
    //    assert(overlay);

    // start with clear state for new scenario
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

void tcSimPythonInterface::LoadDatabase(const std::string &filePath)
{
    assert(mpSimState);

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
    py::exec("LoadDatabase(DatabaseManager)\n");

}

/**
* Loads scenario from Python script file. File should have
* method "CreateScenario(scenario_manager)".
*
* @param filePath complete file path, e.g. "scenario\\fastattack.txt"
*        filePath is only used for information when logging error
* @param fileName just the file name, e.g. "fastattack.txt"
*/
void tcSimPythonInterface::LoadScenario(const std::string &filePath)
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


    //	if (fileNameWx.Contains(".py"))
    //	{
    //		// remove .py extension from fileName
    //		int findIdx = fileNameWx.Find(".py");
    //		fileNameWx = fileNameWx.SubString(0, findIdx - 1);
    //        wxPrintf( "tcSimPythonInterface -- Loading scenario %s\n", fileNameWx.c_str());
    //	}
    //    try {
    py::exec(strutil::format("from %s import *",pythonMoudlePath.c_str()));
    py::exec("CreateScenario(ScenarioManager)\n");
    //    }catch (const pybind11::error_already_set& e) {
    //        mpSimState->Clear();
    //        return;
    //    }


}

/**
*
*/
void tcSimPythonInterface::ProcessCommand(const std::string& command, const std::vector<long>& id,
                                          int param, std::string textParam)
{
    //    PushMode();
    //    SetMenuGroup(id);

    std::string s = "Menu.";

    s += command;
    s += "(";

    char zObject[64];
    GetObjectStringByMode(zObject);
    s += zObject;

    if (param != -1) // add parameter to python call if param != -1
    {
        char zBuff[64];
        sprintf(zBuff,", %d", param);
        s += zBuff;
    }
    else if (textParam.length() > 0)
    {
        s += ",'";
        s += textParam;
        s += "'";
    }

    s += ")\n";


    if (!mpSimState->IsMultiplayerClient() || BypassClientCommand(command))
    {
        CallPython(s.c_str(), "Exception occurred in ProcessCommand\n");
    }
    else
    {
        ClientCommand cmd;
        cmd.menuMode = meMenuMode;
        cmd.idList = id;
        cmd.commandText = s;

        if (cmd.idList.size() == 0)
        {
            cmd.idList = groupInterface->GetUnits();
        }

        clientCommands.push_back(cmd);
    }


    //    PopMode();
}

/**
* Calls python command of the form Menu.<command>(<command object><argString>)
* argString should start with a comma if it is non-empty
*/
void tcSimPythonInterface::ProcessCommandWithArguments(const std::string& command, const std::vector<long>& id,
                                                       const std::string& argString)
{

}

void tcSimPythonInterface::ProcessCallbackString(const std::string &command, const std::vector<long> &id)
{

}


/**
* writes error message in text out to console, if console is attached 
*/
void tcSimPythonInterface::ReportError(const char* text)
{
    fprintf(stderr,text);
    //	if (mpConsole == 0) return;
    //	mpConsole->Print(text);
}


bool tcSimPythonInterface::IsHooked(long id) const
{
    std::vector<long>& hookedId = groupInterface->GetUnits();

    for (size_t n=0; n<hookedId.size(); n++)
    {
        if (hookedId[n] == id) return true;
    }
    return false;
}


void tcSimPythonInterface::Update()
{
    static unsigned int lastUpdate = 0;

    // limit update frequency
    unsigned int t = tcTime::Get()->Get30HzCount();
    if ((t - lastUpdate) < 60) return;
    lastUpdate = t;

    UpdateLogs();
}

/**
* Called immediately before a platform is destroyed. Clear menu platform if necessary
*/
void tcSimPythonInterface::UpdateForDestroyedPlatform(long id)
{
    groupInterface->RemoveUnit(id);

    //tcTrackInterface::SetTrack(anID);

    if (hookedInterface->GetPlatformId() == id)
    {
        hookedInterface->SetPlatform(0);
    }
}

/**
* FEB2014 This used to be in destructor but moved out after crash in vc11
*/
void tcSimPythonInterface::FlushLogs()
{
    /*** print standard error to file ***/
    py::exec(
        "outfile = file('log\\pyout.txt', 'a')\n"
        "errfile = file('log\\pyerr.txt', 'a')\n"
        "outfile.write(myout.getvalue())\n"
        "errfile.write(myerr.getvalue())\n"
        "outfile.close()\n"
        "errfile.close()\n"
        );
}

/**
* Update output and error text logs
* If showPythonErrors is true, then send errors to "Python" message channel in game 
*/
void tcSimPythonInterface::UpdateLogs()
{
    std::string errorText;

    try
    {
        py::exec(
            "outfile = file('log\\pyout.txt', 'a')\n"
            "errfile = file('log\\pyerr.txt', 'a')\n"
            "outfile.write(myout.getvalue())\n"
            "ErrorText = myerr.getvalue()\n"
            "errfile.write(ErrorText)\n"
            "outfile.close()\n"
            "errfile.close()\n"
            "myout.truncate(0)\n"
            "myerr.truncate(0)\n" );

        if (showPythonErrors)
        {
            //			handle<> errorTextHandle(borrowed(PyDict_GetItemString(main_namespace.ptr(), "ErrorText")));
            //			str textObject(errorTextHandle);

            //			errorText = extract<const char*>(textObject);
        }
    }
    catch(error_already_set)
    {
        fprintf(stderr,"Exception occurred during SendTextToConsole\n");
        //		PyErr_Print();
    }
    catch(...)
    {
        fprintf(stderr,"Unknown exception occurred during SendTextToConsole\n");
        PyErr_Print();
    }

    if (errorText.size() > 0)
    {

    }


}





tcSimPythonInterface::tcSimPythonInterface() :
    //    mpConsole(0),
    //    director(0),
    mpHookedObj(0),
    //    overlay(0),
    isModePushed(false),
    showPythonErrors(false)
{

    py::module pybind11_module = py::module::import("pygcb");
    mpSimState = tcSimState::Get();

    InitCommandBypass();

    tcPlatformInterface::AttachSimState(mpSimState);
    tcScenarioInterface::AttachSimState(mpSimState);


    object platformInterfaceType = tcPlatformInterface::GetPlatformInterface();

    PlatformInterface = platformInterfaceType();
    platformInterface = py::cast<tcPlatformInterface*>(PlatformInterface);
    HookedPlatformInterface = platformInterfaceType();

    py::object  InterfaceType = pybind11_module.attr("UnitInfoClass");
    hookedInterface =  py::cast<tcPlatformInterface*>(HookedPlatformInterface);



    // 获取Python类的引用
    GroupInterfaceType = pybind11_module.attr("GroupInterfaceClass");
    GroupInterface = GroupInterfaceType();

    groupInterface = py::cast<tcGroupInterface*>(GroupInterface);


    TrackInterfaceType = pybind11_module.attr("TrackInterfaceClass");
    TrackInterface = TrackInterfaceType();


    object flightPortInterfaceType = tcFlightPortInterface::GetInterface();
    FlightPortInterface = flightPortInterfaceType();
    flightPortInterface = py::cast<tcFlightPortInterface*>(FlightPortInterface);

    object weaponInterfaceType = tcWeaponInterface::GetInterface();
    WeaponInterface = weaponInterfaceType();
    weaponInterface = py::cast<tcWeaponInterface*>(WeaponInterface);


    object missionInterfaceType = tcMissionInterface::GetInterface();

    object scenarioInterfaceType = tcScenarioInterface::GetInterface();
    tcScenarioInterface::AddGoalClasses();
    ScenarioInterface = scenarioInterfaceType();
    scenarioInterface = py::cast<tcScenarioInterface*>(ScenarioInterface);
    tcPlatformInterface::AttachScenarioInterface(scenarioInterface);
    tcWeaponInterface::AttachScenarioInterface(scenarioInterface);
    tcGroupInterface::AttachScenarioInterface(scenarioInterface);

    ScriptedTaskInterface tempInterface;


    TaskInterfaceObject = py::cast(tempInterface);
    taskInterface = py::cast<ScriptedTaskInterface*>(TaskInterfaceObject);

    object databaseInterfaceType = tcDatabaseInterface::GetInterface();
    DatabaseInterface = databaseInterfaceType();
    databaseInterface = py::cast<tcDatabaseInterface*>(DatabaseInterface);

    // 获取主模块（__main__）
    py::module main_module = py::module::import("__main__");

    // 获取主模块的字典（即其属性和函数）
    py::dict main_dict = main_module.attr("__dict__");
    main_dict["UnitInfo"]=PlatformInterface.ptr();
    main_dict["HookedUnitInfo"]=HookedPlatformInterface;
    main_dict["FlightPortInfo"]= FlightPortInterface.ptr();
    main_dict["HookedTrackInfo"]=  TrackInterface.ptr();
    main_dict["ScenarioManager"]=  ScenarioInterface.ptr();
    main_dict["GroupInfo"]=  GroupInterface.ptr();
    main_dict["TaskInterface"]=  TaskInterfaceObject.ptr();
    main_dict["WeaponInfo"]= WeaponInterface.ptr();
    main_dict["DatabaseManager"]= DatabaseInterface.ptr();

    if (tcOptions::Get()->OptionStringExists("ShowPythonErrors"))
    {
        showPythonErrors = true;
    }


}


tcSimPythonInterface::~tcSimPythonInterface() 
{


}
}
