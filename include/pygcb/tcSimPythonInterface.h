/**
**  @file tcSimPythonInterface.h
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

#ifndef __tcSimPythonInterface_h__
#define __tcSimPythonInterface_h__

#if _MSC_VER > 1000
#pragma once
#endif

// Python interface to tcPlatformObject for scripting
//#include "wx/wx.h"

#include "tcPythonInterface.h"
#include "tcPlatformObject.h"
#include "tcSubInterface.h"
#include "tcTrackInterface.h"
#include "tcPlatformInterface.h"
#include "tcFlightPortInterface.h"
//#include "tcPanelInterface.h"
#include "tcGroupInterface.h"
#include "tcWeaponInterface.h"
#include <map>


//class tcMenu;
//class tcDirector;


class tcAllianceSensorMap;
class tcSoundConsole;
class tcCommandQueue;
class tcMapOverlay;
class tcStream;
class tcCommandStream;
class tcTacticalMapView;


namespace ai
{
    class ScriptedTask;
    class ScriptedTaskInterface;

}
using ai::ScriptedTask;
using ai::ScriptedTaskInterface;


/**
* Embedded python scripting interface code.
* Contains all python interface classes.
*/
namespace scriptinterface 
{
	class tcScenarioInterface;
    class tcDatabaseInterface;
    /**
    * Singleton class
    */
    class tcSimPythonInterface : public tcPythonInterface 
    {
    public:
        void SetUnitInfo(std::shared_ptr<tcPlatformObject>apObj);
        void Test();


        void AttachMapData(tcMapData *md);

        void AttachSensorMap(tcAllianceSensorMap *apSM) {tcTrackInterface::SetSensorMap(apSM);}
        void AttachSimState(tcSimState *apSimState);

        int CallPython(const char *commandtext, const char *errortext);
        bool CallTaskScript(ScriptedTask* task, const char* azCommand);
		std::shared_ptr<tcPlatformObject> GetHookedObj() const;
		tcFlightPort* GetHookedObjFlightPort();
        bool IsHooked(int id) const;

        void GetObjectStringByMode(char *str); // gets name of python object to pass to python function
        tcScenarioInterface* GetScenarioInterface() const;

        void ClearScenario();

        void LoadDamageEffect(const std::string&filePath);
        void LoadWeaponDamage(const std::string&filePath);
        void LoadSignatureModel(const std::string&filePath);
        void LoadAcousticModel(const std::string&filePath);

        void LoadDBObject(const std::string&filePath); ///< loads DBObject from Python script file
        void LoadScenario(const std::string&filePath); ///< loads scenario from Python script file



        void ProcessCommand(const std::string& command, const std::vector<int>& id, 
            int param = -1, std::string textParam = "");
		void ProcessCommandWithArguments(const std::string& command, const std::vector<int>& id, 
            const std::string& argString);
        void ProcessCallback(const std::string& command, const std::vector<int>& id);
        void ProcessCallback(const std::string& command, const std::vector<int>& id, 
			float afData, int param, const std::string& textParam);
        void ProcessCallback(const std::string& command, const std::vector<int>& id, 
			float afData1, float afData2, int param, const std::string& textParam);
		void ProcessCallback(const std::string& command, const std::vector<int>& id, 
			int anData, int param, const std::string& textParam);
		void ProcessCallback(const std::string& command, const std::vector<int>& id, 
			const std::string& text, int param = -1);
        void ProcessCallbackArgList(const std::string& command, const std::vector<int>& id, 
										   const std::string& arguments);
		void ProcessCallbackString(const std::string& command, const std::vector<int>& id);
        void ReportError(const char* text);

		
        void UpdateForDestroyedPlatform(int id);

		void Update(); ///< call periodically to send output and error text to console

		void FlushLogs();

		tcCommandStream& operator<<(tcCommandStream& stream);
		tcCommandStream& operator>>(tcCommandStream& stream);
		
		void ClearNewCommand();
		bool HasNewCommand() const;

        static tcSimPythonInterface* Get(); ///< singleton accessor

    private:
        tcSimPythonInterface();
        virtual ~tcSimPythonInterface();

		bool showPythonErrors; ///< true to send python errors to F7 console in game

        object PlatformInterface; ///< python tcPlatformInterface
        tcPlatformInterface *platformInterface; ///< C++ handle to PlatformInterface

        object GroupInterfaceType;
        object GroupInterface; ///< python tcGroupInterface
        tcGroupInterface* groupInterface; ///< C++ handle to GroupInterface

        object HookedPlatformInterface; ///< interface for hooked platform for menu
        tcPlatformInterface *hookedInterface; ///< C++ handle to hooked plat interface

        object SubInterfaceType;
        object TrackInterfaceType;
        object TrackInterface;
        object FlightPortInterface;
        tcFlightPortInterface *flightPortInterface; ///< C++ handle to flightport interface
        
        object WeaponInterfaceType;
        object WeaponInterface;
        tcWeaponInterface* weaponInterface;


        object ScenarioInterface;
        tcScenarioInterface* scenarioInterface; ///< C++ handle to scenario interface


        object DatabaseInterface;
        tcDatabaseInterface* databaseInterface; ///< C++ handle to database interface

        //        tcDirector *director;
        tcSimState *mpSimState;
        std::shared_ptr<tcPlatformObject>mpHookedObj;
//        tcSoundConsole *mpConsole;
//        tcMapOverlay* overlay;

        ScriptedTaskInterface* taskInterface;
        object TaskInterfaceObject;

        enum teInterfaceMode 
		{
            UNIT_MENU,
			GROUP_MENU,
            TRACK_MENU,
            FLIGHT_MENU,
			GAME_MENU, ///< top-level menu with nothing hooked
            WEAPON_MENU
        } meMenuMode;

        bool isModePushed; ///< true if mode is pushed and available for recall with PopMode
        teInterfaceMode pushedMode;
        std::vector<int> pushedPlatformIds;

		struct ClientCommand
		{
            char menuMode;
			std::vector<int> idList;
			std::string commandText;
		};
		std::vector<ClientCommand> clientCommands; ///< commands to send to server

        std::map<std::string, bool> commandBypass;

        bool BypassClientCommand(const std::string& command) const;
        void InitCommandBypass();
		void UpdateLogs();
    };
}

#endif // __tcSimPythonInterface_h__

