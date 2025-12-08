/** 
**  @file Game.h
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

#if !defined _GAME_H_
#define _GAME_H_


#include "commandlist.h"

#include "tcUserInfo.h"
#include "tcTime.h"
#include "tcDateTime.h"

// #include <QSharedMemory>
#include <mutex>
#include <map>
namespace scriptinterface
{
    class tcSimPythonInterface;
};
namespace database
{
    class tcDatabase;
};
class tcSimState;
class tcCommandQueue;
class tcHookInfo;
//class tcOOBView;
//class tcPopupControl;
//class tc3DViewer;
class tcGoalTracker;
class tcDateTime;
class tcDirector;
class tcMessageCenter;
//class tcNetworkView;
//class tcDisplaySettingsView;
//class tcChatBox;
//class tc3DWindow2;
//class tcDraggedIconDisplay;
class tcMapData;
//class tcBriefingView;
//class tcDatabaseViewer;
//class tcMPGameView;
//class tcTVEngine;
//class wxProgressDialog;

using namespace scriptinterface;

#define MAX_COMMAND_STRING_LEN (1024*100)

#ifndef SCENARIO_PATH
#define SCENARIO_PATH "scenarios"
#endif


/** 
 * Main game application class.
 *
 * tcGame holds all of the single instance objects and has the
 * main loop for the simulation. It also handles all mouse events
 * and game commands.
 *
 * cpp file needs to be broken up. Compiler heap overflow error occurs unless
 * /Zm option is used. Using /Zm500 as workaround for now.
 */
class tcGame
{
//    enum teScreenMode
//    {
//        START, ///< show main, multi-pane start view
//        TACTICAL,
//        TEST,
//        NONE
//    };

    enum teGameMode 
    {
        GM_START, ///< Game not started
        GM_PLAY ///< Game started
    };
    enum
	{
        N_BUTTON_BARS = 4
    };



public:
    typedef void (tcGame::*commandFunctionPtr)(const tsCommandInfo &);

    double gameTime;
//    double directorTime; // kind of a hack to keep director going during pause
//    uint64_t nLastCount; // for timing 纳秒

    tcDateTime gameDateTime; ///< object combining date and time
    std::chrono::system_clock::time_point prevRealTime;//推进时的真实时间




    database::tcDatabase* database;
    tcSimState* simState;
    tcMapData* mapData;
//    tcCommandQueue* commandQueue;
    tcSimPythonInterface* pythonInterface;
    tcUserInfo* userInfo;    
    tcGoalTracker* goalTracker; ///< monitors simstate vs. victory goals
//    tcDirector* director; ///< displays scripted graphics and controls view for dramatic mission brief
    tcMessageCenter* messageCenter; ///< tasking, intel, etc. message view



    enum _editctrlstate 
    {
        ECS_GETSAVESCENARIO,
        ECS_GETLOADSCENARIO,
        ECS_NONE
    } meEditControlState;

    int mbPaused;
    bool mbQuit; ///< set to true to exit game to desktop
	bool endGame; ///< set to true to exit game to start screen
    bool mbScenarioEdit; ///< scenario edit mode
    int accelerateTime; ///< time acceleration factor, 0 is no accel, 1 is 2x, 2 is 3x, etc
                        ///< could try merge with pause, so 0 = pause, 1 = norm, 2 = 2x, etc
//    teScreenMode meScreenMode;
//    teScreenMode lastMode;
    teGameMode meGameMode;
    bool mbSwitchToPlay;


    int multiplayerMode; ///< 0 - single-player, 1 - client, 2 - server
	bool togglePopup; ///< true to toggle popup menu state
    std::vector<int> hookedUnits; ///< vector of hooked unit ids
    bool enableClientSync; ///< for multiplayer client
//    std::string versionString;

    std::map<std::string, commandFunctionPtr> textCommands;


    void Activate();
//    bool DirectoryExists(wchar_t *azDirectory);
    void EndGame();
    bool Finish();
    void Init(); ///< basic initialization and start screen init
    bool InitSim();
    void SaveDatabaseToPython(const std::string& dirPath);
    
    void CheckGoals(); ///< checks if any win/loss goals satisfied
    void CheckMultiplayerEndGame(); ///< checks for MP end game or surrender


	void HookRandomFriendly(); ///< hooks random friendly platform
    void ProcessCommandList();
    void ProcessTextCommand(tsCommandInfo cmd_info);
    void AddCommand(const std::string& cmd);///< 添加命令

	void SetScenarioEdit(bool state);

	void SetTheater(float lat_deg, float lon_deg); ///< sets theater view center


    void SetTimeAccel(int accel);

    int NextTimeAccelVal(int current, bool goFaster) const;
    void ShiftTime(float delta_s); ///< shifts time for sky/environment updates


    void SynchTimeAcceleration();

    void UninitGame(); ///< uninitializes components initialized by InitGame()

    bool UpdateFrame();
    bool UpdateStart();
    void UpdateOptions();

    float GetClientSyncFactor();
//    bool GetAppVersion(wchar_t* libName, unsigned short* majorVersion, unsigned short* minorVersion, unsigned short* buildNumber, unsigned short* revisionNumber);

    void ValidateHooked();



    void SetInGame(bool state); ///< test command for multiplayer


    void LoadDamageEffect(const std::string&filePath);
    void LoadWeaponDamage(const std::string&filePath);
    void LoadSignatureModel(const std::string&filePath);
    void LoadAcousticModel(const std::string&filePath);

    void LoadDatabaseObject(const std::string& filePath);

    /**
    * Loads scenario with path+filename of SCENARIO_PATH\<filePath> 相对scenario文件夹
    */
    void LoadScenario(const std::string& filePath, const std::string& caption, bool startInEditMode);

    std::string GetOutSimData();
    //根据id 获得数据库性能数据
    std::string GetOutDBData(int id);
    //根据name 获得数据库性能数据
    std::string GetOutDBData(const std::string& name);
    tcGame();
    ~tcGame();
    //设置网络模式
    void SetNetworkMode(const std::string&  mode);
    //连接服务器
    void ConnectToServer(const std::string& serverIp,const std::string& name ,const std::string& password);
private:

    // struct UnitInfo{
    //     int mnID;
    //     int alliance;
    //     unsigned int  mnModelType;              ///< class MTYPE_ identifier
    //     char mzUnit[128];
    //     char mzClass[128];
    //     double mfLon_rad;              ///< intitude [rad]
    //     double mfLat_rad;              ///< latitude [rad]
    //     float mfAlt_m;                 ///< altitude, negative is subsurface depth [m]
    //     float mfHeading_rad;           ///< relative to north [rad]
    //     float mfClimbAngle_rad;        ///< climb angle defines vertical motion vector [rad]
    //     float mfYaw_rad;               ///< orientation in azimuthal plane
    //     float mfPitch_rad;             ///< orientation in elevation plane
    //     float mfRoll_rad;			   ///< orienation about roll axis
    //     float mfSpeed_kts;             ///< [kts]
    // };
    // struct SimTime
    // {
    //     double mfSimTime;
    //     uint64_t dateTime;
    // };
    // struct SharedSimData
    // {
    //     SimTime simTime;
    //     unsigned int count;
    //     UnitInfo unitInfos[N_GAME_OBJECTS];
    // };
    // struct CommandString
    // {
    //     unsigned int length;
    //     char str[MAX_COMMAND_STRING_LEN+1];
    // };
    // QSharedMemory sharedSimDataMemory;
    // SharedSimData sharedSimData;

    // QSharedMemory commandStringMemory;
    // CommandString  commandStringData;
    std::vector<std::string> cmds;//存储要执行的命令
    std::mutex mtx_cmds;
    std::string outsimdata;//存储仿真数据
    std::mutex mtx_outsimdata;
    int networkMode;//网络模式
    void UpdateOutSimData();

};
#endif
