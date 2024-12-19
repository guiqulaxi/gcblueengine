/** 
**  @file Game.cpp main application class 
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

#include "tcAcousticModel.h"
#ifndef WX_PRECOMP
//#include "wx/wx.h"
#endif

#include "Game.h"
#include "gcb.h"
#include "tcDatabase.h"
#include "tcSimState.h"
#include "AError.h"

#include <iomanip>
#include <tcDatabaseIterator.h>
#include <tcSensorTrackIterator.h>
#include <filesystem>

#include "commandlist.h" // for custom command queue handler
#include "tcCommandQueue.h"
//#include "tcHookInfo.h"
//#include "tcOOBView.h"
//#include "tcPopupControl.h"
//#include "tc3DViewer.h"
#include "tcGoalTracker.h"
#include "tcString.h"
#include "tcSimPythonInterface.h"
#include "tcScenarioInterface.h"
//#include "tcDirector.h"
//#include "tcXmlWindow.h"
#include "tcMapData.h"
#include "tinyxml2.h"
#include <fstream>
// #include "network/tcMultiplayerInterface.h"
// #include "network/tcUpdateMessageHandler.h" // for attach
//#include "tcChatBox.h"
//#include "tc3DWindow2.h"
//#include "tcPopupMessage.h"
//#include "tcLauncherPopup.h"
// #include "tcUserSelectedGroups.h"

#include "tcUnits.h"
#include "tcDateTime.h"

#include "tcGameSerializer.h"
#include "ai/tcMissionManager.h"

// #include "network/tcControlMessageHandler.h" // for test

#include "ai/tcMission.h"
#include "tcScenarioRandomizer.h"
// #include <QImage>
#include "rapidjson/document.h"
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#if defined(_MSC_VER)
#endif

#ifdef _DEBUG
#define new DEBUG_NEW
#endif



using namespace std;
namespace fs = std::filesystem;

// using network::tcMultiplayerInterface;



void tcGame::CheckGoals()
{
    if (tcGameObject::IsEditMode()) return;

    tcAllianceInfo* allianceInfo = tcAllianceInfo::Get();

    std::vector<unsigned char> allianceList = allianceInfo->GetAllianceList();

    //    tcMessageInterface::Get()->ClearChannel("Mission");


    unsigned char nAlliances = (unsigned char)allianceList.size();
    char buff[256];

    // check if everyone has failed (draw)
    bool everyoneFailed = true;
    for (unsigned char k=0; k<nAlliances; k++)
    {
        bool allianceFailed = goalTracker->HasAllianceFailed(allianceList[k]);
        bool allianceNeutral = allianceInfo->IsAllianceNeutral(allianceList[k]);

        if (!allianceFailed && !allianceNeutral)
        {
            everyoneFailed = false;
        }
    }

    //    if (everyoneFailed && !drawReported)
    //    {
    //        SetTimeAccel(0); // pause game
    //        infoConsole->Print("SCENARIO A DRAW\n");
    //        DisplayOutcomeDialog("Scenario is a draw\n");

    //        if (simState->IsMultiplayerServer())
    //        {
    //            std::string s;
    //            s = "*** SCENARIO A DRAW ***";
    //            //tcMultiplayerInterface::Get()->BroadcastChatText("*** GAME OVER ***");
    //            //tcMultiplayerInterface::Get()->BroadcastChatText(s);
    //            EndGame();
    //        }
    //        drawReported = true;
    //        return;
    //    }


    for (unsigned char idx=0; idx < nAlliances; idx++)
    {
        unsigned char alliance = allianceList[idx];

        bool allianceFailed = goalTracker->HasAllianceFailed((int)alliance);
        bool allianceSucceeded = goalTracker->HasAllianceSucceeded((int)alliance);
        


        if (allianceFailed)
        {
            if (goalTracker->HasStatusChanged(alliance))
            {
                fprintf(stdout, "Alliance %d:%s UNABLE TO WIN\n", alliance,allianceInfo->GetAllianceName(alliance).c_str());
                //				infoConsole->Print(buff);

                if (userInfo->IsOwnAlliance(alliance))
                {
                    SetTimeAccel(0); // pause game

                }

                if (simState->IsMultiplayerServer())
                {
                    std::string s;
                    s=strutil::format("*** %s UNABLE TO WIN", allianceInfo->GetAllianceName((unsigned char)alliance).c_str());
                    //tcMultiplayerInterface::Get()->BroadcastChatText("*** GAME UPDATE ***");
                    //tcMultiplayerInterface::Get()->BroadcastChatText(s);
                    //EndGame();
                }
            }
        }

        if (allianceSucceeded)
        {
            if (goalTracker->HasStatusChanged(alliance))
            {
                SetTimeAccel(0); // pause game
                fprintf(stdout, "Alliance %d %s WON\n", alliance, allianceInfo->GetAllianceName((unsigned char)alliance).c_str());

                //				infoConsole->Print(buff);
                if (userInfo->IsOwnAlliance(alliance))
                {
                    //				    DisplayOutcomeDialog("You have won!\n");
                }
                else
                {
                    //                    DisplayOutcomeDialog("You have lost!\n");
                }

                if (simState->IsMultiplayerServer())
                {
                    std::string s;
                    s=strutil::format("*** %s WON", allianceInfo->GetAllianceName((unsigned char)alliance).c_str());
                    //tcMultiplayerInterface::Get()->BroadcastChatText("*** GAME OVER ***");
                    //tcMultiplayerInterface::Get()->BroadcastChatText(s);
                    EndGame();
                }
            }
        }
    }

    CheckMultiplayerEndGame();

}


void tcGame::CheckMultiplayerEndGame()
{
    //    if (simState->IsMultiplayerServer())
    //    {
    //        std::string message;
    //        bool gameOver = tcMultiplayerInterface::Get()->IsGameOver(message);

    //        if (gameOver)
    //        {
    //            //tcMultiplayerInterface::Get()->BroadcastChatText("*** GAME OVER ***");
    //            //tcMultiplayerInterface::Get()->BroadcastChatText(message);

    //            EndGame();
    //        }
    //    }
    //    else if (simState->IsMultiplayerClient())
    //    {
    //        if ((simState->GetTime() == 0))
    //        {
    ////            DisplayOutcomeDialog("GAME OVER\n");
    //        }
    //    }

}





/**
* Ends game and returns to start screen
*/
void tcGame::EndGame()
{
    if (meGameMode == GM_START) return; // ignore if game has not started


    bool endingScenarioEdit = tcGameObject::IsEditMode();

    if (!endingScenarioEdit)
    {
        goalTracker->LogAllianceGoalStatus("log\\goal_results.txt",
                                           userInfo->GetOwnAlliance());

        goalTracker->LogAllDamageReports("log\\damage_summary.csv");

        const std::chrono::system_clock::time_point now =  std::chrono::system_clock::now();
        std::time_t t = std::chrono::system_clock::to_time_t(now);
        std::tm* now_tm = std::localtime(&t);
        std::string aarName = strutil::format("aar\\%04d_%02d_%02d_%02d%02d%02d.xml",
                                              now_tm->tm_year+ 1900, now_tm->tm_mon+1, now_tm->tm_mday, now_tm->tm_hour, now_tm->tm_min, now_tm->tm_sec);
        goalTracker->WriteAAR(aarName);
    }




    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    //    objectControl->SetHookID(-1);

    tcMission::ResetNextId();

    if (!simState->IsMultiplayerActive())
    {
        // reset time
        gameTime = 0;
        accelerateTime = 0;

        // clear briefing console text
        //		briefingConsoleLeft->Clear();
        //		briefingConsoleLeft->SetDelayedTextEffect(true);

        // reset director
        //		director->ClearEvents();
        //        tacticalMap->ClearMapObjects();
        //        tacticalMap->ClearSpecialGraphics();
        //		director->SetStartTime(0);

        // try to reload last scenario played
        std::string lastPath = tcOptions::Get()->GetOptionString("LastScenarioPath");
        std::string lastName = tcOptions::Get()->GetOptionString("LastScenarioName");
        std::string lastExtension = tcOptions::Get()->GetOptionString("LastScenarioExtension");

        simState->Clear();
        //        scenarioSelectView->SetGameStarted(false);
        if ((lastName.length() > 2) && (lastName != "default") && (lastExtension == "py"))
        {
            //			scenarioSelectView->LoadScenario(lastPath, lastName, false);
        }
        else
        {
            pythonInterface->ClearScenario();
        }

        if (simState->IsScenarioLoaded())
        {
            HookRandomFriendly();
        }
    }
    else if (simState->IsMultiplayerServer())
    {
        // try to reload last scenario played
        std::string lastPath = tcOptions::Get()->GetOptionString("LastScenarioPath");
        std::string lastName = tcOptions::Get()->GetOptionString("LastScenarioName");
        std::string lastExtension = tcOptions::Get()->GetOptionString("LastScenarioExtension");

        simState->Clear();
        //        scenarioSelectView->SetGameStarted(false);
        if ((lastName.length() > 2) && (lastName != "default") && (lastExtension == "py"))
        {
            //            scenarioSelectView->LoadScenario(lastPath, lastName, false);
        }
        else
        {
            pythonInterface->ClearScenario();
            
            //            tcMultiplayerInterface* multiplayerInterface = tcMultiplayerInterface::Get();
            //            multiplayerInterface->ResetGame();
            //            multiplayerInterface->SetAllReadyState(false);

            //            scenarioSelectView->SynchScenarioInfo();
        }
    }
    // if in multiplayer client mode, switch to multiplayer off mode
    //	else if (networkView->GetNetworkMode() == tcNetworkView::MULTIPLAYER_CLIENT)
    //	{
    //        // save these so we don't clear the scenario info when logging out of ongoing game
    //        bool isScenarioLoaded = simState->IsScenarioLoaded();
    //        std::string scenarioName = simState->GetScenarioName();
    //        std::string scenarioDescription = simState->GetScenarioDescription();

    //		/* TODO: should have one object for network state vs. current system
    //		** with state in tcGame, tcSimState, tcNetworkView */
    //		// 27AUG08 changed this to NOT log client off at quit
    //        //assert(multiplayerMode == 1);
    //		//networkView->SetNetworkMode(tcNetworkView::MULTIPLAYER_OFF);
    //		//multiplayerMode = 0;
    //        //tcMultiplayerInterface::Get()->BroadcastControlMessage(network::tcControlMessageHandler::CM_OUTGAME);

    //        pythonInterface->ClearScenario();

    //        // restore scenario info
    //        simState->SetScenarioLoaded(isScenarioLoaded);
    //        simState->SetScenarioName(scenarioName);
    //        simState->SetScenarioDescription(scenarioDescription);

    //	}

    //    tcMessageInterface::Get()->SetPopupState(false);

    // set viewer back to object display mode
    //	viewer->SetTerrainActive(false);
    //	viewer->SetClearMode(1); // depth clearing
    //	viewer->SetText(" ");

    //	size3D = MODE3D_START;
    //	Update3DSize();

    // switch mode back to start
    //	meGameMode = GM_START;
    //	meScreenMode = START;
    //    if (!simState->IsMultiplayerActive())
    //    {
    //        startView->SetPane("Scenario");
    //    }
    //    else
    //    {
    //        startView->SetPane("Multiplayer");
    //    }
    //	mbScenarioEdit = false;
    //	endGame = false;
    //    drawReported = false;
    //    startView->SetGameStarted(false);
    //    scenarioSelectView->SetGameStarted(false);

    //    if (!endingScenarioEdit)
    //    {
    //        scenarioSelectView->SetTab("AAR");
    //    }

    //    scenarioSelectView->Init(); // rescan for recently saved scenario

    //    if (infoConsole != 0) infoConsole->Clear();

    //    wxTopLevelWindow::Thaw();
}



/**
* Initializes the game.
*/
void tcGame::Init()
{
    double a = 2.0;
    double b = 2e-12;
    double c = a + b;
    assert(c > a); // check that double precision math is working



    std::cout << "Time init success" << std::endl;

#ifdef _DEBUG
    //   tcSonarEnvironment::Get()->Test();
#endif



    try
    {

        //初始化数据库
        database->addTable("ship");
        database->addTable("simpleair");
        database->addTable("ground");
       database->addTable("missile");
        //tables.push_back("launcher"); // launcher is now a virtual table, special case formed from distinct values in launcher_configuration table
        database->addTable("radar");
        database->addTable("esm");
        database->addTable("optical");
       database->addTable("ecm");
        database->addTable("sonar");
        database->addTable("air");
        database->addTable("flightport");
       database->addTable("ballistic");
        database->addTable("stores");
       database->addTable("torpedo");
        database->addTable("sonobuoy");
        database->addTable("item");
        database->addTable("sub");
        database->addTable("fueltank");
        database->addTable("cm");
        database->addTable("ballistic_missile");
         database->addTable("space");

        database->SerializeSql("", true); // moved to top so that db is loaded for db browse panel
        database->SetProgressReporting( 0, 0);



        if (tcOptions::Get()->OptionStringExists("CopyDatabase"))
        {
            database->SerializeSql("_copy", false);
        }



        tcGameObject::SetGameObjectDatabase(database); // added to allow objects to init themselves

        simState->AttachDB(database);
        simState->AttachMapData(mapData);
        // simState->AttachPythonInterface(pythonInterface);
        simState->AttachUserInfo(userInfo);

        pythonInterface->AttachMapData(mapData);

        tcLauncherState::mpDatabase = database;


        //		progressDialog->Update(65, "Loading low res map data");
        /* ** Initialize mcMapData  * **/
        mapData->AttachOptions(tcOptions::Get());
        mapData->LoadLowRes();
        //mapData->LoadHighRes(-8.0f, 55.0f);
        //mapData->LoadHighResB(-8.0f, 55.0f);

        // added mapdata reference to tcGameObject to allow RandInit()
        // to place objects at legal positions and to set altitude appropriately
        tcGameObject::SetGameObjectMapData(mapData);
        tcPlatformObject::InitPlatformObject();

        // ///////////////////////////////////////////////////////
        // #define K_DEC_LOWRES (int)30
        // #define SCALE_LOWRES (float)120/(float)K_DEC_LOWRES
        // #define SCALE_HIGHRES (float)120.0f
        // #define SCALE_LOOKUP (float)0.5f
        // #define RESLOW_DEG (float)K_DEC_LOWRES/120.0f
        // #define RESHIGH_DEG (float)1.0f/120.0f
        // #define M_LOWRES (int)180*120/K_DEC_LOWRES // latitude cells for low res global map
        // #define N_LOWRES (int)360*120/K_DEC_LOWRES // longitude
        //         size_t  M_HIGHRES =M_LOWRES;
        //         size_t  N_HIGHRES=N_LOWRES;
        //         UINT32 *apData =new UINT32[M_HIGHRES*N_HIGHRES];
        //         mapData->CreateMapArrayHighRes();
        //         mapData->CreateMapImage(0,0,apData);
        //         QImage image(M_HIGHRES,N_HIGHRES,QImage::Format_ARGB32);
        //         for(int m=0;m<M_HIGHRES;m++)
        //         {
        //             for(int n=0;n<M_HIGHRES;n++)
        //             {
        //                 image.setPixel(m,n,apData[(M_HIGHRES-1-m)*N_HIGHRES + n]);
        //             }
        //         }
        //         // QImage image((uchar *)apData, M_HIGHRES, N_HIGHRES, QImage::Format_ARGB32);
        //         image.save("D:/1.png");
        InitSim();
    }
    catch(std::string s)
    {
        throw;
    }
    catch(...)
    {

        throw;
    }
    try
    {

        std::string lastPath = tcOptions::Get()->GetOptionString("LastScenarioPath");
        std::string lastName = tcOptions::Get()->GetOptionString("LastScenarioName");
        std::string lastExtension = tcOptions::Get()->GetOptionString("LastScenarioExtension");

        if ((lastName.length() > 2) && (lastName != "default") && (lastExtension == "py"))
        {
            //			scenarioSelectView->LoadScenario(lastPath, lastName, false);
        }
        else
        {
            // do nothing, state starts clear
        }


        if (simState->IsScenarioLoaded())
        {
            HookRandomFriendly();
        }
        else
        {
        }
    }
    catch(std::string s)
    {
        //		pythonInterface->GetScenarioInterface()->SetProgressReporting(0);
        std::string message;
        message += "Error during scenario loading: ";
        message += s;
        //wxMessageBox(message.c_str(), "Fatal error", wxICON_ERROR);
        throw;
    }
    catch (...)
    {
        //		pythonInterface->GetScenarioInterface()->SetProgressReporting(0);
        //wxMessageBox("Unknown error during scenario loading", "Fatal error", wxICON_ERROR);
        throw;
    }


    float af = 3.2f;
    float bf = 3.7f;
    float cf = -3.7f;
    long ai = long(af);
    long bi = long(bf);
    long ci = long(cf);

    assert(ai == 3);
    assert(bi == 3);
    assert(ci == -3);

}


void tcGame::UninitGame()
{


}


bool tcGame::InitSim()
{
    simState->AttachMapData(mapData);
    // simState->AttachPythonInterface(pythonInterface);
    simState->AttachUserInfo(userInfo);

    //pythonInterface->AttachSensorMap(simState->mcSensorMap.GetMap(userInfo->GetOwnAlliance()));

    pythonInterface->AttachSimState(simState);


    tcSensorMapTrack::AttachDatabase(database);



    tcFlightPort::InitTransitionTimes();

    Aero::LoadAtmosphereTable();

    //加载水声数据
    for (const auto& entry : fs::directory_iterator("database/py/acoustic_noise")) {
        if (fs::is_regular_file(entry.status())) {
            auto pathString=entry.path().string();
            std::replace(pathString.begin(), pathString.end(), '\\', '/');
            LoadAcousticModel(pathString);
        }
    }
    //加载特性数据
    for (const auto& entry : fs::directory_iterator("database/py/signature")) {
        if (fs::is_regular_file(entry.status())) {
            auto pathString=entry.path().string();
            std::replace(pathString.begin(), pathString.end(), '\\', '/');
            LoadSignatureModel(pathString);
        }
    }
    //加载毁伤数据
    for (const auto& entry : fs::directory_iterator("database/py/weapon_damage")) {
        if (fs::is_regular_file(entry.status())) {
            auto pathString=entry.path().string();
            std::replace(pathString.begin(), pathString.end(), '\\', '/');
            LoadWeaponDamage(pathString);
        }
    }
    //加载毁伤效果
    for (const auto& entry : fs::directory_iterator("database/py/damage_effect")) {
        if (fs::is_regular_file(entry.status())) {
            auto pathString=entry.path().string();
            std::replace(pathString.begin(), pathString.end(), '\\', '/');
            LoadDamageEffect(pathString);
        }
    }
    //加载所有数据
    std::vector<std::string> dataDir= {
                                        "stores",
                                        "ballistic",
                                        "ballistic_missile",
                                        "cm",
                                        "ecm",
                                        "esm",
                                        "flightport",
                                        "fueltank",
                                        "ground",
                                        "item",
                                        "missile",
                                        "optical",
                                        "radar",
                                        "ship",
                                        "simpleair",
                                        "sonar",
                                        "sonobuoy",
                                        "space",
                                        "sub",
                                        "torpedo",
                                        "launcher"


    };
    for (auto & dir:dataDir)
    {
        for (const auto& entry : fs::directory_iterator("database/py/"+dir)) {
            if (fs::is_regular_file(entry.status())) {
                auto pathString=entry.path().string();
                std::replace(pathString.begin(), pathString.end(), '\\', '/');
                LoadDatabaseObject(pathString);
            }
        }
    }

     simState->AttachWeaponTester(); // dev mode feature
    return true;
}

void tcGame::SaveDatabaseToPython(const std::string& dirPath)
{
    tcDatabaseIterator iter(0);
    auto& nameToTable=database->GetNameToTable();
    for(auto& kv:nameToTable)
    {
        tcDatabaseObject* obj= simState->mpDatabase->GetObject(kv.first);
        if(obj)
        {
            std::ofstream ofs;
            std::string path= dirPath+"/"+kv.second+"/"+strutil::toPythonVar(obj->mzClass)+".py";
            ofs.open(path);
            std::string valueString;
            obj->WritePython(valueString);
            ofs<<valueString;
            ofs.close();
        }
    }
    for(auto &kv:database->GetAcousticModelData())
    {
        std::ofstream ofs;
        std::string name=kv.first;
        std::string path= dirPath+"/acoustic_noise/"+strutil::toPythonVar(name)+".py";
        ofs.open(path);
        std::string valueString;
        kv.second.WritePython(valueString);
        ofs<<valueString;
        ofs.close();
    }
    for(auto& kv:database->GetSignatureModelData())
    {
        std::ofstream ofs;
        std::string name=kv.first;
        std::string path= dirPath+"/signature/"+strutil::toPythonVar(name)+".py";
        ofs.open(path);
        std::string valueString;
        kv.second.WritePython(valueString);
        ofs<<valueString;
        ofs.close();
    }

    for(auto& kv:database->GetWeaponDamageData().GetData())
    {
        std::ofstream ofs;
        std::string name=kv.first;
        std::string path= dirPath+"/weapon_damage/"+strutil::toPythonVar(name)+".py";
        ofs.open(path);

        std::string valueString;
        kv.second.WritePython(valueString);
        ofs<<valueString;
        ofs.close();
    }
    for(auto& kv:database->GetDamageEffectData().GetData())
    {
        std::ofstream ofs;
        std::string name=kv.first;
        std::string path= dirPath+"/damage_effect/"+strutil::toPythonVar(name)+".py";
        ofs.open(path);
        std::string valueString;
        kv.second.WritePython(valueString);
        ofs<<valueString;
        ofs.close();
    }





    // unsigned long nIterated = 0;
    // for (iter.First(); !iter.IsDone(); iter.Next())
    // {
    //     tcDatabaseObject* obj = iter.Get();
    //     std::ofstream ofs;
    //     std::string path= dirPath+"/"+obj->mzClass.c_str()+".py";
    //     ofs.open(path);
    //     std::string valueString;
    //     obj->WritePython(valueString);
    //     ofs<<valueString;
    //     ofs.close();
    //     nIterated++;
    // }
}






void tcGame::SetInGame(bool state)
{
    if (simState->IsMultiplayerClient())
    {
        if (state)
        {
            //tcMultiplayerInterface::Get()->BroadcastControlMessage(network::tcControlMessageHandler::CM_INGAME);
            //            if (infoConsole != 0)
            //            {
            //                infoConsole->Print("Sent CM_INGAME");
            //            }
        }
        else
        {
            //tcMultiplayerInterface::Get()->BroadcastControlMessage(network::tcControlMessageHandler::CM_OUTGAME);
            //            if (infoConsole != 0)
            //            {
            //                infoConsole->Print("Sent CM_OUTGAME");
            //            }
        }
    }
}


std::string GetFileExtension(const std::string& fileName) {

    size_t dotPos = fileName.rfind('.');

    if (dotPos == std::string::npos) {

        return ""; // 没有找到'.'

    }

    return fileName.substr(dotPos + 1);

}
void tcGame::LoadDamageEffect(const std::string&filePath)
{
    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();
    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();
    if (extension == "py")
    {
        pythonInterface->LoadDamageEffect(filePath.c_str());
    }
}
void tcGame::LoadWeaponDamage(const std::string&filePath)
{
    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();
    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();
    if (extension == "py")
    {
        pythonInterface->LoadWeaponDamage(filePath.c_str());
    }
}
void tcGame::LoadSignatureModel(const std::string&filePath)
{
    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();
    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();
    if (extension == "py")
    {
        pythonInterface->LoadSignatureModel(filePath.c_str());
    }
}
void tcGame::LoadAcousticModel(const std::string&filePath)
{
    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();


    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();
    if (extension == "py")
    {
        pythonInterface->LoadAcousticModel(filePath.c_str());
    }

}

void tcGame::LoadDatabaseObject(const std::string &filePath)
{
    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();


    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();
    if (extension == "py")
    {
        pythonInterface->LoadDBObject(filePath.c_str());
    }

}
/**
* Loads scenario with path+filename of 相对scenario文件夹
*/
void tcGame::LoadScenario(const std::string& filePath, const std::string& caption, bool startInEditMode)
{
    tcGameObject::SetEditMode(false);



    tcSimPythonInterface* pythonInterface =	tcSimPythonInterface::Get();


    // clear briefing in case scenario fails to set it
    pythonInterface->GetScenarioInterface()->ClearSimpleBriefing();

    string extension = GetFileExtension(filePath);

    tcScenarioRandomizer::Get()->Clear();


    if (extension == "py")
    {
        pythonInterface->LoadScenario(filePath.c_str());
    }
    else if (extension == "dat")
    {
        tcGameSerializer gameSerializer;

        try
        {
            gameSerializer.LoadFromBinary(filePath.c_str());
        }
        catch (...)
        {
            fprintf(stderr,"Error loading scenario, file may be corrupt.");
        }
    }
    else
    {
        fprintf(stderr, "tcScenarioSelectView::LoadScenario - Bad extension (%s)\n",
                extension.c_str());
        return;
    }



    if (tcSimState::Get()->msScenarioInfo.mbLoaded)
    {

        tcOptions::Get()->SetOptionString("LastScenarioPath", filePath.c_str());
        tcOptions::Get()->SetOptionString("LastScenarioName", caption.c_str());
        tcOptions::Get()->SetOptionString("LastScenarioExtension", extension.c_str());

        //        string filePathToSave(filePath.c_str());
        //        filePathToSave = filePathToSave.BeforeLast('.'); // remove extension
        //        filePathToSave.Replace(".","/");
        //        filePathToSave = wxString("scenarios/") + filePathToSave + wxString(".") + extension;
        //        string fileName(filePathToSave);
        //        bool fileExists = fileName.FileExists();
        //        assert(fileExists);
        //        tcOptions::Get()->SetOptionString("ScenarioSavePath", filePathToSave.c_str());


    }
    else
    {
        string s =
            strutil::format("Error in scenario %s (File may be missing, file name may have space in it, or error in scenario). "
                            "Check log/pyerr.txt for details.",
                            filePath);
        fprintf(stderr, s.c_str());

    }
        SaveDatabaseToPython("./database/py");
}

string tcGame::GetOutSimData()
{
    std::lock_guard<std::mutex> lock(mtx_outsimdata);
    return  outsimdata;
}





void tcGame::SetScenarioEdit(bool state)
{
    if ((mbScenarioEdit == state) || simState->IsMultiplayerActive()) return;

    SetTimeAccel(0);
    tcGameObject::SetEditMode(state);

    mbScenarioEdit = state;

}



/**
* Sets theater view center for tacticalMap.
*/
void tcGame::SetTheater(float lat_deg, float lon_deg)
{
    //std::string s = strutil::format("lon %.2f lat %.2f", lon_deg, lat_deg);
    //if (infoConsole != 0) infoConsole->Print(s.c_str());

    if ((lon_deg < -180.0f) || (lon_deg >= 180.0f) || (lat_deg < -90.0f) || (lat_deg > 90.0f))
    {
        fprintf(stderr, "tcGame::SetTheater - out of bounds (lat %f deg, lon %f deg)",
                lat_deg, lon_deg);
        assert(false);
        return;
    }

    int theaterDecimation = mapData->GetTheaterDecimation();
    if (!mapData->IsTheaterDecimationValid(theaterDecimation) || (theaterDecimation > 4))
    {
        theaterDecimation = mapData->GetHighResDecimation();
    }

    mapData->LoadHighResC(lon_deg, lat_deg, theaterDecimation);

}




/**
* Time acceleration mode change
* This is a more general version of SetPauseMode
*/
void tcGame::SetTimeAccel(long accel)
{

    simState->SetTimeAcceleration(accel);

    //    if (mbScenarioEdit)
    //    {
    //        if ((accel != 0) && (simState->GetTime() == 0))
    //        {
    //            tcOptions* options = tcOptions::Get();
    //            std::string revertFile = options->GetOptionString("ScenarioSavePath"); // full path and file name of last scenario
    //            std::string msg;

    //        }
    //        //return;
    //    }

       if (accel == 0)
       {
           mbPaused = true;
           accelerateTime = 0;
       }
    //    else if ((accel <= 60) || (accel == 120))
    //    {
    //        mbPaused = false;
    //        accelerateTime = accel - 1;
    //    }
    //    else if (accel == 99)
    //    {
    //        if (!mbPaused && (accelerateTime > 0))
    //        {
    //            accelerateTime = NextTimeAccelVal(accelerateTime, false);
    //        }
    //        else
    //        {
    //            mbPaused = true;
    //            accelerateTime = 0;
    //        }
    //    }
    //    else if (accel == 100)
    //    {
    //        mbPaused = !mbPaused; // toggle pause
    //        accelerateTime = 0;
    //    }
    //    else if (accel == 101)
    //    {
    //        if (!mbPaused)
    //        {
    //            accelerateTime = NextTimeAccelVal(accelerateTime, true);
    //        }
    //        else
    //        {
    //            mbPaused = false;
    //            accelerateTime = 0;
    //        }
    //    }
    //    else
    //    {
    //        fprintf(stderr, "tcGame::SetTimeAccel - accel out of range\n");
    //        return;
    //    }

    //    if (simState->IsMultiplayerClient())
    //    {
    //        long accelRequest = mbPaused ? 0 : accelerateTime + 1;

    //        std::string commandText = strutil::format("//gamespeed %d", accelRequest);
    //        //tcMultiplayerInterface::Get()->BroadcastChatText(commandText);
    //    }
    //    else
    //    {
    //        simState->SetTimeAcceleration(mbPaused ? 0 : accelerateTime+1);
    //    }
}



/**
* Used to test sky and date/time functions.
* @param delta_s time offset in seconds to apply to gameDateTime
*/
void tcGame::ShiftTime(float delta_s)
{
    tcDateTime dt;
    simState->GetDateTime(dt);
    dt.AdjustTimeSeconds(delta_s);
    simState->SetDateTime(dt);
}



/**
* If this object is running as a multiplayer client,
* set tcGame (main loop) time accel to simstate time accel.
* If running as server, set simstate to main loop time accel.
* Eventually this will all be moved to simstate to avoid
* this awkwardness.
*/
void tcGame::SynchTimeAcceleration()
{
    if (multiplayerMode == 0) return;

    if (multiplayerMode == 1) // client
    {
        long accel = simState->GetTimeAcceleration();//获得服务器的倍数
        if (accel == 0)
        {
            mbPaused = true;
            accelerateTime = 0;
        }
        else
        {
            mbPaused = false;
            accelerateTime = accel - 1;
        }
    }
    else // server
    {
        if (mbPaused)
        {
            simState->SetTimeAcceleration(0);
        }
        else
        {
            simState->SetTimeAcceleration(accelerateTime + 1);
        }
    }
}



/**
* UpdateStart.
*
* This method is called at game startup.
*/
bool tcGame::UpdateStart()
{
    return mbQuit;
}


bool tcGame::UpdateFrame()
{
    tcTime::Get()->Update();

    static unsigned long snFrameCount = 0;
    static unsigned long snprevFrameCount = 0;//

    static uint64_t  diff_ms;//时间差
    static double fps=0;
    static float fdt=0.025;//推进步长秒
    if(snFrameCount==0)//第一次
    {
        prevRealTime = std::chrono::system_clock::now();
    }
    else
    {
        auto curRealTime = std::chrono::system_clock::now();
        auto diff = std::chrono::duration_cast<std::chrono::milliseconds>(
            curRealTime-prevRealTime
            );
        diff_ms= diff.count();
    }

    if(diff_ms>=1000)//隔一秒统计一遍帧数
    {

        fps= (snFrameCount-snprevFrameCount)*1000.0/diff_ms;//计算帧率
        snprevFrameCount=snFrameCount;
        diff_ms=0;
        prevRealTime=std::chrono::high_resolution_clock::now();
    }




    const float dateTimeScale = 1.0f; // for testing sky effects

    if (endGame)
    {
        EndGame();
        return UpdateStart();
    }

    simState->Update();

    gameTime = simState->GetTime();
    simState->GetDateTime(gameDateTime);

    auto speedMax=(unsigned long)(fps*0.025);//全速最大推演倍数 snFrameCount%speedMax==0才推进就是1倍
    if(simState->GetTimeAcceleration()>0)
    {
        auto delta=speedMax/simState->GetTimeAcceleration();//按指定倍数推进
        delta=delta==0?1:delta;
        if (snFrameCount%delta==0)
        {
            gameTime += fdt;
            gameDateTime.AdjustTimeSeconds(fdt*dateTimeScale);
            simState->SetTime(gameTime);
            simState->SetDateTime(gameDateTime);

        }
    }

    //    directorTime += fdt; // run director when not in simple brief mode
    std::cout << "\r";
    std::cout << std::left<<std::setw(10) << simState->GetTime()<<" " ;
    std::cout << simState->GetDateTime().GetYear()<<"-" ;
    std::cout << std::left<<std::setw(2)<<simState->GetDateTime().GetMonth()<<"-" ;
    std::cout << std::left<<std::setw(2)<<simState->GetDateTime().GetDay()<<" " ;
    std::cout <<std::left<<std::setw(2)<< simState->GetDateTime().GetHour()<<":" ;
    std::cout << std::left<<std::setw(2)<<simState->GetDateTime().GetMinute()<<":" ;
    std::cout << std::left<<std::setw(2)<<simState->GetDateTime().GetSecond() ;
    //更新输出数据
    UpdateOutSimData();
    //处理命令
    ProcessCommandList();


    if (snFrameCount % 90 == 0)
    {
        CheckGoals(); // checks win/loss goals and prints status
    }

    snFrameCount++;

    //    tcSimPythonInterface::Get()->Update();
    if (mbQuit) simState->Clear(); // prevent crash when gameobj model deleted after 3D engine

    return mbQuit;
}




/**
* Periodically call to check apply any recent changes to tcOptions
*/
void tcGame::UpdateOptions()
{
    tcOptions* options = tcOptions::Get();
    // tcTVEngine* engine = tcTVEngine::Get();

    //engine->UpdateOptions();
    tcUnits::Get()->Update();
    enableClientSync = (options->syncClient != 0);

    //    tcSound* sound = tcSound::Get();
    //    sound->SetEffectVolume(options->effectVolume);
    //    sound->SetMusicVolume(options->musicVolume);

    tcDatabaseObject::displayNATO = (options->natoNames != 0);

    //#ifdef _DEBUG
    static float lastUpdateTime = 0;
    float t = simState->GetTime();
    if (lastUpdateTime > t) lastUpdateTime = t;

    if (((t - lastUpdateTime) >= 1.0) && options->OptionStringExists("EnableXmlLog"))
    {
        tcGameSerializer serializer;
        lastUpdateTime = t;

        tinyxml2::XMLDocument doc;
        serializer.SaveToXml(doc);
        std::string fileName = strutil::format("log/unit_state.xml");
        doc.SaveFile(fileName.c_str());
    }

    //#endif
}




void tcGame::Activate() {}

bool tcGame::Finish()
{
    //	tcSound::Get()->UnInit();

//	if (director) delete director;

//tcMultiplayerInterface::Get()->LogOutAllPlayers();

#ifdef _DEBUG
    tcSimPythonInterface::Get()->FlushLogs();
#endif

    return true;
}


/**
* @returns a time scale factor to try to keep client synchronized with server
* returns 1.0 if not multiplayer client
*/
float tcGame::GetClientSyncFactor()
{
    if (multiplayerMode != 1) return 1.0; // return 1.0 if not multiplayer client

    if (!enableClientSync) return 1.0;

    const float targetLag = -0.15f;
    float multiplayerTimeLag_s = (float)simState->GetMultiplayerTimeLag();

    // scale factor applies to simulation time step, so < 1 slows down client
    float scaleFactor = 1.0f + 0.5*(multiplayerTimeLag_s - targetLag);
    scaleFactor = std::min(scaleFactor, 1.05f);
    scaleFactor = std::max(scaleFactor, 0.95f);

    return scaleFactor;
}

//bool tcGame::HandleEraseBkgnd(WXHDC hDC)
//{
//    return TRUE;
//}

/**
* Hooks first friendly platform.
* Used to avoid blank 3D screen in rand scenario
*/
void tcGame::HookRandomFriendly()
{
    const unsigned maxPlats = 32;
    long id[maxPlats];

    int ownAlliance = userInfo->GetOwnAlliance();
    if (ownAlliance == 0) return; // no alliance selected yet (multiplayer)

    unsigned count = simState->GetAlliancePlatforms(&id[0], maxPlats, ownAlliance);

    if (count)
    {
        unsigned idx = rand() % count;
        //		NewHook(id[idx]);
    }
    //#ifdef _DEBUG
    //	else
    //	{
    //		fprintf(stderr, "tcGame::HookRandomFriendly - No friendlies found.\n");
    //	}
    //#endif
}



/**
* @return next value in sequence, up/down based on goFaster
* values are accel scale factor minus 1, e.g. 0 is real time
*/
int tcGame::NextTimeAccelVal(int current, bool goFaster) const
{
    // allow faster than
    if (tcPlatformInterface::IsDeveloperModeStatic())
    {
        if (current >= 119)
        {
            if (goFaster)
            {
                return (2*current + 1);
            }
            else
            {
                return ((current -1)/2);
            }
        }
    }

    if (goFaster)
    {
        switch (current)
        {
        case 0: return 1; // 1X -> 2X
        case 1: return 3; // 2X -> 4X
        case 3: return 9; // 4X -> 10X
        case 9: return 29; // 10X -> 30X
        case 29: return 59; // 30X -> 60X
        case 59: return 119; // 60X -> 120X
        default: return std::min(current, 119);
        }
    }
    else
    {
        switch (current)
        {
        case 1: return 0; // 2X -> 1X
        case 3: return 1; // 4X -> 2X
        case 9: return 3; // 10X -> 4X
        case 29: return 9; // 30X -> 10X
        case 59: return 29; // 60X -> 30X
        case 119: return 59; // 120X -> 60X
        default: return std::min(current, 119);
        }
    }

}



void tcGame::ProcessCommandList()
{
    //    if(!commandStringMemory.attach(QSharedMemory::ReadWrite))//将shareMemory与该进程绑定使之可以访问shareMemory里的内容
    //    {
    //        std::cerr<<("can't attach share memory");
    //        std::cerr<<commandStringMemory.errorString().toStdString();
    //        return  ;
    //    }
    // commandStringMemory.lock();//给shareMemory枷锁
    // const char *from = (char*)commandStringMemory.data();
    // char *to = (char*)&commandStringData;
    // memcpy(to,from,sizeof(unsigned long));//数据从该进程中拷贝到共享数据内存中
    // from+=sizeof (unsigned int);
    // to+=sizeof (unsigned int);
    // memcpy(to,from,commandStringData.length+1);//数据从该进程中拷贝到共享数据内存中
    // ((CommandString*)commandStringMemory.data())->length=0;
    //  ((CommandString*)commandStringMemory.data())->str[0]=0;
    // commandStringData.unlock();
    //    commandStringMemory.detach();//将shareMemeory与该进程分离
    //执行

    std::lock_guard<std::mutex> lock(mtx_cmds);
    for (auto &cmd:cmds) {
        py::exec(cmd);
    }
    cmds.clear();

}


/**
* Process ESC key event. Cancels GUI command if active,
* otherwise quits the game.
*/
//void tcGame::ProcessEsc()
//{
//	if (popupControl->mbActive)
//	{
//		popupControl->SetActive(false);
//		return;
//	}
//	else if (tacticalMap->IsMapCmdActive())
//	{
//		tacticalMap->DeactivateMapCommand();
//		return;
//	}
//    else if (chatBox->mbActive)
//    {
//        chatBox->SetActive(false);
//        return;
//    }


//	wxMessageDialog confirmQuit(this, "Exit game?", "Confirm", wxOK | wxCANCEL, wxDefaultPosition);
//	if (confirmQuit.ShowModal() == wxID_OK)
//	{
//		EndGame();
//	}
//}


/**
* Calls Python callback
*/
//void tcGame::ProcessCallback(tsCommandInfo& cmd)
//{
//	// done this way for easy compatibility with old code body
//	char* azCallback = cmd.mzString;
//	char* azUserInput = cmd.mzUserInput;
//	std::vector<long>& id = cmd.platformID;
//	int param = cmd.mnData;
//	const std::string& textParam = cmd.textParam;

//    std::string userInput(azUserInput);
//    userInput = userInput.BeforeFirst(' ');

//	if (userInput == "Heading")
//	{
//		float fHeading = tacticalMap->GetMapCmdHeading();
//		pythonInterface->ProcessCallback(azCallback, id, fHeading, param, textParam);
//	}
//	else if (userInput == "Target")
//	{
//		long nTarget = tacticalMap->GetMapCmdTarget();
//		pythonInterface->ProcessCallback(azCallback, id, nTarget, param, textParam);
//	}
//	else if (userInput == "Datum")
//	{
//		tcPoint p;
//		tacticalMap->GetMapCmdDatum(p);
//		pythonInterface->ProcessCallback(azCallback, id, p.x, p.y, param, textParam);
//	}
//    else if (userInput == "Box")
//    {
//		tcPoint p1;
//        tcPoint p2;
//		tacticalMap->GetMapCmdDatum(p1);
//        tacticalMap->GetMapCmdDatum2(p2);
//        std::string s;
//        s=strutil::format("%f,%f,%f,%f", p1.x, p1.y, p2.x, p2.y);
//        if (param != -1) s += strutil::format(",%d", param);
//        pythonInterface->ProcessCallbackArgList(azCallback, id, s);
//    }
//    else if (userInput == "Line")
//    {
//		tcPoint p1;
//        tcPoint p2;
//		tacticalMap->GetMapCmdDatum(p1);
//        tacticalMap->GetMapCmdDatum2(p2);
//        std::string s;
//        s=strutil::format("%f,%f,%f,%f", p1.x, p1.y, p2.x, p2.y);
//        if (param != -1) s += strutil::format(",%d", param);
//        pythonInterface->ProcessCallbackArgList(azCallback, id, s);
//    }
//	else if (userInput == "Text")
//	{
//        std::string s; /// don't need single quotes any more, triple quoting JUN2010 ("'");
//        s += cmd.textParam;
//        //s += "'";
//		pythonInterface->ProcessCallback(azCallback, id, s, param);
//	}
//	else if (userInput == "Null") // necessary? or always handled in GetUserInput
//	{
//		pythonInterface->ProcessCallback(azCallback, id);
//	}
//	else
//	{
//		fprintf(stderr, "tcGame::ProcessCallback -- unrecognized user input field (%s)\n",
//            userInput.c_str().AsChar());
//	}
//}

/**
* Gets user input for Python call back and then calls Python callback
*/
//void tcGame::GetUserInput(const tsCommandInfo& cmd)
//{
//	const char* azCallback = cmd.mzString;
//	const char* azUserInput = cmd.mzUserInput;
//	std::vector<long> id = cmd.platformID;
//	int param = cmd.mnData;

//	tacticalMap->SetMapCmdCallback(azCallback, id, param, cmd.textParam);


//    std::string userInput(azUserInput);
//    std::string userInputRoot(userInput.BeforeFirst(' '));


//	if (userInputRoot == "Heading")
//	{
//		tacticalMap->ActivateMapCommand(MC_HEADING);
//	}
//	else if (userInputRoot == "Target")
//	{
//		tacticalMap->ActivateMapCommand(MC_TARGET);
//	}
//	else if (userInputRoot == "Datum")
//	{
//		tacticalMap->ActivateMapCommand(MC_DATUM);
//	}
//    else if (userInputRoot == "Box")
//    {
//        tacticalMap->ActivateMapCommand(MC_BOX);
//    }
//    else if (userInputRoot == "Line")
//    {
//        tacticalMap->ActivateMapCommand(MC_LINE);
//    }
//	else if (userInputRoot == "Text")
//	{
//        std::string textCaption(userInput.AfterFirst(' '));
//        if (textCaption.size() == 0)
//        {
//            textCaption = "Enter text";
//        }

//		tsCommandInfo callbackCmd = cmd;
//		callbackCmd.commandType = PYTHON_CALLBACK;

//		tcTextEntryBox* textEntry = new tcTextEntryBox(wxPoint(mnWidth/2-100, mnHeight/2-30), wxSize(210, 60));
//        textEntry->SetCaption(textCaption);
//		textEntry->SetCommand(callbackCmd);
//        textEntry->SetActive(true);
//        textEntry->Raise();

//	}
//    else if (userInputRoot == "File")
//    {
//        std::string wildCard(userInput.AfterFirst(' '));
//        if (wildCard.size() == 0)
//        {
//            wildCard = "*.*";
//        }

//        wxFileDialog fileDialog(this, "Choose a file", "", "", wildCard);
//        if (fileDialog.ShowModal() == wxID_OK)
//        {
//            std::string filePath(fileDialog.GetPath());
//            for (size_t n=0; n<filePath.size(); n++)
//            {
//                wxChar cn = filePath[n];
//                if (filePath[n] == wxChar('\\'))
//                {
//                    filePath.SetChar(n, '/');
//                }
//            }

//            std::string filePath2(filePath.c_str()); // full path and filename

//            std::string callback(cmd.mzString);
//            pythonInterface->ProcessCallback(callback, id, filePath2, param);
//        }
//    }
//    else if (userInputRoot == "Paragraph")
//    {
//        std::string startText;
//        std::string caption(userInput.AfterFirst(' '));

//        if (caption == "ScenarioDescription")
//        {
//            caption = "Enter scenario description";
//            startText = simState->GetScenarioDescription();
//        }
//        else if (caption == "Briefing")
//        {
//            caption = "Enter briefing text";
//            tcScenarioInterface* scenarioInterface = tcSimPythonInterface::Get()->GetScenarioInterface();
//            startText = scenarioInterface->GetSimpleBriefing(userInfo->GetOwnAlliance()).c_str();
//        }
//        else
//        {
//            caption = "Enter text";
//        }

//        tcTextDialog inputDialog(tacticalMap, -1, caption, startText,
//            wxPoint(200, 150), wxSize(400, 250) );

//        if (inputDialog.ShowModal() != wxID_OK) return;

//        std::string dialogText = inputDialog.GetText();

//        std::string dialogText2(dialogText.c_str());

//        std::string callback(cmd.mzString);
//        pythonInterface->ProcessCallback(callback, id, dialogText2, param);
//    }
//    else if (userInputRoot == "Null")
//	{
//		pythonInterface->ProcessCallback(azCallback, id);
//	}
//	else
//	{
//		tacticalMap->SetMapCmdCallback("", id, -1, "");
//	}
//}



//void tcGame::TextCommandShowFlightPanel(const tsCommandInfo& cmd)
//{
//    tcPlatformObject* platform = tcSimPythonInterface::Get()->GetHookedObj();
//    tcFlightPort* flightPort = tcSimPythonInterface::Get()->GetHookedObjFlightPort();
//    if (flightPort)
//    {
//        // Freeze() to prevent flicker, not sure why this works
//        /*
//        popupControl->Freeze();
//        popupControl->SetMenu(MENUMODE_FLIGHTPANEL);
//        popupControl->Track(wxPoint(mrectMap.left+220,mrectMap.top+70));
//        */

//        std::string xmlFile;
//        if (flightPort->GetHangarCapacity() > 20)
//        {
//            xmlFile = "xml/flightport_gui_large.xml";
//        }
//        else
//        {
//            xmlFile = "xml/flightport_gui_default.xml";
//        }

//        tcFlightPortGui* existingGui = tcFlightPortGui::GetExistingGui(platform->mnID);
//        if (existingGui == 0)
//        {
//            tcFlightPortGui* gui = new tcFlightPortGui(platform->mnID, wxPoint(250, 200), xmlFile.c_str());
//        }
//        else// toggle close if exists already
//        {
//            existingGui->DestroyWindow();
//        }
//    }
//}

//void tcGame::TextCommandShowStoresPanel(const tsCommandInfo& cmd)
//{
//    if (tcPlatformObject* obj = tcSimPythonInterface::Get()->GetHookedObj())
//    {
//        if (tcStores* stores = obj->GetMagazine(0))
//        {
//            tcStoresGui* existingGui = tcStoresGui::GetExistingGui(obj->mnID, -1);
//            if (existingGui == 0)
//            {
//                tcStoresGui* gui = new tcStoresGui(obj->mnID, -1, 0, wxPoint(500, 200), "xml/stores_gui_table.xml");
//            }
//            else// toggle close if exists already
//            {
//                existingGui->DestroyWindow();
//            }

//        }
//    }
//}

//void tcGame::TextCommandShowPlatformPanel(const tsCommandInfo& cmd)
//{
//    tcPlatformObject* obj = tcSimPythonInterface::Get()->GetHookedObj();
//    if (obj)
//    {
//        tcPlatformGui* existingGui = tcPlatformGui::GetExistingGui(obj->mnID, -1);
//        if (existingGui == 0)
//        {
//            tcPlatformGui* gui = new tcPlatformGui(obj->mnID, -1, wxPoint(220, 70), "xml/platform_gui_default.xml");
//        }
//        else // toggle close if exists already
//        {
//            existingGui->DestroyWindow();
//        }
//    }
//}

//void tcGame::TextCommandShowSonarPanel(const tsCommandInfo& cmd)
//{
//	if (!tcPlatformInterface::GetDeveloperMode() && !tcGameObject::IsEditMode()) return;

//    ShowSonarPanel();
//}

//void tcGame::TextCommandCopperMap(const tsCommandInfo& cmd)
//{
//    tcOptions::Get()->mnMapMode = 0;
//    RefreshMaps();
//}

//void tcGame::TextCommandYellowBlueMap(const tsCommandInfo& cmd)
//{
//    tcOptions::Get()->mnMapMode = 1;
//    RefreshMaps();
//}

//void tcGame::TextCommandBlackBlueMap(const tsCommandInfo& cmd)
//{
//    tcOptions::Get()->mnMapMode = 2;
//    RefreshMaps();
//}

//void tcGame::TextCommandReimportPython(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;

//    tcSimPythonInterface::Get()->ReimportModules();

////    infoConsole->Print("Reimporting python");
//}

//void tcGame::TextCommandSetFormationEditId(const tsCommandInfo& cmd)
//{
//    long id = long(cmd.mnData);
//    if (tacticalMap != 0)
//    {
//        tacticalMap->SetFormationEditId(id);
//    }
//    else
//    {
//        assert(false);
//    }
//}



//void tcGame::TextCommandShowAirInfo(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;
//    ShowAirInfo();
//}

//void tcGame::TextCommandTestCollision(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;
//    TestCollision();
//}

//void tcGame::TextCommandTestCrossSection(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;
//    TestCrossSection();
//}

//void tcGame::TextCommandToggleUserAlliance(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;
//    simState->ToggleUserAlliance();
//	tacticalMap->UpdateROEButtons();
//    infoConsole->Print("Toggling user alliance");
//}

//void tcGame::TextCommandShowPlatformDebug(const tsCommandInfo& cmd)
//{
//    if (!tcPlatformInterface::GetDeveloperMode()) return;
//    ShowPlatformDebug();
//}



/**
* Call once at startup
*/
//void tcGame::RegisterTextCommands()
//{
//    textCommands.clear();

//    textCommands["ShowFlightPanel"] = &tcGame::TextCommandShowFlightPanel;
//    textCommands["ShowStoresPanel"] = &tcGame::TextCommandShowStoresPanel;
//    textCommands["ShowPlatformPanel"] = &tcGame::TextCommandShowPlatformPanel;
//    textCommands["CopperMap"] = &tcGame::TextCommandCopperMap;
//    textCommands["YellowBlueMap"] = &tcGame::TextCommandYellowBlueMap;
//    textCommands["BlackBlueMap"] = &tcGame::TextCommandBlackBlueMap;
//    textCommands["SetFormationEditId"] = &tcGame::TextCommandSetFormationEditId;

//    // "dev mode" commands
//    textCommands["ShowAirInfo"] = &tcGame::TextCommandShowAirInfo;
//    textCommands["TestCollision"] = &tcGame::TextCommandTestCollision;
//    textCommands["TestCrossSection"] = &tcGame::TextCommandTestCrossSection;
//    textCommands["ToggleUserAlliance"] = &tcGame::TextCommandToggleUserAlliance;
//    textCommands["ShowPlatformDebug"] = &tcGame::TextCommandShowPlatformDebug;
//    textCommands["ShowSonarPanel"] = &tcGame::TextCommandShowSonarPanel;
//    textCommands["ReimportPython"] = &tcGame::TextCommandReimportPython;

//}


/**
* command string is contained in cmd_info.mzString, this is the text version
* of ProcessCommand. Currently used for special commands originated in Python,
* such as "ShowFlightPanel".
*/
void tcGame::ProcessTextCommand(tsCommandInfo cmd_info)
{
    std::string s = cmd_info.mzString;

    std::map<std::string, commandFunctionPtr>::iterator iter =
        textCommands.find(s);

    if (iter != textCommands.end())
    {
        (this->*iter->second)(cmd_info);
    }
    else
    {
        fprintf(stderr, "Unrecognized text command (%s)\n", s.c_str());
        assert(false);
    }

#if 0
    if (s == "ShowFlightPanel")
    {
        tcPlatformObject* platform = tcSimPythonInterface::Get()->GetHookedObj();
        tcFlightPort* flightPort = tcSimPythonInterface::Get()->GetHookedObjFlightPort();
        if (flightPort)
        {
            // Freeze() to prevent flicker, not sure why this works
            /*
            popupControl->Freeze();
            popupControl->SetMenu(MENUMODE_FLIGHTPANEL);
            popupControl->Track(wxPoint(mrectMap.left+220,mrectMap.top+70));
            */

            std::string xmlFile;
            if (flightPort->GetHangarCapacity() > 20)
            {
                xmlFile = "xml/flightport_gui_large.xml";
            }
            else
            {
                xmlFile = "xml/flightport_gui_default.xml";
            }

            tcFlightPortGui* existingGui = tcFlightPortGui::GetExistingGui(platform->mnID);
            if (existingGui == 0)
            {
                tcFlightPortGui* gui = new tcFlightPortGui(platform->mnID, wxPoint(250, 200), xmlFile.c_str());
            }
            else// toggle close if exists already
            {
                existingGui->DestroyWindow();
            }
        }
    }
    else if (s == "ShowStoresPanel")
    {
        if (tcPlatformObject* obj = tcSimPythonInterface::Get()->GetHookedObj())
        {
            if (tcStores* stores = obj->GetMagazine(0))
            {
                tcStoresGui* existingGui = tcStoresGui::GetExistingGui(obj->mnID, -1);
                if (existingGui == 0)
                {
                    tcStoresGui* gui = new tcStoresGui(obj->mnID, -1, 0, wxPoint(500, 200), "xml/stores_gui_table.xml");
                }
                else// toggle close if exists already
                {
                    existingGui->DestroyWindow();
                }

            }
        }
    }
    else if (s == "ShowPlatformPanel")
    {
        tcPlatformObject* obj = tcSimPythonInterface::Get()->GetHookedObj();
        if (obj)
        {
            tcPlatformGui* existingGui = tcPlatformGui::GetExistingGui(obj->mnID, -1);
            if (existingGui == 0)
            {
                tcPlatformGui* gui = new tcPlatformGui(obj->mnID, -1, wxPoint(220, 70), "xml/platform_gui_default.xml");
            }
            else // toggle close if exists already
            {
                existingGui->DestroyWindow();
            }
        }
    }
    else if (s == "CopperMap")
    {
        tcOptions::Get()->mnMapMode = 0;
        RefreshMaps();
    }
    else if (s == "YellowBlueMap")
    {
        tcOptions::Get()->mnMapMode = 1;
        RefreshMaps();
    }
    else if (s == "BlackBlueMap")
    {
        tcOptions::Get()->mnMapMode = 2;
        RefreshMaps();
    }
    else if (s == "SetFormationEditId")
    {
        long id = long(cmd_info.mnData);
        if (tacticalMap != 0)
        {
            tacticalMap->SetFormationEditId(id);
        }
        else
        {
            assert(false);
        }
    }
#endif

}

void tcGame::AddCommand(const std::string &cmd)
{
    std::lock_guard<std::mutex> lock(mtx_cmds);
    this->cmds.push_back(cmd);
}


/**
* Used for quick mouse-targeting of another platform.
* Map posts this event when right mouse button is 
* clicked over another platform.
* Python script is used to do the targeting to allow
* this to be customized.
*/
//void tcGame::SecondaryHook(wxCommandEvent& event)
//{
//	long hookID = tacticalMap->GetHookID();
//	long nSecondaryHookID = event.GetExtraLong(); // 2.6.3 m_extraLong;

//	if ((hookID == NULL_INDEX) || (hookID == nSecondaryHookID))
//	{
//		return;
//	}
//	pythonInterface->ProcessSecondaryHook(nSecondaryHookID);

//}

/**
* After game started, calculates collision point on current hooked obj
* based on look direction and position of camera. If collision occurs, 
* adds explosion graphic to obj at collision point
*/
//void tcGame::TestCollision()
//{
//    if (meGameMode == GM_START) return; // ignore if game has not started

////    infoConsole->Print("Testing collision");


//    float cameraAz = viewer->GetCameraAz();
//    float cameraEl = viewer->GetCameraEl();
//    float cameraRange = viewer->GetCameraRange();

//    float camx = -cosf(cameraEl)*sinf(cameraAz);
//    float camz = -cosf(cameraEl)*cosf(cameraAz);
//    float camy = -sinf(cameraEl);







//    long hookID = tacticalMap->GetHookID();

//    tcGameObject* hookedObj = simState->GetObject(hookID);
//    if (hookedObj == 0) return;




//    Vector3d start_eun(-camx*cameraRange, -camy*cameraRange, -camz*cameraRange);
//    Vector3d dir_eun(camx, camy, camz);


//    unsigned int nHits = hookedObj->CalculateRandomHits(start_eun, dir_eun, cameraRange, 0.01f, 8);


//    tcGameObject testObj;
//    testObj.mcKin = hookedObj->mcKin;
//    testObj.mcKin.mfAlt_m += start_eun.y();
//    testObj.mcKin.mfLat_rad += start_eun.z() * C_MTORAD;
//    testObj.mcKin.mfLon_rad += start_eun.x() * C_MTORAD / cosf(testObj.mcKin.mfLat_rad);
//    testObj.mcKin.mfHeading_rad = cameraAz + C_PI;
//    testObj.mcKin.mfClimbAngle_rad = -cameraEl;
//    testObj.mcKin.mfPitch_rad = -cameraEl;
//    testObj.mcKin.mfRoll_rad = 0;
//    testObj.mcKin.mfSpeed_kts = 20000;


//    Vector3d pos;
//    float distance_m;
//    bool collides = hookedObj->CalculateCollisionPointArb(start_eun, dir_eun, pos, distance_m);

//    Vector3d pos2;
//    float dt_s;
//    float dist_m;
//    bool collides2 = hookedObj->CalculateCollisionPoint(&testObj, pos2, dt_s, dist_m);

//    if (collides)
//    {
//        std::string s;
//        s=strutil::format("RUF: %.1f %.1f %.1f", pos.x(), pos.y(), pos.z());
////        infoConsole->Print(s.c_str());

//        //hookedObj->model->AddExplosion(pos);
//    }
//    else
//    {
////        infoConsole->Print("No collision");
//    }

//}



/**
* Prints computed cross-section of hooked object from current camera angle
*/
//void tcGame::TestCrossSection()
//{
//    if (meGameMode == GM_START) return; // ignore if game has not started

//    infoConsole->Print("Testing cross-section");


//    float cameraAz = viewer->GetCameraAz();
//    float cameraEl = viewer->GetCameraEl();
//    float cameraRange = viewer->GetCameraRange();

//    float camx = -cosf(cameraEl)*sinf(cameraAz); // east
//    float camz = -cosf(cameraEl)*cosf(cameraAz); // north
//    float camy = -sinf(cameraEl); // up


//    long hookID = tacticalMap->GetHookID();

//    tcGameObject* hookedObj = simState->GetObject(hookID);
//    if (hookedObj == 0) return;

//    Vector3d dir_eun(camx, camy, camz);

//    unsigned int startCount = tcTime::Get()->GetUpdated30HzCount();

//    float area_m2 = 0;
//    for (size_t k=0; k<10; k++)
//    {
//        area_m2 = hookedObj->CalculateCrossSectionDir(dir_eun);
//    }

//    unsigned int duration = tcTime::Get()->GetUpdated30HzCount() - startCount;

//    std::string s;
//    s=strutil::format("Area: %.1f m2 (%d tics)", area_m2, duration);
//    infoConsole->Print(s.c_str());

//}

/**
* Check that each hooked id still exists in simulation, otherwise removed from hooked list
*/
void tcGame::ValidateHooked()
{
    unsigned char playerAlliance = tcUserInfo::Get()->GetOwnAlliance();
    std::vector<long> validHooks;

    for (size_t n=0; n<hookedUnits.size(); n++)
    {
        long id = hookedUnits[n];
        if (simState->GetObject(id) != 0)
        {
            validHooks.push_back(id);
        }
        else if (simState->IsMultiplayerClient())
        {
            if (tcSensorMapTrack* track = simState->mcSensorMap.GetSensorMapTrack(id, playerAlliance))
            {
                validHooks.push_back(id);
            }
        }
    }

    if (validHooks.size() < hookedUnits.size())
    {
        //        NewGroupHook(validHooks);
    }
}

/**
* The tcGame object constructor.
*
*/
tcGame::tcGame()
    :
    messageCenter(0),
    enableClientSync(true)
{



    simState = tcSimState::Get();
    database = tcDatabase::Get();
    //    commandQueue = tcCommandQueue::Get();
    
#ifdef _DEBUG
    database->LogSqlColumns("column_log.csv");
#endif


    pythonInterface = tcSimPythonInterface::Get();
    goalTracker = tcGoalTracker::Get();

    userInfo = tcUserInfo::Get();
    tcUserInfo::AttachAllianceInfo();
    tcControllableObject::AttachUserInfo();
    tcControllableObject::AttachAllianceInfo();
    tcControllableObject::AttachDatabase();

    mapData = tcMapData::Get();


    mbQuit = false;
    endGame = false;
    mbPaused = false;
    mbScenarioEdit = false;
    accelerateTime = 0;
    //	meScreenMode = TACTICAL;
    //    lastMode = NONE;

    //	mb3DActive = true;
    //	size3D = MODE3D_SMALL;
    meEditControlState = ECS_NONE;
    mbSwitchToPlay = false;
    gameTime = 0;
    //    nLastCount = 0;
    multiplayerMode = 0; // single-player default

    togglePopup = false;

    std::cout << "Game constructor success" << std::endl;

    // sharedSimDataMemory.setKey("SharedSimData");
    // if(sharedSimDataMemory.isAttached())
    // {
    //     sharedSimDataMemory.detach();//将该进程与共享内存段分离
    // }
    // sharedSimDataMemory.create(sizeof (SharedSimData), QSharedMemory::ReadWrite);

    // commandStringMemory.setKey("CommandString");//设置标志一定要与共享内存的标志一样
    // if(commandStringMemory.isAttached())
    // {
    //     commandStringMemory.detach();//将该进程与共享内存段分离
    // }
    // commandStringMemory.create(sizeof (CommandString), QSharedMemory::ReadWrite);
}

/**
* The tcGame object destructor.
*
*/
tcGame::~tcGame()
{
    //	messageConsole = 0;

    Finish();
}
std::string mnModelType2String(int mnModelType)
{
    std::string str="OBJECT";
    switch (mnModelType) {

    case MTYPE_OBJECT:
        str="MTYPE_OBJECT";
        break;
    case MTYPE_SURFACE:
        str="MTYPE_SURFACE";
        break;
    case MTYPE_CARRIER:
        str="MTYPE_CARRIER";
        break;
    case MTYPE_AIR :
        str="MTYPE_AIR";
        break;
    case MTYPE_FIXEDWING:
        str="MTYPE_FIXEDWING";
        break;
    case MTYPE_MISSILE:
        str="MTYPE_MISSILE";
        break;
    case MTYPE_HELO:
        str="MTYPE_HELO";
        break;
    case MTYPE_SUBSURFACE:
        str="MTYPE_SUBSURFACE";
        break;
    case MTYPE_SUBMARINE:
        str="MTYPE_SUBMARINE";
        break;
    case MTYPE_TORPEDO :
        str="MTYPE_TORPEDO";
        break;
    case MTYPE_FIXED :
        str="MTYPE_FIXED";
        break;
    case MTYPE_PLATFORM :
        str="MTYPE_PLATFORM";
        break;
    case MTYPE_FIXEDWINGX :
        str="MTYPE_FIXEDWINGX";
        break; // model with more realism
    case MTYPE_AIRFIELD :
        str="MTYPE_AIRFIELD";
        break;
    case MTYPE_BALLISTIC :
        str="MTYPE_BALLISTIC";
        break;
    case MTYPE_SONOBUOY :
        str="MTYPE_SONOBUOY";
        break;
    case MTYPE_AIRCM :
        str="MTYPE_AIRCM";
        break;// air countermeasure model
    case MTYPE_GROUNDVEHICLE :
        str="MTYPE_GROUNDVEHICLE";
        break;// e.g. ground mobile SAM
    case MTYPE_FUELTANK :
        str="MTYPE_FUELTANK";
        break;
    case MTYPE_LASERGUIDEDBOMB:
        str="LASERGUIDEDBOMB";
        break;
    case MTYPE_WATERCM:
        str="MTYPE_WATERCM";
        break; // water countermeasure model
    case MTYPE_BALLISTICMISSILE :
        str="BALLISTICMISSILE";
        break;
    case MTYPE_ROCKET :
        str="MTYPE_ROCKET";
        break;
    case MTYPE_SPACE :
        str="MTYPE_SPACE";
        break;
    default:
        str="MTYPE_OBJECT";
        break;
    }
    return str;

}
void tcTrackToJson(const tcSensorMapTrack& track,rapidjson::Value& v,rapidjson::Document& d) {
    v.AddMember("mfLon_rad", track.mfLon_rad,d.GetAllocator());
    v.AddMember("mfLat_rad", track.mfLat_rad,d.GetAllocator());
    v.AddMember("mfAlt_m", track.mfAlt_m,d.GetAllocator());
    v.AddMember("mfSpeed_kts", track.mfSpeed_kts,d.GetAllocator());
    v.AddMember("mfHeading_rad", track.mfHeading_rad,d.GetAllocator());
    v.AddMember("mfClimbAngle_rad", track.mfClimbAngle_rad,d.GetAllocator());
    v.AddMember("bearing_rad", track.bearing_rad,d.GetAllocator());
    v.AddMember("bearingRate_radps", track.bearingRate_radps,d.GetAllocator());
    v.AddMember("mfTimestamp", track.mfTimestamp,d.GetAllocator());

    v.AddMember("mnID", (int)track.mnID,d.GetAllocator());
    v.AddMember("mnClassification", track.mnClassification,d.GetAllocator());
    v.AddMember("mnAffiliation", track.mnAffiliation,d.GetAllocator());
    v.AddMember("mnAlliance", track.mnAlliance,d.GetAllocator());
    v.AddMember("mnFlags", track.mnFlags,d.GetAllocator());

    rapidjson::Value sensorReports(rapidjson::kArrayType);
    for (const auto& report : track.maSensorReport) {
        rapidjson::Value reportObj;
        reportObj.SetObject();
        reportObj.AddMember("timeStamp", report.timeStamp,d.GetAllocator());
        reportObj.AddMember("startTime", report.startTime,d.GetAllocator());
        reportObj.AddMember("platformID", (int)report.platformID,d.GetAllocator());
        reportObj.AddMember("sensorID", (int)report.sensorID,d.GetAllocator());
        reportObj.AddMember("validFlags", report.validFlags,d.GetAllocator());
        rapidjson::Value emitterList(rapidjson::kArrayType);
        for (const auto& emitter : report.emitterList) {
            rapidjson::Value emitterValue(rapidjson::kNumberType);
            emitterValue.SetInt64(emitter); // 使用文档的分配器来分配内存
            emitterList.PushBack(emitterValue, d.GetAllocator());
        }
        reportObj.AddMember("emitterList", emitterList,d.GetAllocator());
        reportObj.AddMember("classification", report.classification,d.GetAllocator());
        reportObj.AddMember("alliance", report.alliance,d.GetAllocator());
        reportObj.AddMember("databaseID", (int64_t)report.databaseID,d.GetAllocator());
        reportObj.AddMember("lonEstimate_rad", report.lonEstimate_rad,d.GetAllocator());
        reportObj.AddMember("latEstimate_rad", report.latEstimate_rad,d.GetAllocator());
        reportObj.AddMember("C11", report.C11,d.GetAllocator());
        reportObj.AddMember("C22", report.C22,d.GetAllocator());
        reportObj.AddMember("C12", report.C12,d.GetAllocator());
        reportObj.AddMember("altEstimate_m", report.altEstimate_m,d.GetAllocator());
        reportObj.AddMember("altVariance", report.altVariance,d.GetAllocator());
        reportObj.AddMember("speedEstimate_mps", report.speedEstimate_mps,d.GetAllocator());
        reportObj.AddMember("speedVariance", report.speedVariance,d.GetAllocator());
        reportObj.AddMember("headingEstimate_rad", report.headingEstimate_rad,d.GetAllocator());
        reportObj.AddMember("headingVariance", report.headingVariance,d.GetAllocator());
        reportObj.AddMember("climbEstimate_rad", report.climbEstimate_rad,d.GetAllocator());
        reportObj.AddMember("climbVariance", report.climbVariance,d.GetAllocator());
        sensorReports.PushBack(reportObj,d.GetAllocator());
    }
    v.AddMember("maSensorReport", sensorReports,d.GetAllocator());

    rapidjson::Value emitterInfos(rapidjson::kArrayType);
    for (const auto& info : track.emitterInfo) {
        rapidjson::Value infoObj;
        infoObj.SetObject();
        infoObj.AddMember("mnEmitterID", (int64_t)info.mnEmitterID,d.GetAllocator());
        infoObj.AddMember("mfTimestamp", info.mfTimestamp,d.GetAllocator());
        infoObj.AddMember("mnMode", info.mnMode,d.GetAllocator());
        emitterInfos.PushBack(infoObj, d.GetAllocator());
    }
    v.AddMember("emitterInfo", emitterInfos,d.GetAllocator());

    rapidjson::Value intercepts(rapidjson::kArrayType);
    for (const auto& intercept : track.intercepts) {
        intercepts.PushBack((int64_t)intercept, d.GetAllocator());
    }
    v.AddMember("intercepts", intercepts,d.GetAllocator());

    rapidjson::Value engaged(rapidjson::kArrayType);
    for (const auto& engage : track.engaged) {
        engaged.PushBack((int64_t)engage, d.GetAllocator());
    }
    v.AddMember("engaged", engaged,d.GetAllocator());

    rapidjson::Value ambiguityList(rapidjson::kArrayType);
    for (const auto& ambiguity : track.ambiguityList) {
        ambiguityList.PushBack((int64_t)ambiguity, d.GetAllocator());
    }
    v.AddMember("ambiguityList", ambiguityList,d.GetAllocator());

    rapidjson::Value errorPoly(rapidjson::kArrayType);
    for (const auto& point : track.errorPoly) {
        rapidjson::Value pointObj;
        pointObj.SetObject();
        pointObj.AddMember("x", point.x,d.GetAllocator());
        pointObj.AddMember("y", point.y,d.GetAllocator());
        errorPoly.PushBack(pointObj, d.GetAllocator());
    }
    v.AddMember("errorPoly", errorPoly,d.GetAllocator());
    v.AddMember("errorPolyLonWidth_rad", track.errorPolyLonWidth_rad,d.GetAllocator());
    v.AddMember("errorPolyLatWidth_rad", track.errorPolyLatWidth_rad,d.GetAllocator());
    v.AddMember("alwaysVisible", track.alwaysVisible,d.GetAllocator());
}

void  tcGameObjectToJson(const tcGameObject& obj,rapidjson::Value& unitinfo,rapidjson::Document& document)
{
    rapidjson::Value mzUnitValue(rapidjson::kStringType);
    mzUnitValue.SetString(obj.mzUnit.c_str(), document.GetAllocator()); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mzUnit",mzUnitValue,document.GetAllocator());
    rapidjson::Value mnIDValue(rapidjson::kStringType);
    mnIDValue.SetInt64(obj.mnID); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mnID",mnIDValue,document.GetAllocator());
    rapidjson::Value mnModelTypeValue(rapidjson::kStringType);
    mnModelTypeValue.SetString(mnModelType2String(obj.mnModelType).c_str(), document.GetAllocator()); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mnModelType",mnModelTypeValue,document.GetAllocator());
    rapidjson::Value mzClassValue(rapidjson::kStringType);
    mzClassValue.SetString(obj.mzClass.c_str(), document.GetAllocator()); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mzClass",mzClassValue,document.GetAllocator());
    rapidjson::Value allianceValue(rapidjson::kNumberType);
    allianceValue.SetInt(obj.GetAlliance()); // 使用文档的分配器来分配内存
    unitinfo.AddMember("alliance",allianceValue,document.GetAllocator());
    rapidjson::Value mfLon_radValue(rapidjson::kNumberType);
    mfLon_radValue.SetDouble(obj.mcKin.mfLon_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfLon_rad",mfLon_radValue,document.GetAllocator());
    rapidjson::Value mfLat_radValue(rapidjson::kNumberType);
    mfLat_radValue.SetDouble(obj.mcKin.mfLat_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfLat_rad",mfLat_radValue,document.GetAllocator());
    rapidjson::Value mfAlt_mValue(rapidjson::kNumberType);
    mfAlt_mValue.SetFloat(obj.mcKin.mfAlt_m); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfAlt_m",mfAlt_mValue,document.GetAllocator());
    rapidjson::Value mfHeading_radValue(rapidjson::kNumberType);
    mfHeading_radValue.SetFloat(obj.mcKin.mfHeading_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfHeading_rad",mfHeading_radValue,document.GetAllocator());
    rapidjson::Value mfClimbAngle_radValue(rapidjson::kNumberType);
    mfClimbAngle_radValue.SetFloat(obj.mcKin.mfClimbAngle_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfClimbAngle_rad",mfClimbAngle_radValue,document.GetAllocator());
    rapidjson::Value mfYaw_radValue(rapidjson::kNumberType);
    mfYaw_radValue.SetFloat(obj.mcKin.mfYaw_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfYaw_rad",mfYaw_radValue,document.GetAllocator());
    rapidjson::Value mfPitch_radValue(rapidjson::kNumberType);
    mfPitch_radValue.SetFloat(obj.mcKin.mfPitch_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfPitch_rad",mfPitch_radValue,document.GetAllocator());
    rapidjson::Value mfRoll_radValue(rapidjson::kNumberType);
    mfRoll_radValue.SetFloat(obj.mcKin.mfRoll_rad); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfRoll_rad",mfRoll_radValue,document.GetAllocator());
    rapidjson::Value mfSpeed_ktsValue(rapidjson::kNumberType);
    mfSpeed_ktsValue.SetFloat(obj.mcKin.mfSpeed_kts); // 使用文档的分配器来分配内存
    rapidjson::Value mfDamageLevelValue(rapidjson::kNumberType);
    mfDamageLevelValue.SetFloat(obj.GetDamageLevel()); // 使用文档的分配器来分配内存
    unitinfo.AddMember("mfDamageLevel",mfDamageLevelValue,document.GetAllocator());
}

void tcGame::UpdateOutSimData()
{

    rapidjson::Document document;
    document.SetObject();
    //更新对象位置
    tcGameObject *obj;
    long cmappos = simState->maPlatformState.GetStartPosition();
    int nSize = simState->maPlatformState.GetCount();
    long nKey;
    //遍历对象更新
    // sharedSimData.count=nSize;

    rapidjson::Value mfSimTimeValue(rapidjson::kNumberType);
    mfSimTimeValue.Set(simState->GetTime()); // 使用文档的分配器来分配内存
    document.AddMember("mfSimTime",mfSimTimeValue,document.GetAllocator());

    rapidjson::Value dateTimeValue(rapidjson::kNumberType);
    dateTimeValue.Set(simState->GetDateTime().GetTimeT()); // 使用文档的分配器来分配内存
    document.AddMember("dateTime",dateTimeValue,document.GetAllocator());

    rapidjson::Value unitinfos(rapidjson::kArrayType);
    for (int i=0;i<nSize;i++)
    {
        simState->maPlatformState.GetNextAssoc(cmappos,nKey,obj);
        // 创建一个 Value 对象，用来存储字符串 "hello"
        rapidjson::Value unitinfo(rapidjson::kObjectType);
        tcGameObjectToJson(*obj,unitinfo,document);
        unitinfos.PushBack(unitinfo,document.GetAllocator());
    }
    document.AddMember("unitInfo",unitinfos,document.GetAllocator());

    //遍历每一方的探测目标
    //SensorMapTrack:[{"alliance":1,}]
    tcAllianceInfo* allianceInfo = tcAllianceInfo::Get();
    auto allianceList =allianceInfo->GetAllianceList();
    rapidjson::Value alliancesTrackJson(rapidjson::kArrayType);
    for(auto alliance :allianceList)
    {
        rapidjson::Value allianceTrackJson(rapidjson::kObjectType);
        allianceTrackJson.AddMember("alliance",alliance,document.GetAllocator());
        rapidjson::Value tracksJson(rapidjson::kArrayType);
        tcSensorTrackIterator iter(alliance, 0xFFFF);
        for (iter.First();iter.NotDone();iter.Next())
        {
            rapidjson::Value trackJson(rapidjson::kObjectType);
            tcSensorMapTrack* track = iter.Get();
            tcTrackToJson(*track,trackJson,document);
            tracksJson.PushBack(trackJson,document.GetAllocator());
        }
        allianceTrackJson.AddMember("tracks",tracksJson,document.GetAllocator());
        alliancesTrackJson.PushBack(allianceTrackJson,document.GetAllocator());
    }


    document.AddMember("allianceTrack",alliancesTrackJson,document.GetAllocator());
    {
        std::lock_guard<std::mutex> lock(mtx_outsimdata);
        // 将 JSON 文档序列化为字符串
        rapidjson::StringBuffer buffer;
        rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);
        document.Accept(writer);
        // 输出 JSON 字符串
        //  std::cout << buffer.GetString() << std::endl;
        // exit(0);
        outsimdata=buffer.GetString();

    }



    // sharedSimDataMemory.lock();
    // char *to = (char*)sharedSimDataMemory.data();
    // const char *from = (char*)&sharedSimData;
    // memcpy(to,from, sizeof(sharedSimData.count)+sharedSimData.count*sizeof(UnitInfo));//数据从该进程中拷贝到共享数据内存中
    // sharedSimDataMemory.unlock();//共享内层解锁
}


