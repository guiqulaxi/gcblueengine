/** 
**  @file tcMultiplayerInterface.cpp 
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

// #include "stdwx.h" // precompiled header file

// #ifndef WX_PRECOMP
// #include "wx/wx.h" 
// #endif
// 修复 Windows SDK 宏冲突问题

// #include "wx/ffile.h"
#include "network/tcNetworkInterface.h"
#include "network/tcMultiplayerInterface.h"
#include "network/tcMessageHandler.h"
#include "network/tcConnectionData.h"
#include "network/tcAuthenticationMessageHandler.h"
#include "network/tcTextMessageHandler.h"
#include "network/tcControlMessageHandler.h"
//#include "network/tcUpdateMessageHandler.h"
#include "common/tcStream.h"
#include "common/tcObjStream.h"
#include <iostream>
#include <queue>
#include <sstream>
#include <cassert>
//#include "tcSound.h"
#include "tcTime.h"
#ifdef GetObject
// a former included windows.h might have defined a macro called GetObject, which affects
// GetObject defined here. This ensures the macro does not get applied
#pragma push_macro("GetObject")
#define TC_WINDOWS_GETOBJECT_WORKAROUND_APPLIED
#undef GetObject
#endif
#include "tcSimState.h"
#include "tcGameObjIterator.h"
//#include "tcConsoleBox.h"
#include "tcAccountDatabase.h"
#include "tcUserInfo.h"
// #include "scriptinterface/tcSimPythonInterface.h"
// #include "scriptinterface/tcScenarioInterface.h"
// #include "tcScenarioSelectView.h"
// #include "wxcommands.h"
#include "ai/tcMissionManager.h"
#include "database/tcDatabaseIterator.h"
#include "tcAllianceSensorMap.h"
//#include "tcConsoleBox.h"
#include "tcAccountDatabase.h"
#include "tcUserInfo.h"
// #include "scriptinterface/tcSimPythonInterface.h"
// #include "scriptinterface/tcScenarioInterface.h"
// #include "tcScenarioSelectView.h"
// #include "wxcommands.h"
#include "ai/tcMissionManager.h"
#include "database/tcDatabaseIterator.h"
#include "tcAllianceSensorMap.h"
#include "tcMultiplayerInterface.h"
#include "tcUpdateMessageHandler.h"
//#include "tcScenarioInterface.h"



using namespace network;
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

BEGIN_NAMESPACE(network)

// BEGIN_EVENT_TABLE(tcMultiplayerInterface, wxEvtHandler)
//     EVT_SOCKET(-1, tcMultiplayerInterface::OnSocketEvent)
// END_EVENT_TABLE()

/**
* Erases map entry for id. Used to force server to resend
* create message for id.
*/
void tcPlayerStatus::EraseEntry(int id)
{
    std::map<int, UpdateInfo>::iterator iter;

    if (id == -1) return;

    iter = lastUpdate.find(id);
    if (iter == lastUpdate.end()) 
    {
        return;
    }
    lastUpdate.erase(iter); // erase entry
}

unsigned char tcPlayerStatus::GetAlliance() const
{
	return alliance;
}

int tcPlayerStatus::GetConnectionId() const
{
    return connectionId;
}

unsigned char tcPlayerStatus::GetGameSpeed() const
{
    return requestedGameSpeed;
}

/**
* Gets time of last update to player for a game object
* @param updateTime [30 Hz tics] set to last updateTime for obj id
* @return true if id exists in update map, false otherwise
*/
bool tcPlayerStatus::GetLastUpdate(int id, unsigned int& updateTime, unsigned int& detailedUpdateTime)
{
    std::map<int, UpdateInfo>::iterator mapIter;

    if (id == -1) return false;

    mapIter = lastUpdate.find(id);
    if (mapIter == lastUpdate.end()) 
    {
        return false;
    }

    updateTime = mapIter->second.updateTime;
    detailedUpdateTime = mapIter->second.detailedUpdateTime;

    return true;
}


const std::string& tcPlayerStatus::GetName() const
{
	return name;
}

const std::string& tcPlayerStatus::GetNameWithRank() const
{
	return nameWithRank;
}

unsigned char tcPlayerStatus::GetRank() const
{
	return rank;
}

bool tcPlayerStatus::IsXmlObserver() const
{
    return isXmlObserver;
}

bool tcPlayerStatus::IsCommander() const
{
    return isCommander;
}

bool tcPlayerStatus::IsGM() const
{
    return (GetRank() == tcUserInfo::RANK_GM);
}

bool tcPlayerStatus::IsInGame() const
{
    return isInGame;
}

bool tcPlayerStatus::IsReady() const
{
	return isReady;
}

void tcPlayerStatus::SetAlliance(unsigned char val)
{
	alliance = val;
}

void tcPlayerStatus::SetConnectionId(int id)
{
    connectionId = id;
}

void tcPlayerStatus::SetGameEnd(bool state)
{
    wantsGameEnd = state;
}

void tcPlayerStatus::SetGameSpeed(unsigned char val)
{
    requestedGameSpeed = val;
}

void tcPlayerStatus::SetInGame(bool state)
{
    isInGame = state;
}

void tcPlayerStatus::SetName(const std::string& s)
{
	name = s;
}

void tcPlayerStatus::SetNameWithRank(const std::string& s)
{
	nameWithRank = s;
}

void tcPlayerStatus::SetRank(unsigned char val)
{
	rank = val;
}

void tcPlayerStatus::SetReady(bool state)
{
	isReady = state;
}

void tcPlayerStatus::SetSurrender(bool state)
{
    wantsSurrender = state;
}

/**
* Updates lastUpdate time. 
* A new map entry is created if this is the first update.
*/
void tcPlayerStatus::SetUpdate(int id, unsigned int updateTime)
{
    if (id == -1) return; // return and do nothing if null idx passed

    lastUpdate[id].updateTime = updateTime;
}

void tcPlayerStatus::SetXmlObserver(bool state)
{
    isXmlObserver = state;
}

/**
* Updates lastUpdate detailed update time. 
* A new map entry is created if this is the first update.
*/
void tcPlayerStatus::SetDetailedUpdate(int id, unsigned int detailedUpdateTime)
{
    if (id == -1) return; // return and do nothing if null idx passed

    lastUpdate[id].detailedUpdateTime = detailedUpdateTime;
}

bool tcPlayerStatus::WantsGameEnd() const
{
    return wantsGameEnd;
}

bool tcPlayerStatus::WantsSurrender() const
{
    return wantsSurrender;
}


/** 
* @return singleton instance 
*/
tcMultiplayerInterface* tcMultiplayerInterface::Get()
{
    static tcMultiplayerInterface instance;
    return &instance;
}

/**
* @return true if entityUpdateReceived flag was set
* clear flag if true
* Used to update simstate when entity update occurs to avoid position glitches
*/
bool tcMultiplayerInterface::EntityUpdateReceived()
{
    return tcUpdateMessageHandler::EntityUpdateReceived();
}

/**
* Adds tcConsoleBox to chat subscriber vector. Chat text will be printed
* to the tcConsoleBox when new text arrives.
*/
// void tcMultiplayerInterface::AddChatSubscriber(tcConsoleBox* subscriber)
// {
//     chatSubscribers.push_back(subscriber);
// }

/**
* Removes tcConsoleBox from chat subscriber list
*/
// void tcMultiplayerInterface::RemoveChatSubscriber(tcConsoleBox* subscriber)
// {

//     for(std::vector<tcConsoleBox*>::iterator iter = chatSubscribers.begin()
//         ; iter != chatSubscribers.end(); ++iter)
//     {
//         if ((*iter) == subscriber)
//         {
//             chatSubscribers.erase(iter);
//             return;
//         }
//     }
//     fprintf(stderr, "Error - RemoveChatSubscriber - Not found\n");
// }

/**
* Adds message handler for message with messageId.
* tcMessageHandler::Handle method will be called for any matching messages received 
* Currently tcMultiplayerInterface deletes the message handlers--may want to change 
* this such that creator deletes or use shared pointer.
*/
void tcMultiplayerInterface::AddMessageHandler(int messageId, tcMessageHandler* handler)
{
    std::map<int, std::vector<tcMessageHandler*> >::iterator mapIter;

    mapIter = messageMap.find(messageId);
    if (mapIter == messageMap.end()) 
    {
        // create new map pair
        std::vector<tcMessageHandler*> mm;
        mm.push_back(handler);
        messageMap[messageId] = mm; 
    }
    else
    {
        // add handler to existing map pair
        mapIter->second.push_back(handler);
		assert(false); // duplicate handler
    }
}

/**
* @return true if alliance has commander
*/
bool tcMultiplayerInterface::AllianceHasCommander(unsigned char alliance)
{
	if (alliance == 0) return true; // observers don't count, not sure if default should be true

	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int destination = *iter;    
		
        const tcPlayerStatus& player = GetPlayerStatus(destination);
		if ((player.GetAlliance() == alliance) && (player.IsCommander()))
        {
		    return true;
        }
	}

	return false;
}

/**
* Assign first member of alliance as commander
* should call only when alliance has no commander
*/
void tcMultiplayerInterface::AssignNewCommander(unsigned char alliance)
{
	if (alliance == 0) return; // observers don't count

	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int destination = *iter;    
		
        tcPlayerStatus& player = GetPlayerStatus(destination);
		if (player.GetAlliance() == alliance)
        {
			player.isCommander = true;
		    return;
        }
	}

	// no players found for alliance
}


// void tcMultiplayerInterface::AttachMPGameView(tcMPGameView* gv)
// {
// 	mpGameView = gv;
// 	assert(mpGameView != 0);
// }

// void tcMultiplayerInterface::AttachScenarioSelectView(tcScenarioSelectView* ssv)
// {
// 	scenarioSelectView = ssv;
// 	assert(scenarioSelectView != 0);
// }


/**
* Authenticate (username, passwordHash pair) for connection. 
* If successful set isAuthenticated of player to true, otherwise
* terminate the connection
*/
void tcMultiplayerInterface::AuthenticatePlayer(int connectionId, const std::string& username,
												const std::string& passwordHash)
{
	
	tcPlayerStatus& playerStatus = GetPlayerStatus(connectionId);

	if (playerStatus.name == "error")
	{
		fprintf(stderr, "tcMultiplayerInterface::AuthenticatePlayer -- Bad connection id\n");
		return;
	}

    // first check for valid username
    if ((username.length() < 3) || (username == "NoName"))
    {
        std::ostringstream s;
        s << "Invalid or missing username (" << username << ")";
        SendChatText(connectionId, s.str());
        return;
    }
    
    std::ostringstream s;
    s << "*** " << playerStatus.GetNameWithRank() << " has entered the game (new player)";
    std::string welcomeMsg = s.str();

    if (GetPlayerConnectionId(username) != -1)
    {
        std::ostringstream s;
        s << "A player with your username is already logged in (" << username << ")";
        SendChatText(connectionId, s.str());
        return;
    }


	int status = tcAccountDatabase::Get()->AuthenticateUser(username, passwordHash);

	std::string msg;
	if (status == tcAccountDatabase::SUCCESS)
	{
		playerStatus.name = username;
		
		int loginStatus = LogInPlayer(username, connectionId, playerStatus, msg);

		if (loginStatus == tcAccountDatabase::SUCCESS)
		{
			playerStatus.isAuthenticated = true;
			SendSoundEffect(connectionId, "Welcome");

			std::vector<int> connectionList;
			connectionList.push_back(connectionId);
			SendScenarioInfo(connectionList);

            SendDatabaseInfo(connectionId);

			std::ostringstream s;
            s << "*** " << playerStatus.GetNameWithRank() << " has entered the game";
			BroadcastChatText(s.str());
		}
		else if (loginStatus == tcAccountDatabase::DUPLICATE_LOGIN)
		{
			playerStatus.name += "_DUP";
		}
    
	}
	else if (status == tcAccountDatabase::USER_NOT_FOUND)
	{
		// if acceptAllClients then add this user to the database and login
		if (acceptAllClients)
		{
			int status = tcAccountDatabase::Get()->AddUser(username, passwordHash, "unk");
			if (status == tcAccountDatabase::SUCCESS)
			{
				std::ostringstream oss;
                oss << "*** Added account for " << username;
                msg = oss.str();
				playerStatus.name = username;

				int loginStatus = LogInPlayer(username, connectionId, playerStatus, msg);

				if (loginStatus == tcAccountDatabase::SUCCESS)
				{
					playerStatus.isAuthenticated = true;
					SendSoundEffect(connectionId, "Welcome");

					std::vector<int> connectionList;
					connectionList.push_back(connectionId);
					SendScenarioInfo(connectionList);

                    SendDatabaseInfo(connectionId);

					std::ostringstream s;
                    s << "*** " << playerStatus.GetNameWithRank() << " has entered the game (new player)";
					BroadcastChatText(s.str());
					SendChatText(connectionId, "A new account has been created for you.\n");
					SendChatText(connectionId, "Please choose your alliance with the '/alliance <#>' command");
				}
				else if (loginStatus == tcAccountDatabase::DUPLICATE_LOGIN)
				{
					playerStatus.name += "_DUP";
				}


			}
			else
			{
				std::ostringstream oss;
                oss << "*** Error adding account " << username << " (" << status << ")";
                msg = oss.str();
			}
		}
		else
		{
			std::ostringstream oss;
            oss << "Username, " << username << ", is not registered\n";
            msg = oss.str();
		}
	}
	else if (status == tcAccountDatabase::PASSWORD_INVALID)
	{
		std::ostringstream oss;
        oss << "Invalid password for username, " << username << "\n";
        msg = oss.str();
	}
	else
	{
		msg = "Unknown login error.";
	}

	SendChatText(connectionId, msg);

}

/**
* Logs player in after username/password has been authenticated. Checks for duplicate
* logins, etc.
* @return tcAccountDatabase::SUCCESS if successful
*/
int tcMultiplayerInterface::LogInPlayer(const std::string& username, int connectionId, 
										tcPlayerStatus& playerStatus, std::string& msg)
{
	tcConnectionData* connection = networkInterface->GetConnection(connectionId);
	tcSimState* simState = tcSimState::Get();

	std::string ipAddress = connection->GetIdString();

	int loginStatus = tcAccountDatabase::Get()->LogIn(username, ipAddress);

	if (loginStatus == tcAccountDatabase::SUCCESS)
	{
		tcAccountDatabase::UserData userData;
		tcAccountDatabase::Get()->GetUserData(username, userData);
		
		playerStatus.data = userData;

		playerStatus.SetAlliance(userData.alliance);
		if (simState->GetTime() <= 0) // if game hasn't started yet
		{
			playerStatus.SetAlliance(0); // assign to Observers to start
            playerStatus.SetGameSpeed(1);

            tcAccountDatabase::Get()->SetUserAlliance(username, 0);
		}
		else
		{
			playerStatus.SetReady(true); // always ready if game is in progress
            playerStatus.SetGameSpeed((unsigned char)(simState->GetTimeAcceleration()));
		}

        playerStatus.SetXmlObserver(false);
        playerStatus.SetInGame(false);
        playerStatus.SetGameEnd(false);
        playerStatus.SetSurrender(false);


		SendControlMessage(connectionId, tcControlMessageHandler::CM_ALLIANCE, userData.alliance);

		if (playerStatus.alliance != 0)
		{
			SendBriefingText(connectionId, playerStatus.alliance);
		}

		unsigned char rank = tcUserInfo::Get()->ScoreToRank(userData.score);
		playerStatus.SetRank(rank);
		std::string rankString = tcUserInfo::Get()->RankToString(rank);
		rankString += " ";
		rankString += username;
		playerStatus.SetNameWithRank(rankString);
		
		playerStatus.SetConnectionId(connectionId);
		playerToConnection[username] = connectionId;

		// if player's alliance has no commander then make this player commander
		if (!AllianceHasCommander(playerStatus.GetAlliance()))
		{
			playerStatus.isCommander = true;
		}

        std::ostringstream oss;
        oss << "Welcome " << playerStatus.GetNameWithRank() << " (Alliance " << (int)playerStatus.GetAlliance() << ")\n";
        msg = oss.str();

        std::ostringstream eventString;
        eventString << playerStatus.GetName() << " logged on (" << "time" << ")";
        recentEvents.push_back(eventString.str());
	}
	else if (loginStatus == tcAccountDatabase::DUPLICATE_LOGIN)
	{
        std::ostringstream oss;
        oss << "Username, " << username << ", is already logged in\n";
        msg = oss.str();
	}
	else
	{
        std::ostringstream oss;
        oss << "Unknown login error for username, " << username << "\n";
        msg = oss.str();
	}

	return loginStatus;
}

/**
* Log out all players that are logged in. Call before shutting down server.
*/
void tcMultiplayerInterface::LogOutAllPlayers()
{
	if (!IsServer()) return;

	for (std::map<int,tcPlayerStatus>::iterator iter = playerInfo.begin();
        iter != playerInfo.end(); ++iter) 
    {
		if (iter->second.isAuthenticated)
		{
			LogOutPlayer(iter->second.name);
			iter->second.isAuthenticated = false;
		}
    }

}

void tcMultiplayerInterface::LogOutPlayer(const std::string& username)
{
	std::map<std::string, int>::iterator iter = 
		playerToConnection.find(username);

	if (iter == playerToConnection.end())
	{
		fprintf(stderr, "tcMultiplayerInterface::LogOutPlayer - %s not found in playerToConnection map\n",
            username.c_str());
		return;
	}

	tcPlayerStatus playerStatus = GetPlayerStatus(iter->second);
	bool playerWasCommander = playerStatus.IsCommander();
	unsigned char playerAlliance = playerStatus.GetAlliance();

    std::string eventString = strutil::format("%s logged off (%s)", playerStatus.GetName().c_str(),
        tcDateTime::Now().asStringTOD());
    recentEvents.push_back(eventString);


	playerToConnection.erase(iter);
	tcAccountDatabase::Get()->LogOut(username);

	// iterate through objects and release control of objects controller by player
	tcGameObjIterator objIter;
//    unsigned updateCount = 0;
    for (objIter.First(); objIter.NotDone(); objIter.Next())
    {
        std::shared_ptr<tcGameObject> obj = objIter.Get();
		if (obj->GetController() == username)
		{
			obj->SetController("");
            obj->SetAccessLevel(0);
		}
	}

	// if departing player was commander, then assign a new commander
	if (playerWasCommander)
	{
		AssignNewCommander(playerAlliance);
	}

}

/**
* Broadcast chat text to all connected clients
* @param alliance 0 to broadcast to all players, otherwise only send to players matching alliance
*/
void tcMultiplayerInterface::BroadcastChatText(const std::string& message, unsigned char alliance)
{
    char buff[256];
    unsigned messageLength;

    int protocol = tcpChat ? tcNetworkInterface::TCP : tcNetworkInterface::UDP;

    tcTextMessageHandler::CreateMessage(messageLength, (unsigned char*)buff, message, 255);
   
	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int destination = *iter;    
		
        tcPlayerStatus& player = GetPlayerStatus(destination);
        if ((alliance == 0) || (player.GetAlliance() == alliance))
        {
		    networkInterface->SendMessage(destination, MSG_CHATTEXT, 
                messageLength, (unsigned char*)buff, protocol);
        }
	}

	if (IsServer())
	{
		chatText.push(message); // echo text here for server so that all chat subscribers receive new text


        // save for html status log (don't save alliance-only chat)
        if (alliance == 0)
        {
            std::string message2 = message;
            strutil::replace_all(message2,"<", "&lt;");
            strutil::replace_all(message2,">", "&gt;");
            // message2.Replace("<", "&lt;");
            // message2.Replace(">", "&gt;");

            std::string s;
            s = message2 + " (time)";
            recentChat.push_back(s);
        }
	}
}

/**
* Broadcast control message to all connected clients
*/
void tcMultiplayerInterface::BroadcastControlMessage(int messageCode)
{
    unsigned char data[64];
    unsigned messageSize;

    tcControlMessageHandler::CreateControlMessage(messageCode, messageSize, data);


	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int id = *iter;

        networkInterface->SendMessage(id, MSG_CONTROL, 
            (messageSize+1), data, 
            tcNetworkInterface::TCP);
	}

}

/**
* Broadcasts database info to all clients
* Should be used when scenario is changed
*/
void tcMultiplayerInterface::BroadcastDatabaseInfo()
{
	const std::vector<int>& destinations = GetConnectionVector();

	SendDatabaseInfo(destinations);
}

/**
* Broadcasts scenario info to all clients
* Should be used when scenario is changed
*/
void tcMultiplayerInterface::BroadcastScenarioInfo()
{
	const std::vector<int>& destinations = GetConnectionVector();

	SendScenarioInfo(destinations);
}


/**
* Clears messageMap, deleting all message handlers
*/
void tcMultiplayerInterface::ClearMessageMap()
{
    std::map<int, std::vector<tcMessageHandler*> >::iterator mapIter;

    mapIter = messageMap.begin();

    for (mapIter = messageMap.begin(); mapIter != messageMap.end();
        ++mapIter)
    {
        std::vector<tcMessageHandler*>& mm = mapIter->second;
        size_t nHandlers = mm.size();
        for (size_t n = 0; n < nHandlers; n++)
        {
            assert(mm[n]);
            delete mm[n];
        }
        mm.clear();
    }
    messageMap.clear();
}

/*
std::string tcMultiplayerInterface::GetChatText()
{
    if (chatText.empty()) return "ERROR";
    std::string text = chatText.front();
    chatText.pop();
    return text;
}
*/

bool tcMultiplayerInterface::GetAcceptAllClients() const
{
	return acceptAllClients;
}

const std::list<int>& tcMultiplayerInterface::GetConnectionList() const
{
	return networkInterface->GetConnectionList();
}


const std::string& tcMultiplayerInterface::GetConnectionStatus(int connectionId)
{
	static std::string s;
	if (!IsConnecting())
	{
		const tcPlayerStatus& status = GetPlayerStatus(connectionId);

        std::string s2 = strutil::format("%s (%d) ", status.GetName().c_str(),
			status.GetAlliance());

		s = s2.c_str();
	}
	else
	{
		s = "";
	}

	s += networkInterface->GetConnectionStatus(connectionId).c_str();
	
    return s;
}

/**
* Version that returns list of connection ids as vector (more expensive)
*/
const std::vector<int>& tcMultiplayerInterface::GetConnectionVector() const
{
	static std::vector<int> connectionVector;

	connectionVector.clear();
	const std::list<int>& connectionList = GetConnectionList();
	for (std::list<int>::const_iterator k=connectionList.begin();
		 k != connectionList.end(); ++k)
	{
		connectionVector.push_back(*k);
	}

	return connectionVector;
}

// EventHandler* tcMultiplayerInterface::GetEvtHandler() const
// {
//     assert(evtHandler);
//     return evtHandler;
// }

/**
* @return identification name string for player using this interface
*/
const std::string& tcMultiplayerInterface::GetName() const
{
    return myName;
}

unsigned int tcMultiplayerInterface::GetNumConnections()
{
    return networkInterface->GetNumConnections();
}

/**
* @return hashed password string for player using this interface
*/
const std::string& tcMultiplayerInterface::GetPassword() const
{
    return passwordHash;
}

/**
* @return -1 if not found
*/
int tcMultiplayerInterface::GetPlayerConnectionId(const std::string& playerName)
{
	std::map<std::string, int>::const_iterator iter = 
		playerToConnection.find(playerName);

	if (iter != playerToConnection.end())
	{
		return iter->second;
	}
	else
	{
		return -1;
	}
}

const std::string& tcMultiplayerInterface::GetPlayerName(int connectionId)
{
	return GetPlayerStatus(connectionId).GetName();
}

/**
* @return tcPlayerStatus object associated with connectionId
* @see tcPlayerStatus
*/
tcPlayerStatus& tcMultiplayerInterface::GetPlayerStatus(int connectionId)
{
    std::map<int,tcPlayerStatus>::iterator mapIter;

    mapIter = playerInfo.find(connectionId);
    if (mapIter == playerInfo.end()) 
    {
        fprintf(stderr, "Error - tcMultiplayerInterface::GetPlayerStatus  - "
            "conn id: %d not found\n", connectionId);
        return errorPlayerStatus;
    }

    return mapIter->second;
}


// unsigned tcMultiplayerInterface::GetTeamGameSpeed() const
// {
//     assert(mpGameView != 0);

//     return mpGameView->GetTeamSpeed();
// }

// unsigned tcMultiplayerInterface::GetFastestGameSpeed() const
// {
//     assert(mpGameView != 0);

//     return mpGameView->GetFastestSpeed();
// }


/**
* Clear message map and (re)initialize based on 
* multiplayer mode.
*/
void tcMultiplayerInterface::InitMessageHandlers()
{
    ClearMessageMap();

    // common handlers
    // register chat text message handler
    AddMessageHandler(MSG_CHATTEXT, new tcTextMessageHandler(chatText));
    AddMessageHandler(MSG_CONTROL, new tcControlMessageHandler());
	AddMessageHandler(MSG_AUTHENTICATION, new tcAuthenticationMessageHandler());

    if (IsServer())
    { // server-specific handlers
        // server needs update msg handler to handle command updates from client
        AddMessageHandler(MSG_UPDATE, new tcUpdateMessageHandler());
    }
    else
    { // client-specific handlers
        AddMessageHandler(MSG_UPDATE, new tcUpdateMessageHandler());
    }
}

bool tcMultiplayerInterface::IsChatTextAvail()
{
    return !chatText.empty();
}

/**
* Tests if text is a command. Commands start with a
* forward slash '/'
* @return true if text is a (server) command
*/
bool tcMultiplayerInterface::IsCommand(const std::string& text)
{
    std::string candidate(text);
    return ((candidate.find('/') == 0));
}

bool tcMultiplayerInterface::IsConnecting() const
{
	if (IsServer()) return false;

	return (networkInterface->IsConnecting());
}

/**
* Check for mutually agreed end of game, or surrender of one team
*/
bool tcMultiplayerInterface::IsGameOver(std::string& message) const
{
    message.clear();

    std::vector<TeamInfo>& teamList = tcUpdateMessageHandler::GetLatestTeamList();

	size_t nTeams = teamList.size();

    bool anyPlayersInGame = false;
    bool allPlayersEndGame = true;
    bool anyPlayerSurrender = false;
    unsigned char surrenderAlliance;
    std::string surrenderName;

	for (size_t n=0; n<nTeams; n++)
	{
        TeamInfo& teamInfo = teamList[n];

		size_t nPlayers = teamList[n].playerList.size();
		
		for (size_t k=0; k<nPlayers; k++)
		{
            anyPlayersInGame = true;
            allPlayersEndGame = allPlayersEndGame && teamList[n].playerList[k].endGame;
            
            if (teamList[n].playerList[k].surrenderGame)
            {
                anyPlayerSurrender = true;
                surrenderAlliance = teamInfo.alliance;
                surrenderName = teamInfo.name;
            }
		}
    }

    tcSimState* simState = tcSimState::Get();
    bool noplayerTimeout = (!anyPlayersInGame) && (simState->GetTime() > 60.0);

    bool gameOver = noplayerTimeout || 
        (anyPlayersInGame && (allPlayersEndGame || anyPlayerSurrender));

    if (gameOver)
    {
        if (noplayerTimeout)
        {
            message+=("Game ended, no players remaining");
        }
        else if (allPlayersEndGame)
        {
            message+="Game ended by agreement between players";
        }
        else
        {
            message+=strutil::format("Game ended when %s surrendered", surrenderName.c_str());
        }
        return true;
    }
    else
    {
        return false;
    }
}

bool tcMultiplayerInterface::IsNewPlayer(int id)
{
    std::map<int,tcPlayerStatus>::const_iterator mapIter;

    mapIter = playerInfo.find(id);
    if (mapIter == playerInfo.end()) 
    {
        return true;
    }
    else
    {
        return false;
    }
}

/**
* @return true if acting as a server
*/
bool tcMultiplayerInterface::IsServer() const
{
    return networkInterface->IsServer();
}

void tcMultiplayerInterface::MakeClient()
{
	if (IsServer()) LogOutAllPlayers();

    networkInterface->MakeClient();
    tcMessageHandler::SetAsClient();
    InitMessageHandlers();
}


void tcMultiplayerInterface::MakeServer()
{
    networkInterface->MakeServer();
    tcMessageHandler::SetAsServer();
    InitMessageHandlers();

	myName = "SERVER";

    logFilePath = tcOptions::Get()->GetOptionString("ServerLogFile");
}

/**
* Resets network interface to initial client state.
* This will close all open connections.
* (Same implementation as MakeClient())
*/
void tcMultiplayerInterface::Reset()
{
	MakeClient();
}


/**
* Call when new scenario is loaded. Resets all players to observer team.
*/
void tcMultiplayerInterface::ResetGame()
{
	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter;

    for(iter = connectionList.begin() ; iter != connectionList.end(); ++iter)
    {
        int id = *iter;

		tcPlayerStatus& player = GetPlayerStatus(id);

		player.SetAlliance(0);
		player.isCommander = false;
        player.isInGame = false;
        player.wantsGameEnd = false;
        player.wantsSurrender = false;
        std::ostringstream eventString;
        eventString << player.GetName() << " logged on (" << "time" << ")";
        recentEvents.push_back(eventString.str());
	}



    BroadcastScenarioInfo();
}

// void tcMultiplayerInterface::PlayerLoggedOff(const tcPlayerStatus& playerStatus)
// {
//     // wxString eventString = wxString::Format("%s logged off (%s)", playerStatus.GetName().c_str(),
//     //     wxDateTime::Now().FormatISOTime().c_str());
//     std::ostringstream eventString;
//     eventString << playerStatus.GetName() << " logged off (" << "time" << ")";
//     recentEvents.push_back(eventString.str());

//     BroadcastScenarioInfo();

//     lastOptionsUpdate = tcTime::Get()->GetUpdated30HzCount() - 60;
// }


/**
* Call at client when lost connection to server
*/
void tcMultiplayerInterface::OnLostServer()
{
    chatText.push(std::string("Lost connection to server"));
    fprintf(stderr, "Lost connection to server\n");

    MakeClient();
}


void tcMultiplayerInterface::OpenConnection(const std::string& hostName)
{
    networkInterface->OpenConnection(hostName.c_str());
}


/**
* Send queued chat text to subscribers. This should be periodically called
* as part of the update method
*/
void tcMultiplayerInterface::DistributeChatText()
{
    while (!chatText.empty())
    {
        std::string text = chatText.front();
        chatText.pop();

        // for(std::vector<tcConsoleBox*>::iterator iter = chatSubscribers.begin()
        //     ; iter != chatSubscribers.end(); ++iter)
        // {
        //     (*iter)->Print(text.c_str());
        // }
    }

}

/**
* Process command to change alliance of player
*/
void tcMultiplayerInterface::ProcessAllianceCommand(tcPlayerStatus& player, const std::string& args)
{
    // wxString msg;
    std::string msg;
    // wxString message2 = message;
    //std::string message2 = args;

    
    int connectionId = player.GetConnectionId();
    
	tcSimState* simState = tcSimState::Get();
    bool changeAllowed = player.data.CanSwitchAlliance() || 
                         simState->IsMultiplayerGameStarted() || 
                         allowAllTeamChanges;

    if (changeAllowed)
    {
        int alliance;
        if (sscanf(args.c_str(), "%d", &alliance) == 1)
    	{
    		player.alliance = alliance;
    		tcAccountDatabase::Get()->SetUserAlliance(player.GetName(), player.alliance);
    
			SendControlMessage(connectionId, tcControlMessageHandler::CM_ALLIANCE, alliance);
            msg = "*** Success - alliance set to " + std::to_string(alliance);

			// update briefing text for new alliance
			if (alliance != 0)
			{
				SendBriefingText(connectionId, alliance);
				SendScenarioInfo(connectionId);

				// if player's new alliance has no commander then make this player commander
				if (!AllianceHasCommander(player.GetAlliance()))
				{
					player.isCommander = true;
				}
			}
            else
            {
                player.isCommander = false;
            }

            player.SetReady(false); // clear ready status on side change
		}
    	else
    	{
            msg = "*** Error - bad alliance change argument (" + args + ")";
    	}
    }
    else
    {
        msg = "*** Team change not allowed while game in progress";
    } 
    
    SendChatText(connectionId, msg);
}

/**
*
*/
void tcMultiplayerInterface::ProcessChangeCommander(tcPlayerStatus& player, const std::string& args)
{
    std::string msg;

    int connectionId = player.GetConnectionId();

    unsigned char alliance = player.GetAlliance();

    if (alliance == 0)
    {
        msg = "*** Cannot change commander while on Observer team";
        SendChatText(connectionId, msg);
        return;
    }

    if (player.IsCommander() || (!AllianceHasCommander(alliance)))
    {
        int newCommanderId = GetPlayerConnectionId(args);
        if (newCommanderId != -1)
        {
            tcPlayerStatus& pstatus = GetPlayerStatus(newCommanderId);
            player.isCommander = false;
            pstatus.isCommander = true;

            msg=strutil::format("*** %s is now team commander", pstatus.GetNameWithRank().c_str());
            BroadcastChatText(msg);
            return;
        }
        else
        {
            msg=strutil::format("*** player %s not found", args);
        }

    }
    else
    {
        msg = "*** Failed. Ask team commander to change commander";
    }

    SendChatText(connectionId, msg);
}



/**
*
*/
void tcMultiplayerInterface::ProcessChangeReady(tcPlayerStatus& player, const std::string& args)
{
    std::string msg;

    int connectionId = player.GetConnectionId();


    if (args != "0")
    {
        if (!player.IsReady())
        {
            player.SetReady(true);
            msg = "*** Your status is now READY";
        }
        else
        {
            msg = "*** Status already is ready";
        }
    }
    else
    {
        if (player.IsReady())
        {
            player.SetReady(false);
            msg = "*** Your status is now STAND DOWN";
        }
        else
        {
            msg = "*** Status already is stand down";
        }
    }

     SendChatText(connectionId, msg);
}



void tcMultiplayerInterface::ProcessGameMasterCommand(tcPlayerStatus& player, const std::string& args)
{
    // assert(IsServer());
    
    // using scriptinterface::tcScenarioInterface;
    // tcScenarioInterface* scenarioInterface = tcSimPythonInterface::Get()->GetScenarioInterface();
    // // assert(scenarioInterface);
    tcSimState *simState = tcSimState::Get();
    
    int connectionId = player.GetConnectionId();

    bool syntaxError = true;
    std::string msg;
    
    if (player.IsGM())
    {
        size_t spacePos = args.find(' ');
        std::string command = (spacePos != std::string::npos) ? args.substr(0, spacePos) : args;
        std::string params = (spacePos != std::string::npos) ? args.substr(spacePos + 1) : "";

        if ((command == "help") || (command == ""))
        {
            syntaxError = false;
            SendChatText(connectionId, "*** /gm help ***");
            SendChatText(connectionId, "    /gm help - print GM command list");
            SendChatText(connectionId, "    /gm addaccount '<username>' '<email>'");
         //   SendChatText(connectionId, "    /gm getaccountdata '<username>' '<param>'");
         //   SendChatText(connectionId, "    /gm setaccountdata '<username>' '<param>' <value>");
            SendChatText(connectionId, "    /gm create '<class>' '<unitname>' <alliance> <lat_deg> <lon_deg> (<alt_m>)");
            SendChatText(connectionId, "    /gm destroy <id>");
            SendChatText(connectionId, "    /gm kick '<playername>'");
            SendChatText(connectionId, "    /gm move <id> <lat_deg> <lon_deg> (<alt_m>)");
         //   SendChatText(connectionId, "    /gm reload <id>");
            SendChatText(connectionId, "    /gm repair <id>");
         //   SendChatText(connectionId, "    /gm setalliance <id> <alliance>");
            SendChatText(connectionId, "    /gm setcontroller <id> '<player>'");
            SendChatText(connectionId, "    /gm setteamchanges <0 or 1>");
        }
        else if (command == "addaccount")
        {
            syntaxError = false;

            ProcessGMAddAccount(params, msg);
        }
        else if (command == "create")
        {
            syntaxError = false;
            
            ProcessGMCreate(params, msg);
        }
        else if (command == "destroy")
        {
            int id;
            if (sscanf(params.c_str(), "%d", &id) == 1)
            {
                syntaxError = false;
                simState->DeleteObject(id);
                msg = "*** Entity " + std::to_string(id) + " destroyed";
            }
        }
        else if (command == "kick")
        {
            syntaxError = false;

            ProcessGMKick(params, msg);
        }
        else if (command == "move")
        {
            syntaxError = false;
            
            ProcessGMMove(params, msg);
        }
        else if (command == "repair")
        {
            int id;
            if (sscanf(params.c_str(), "%d", &id) == 1)
            {
                syntaxError = false;
                if (std::shared_ptr<tcGameObject> obj = simState->GetObject(id))
                {
                    obj->ApplyRepairs(2.0f);
                    msg = "*** Entity " + std::to_string(id) + " repaired";
                }
                else
                {
                    msg = "*** Entity " + std::to_string(id) + " not found";
                }
            }
        }
        else if (command == "setcontroller")
        {
            syntaxError = false;
            ProcessGMSetController(params, msg);
        }
        else if (command == "setteamchanges")
        {
            syntaxError = false;
            ProcessGMSetTeamChanges(params, msg);
        }
    }
    else
    {
        syntaxError = false;
        msg = "*** Denied - insufficient permissions for /gm commands";
    }
    
    if (syntaxError)
    {
        msg = "*** Syntax error (" + args + ")";
    }
    
    SendChatText(connectionId, msg);
}

void tcMultiplayerInterface::ProcessGameSpeed(tcPlayerStatus& player, const std::string& args)
{
    int connectionId = player.GetConnectionId();
   
	//tcSimState* simState = tcSimState::Get();

    int val;
    if (sscanf(args.c_str(), "%d", &val) != 1 || (val < 0) || (val > 32))
    {
        std::string msg = "*** Error - bad game speed argument (" + args + ")";
        SendChatText(connectionId, msg);
        return;
    }

    //std::string msg = "*** Updated game speed request from " + 
    //        std::to_string(player.GetGameSpeed()) + "X to " + std::to_string(val) + "X";

    player.SetGameSpeed((unsigned char)(val));

    //SendChatText(connectionId, msg);
}


/**
* Adds new player account to database
* /gm addaccount '<username>' '<email>'
* @param args argument string
* @param msg message text to be returned
*/
void tcMultiplayerInterface::ProcessGMAddAccount(const std::string& args, std::string& msg)
{
    size_t firstQuote = args.find('\'');
    if (firstQuote == std::string::npos) return;
    
    size_t secondQuote = args.find('\'', firstQuote + 1);
    if (secondQuote == std::string::npos) return;
    
    std::string username = args.substr(firstQuote + 1, secondQuote - firstQuote - 1);
    
    size_t thirdQuote = args.find('\'', secondQuote + 1);
    if (thirdQuote == std::string::npos) return;
    
    size_t fourthQuote = args.find('\'', thirdQuote + 1);
    if (fourthQuote == std::string::npos) return;
    
    std::string email = args.substr(thirdQuote + 1, fourthQuote - thirdQuote - 1);

    if (username.size() < 3)
    {
        msg = "*** Username too short (" + username + ")";
        return;
    }

    int status = tcAccountDatabase::Get()->AddUser(username, "", email);
    if (status == tcAccountDatabase::SUCCESS)
    {
        msg = "*** Added account for " + username;
    }
    else
    {
        msg = "*** Error adding account " + username + " (" + std::to_string(status) + ")";
    }
}


/**
* Creates a new game entity
* /gm create '<class>' '<unitname>' <alliance>
* @param args argument string
* @param msg message text to be returned
*/
void tcMultiplayerInterface::ProcessGMCreate(const std::string& args, std::string& msg)
{
    const char delim = '\'';
    size_t firstDelim = args.find(delim);
    if (firstDelim == std::string::npos) {
        msg = "*** Syntax error in create command";
        return;
    }
    
    size_t secondDelim = args.find(delim, firstDelim + 1);
    if (secondDelim == std::string::npos) {
        msg = "*** Syntax error in create command";
        return;
    }
    
    std::string unitClass = args.substr(firstDelim + 1, secondDelim - firstDelim - 1);
    
    size_t thirdDelim = args.find(delim, secondDelim + 1);
    if (thirdDelim == std::string::npos) {
        msg = "*** Syntax error in create command";
        return;
    }
    
    size_t fourthDelim = args.find(delim, thirdDelim + 1);
    if (fourthDelim == std::string::npos) {
        msg = "*** Syntax error in create command";
        return;
    }
    
    std::string unitName = args.substr(thirdDelim + 1, fourthDelim - thirdDelim - 1);
    
    size_t posAfterFourthDelim = args.find_first_not_of(' ', fourthDelim + 1);
    if (posAfterFourthDelim == std::string::npos) {
        msg = "*** Syntax error in create command";
        return;
    }
    
    size_t nextSpace = args.find(' ', posAfterFourthDelim);
    std::string s1 = (nextSpace != std::string::npos) ? 
        args.substr(posAfterFourthDelim, nextSpace - posAfterFourthDelim) : 
        args.substr(posAfterFourthDelim);

    int alliance = 0;
    int val;
    if ((sscanf(s1.c_str(), "%d", &val) != 1) || (val < 0))
    {
        msg = "*** Bad alliance value for create, class '" + unitClass + "', unit '" + unitName + "'";
        return;
    }
    alliance = val;

    double lat_deg = 0;
    std::string params = args.substr(nextSpace + 1);
    size_t firstSpace = params.find(' ');
    s1 = (firstSpace != std::string::npos) ? params.substr(0, firstSpace) : params;
    
    if (sscanf(s1.c_str(), "%lf", &lat_deg) != 1)
    {
        msg = "*** Bad latitude for /gm create";
        return;  
    }
    
    double lon_deg = 0;
    std::string remaining = (firstSpace != std::string::npos) ? params.substr(firstSpace + 1) : "";
    firstSpace = remaining.find(' ');
    s1 = (firstSpace != std::string::npos) ? remaining.substr(0, firstSpace) : remaining;
    
    if (sscanf(s1.c_str(), "%lf", &lon_deg) != 1)
    {
        msg = "*** Bad longitude for /gm create";
        return;  
    }

    float alt_m = 0;
    if (firstSpace != std::string::npos)
    {
        std::string altStr = remaining.substr(firstSpace + 1);
        sscanf(altStr.c_str(), "%f", &alt_m);
    }

    tcSimState* simState = tcSimState::Get();
    // long id = simState->CreateGameObject(unitClass, unitName, alliance, lat_deg, lon_deg, alt_m);

    // if (id != -1)
    // {
    //     msg = "*** Created object id " + std::to_string(id) + ", class '" + unitClass + "', unit '" + unitName + "'";
    // }
    // else
    // {
    //     msg = "*** Error creating object, class '" + unitClass + "', unit '" + unitName + "'";
    // }


}

/**
* Kick player from game
* /gm kick '<playername>'
* @param args argument string
* @param msg message text to be returned
*/
void tcMultiplayerInterface::ProcessGMKick(const std::string& args, std::string& msg)
{
    const char delim = '\'';
    size_t firstDelim = args.find(delim);
    if (firstDelim == std::string::npos) return;
    
    size_t secondDelim = args.find(delim, firstDelim + 1);
    if (secondDelim == std::string::npos) return;
    
    std::string playername = args.substr(firstDelim + 1, secondDelim - firstDelim - 1);
    
    int playerId = GetPlayerConnectionId(playername);
    if (playerId == -1) return;

    SendChatText(playerId, "You have been kicked from the game");

    LogOutPlayer(playername);

    playerInfo.erase(playerId);
    networkInterface->RemoveConnection(playerId);
}


/**
* Moves a game entity
* move <id> <lat_deg> <lon_deg> (<alt>)
* use "move <id> 0 0 <alt>" to only change altitude
* @param args argument string
* @param msg message text to be returned
*/
void tcMultiplayerInterface::ProcessGMMove(const std::string& args, std::string& msg)
{
    size_t firstSpace = args.find(' ');
    if (firstSpace == std::string::npos) {
        msg = "*** Syntax error for /gm move";
        return;
    }
    
    std::string params = args.substr(firstSpace + 1);
    firstSpace = params.find(' ');
    std::string s1 = (firstSpace != std::string::npos) ? params.substr(0, firstSpace) : params;
    
    int id = -1;
    if (sscanf(s1.c_str(), "%d", &id) != 1)
    {
        msg = "*** Syntax error for /gm move";
        return;
    }
    
    double lat_deg = 0;
    std::string remaining = (firstSpace != std::string::npos) ? params.substr(firstSpace + 1) : "";
    firstSpace = remaining.find(' ');
    s1 = (firstSpace != std::string::npos) ? remaining.substr(0, firstSpace) : remaining;
    
    if (sscanf(s1.c_str(), "%lf", &lat_deg) != 1)
    {
        msg = "*** Syntax error for /gm move";
        return;
    }
    
    double lon_deg = 0;
    std::string remaining2 = (firstSpace != std::string::npos) ? remaining.substr(firstSpace + 1) : "";
    firstSpace = remaining2.find(' ');
    s1 = (firstSpace != std::string::npos) ? remaining2.substr(0, firstSpace) : remaining2;
    
    if (sscanf(s1.c_str(), "%lf", &lon_deg) != 1)
    {
        msg = "*** Syntax error for /gm move";
        return;
    }
    
    bool changeLatLon = (lat_deg != 0) || (lon_deg != 0);
    
    double alt_m = 0;
    bool changeAlt = true;
    std::string altStr = (firstSpace != std::string::npos) ? remaining2.substr(firstSpace + 1) : "";
    if (sscanf(altStr.c_str(), "%lf", &alt_m) != 1)
    {
        changeAlt = false;
    }
    
    tcSimState* simState = tcSimState::Get();
    
    if (std::shared_ptr<tcGameObject> obj = simState->GetObject(id))
    {
        if (changeLatLon)
        {
            obj->mcKin.mfLat_rad = C_PIOVER180 * lat_deg;
            obj->mcKin.mfLon_rad = C_PIOVER180 * lon_deg;
        }
        if (changeAlt)
        {
            obj->mcKin.mfAlt_m = (float)alt_m;
        }
    
        msg = "*** Entity " + std::to_string(id) + " moved";
    }
    else
    {
        msg = "*** Entity " + std::to_string(id) + " not found";
    }
    
}

/**
* Changes controlling player of a game entity
* setcontroller <id> '<player>'
* use setcontroller <id> '' to clear controller of entity
* @param args argument string
* @param msg message text to be returned
*/
void tcMultiplayerInterface::ProcessGMSetController(const std::string& args, std::string& msg)
{
    size_t firstSpace = args.find(' ');
    if (firstSpace == std::string::npos) {
        msg = "*** Syntax error for /gm setcontroller, bad id";
        return;
    }
    
    std::string params = args.substr(firstSpace + 1);
    firstSpace = params.find(' ');
    std::string s1 = (firstSpace != std::string::npos) ? params.substr(0, firstSpace) : params;
    
    int id = -1;
    if (sscanf(s1.c_str(), "%d", &id) != 1)
    {
        msg = "*** Syntax error for /gm setcontroller, bad id";
        return;
    }

    tcSimState* simState = tcSimState::Get();
    std::shared_ptr<tcGameObject> obj = simState->GetObject(id);
    if (obj == 0)
    {
        msg = "*** entity not found (" + std::to_string(id) + ")";
        return;
    }
    

    size_t firstQuote = params.find('\'');
    if (firstQuote == std::string::npos) {
        msg = "*** Syntax error for /gm setcontroller, missing quote";
        return;
    }
    
    size_t secondQuote = params.find('\'', firstQuote + 1);
    if (secondQuote == std::string::npos) {
        msg = "*** Syntax error for /gm setcontroller, missing quote";
        return;
    }
    
    std::string playername = params.substr(firstQuote + 1, secondQuote - firstQuote - 1);

    if (playername.size() > 0)
    {
        int playerId = GetPlayerConnectionId(playername);
        if (playerId == -1)
        {
            msg = "*** player not found (" + playername + ")";
            return;
        }
        else
        {
            obj->SetController(playername);
            msg = "*** entity " + std::to_string(id) + " controller is now " + playername;
            return;
        }

    }
    else
    {
        obj->SetController("");
        msg = "*** entity " + std::to_string(id) + " controller cleared";
        return;
    }
}

void tcMultiplayerInterface::ProcessGMSetTeamChanges(const std::string& args, std::string& msg)
{
    int id = -1;
    if (sscanf(args.c_str(), "%d", &id) != 1)
    {
        msg = "*** Syntax error for /gm setteamchanges, parameter should be 0 or 1";
        return;
    }

    if (id != 0)
    {
        allowAllTeamChanges = true;
        msg = "*** Server now allowing all team changes";
    }
    else
    {
        allowAllTeamChanges = false;
        msg = "*** Server now restricting team changes";
    }
}


/**
* Process command from client (after command is received at server)
* text commands start with a forward slash '/'
* @return string to send back to client
*/
void tcMultiplayerInterface::ProcessCommandClient(int connectionId, 
                                               const std::string& text)
{        
    tcPlayerStatus& pstatus = GetPlayerStatus(connectionId);
    
    if (!pstatus.isAuthenticated)
    {
        SendChatText(connectionId, "*** command rejected, client not authenticated");
        return;
    }
    
    // Find the first '/' character
    size_t slashPos = text.find('/');
    if (slashPos == std::string::npos) {
        SendChatText(connectionId, "*** invalid command format");
        return;
    }
    
    // Extract everything after the first '/'
    std::string commandLine = text.substr(slashPos + 1);
    
    // Find the first space to separate command from arguments
    size_t spacePos = commandLine.find(' ');
    std::string command, args;
    
    if (spacePos != std::string::npos) {
        command = commandLine.substr(0, spacePos);
        args = commandLine.substr(spacePos + 1);
    } else {
        command = commandLine;
        args = "";
    }

	// check for double slash command. These are silent with no echo back
	if (command.find('/') != 0)
	{
		SendChatText(connectionId, text);
	}
	else
	{		
		command = command.substr(1); // remove leading slash
	}

    // replace this with map lookup if it grows too large
    if (command == "help")
    {
        SendChatText(connectionId, "*** Command list:");
        SendChatText(connectionId, "    /help - print this command list");
        SendChatText(connectionId, "    /alliance <team> - change teams");
        SendChatText(connectionId, "    /commander <playername> - change team commander");
        SendChatText(connectionId, "    /ready - toggle ready status");
        SendChatText(connectionId, "    /scenario <name> - change scenario");
        SendChatText(connectionId, "    /start - start game (commander only)");
        SendChatText(connectionId, "    /surrender - end game with loss for your team");
        SendChatText(connectionId, "    /teamchat <message> - send message to team only");
        SendChatText(connectionId, "    /who - list players");
        SendChatText(connectionId, "    // - GM commands (if authorized)");
    }
    else if (command == "alliance")
    {
        ProcessAllianceCommand(pstatus, args);
    }
    else if (command == "commander")
    {
        ProcessChangeCommander(pstatus, args);
    }
    else if (command == "ready")
    {
        ProcessChangeReady(pstatus, args);
    }
    else if (command == "scenario")
    {
        ProcessScenarioCommand(pstatus, args);
    }
    else if (command == "start")
    {
        ProcessStartGame(pstatus, args);
    }
    else if (command == "surrender")
    {
        ProcessSurrender(pstatus, args);
    }
    else if (command == "teamchat")
    {
        ProcessTeamChat(pstatus, args);
    }
    else if (command == "who")
    {
        ProcessWho(pstatus, args);
    }
    else if (command == "") // GM command
    {
        ProcessGameMasterCommand(pstatus, args);
    }
    else
    {
        std::string msg = "*** Unknown command: " + command;
        SendChatText(connectionId, msg);
    }
}

/**
* Process server command
* text commands start with a forward slash '/'
*/
void tcMultiplayerInterface::ProcessCommandServer(const std::string& text)
{
    assert(IsServer());
    std::string candidate(text);

     std::string commandLine = strutil::after_first(candidate,'/');

    std::string command = strutil::before_first(candidate,' ');
    std::string args =strutil::after_first(candidate,' ');

    /* replace this with a std::map<std::string, handle> registry system
    ** when it outgrows this switch */
    
    if (command == "help")
    {
        chatText.push(std::string("*** Help ***"));
        chatText.push(std::string("    /gm <argument list> - GM commands"));
        chatText.push(std::string("    /help - print command list"));
    }
    else if (command == "gm")
    {
        ProcessGameMasterCommand(serverPlayerStatus, args);
    }
	else if (command == "scenario")
	{
		ProcessScenarioCommand(serverPlayerStatus, args);
	}
    else
    {
        chatText.push(std::string("*** unrecognized command ***"));
        //tcSound::Get()->PlayEffect("intercom");
    }
    
}


void tcMultiplayerInterface::ProcessEndGame(tcPlayerStatus& player, const std::string& args)
{
    // assert(IsServer());

    std::string msg;
    
    int connectionId = player.GetConnectionId();
    
    if (player.IsCommander() || player.IsGM())
    {
        player.SetGameEnd(true);
        msg = "*** End game requested";
    }
    else
    {
        msg = "*** Only team commander or GM can end game";
    } 
    
    SendChatText(connectionId, msg);
}

void tcMultiplayerInterface::ProcessSurrender(tcPlayerStatus& player, const std::string& args)
{
    // assert(IsServer());

    std::string msg;
    
    int connectionId = player.GetConnectionId();
    
	if (player.IsCommander())
    {
        player.SetSurrender(true);
        msg = "*** Surrender requested";
    }
    else
    {
        msg = "*** Only team commander can surrender game";
    } 
    
    SendChatText(connectionId, msg);
}

/**
* Process single receive message for connection associated with connectionId
*/
void tcMultiplayerInterface::ProcessMessage(int messageId, int connectionId,
                                unsigned messageSize, const unsigned char *data)
{

    std::map<int, std::vector<tcMessageHandler*> >::iterator mapIter;

    mapIter = messageMap.find(messageId);
    if (mapIter == messageMap.end()) 
    {
        fprintf(stderr, 
            "Warning - tcMultiplayerInterface::ProcessMessage unrecognized message ID (%d)\n", 
            messageId);
        return;
    }

    // call all registered message handlers for this message
    std::vector<tcMessageHandler*>& mm = mapIter->second;
    size_t nHandlers = mm.size();
    for (size_t n = 0; n < nHandlers; n++)
    {
        assert(mm[n]);
        mm[n]->Handle(connectionId, messageSize, data);
    }
}

/**
*
*/
void tcMultiplayerInterface::ProcessReceiveMessages()
{
    int messageId;
    unsigned messageSize;

	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int connId = *iter;
        const unsigned char *tcp_data = networkInterface->ReceiveMessage(connId, messageId, 
            messageSize, tcNetworkInterface::TCP);
        if (tcp_data != NULL)
        {
            ProcessMessage(messageId, connId, messageSize, tcp_data);
        }

        const unsigned char *udp_data = networkInterface->ReceiveMessage(connId, messageId, 
            messageSize, tcNetworkInterface::UDP);
        if (udp_data != NULL)
        {
            ProcessMessage(messageId, connId, messageSize, udp_data);
        }
    }
}


/**
* Process command to change scenario
*/
void tcMultiplayerInterface::ProcessScenarioCommand(tcPlayerStatus& player, const std::string& args)
{
    // assert(IsServer());

 //    std::string msg;
    
 //    int connectionId = player.GetConnectionId();
    
 //    tcSimState* simState = tcSimState::Get();
 //    if (simState->IsScenarioLoaded() && (simState->GetTime() > 0))
 //    {
 //        msg = "*** Cannot change scenario after game started";
    // 	SendChatText(connectionId, msg);
 //        return;
 //    }

    // if (true) // allow any player for now, used to be: player.IsCommander())
 //    {
 //    	std::string scenario = args;
    // 	size_t firstQuote = scenario.find('"');
    // 	size_t secondQuote = (firstQuote != std::string::npos) ? scenario.find('"', firstQuote + 1) : std::string::npos;
    // 	if (firstQuote != std::string::npos && secondQuote != std::string::npos) // isolate text between quotes
    // 	{
    // 		scenario = scenario.substr(firstQuote + 1, secondQuote - firstQuote - 1);
    // 	}

    // 	bool success = scenarioSelectView->LoadScenarioByName(scenario, false);
    // 	if (success)
    // 	{
    // 		msg = "*** Change scenario success: " + scenario;
    // 		SendChatText(connectionId, msg);

    // 		msg = "*** " + player.GetNameWithRank() + " changed scenario to " + scenario;
    // 		BroadcastChatText(msg);
    // 	}
    // 	else
    // 	{
    // 		msg = "*** Change scenario failed, did not find scenario: " + scenario;
    // 		SendChatText(connectionId, msg);
    // 	}
 //    }
 //    else
 //    {
 //        msg = "*** Only team commander can change scenario";
    // 	SendChatText(connectionId, msg);
 //    }
    
    
}



/**
* Process command to start game
*/
void tcMultiplayerInterface::ProcessStartGame(tcPlayerStatus& player, const std::string& args)
{
    // assert(IsServer());

 //    std::string msg;
    
 //    int connectionId = player.GetConnectionId();
    
    // if (player.IsCommander())
 //    {
    // 	bool allReady = mpGameView->IsEveryoneReady();

    // 	if (allReady)
    // 	{
    // 		// post start game event
    // 		EventHandler* evtHandler = this->GetEvtHandler();
    // 		// TODO: Create appropriate event structure for non-wx implementation
    // 		// For now, we'll just call the start game method directly
    // 		// wxCommandEvent command(wxEVT_COMMAND_BUTTON_CLICKED, ID_STARTGAME);
    // 		// evtHandler->AddPendingEvent(command);

    // 		std::ostringstream oss;
 //            oss << "*** " << player.GetNameWithRank() << " started game";
    // 		BroadcastChatText(oss.str());

 //            // TODO: Replace wxDateTime with standard C++ time functions
 //            // wxString eventString = wxString::Format("Game start (%s)", wxDateTime::Now().FormatISOTime().c_str());
 //            // recentEvents.push_back(eventString);
 //            recentEvents.push_back("Game start");
 //        }
    // 	else
    // 	{
    // 		msg = "*** Start game failed. All players are not ready.";
    // 		SendChatText(connectionId, msg);
    // 	}
 //    }
 //    else
 //    {
 //        msg = "*** Only team commander can start game";
    // 	SendChatText(connectionId, msg);
 //    }

    
    
}




/**
* Send chat text to all players with matching alliance
*/
void tcMultiplayerInterface::ProcessTeamChat(const tcPlayerStatus& player, const std::string& msg)
{
    // create string with name prepended to text to identify source
    std::string namedText = std::string("[TEAM] <") + player.GetNameWithRank() + std::string("> ") + 
        msg;

    BroadcastChatText(namedText, player.GetAlliance());
}


/**
* Send list of players currently in game back to client
*/
void tcMultiplayerInterface::ProcessWho(tcPlayerStatus& player, const std::string& args)
{
	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    SendChatText(player.connectionId, "");
	SendChatText(player.connectionId, "Players currently in game:");
    for( ; iter != connectionList.end(); ++iter)
    {
		tcPlayerStatus& playerInfo = GetPlayerStatus(*iter);
		const std::string& connectionStatus = networkInterface->GetConnectionStatus(*iter, 0);

		std::string s = playerInfo.GetNameWithRank() + " [" + 
			std::to_string(playerInfo.GetAlliance()) + "] " + connectionStatus;

		SendChatText(player.connectionId, s);
    }
}


void tcMultiplayerInterface::SendAuthRequest(int destination)
{
	unsigned char buff[16];
	unsigned messageSize;

	tcAuthenticationMessageHandler::CreateAuthenticationRequest(messageSize, buff);

	networkInterface->SendMessage(destination, MSG_AUTHENTICATION, 
		messageSize, buff, tcNetworkInterface::TCP);
}

void tcMultiplayerInterface::SendAuthResponse(int destination)
{
	unsigned char buff[256];
	unsigned messageSize;

	tcAuthenticationMessageHandler::CreateAuthenticationResponse(myName, passwordHash, 
		messageSize, buff);

	networkInterface->SendMessage(destination, MSG_AUTHENTICATION, 
		messageSize, buff, tcNetworkInterface::TCP);

}

/**
* Sends simple briefing text to client for indicated alliance
* This is the only way of getting briefing info in multiplayer
*/
void tcMultiplayerInterface::SendBriefingText(int destination, int alliance)
{
	tcUpdateStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::BRIEFING_TEXT, stream);
    //tcUpdateMessageHandler::AddBriefingText(alliance, stream);

	SendUpdateMessageTCP(destination, stream);
}

/**
* Sends a test message of text to destination
*/
void tcMultiplayerInterface::SendChatText(int destination, const std::string& message)
{
    // first check for local message
    if (destination == 0)
    {
        chatText.push(message);
        return;
    }
    
    char buff[256];
    unsigned messageLength;

    int protocol = tcpChat ? tcNetworkInterface::TCP : tcNetworkInterface::UDP;

    tcTextMessageHandler::CreateMessage(messageLength, (unsigned char*)buff, message, 255);
   
    networkInterface->SendMessage(destination, MSG_CHATTEXT, 
        messageLength, (unsigned char*)buff, protocol);
}

/** 
* Send control message to destination using TCP
*/
void tcMultiplayerInterface::SendControlMessage(int destination, int messageCode, int param)
{
    unsigned char data[64];
    unsigned messageSize;

    tcControlMessageHandler::CreateControlMessage(messageCode, messageSize, data, param);
    networkInterface->SendMessage(destination, MSG_CONTROL, 
        messageSize , data, 
        tcNetworkInterface::TCP);
}

/** 
* Send control message to destination using UDP
*/
void tcMultiplayerInterface::SendControlMessageUDP(int destination, int messageCode, int param)
{
    unsigned char data[64];
    unsigned messageSize;

    tcControlMessageHandler::CreateControlMessage(messageCode, messageSize, data, param);
    networkInterface->SendMessage(destination, MSG_CONTROL, 
        messageSize , data, 
        tcNetworkInterface::UDP);
}

/**
* Merge these send methods into common
*/
void tcMultiplayerInterface::SendControlMessageUDPAck(int destination, int messageCode, int param)
{
    unsigned char data[64];
    unsigned messageSize;

    tcControlMessageHandler::CreateControlMessage(messageCode, messageSize, data, param);
    networkInterface->SendMessage(destination, MSG_CONTROL, 
        messageSize , data, 
        tcNetworkInterface::UDP_ACK);
}

/**
* Sends control request message to server requesting control of object id by player
*/
void tcMultiplayerInterface::SendControlRelease(int id)
{
    static std::vector<int> id_list;

    id_list.clear();
    id_list.push_back(id);

    SendControlRelease(id_list);
}


/**
* Sends control request message to server requesting release of control of object id by player
*/
void tcMultiplayerInterface::SendControlRelease(const std::vector<int>& id)
{
	if (IsServer())
	{
		fprintf(stderr, "tcMultiplayerInterface::SendControlRelease - called by server\n");
        assert(false);
		return;
	}

    if (id.size() == 0)
    {
        assert(false);
        return;
    }

	// server should be only connection
	const std::list<int>& connectionList = networkInterface->GetConnectionList();
	if (connectionList.size() == 0)
	{
		fprintf(stderr, "tcMultiplayerInterface::SendControlRelease - no connections\n");
        assert(false);
		return;
	}

    std::list<int>::const_iterator iter = connectionList.begin();
	int destination = *iter; 

	tcStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::CONTROL_REQUEST, stream);

    for (size_t k=0; k<id.size(); k++)
    {
        tcUpdateMessageHandler::AddControlRelease(id[k], stream);
    }

	SendUpdateMessageAck(destination, stream);
}


/**
* Sends control request message to server requesting control of object id by player
*/
void tcMultiplayerInterface::SendControlRequest(int id)
{
    static std::vector<int> id_list;

    id_list.clear();
    id_list.push_back(id);

    SendControlRequest(id_list);
}


/**
* Sends control request message to server requesting control of object id by player
*/
void tcMultiplayerInterface::SendControlRequest(const std::vector<int>& id)
{
	if (IsServer())
	{
		fprintf(stderr, "tcMultiplayerInterface::SendControlRequest - called by server\n");
        assert(false);
		return;
	}

    if (id.size() == 0)
    {
        assert(false);
        return;
    }

	// server should be only connection
	const std::list<int>& connectionList = networkInterface->GetConnectionList();
	if (connectionList.size() == 0)
	{
		fprintf(stderr, "tcMultiplayerInterface::SendControlRequest - no connections\n");
        assert(false);
		return;
	}

    std::list<int>::const_iterator iter = connectionList.begin();
	int destination = *iter; 

	tcStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::CONTROL_REQUEST, stream);

    for (size_t k=0; k<id.size(); k++)
    {
	    tcUpdateMessageHandler::AddControlRequest(id[k], stream);
    }

	SendUpdateMessageAck(destination, stream);
}

void tcMultiplayerInterface::SendScenarioInfo(const std::vector<int>& destinations)
{
	tcUpdateStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SCENARIO_INFO, stream);
	tcUpdateMessageHandler::AddScenarioInfo(stream);

	for (unsigned n=0; n<destinations.size(); n++)
	{
		int connectionId = destinations[n];

		tcPlayerStatus& player = GetPlayerStatus(connectionId);

		tcUpdateStream destStream(stream);
		SendUpdateMessageTCP(destinations[n], destStream);


		SendBriefingText(destinations[n], player.alliance);
	}
	
}


/**
* Version to send to one destination. Does not send briefing text
*/
void tcMultiplayerInterface::SendScenarioInfo(int destination)
{
	tcUpdateStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SCENARIO_INFO, stream);
	tcUpdateMessageHandler::AddScenarioInfo(stream);


//	tcPlayerStatus& player = GetPlayerStatus(destination);

	SendUpdateMessageTCP(destination, stream);
}

void tcMultiplayerInterface::SendDatabaseInfo(const std::vector<int>& destinations)
{
	for (unsigned n=0; n<destinations.size(); n++)
	{
		int connectionId = destinations[n];
        SendDatabaseInfo(connectionId);
    }
}


/**
* Sends database classname, id pairs to synchronize client database with server database
* Version to send to one destination.
*/
void tcMultiplayerInterface::SendDatabaseInfo(int destination)
{
    assert(IsServer());

    tcDatabaseIterator iter(0); // 0 is pass all

	tcUpdateStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::DATABASE_INFO, stream);
    size_t nInfo = 0;

    stream << int(-1); // -1 is signal to clear database on receipt of this message

    for (iter.First(); !iter.IsDone(); iter.Next())
    {
        std::shared_ptr<tcDatabaseObject> obj = iter.Get();

        assert(obj != 0);
        assert(obj->mnKey != -1);

        stream << obj->mnKey;
        stream << std::string(obj->mzClass.c_str());
        nInfo++;

        if (stream.size() > (stream.GetMaxSize() - 256))
        {
            SendUpdateMessageTCP(destination, stream);
            stream.clear();
            tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::DATABASE_INFO, stream);
            nInfo = 0;
        }
    }

    if (nInfo > 0)
    {
        SendUpdateMessageTCP(destination, stream);
    }

}


void tcMultiplayerInterface::SendSoundEffect(const std::string& player, const std::string& effect, int id)
{
	int connectionId = GetPlayerConnectionId(player);

	if (connectionId != -1)
	{
		SendSoundEffect(connectionId, effect, id);
	}
}

void tcMultiplayerInterface::SendSoundEffect(int destination, const std::string& effect, int id)
{
	tcStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SOUND_EFFECT, stream);

	tcUpdateMessageHandler::AddSoundEffect(id, effect, stream);

	SendUpdateMessage(destination, stream);

}

void tcMultiplayerInterface::SendTestUDP(int destination, const std::string& message)
{
	size_t messageLength = message.length();
	if (messageLength > 255) messageLength = 255;
	networkInterface->SendMessage(
		destination, MSG_CHATTEXT, 
		(unsigned)(messageLength+1), (unsigned char*)message.c_str(),
		tcNetworkInterface::UDP);
}

void tcMultiplayerInterface::SendUpdateMessage(int destination, tcStream& stream)
{
    size_t streamSize = stream.size();
    char* buffer = new char[streamSize];
    stream.read(buffer, streamSize);

    networkInterface->SendMessage(destination, MSG_UPDATE, streamSize, (unsigned char*)buffer,
        tcNetworkInterface::UDP);

    delete[] buffer;
}

void tcMultiplayerInterface::SendUpdateMessageAck(int destination, tcStream& stream)
{
    size_t streamSize = stream.size();
    char* buffer = new char[streamSize];
    stream.read(buffer, streamSize);

    networkInterface->SendMessage(destination, MSG_UPDATE, streamSize, (unsigned char*)buffer,
        tcNetworkInterface::UDP_ACK);

    delete[] buffer; 
}

void tcMultiplayerInterface::SendUpdateMessageTCP(int destination, tcStream& stream)
{
    size_t streamSize = stream.size();
    char* buffer = new char[streamSize];
    stream.read(buffer, streamSize);

    networkInterface->SendMessage(destination, MSG_UPDATE, streamSize, (unsigned char*)buffer,
		tcNetworkInterface::TCP);

    delete[] buffer; 
}

void tcMultiplayerInterface::SetAcceptAllClients(bool state)
{
	acceptAllClients = state;
}


void tcMultiplayerInterface::SetAllEndGameState(bool state)
{
    if (!IsServer())
    {
        assert(false);
        return;
    }

    std::map<int, tcPlayerStatus>::iterator iter = playerInfo.begin();

    for( ; iter != playerInfo.end(); ++iter)
    {
        tcPlayerStatus& player = iter->second;

        player.SetGameEnd(state);
    }
}

/**
* Set or clear ready state for all players
*/
void tcMultiplayerInterface::SetAllReadyState(bool state)
{
    if (!IsServer())
    {
        assert(false);
        return;
    }

    const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int destination = *iter;    
		
        tcPlayerStatus& player = GetPlayerStatus(destination);
        player.SetReady(state);
	}
}


/**
* 0 - UDP, otherwise - TCP
*/
void tcMultiplayerInterface::SetChatProtocol(int code)
{
	if (code)
	{
		tcpChat = true;
	}
	else
	{
		tcpChat = false; // use UDP
	}
}

/**
* Sets wxWidgets event handler for posting messages to application.
*/
// void tcMultiplayerInterface::SetEvtHandler(wxEvtHandler *eh)
// {
//     evtHandler = eh;
// }

/**
* Sets identification name string for player using this interface
*/
void tcMultiplayerInterface::SetName(const std::string& name)
{
	if (IsServer()) return; // don't allow server to change name

    myName = name;

	// limit size of name
	if (myName.size() >= 24)
	{
		myName = myName.substr(0, 23);
	}
}

void tcMultiplayerInterface::SetPassword(const std::string& plainText)
{
	passwordHash = tcAccountDatabase::Get()->GetMD5digest(plainText);
}

/**
* Sets ping time associated with connection
*/
void tcMultiplayerInterface::SetPingTime(int connectionId, float ping_s)
{
    networkInterface->SetPingTime(connectionId, ping_s);
}

void tcMultiplayerInterface::SetVersionString(const char* s)
{
    versionString = s;
}

/**
* This must be called regularly to perform network functions.
* (avoids need for multithreadeding)
* Need to clean this up to better isolate server vs. client processing
*/
void tcMultiplayerInterface::Update()
{
	bool gameStarted = true; //(simState->GetTime() > 0);

	unsigned startCount = tcTime::Get()->GetUpdated30HzCount();

    networkInterface->Update();

	unsigned endCount = tcTime::Get()->GetUpdated30HzCount();

	unsigned elapsed = endCount - startCount;
	if ((elapsed > updateCount) || ((endCount >> 3) % 5 == 0))
	{
		updateCount = elapsed;
	}

    // process receive messages
    ProcessReceiveMessages();

    // distribute chat text
    DistributeChatText();

    // update player information
    UpdatePlayerInfo();

    // periodically update parameters for tcOptions changes by user
    UpdateOptions();

    // state update for entities (game objects)
    if (gameStarted) UpdateEntities();

    if (IsServer())
    {
        if (gameStarted) 
        {
            UpdateSensorMaps();
            UpdateMissions();
        }

		UpdateGoalStatus();

		UpdateTeamStatus();

        UpdateServerStatus();
    }

    /* update time when paused only. This is redundant
    ** with obj state update which also has time info, but is 
    ** included as a heartbeat message.
    **
    ** Modified to always update to accomodate game speed requests
    **/
    if (IsServer())
    {
        UpdateTime();
    }
    
    UpdatePing();

}


/**
* Server only -- send updates for destroyed objects to client
* @param connIdx connection index of client to update
*/
void tcMultiplayerInterface::UpdateDestroyedEntities(tcPlayerStatus& pstatus)
{
    int connId = pstatus.connectionId;

    tcSimState* simState = tcSimState::Get();
    assert(simState);

    /* iterate through all pstatus objects and add to destroy stream if
    ** the object no inter exists
    */
    tcStream stream;
    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::DESTROY, stream);

    unsigned destroyCount = 0;
    for (std::map<int, tcPlayerStatus::UpdateInfo>::iterator iter = pstatus.lastUpdate.begin();
        iter != pstatus.lastUpdate.end(); )
    {
        int id = iter->first;
        if (simState->GetObject(id))
        {
            ++iter;
        }
        else
        {
            tcUpdateMessageHandler::AddDestroy(id, stream);
            pstatus.lastUpdate.erase(iter++);
            destroyCount++;
        }
    }

    if (destroyCount)
    {
        SendUpdateMessage(connId, stream);
#ifdef _DEBUG
        double t = simState->GetTime();
        fprintf(stdout, "Sent obj destroy msg, time: %.1f\n", t);
#endif
    }
    
}

void tcMultiplayerInterface::UpdateEntityCommands(tcPlayerStatus& pstatus, bool clearNewCmdFlag)
{
    int connId = pstatus.connectionId;

    tcSimState* simState = tcSimState::Get();
    assert(simState);

#ifdef _DEBUG
    double t = simState->GetTime();
#endif

    // iterate through all game objects and build command update stream
    tcCommandStream commandStream;
    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::COMMAND_UPDATE, commandStream);

    tcGameObjIterator iter;
    unsigned updateCount = 0;
    for (iter.First();iter.NotDone();iter.Next())
	{
		std::shared_ptr<tcGameObject> obj = iter.Get();
		if (obj->HasNewCommand())
		{
			if ((pstatus.alliance == obj->GetAlliance()) || !IsServer())
			{
				tcUpdateMessageHandler::AddCommandUpdate(obj, commandStream);
				
				updateCount++;
#ifdef _DEBUG
				fprintf(stdout, "%d ", obj->mnID);
#endif
			}

			// extremely important! not clearing command will flood network
			if (clearNewCmdFlag) obj->ClearNewCommand();
		}

        // create new message if updateCount gets too large
        if (updateCount >= 4)
        {
            SendUpdateMessage(connId, commandStream);
#ifdef _DEBUG
            fprintf(stdout, "Sent obj command update, time: %.1f\n", t);
#endif
            commandStream.clear();
            tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::COMMAND_UPDATE, commandStream);
            updateCount = 0;
        }
    }

    if (updateCount)
    {
        SendUpdateMessage(connId, commandStream);
#ifdef _DEBUG
        fprintf(stdout, "Sent obj command update, time: %.1f\n", t);
#endif
    }
}

void tcMultiplayerInterface::UpdateEntitiesXml(tcPlayerStatus& pstatus)
{
    if (!pstatus.IsXmlObserver())
    {
        assert(false);
        return;
    }
}


/**
* Periodically sends goal status (win/loss) to all clients
*/
void tcMultiplayerInterface::UpdateGoalStatus()
{
	static unsigned int lastUpdate = 0;

    assert(IsServer());

	unsigned t = tcTime::Get()->Get30HzCount();
	if (t - lastUpdate < goalUpdateInterval) return;
	lastUpdate = t;

	const std::list<int>& connectionList = networkInterface->GetConnectionList();

	std::list<int>::const_iterator iter = connectionList.begin();
//	unsigned n = 0;
	for( ; iter != connectionList.end(); ++iter)
	{
		int connectionId = *iter;

		tcPlayerStatus& player = GetPlayerStatus(connectionId);

		if ((player.isAuthenticated) && (player.GetAlliance() != 0))
		{
			tcUpdateStream updateStream;

			tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::GOAL_STATUS, updateStream);
			tcUpdateMessageHandler::AddGoalStatus(player.GetAlliance(), updateStream);

			SendUpdateMessageAck(connectionId, updateStream);

			fprintf(stdout, "Performed goal status update, conn %d, t: %d\n", 
				connectionId, t);
		}
	}

}


/**
* Send script command messages to server
*/
void tcMultiplayerInterface::UpdateScriptCommands(int connectionId)
{
//     assert(!IsServer());

// 	tcSimPythonInterface* pythonInterface = tcSimPythonInterface::Get();

// 	if (!pythonInterface->HasNewCommand()) return;

// 	tcCommandStream commandStream;
// 	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SCRIPT_COMMANDS, commandStream);

// 	pythonInterface->operator>>(commandStream);

// 	pythonInterface->ClearNewCommand();

// 	SendUpdateMessage(connectionId, commandStream);
// #ifdef _DEBUG
// 	fprintf(stdout, "Sent script commands\n");
// #endif

}

void tcMultiplayerInterface::GetUpdatePeriod(std::shared_ptr<const tcGameObject> obj, const std::string& playerName,
                                                     unsigned int& updatePeriod, unsigned int& detailedUpdatePeriod) const
{
    bool playerControlled = obj->IsControlledBy(playerName);

    detailedUpdatePeriod = playerControlled ? 300 : 900;

    std::shared_ptr<const tcFlightOpsObject> flightOps =  std::dynamic_pointer_cast<const tcFlightOpsObject>(obj);
    bool largeFlightOps = (flightOps == 0) ? false : (flightOps->CurrentAirComplementSize() > 8);
    
    if (!playerControlled)
    {
        if (!largeFlightOps)
        {
            updatePeriod = 90;
        }
        else
        {
            updatePeriod = 90;
        }
    }
    else
    {
        if (!largeFlightOps)
        {
            updatePeriod = 25;
        }
        else
        {
            updatePeriod = 60;
        }
    }
}

/**
* Server only -- send create updates for new entities to client
*/
void tcMultiplayerInterface::UpdateNewAndExistingEntities(tcPlayerStatus& pstatus)
{
    int connId = pstatus.connectionId;

    unsigned int t = tcTime::Get()->Get30HzCount();
    
	const std::string& playerName = pstatus.GetName();

    // create stream for new entities
    tcCreateStream createStream;
    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::CREATE, createStream);

    // update stream for existing entities
    tcUpdateStream updateStream;
    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::UPDATE, updateStream);


    tcGameObjIterator iter;
    unsigned createCount = 0;
    unsigned updateCount = 0;
	//const unsigned int maxMessageSize = tcMessage::GetMaxMessageSize();
        
    bool isObserver = pstatus.alliance == 0;

    for (iter.First(); iter.NotDone(); iter.Next())
    {
        std::shared_ptr<tcGameObject> obj = iter.Get();
        if (isObserver || (pstatus.alliance == obj->GetAlliance()))
        {
            unsigned int lastUpdate, lastDetailedUpdate;
            if (pstatus.GetLastUpdate(obj->mnID, lastUpdate, lastDetailedUpdate))
            {
				unsigned int dt = t - lastUpdate;
                unsigned int updatePeriod, detailedUpdatePeriod;
                GetUpdatePeriod(obj, playerName, updatePeriod, detailedUpdatePeriod);

                bool doUpdate = (dt >= updatePeriod);

				if (doUpdate)
				{
                    unsigned int dt_detailed = t - lastDetailedUpdate;
                    bool detailUpdate = (dt_detailed >= detailedUpdatePeriod);
                    if (!detailUpdate)
                    {
                        updateStream.SetDetailLevel(0);
                    }
                    else
                    {
                        updateStream.SetDetailLevel(1);
                    }

                    bool updateAdded = tcUpdateMessageHandler::AddUpdate(obj, updateStream);
                    
                    if (updateAdded)
                    {
                        updateCount++;
                    }
                    else
                    {
                        bool updating = true;
                        unsigned messageCount = 0;
                        while (updating && (messageCount < 8))
                        {
                            SendUpdateMessage(connId, updateStream);
#ifdef _DEBUG
                            fprintf(stdout, "Sent obj state update, time: %d\n", t);
#endif
                            updateStream.clear();
                            tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::UPDATE, 
                                updateStream);

                            updating = !tcUpdateMessageHandler::AddUpdate(obj, updateStream);
                            messageCount++;
                        }

                        if (messageCount >= 8)
                        {
                            fprintf(stderr, "tcMultiplayerInterface::UpdateNewAndExistingEntities - "
                                "exceeded partial update msg limit (%s)\n", obj->mzUnit.c_str());
                        }
                        else
                        {
#ifdef _DEBUG
                        fprintf(stdout, "   partial update msg count: %d\n", messageCount);
#endif
                        }
                        updateCount = 1;
                    }

					pstatus.SetUpdate(obj->mnID, t);
                    if (detailUpdate) pstatus.SetDetailedUpdate(obj->mnID, t);
				}

                
                // create new message if updateCount gets too large
				if (updateCount >= 6)
                {
                    SendUpdateMessage(connId, updateStream);
        #ifdef _DEBUG
                    fprintf(stdout, "Sent obj state update, time: %d\n", t);
        #endif
                    updateStream.clear();
                    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::UPDATE, 
                        updateStream);
                    updateCount = 0;
                }
            }
            else
            {
                bool createAdded = tcUpdateMessageHandler::AddCreate(obj, createStream);
                
                if (createAdded)
                {
                    createCount++;
                }
                else
                {
                    bool updating = true;
                    unsigned messageCount = 0;
                    while (updating && (messageCount < 8))
                    {
                        SendUpdateMessage(connId, createStream);
#ifdef _DEBUG
                        fprintf(stdout, "Sent obj create msg, time: %d\n", t);
#endif
                        createStream.clear();
                        tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::CREATE, 
                            createStream);

                        updating = !tcUpdateMessageHandler::AddCreate(obj, createStream);
                        messageCount++;
                    }

                    if (messageCount >= 8)
                    {
                        fprintf(stderr, "tcMultiplayerInterface::UpdateNewAndExistingEntities - "
                            "exceeded partial create msg limit (%s)\n", obj->mzUnit.c_str());
                    }
                    else
                    {
#ifdef _DEBUG
                        fprintf(stdout, "   partial create msg count: %d\n", messageCount);
#endif
                    }

                    createCount = 1;
                }

                // set time to force update at next opportunity
                pstatus.SetUpdate(obj->mnID, (unsigned int)(t-200));
                pstatus.SetDetailedUpdate(obj->mnID, (unsigned int)(t-200));
#ifdef _DEBUG
                fprintf(stdout, "C%d ", obj->mnID);
#endif

				if (createCount >= 8)
                {
                    SendUpdateMessage(connId, createStream);
        #ifdef _DEBUG
                    fprintf(stdout, "Sent obj create msg, time: %d\n", t);
        #endif
                    createStream.clear();
                    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::CREATE, 
                        createStream);
                    createCount = 0;
                }

            }
            
            
        }
    }

    if (createCount)
    {
        SendUpdateMessage(connId, createStream);
#ifdef _DEBUG
        fprintf(stdout, " -- object create msg sent\n");
#endif
    }
    
    if (updateCount)
    {
        SendUpdateMessage(connId, updateStream);
#ifdef _DEBUG
        fprintf(stdout, "Sent obj state update, time: %d\n", t);
#endif
    }   
    
}


/**
* Update air missions for flightops
*/
void tcMultiplayerInterface::UpdateMissions()
{   
    static unsigned lastUpdate = 0;

    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < missionUpdateInterval) return;
    lastUpdate = currentTime;


    // build list of authenticated players
    std::vector<int> validPlayers;
    const std::list<int>& connectionList = networkInterface->GetConnectionList();

    std::list<int>::const_iterator iter = connectionList.begin();
    for( ; iter != connectionList.end(); ++iter)
    {
        int id = *iter;
        
        tcPlayerStatus& player = GetPlayerStatus(id);
        if (player.isAuthenticated && !player.IsXmlObserver())
        {
            validPlayers.push_back(id);
        }
    }

    // for each player, add flight ops missions to update message
    // send to player if there is at least one update
    for (size_t k=0; k<validPlayers.size(); k++)
    {
        int id = validPlayers[k];
        tcPlayerStatus& player = GetPlayerStatus(id);

        tcUpdateStream updateStream;
        tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::AUTO_MISSIONS, updateStream);
        unsigned nUpdates = 0;

        tcGameObjIterator iter;

        for (iter.First(); iter.NotDone(); iter.Next())
        {
            std::shared_ptr<tcGameObject> obj = iter.Get();
            std::shared_ptr<tcFlightOpsObject> flightOps =  std::dynamic_pointer_cast<tcFlightOpsObject>(obj);
            if ((flightOps != 0) && (obj->IsControlledBy(player.GetName())))
            {
                ai::tcMissionManager* missionManager = flightOps->GetFlightPort()->GetMissionManager();
                if ((missionManager != 0) && (missionManager->GetMissionCount() > 0))
                {
                    tcUpdateMessageHandler::AddAirMissionUpdate(flightOps, updateStream);
                    nUpdates++;
                }
            }
        }
        
        SendUpdateMessage(id, updateStream); // always send so that deletes get performed correctly at client

    }



}


/**
* Send state updates on objects to clients (command info in both directions)
*/
void tcMultiplayerInterface::UpdateEntities()
{
    unsigned int t = tcTime::Get()->Get30HzCount();

    std::map<int, tcPlayerStatus>::iterator iter = playerInfo.begin();

    unsigned nPlayers = playerInfo.size();

    unsigned n = 0;
    for( ; iter != playerInfo.end(); ++iter)
    {
        int id = iter->first;
        tcPlayerStatus& player = iter->second;

		// always do script command update at client
		if (!IsServer())
		{
			UpdateScriptCommands(id);
		}

        /* always do new cmd update, clear flag on last only.
		** New commands need to be send to all clients at once with
		** this system */
        bool clearNewCmdFlag = (n++ == (nPlayers - 1));
        UpdateEntityCommands(player, clearNewCmdFlag); 
        
        unsigned int dt = t - player.entityUpdateTime;
		
        if ((dt > entityUpdateInterval) && (player.isAuthenticated) && IsServer())
		{
			player.entityUpdateTime = t;

            if (!player.IsXmlObserver())
            {

                if (player.isInGame)
                {
                    UpdateDestroyedEntities(player);
                    UpdateNewAndExistingEntities(player);
                }
                else
                {
                    SendControlMessage(player.connectionId, network::tcControlMessageHandler::CM_TIME);
                }

                //fprintf(stdout, "Performed entity state update, conn %d, t: %d\n", 
                //	id, t);
            }
            else
            {
                UpdateEntitiesXml(player);
            }
		}


    }


}


/**
* Periodically update multiplayer parameters based on tcOptions state, allows
* options to be changed "on the fly"
*/
void tcMultiplayerInterface::UpdateOptions()
{
    unsigned int t = tcTime::Get()->Get30HzCount();
    const unsigned int updateInterval = 60; // 30 Hz tics to update options
    if ((t - lastOptionsUpdate) < updateInterval) return;

    lastOptionsUpdate = t;
    if (!IsServer()) return; // only applies to server for now

    tcOptions* options = tcOptions::Get();

    sendDetailedTrackInfo = (options->sendTrackDetails != 0);
    tcSensorMapTrack::sendDetailedTrackInfo = sendDetailedTrackInfo;

    switch (options->sensorUpdateRate)
    {
        case 0:  sensorUpdateInterval = 90; break;
        case 1:  sensorUpdateInterval = 60; break;
        case 2:  sensorUpdateInterval = 30; break;
        case 3:  sensorUpdateInterval = 15; break;
        default: sensorUpdateInterval = 30; break;
    }
}



/**
*
*/
void tcMultiplayerInterface::UpdatePing()
{
    static unsigned lastUpdate = 0;
    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < 30) return;
    
    lastUpdate = currentTime;

    const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int id = *iter;

        SendControlMessageUDPAck(id, tcControlMessageHandler::CM_PING, 0);
    }
}

/**
*
*/
void tcMultiplayerInterface::UpdatePlayerInfo()
{
    static unsigned lastUpdate = 0;
    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < 5) return;
    
    lastUpdate = currentTime;

    // add new connections
    const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int connId = *iter;

        if (IsNewPlayer(connId))
        {
            tcPlayerStatus stat;
            stat.ping_s = 0;
			stat.startTime = tcTime::Get()->Get30HzCount();
            stat.timestamp = stat.startTime;
			stat.entityUpdateTime = 0;
			stat.sensorUpdateTime = 0;
            stat.name = "Anonymous";
            stat.isXmlObserver = false;
            stat.isCommander = false;
			stat.isReady = false;
			stat.isAuthenticated = false;
            stat.connectionId = connId;

			if (IsServer())
			{
				SendAuthRequest(connId);
			}
			else
			{
				stat.name = "SERVER";
			}           
			
			playerInfo[connId] = stat;
            //tcSound::Get()->PlayEffect("intercom");
        }
        else
        {
            playerInfo[connId].timestamp = tcTime::Get()->Get30HzCount();
        }
    }


    std::queue<int> eraseKeys;

    for (std::map<int,tcPlayerStatus>::iterator iter = playerInfo.begin();
        iter != playerInfo.end(); ++iter) 
    {
        unsigned t = iter->second.timestamp;
        // key is in iter->first, value in iter->second

		if (IsServer() && !iter->second.isAuthenticated && 
              (currentTime - iter->second.startTime > 240))
		{
            eraseKeys.push(iter->first);
            //tcSound::Get()->PlayEffect("fslide");
		}
        else if (currentTime - t > 15)
        {
            eraseKeys.push(iter->first);
            //tcSound::Get()->PlayEffect("fslide");
			LogOutPlayer(iter->second.name);

			if (IsServer())
			{
                std::string msg = strutil::format("*** %s has left the game",
					iter->second.GetNameWithRank().c_str());
                BroadcastChatText(msg);
			}
			else
			{
                OnLostServer();
			}
        }

    }

    while (!eraseKeys.empty())
    {
        int id = eraseKeys.front();
        playerInfo.erase(id);
        networkInterface->RemoveConnection(id);
        eraseKeys.pop();
    }
}

/**
* Send sensor map update for player at connIdx
*/
void tcMultiplayerInterface::UpdateSensorMap(tcPlayerStatus& pstatus)
{
    int connId = pstatus.connectionId;
    int alliance = pstatus.alliance;

    tcSimState* simState = tcSimState::Get();
    assert(simState);

    tcSensorMap* sensorMap = simState->GetSensorMap();
    tcAllianceSensorMap* allianceSensorMap = sensorMap->GetMap(alliance);
	if (allianceSensorMap == 0) return;
	

    tcUpdateStream stream;
    tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SENSOR_UPDATE, stream);
    stream.SetDoneFlag(false);


    unsigned int nMessages = 0;
	const unsigned int maxMessages = 4;
    bool doneWriting = false;

    while (!doneWriting && (nMessages++ < maxMessages))
    {    
        tcUpdateMessageHandler::AddSensorUpdateHeader(alliance, stream);
        size_t initialStreamSize = stream.size();

        *allianceSensorMap >> stream;
        doneWriting = stream.GetDoneFlag();

        if (stream.size() > initialStreamSize)
        {
            SendUpdateMessage(connId, stream);
            fprintf(stdout, ">> sensormap update msg sent, connId (%d) size (%d) msg (%d)\n",
                connId, stream.size(), nMessages);
        }

        if (!doneWriting)
        {
            stream.clear();
            tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::SENSOR_UPDATE, stream);
            stream.SetDoneFlag(false);
        }
    }

    if (nMessages >= maxMessages)
    {
        fprintf(stderr, "tcMultiplayerInterface::UpdateSensorMap - exceeded max messages\n");
    }
}

/**
* Periodically send sensor updates to clients
*/
void tcMultiplayerInterface::UpdateSensorMaps()
{
    assert(IsServer());

    unsigned int t = tcTime::Get()->Get30HzCount();

    std::map<int, tcPlayerStatus>::iterator iter = playerInfo.begin();

    for( ; iter != playerInfo.end(); ++iter)
    {
        tcPlayerStatus& player = iter->second;
        unsigned int dt = t - player.sensorUpdateTime;
        if ((dt > sensorUpdateInterval) && (player.isAuthenticated) && (player.isInGame))
        {
            player.sensorUpdateTime = t;
            
            UpdateSensorMap(player);
        }
    }

}


/**
*
*/
void tcMultiplayerInterface::UpdateServerStatus()
{
    static unsigned lastUpdate = 0;
    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < 150) return;
    
    lastUpdate = currentTime;

    WriteHtmlStatus(logFilePath);
}


void tcMultiplayerInterface::UpdateTeamStatus()
{
    assert(IsServer());

	unsigned int updateInterval = teamUpdateInterval;

	tcSimState* simState = tcSimState::Get();
    if (simState->IsMultiplayerGameStarted())
	{
		updateInterval = 19; // faster update before game starts
	}

	static unsigned lastUpdate = 0;
    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < updateInterval) return;
    
    lastUpdate = currentTime;

	tcUpdateStream stream;
	tcUpdateMessageHandler::InitializeMessage(tcUpdateMessageHandler::TEAM_STATUS, stream);
	tcUpdateMessageHandler::AddTeamStatus(stream);


	const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();

    for( ; iter != connectionList.end(); ++iter)
    {
        int id = *iter;

		tcUpdateStream connStream(stream);

        SendUpdateMessageTCP(id, connStream);
	}

    //mpGameView->SetTeamList(tcUpdateMessageHandler::GetLatestTeamList());
}


/**
* Periodically broadcasts time update to all clients
* Set time acceleration based on game speed requests of commanders
*/
void tcMultiplayerInterface::UpdateTime()
{
    static unsigned lastUpdate = 0;    
    static int lastAccel = 0;
    
    // send time update if acceleration has changed
    tcSimState* simState = tcSimState::Get();
    int currentAccel = simState->GetTimeAcceleration();
    if (currentAccel != lastAccel)
    {
        BroadcastControlMessage(tcControlMessageHandler::CM_TIME);
    }
    lastAccel = currentAccel;


    unsigned currentTime = tcTime::Get()->Get30HzCount();
    if (currentTime - lastUpdate < 30) return;
    lastUpdate = currentTime;

    // update time acceleration
    const std::list<int>& connectionList = networkInterface->GetConnectionList();
    std::list<int>::const_iterator iter = connectionList.begin();
    int minVal = 999;
    int maxVal = -1;

    for( ; iter != connectionList.end(); ++iter)
    {
        int destination = *iter;    
		
        tcPlayerStatus& player = GetPlayerStatus(destination);
        
        if (player.IsCommander())
        {
            int requestedSpeed = (int)player.GetGameSpeed();
            minVal = std::min(minVal, requestedSpeed);
            maxVal = std::max(maxVal, requestedSpeed);
        }
    }
    
    // any commander can slow down time accel
    // commanders must agree to speed up time
    bool legalChange = (minVal < currentAccel) || 
        ((minVal > currentAccel) && (minVal == maxVal));
    if ((maxVal != -1) && legalChange)
    {
        //EventHandler* evtHandler = this->GetEvtHandler();
		// wxCommandEvent command(wxEVT_COMMAND_BUTTON_CLICKED, ID_SETTIMEACCEL);
        //command.m_extraint = minVal; // 2.6.3 code
        // command.SetExtraint(minVal);
        // evtHandler->AddPendingEvent(command);
		
		// TODO: 实现适当的事件处理机制来替代wxWidgets事件
    }
    

    // send time message to all clients if game is paused
    if (currentAccel == 0)
    {
        BroadcastControlMessage(tcControlMessageHandler::CM_TIME);
    }
}

void tcMultiplayerInterface::WriteHtmlStatus(const std::string& filePath)
{
    // assert(IsServer());

    // wxFFile outFile(filePath.c_str(), "w");
    // if (!outFile.IsOpened()) return;
	FILE* outFile = fopen(filePath.c_str(), "w");
	if (!outFile) return;

    // trim length of recentEvents if necessary
    if (recentEvents.size() > 16)
    {
        // recentEvents.RemoveAt(0, recentEvents.size() - 16);
		recentEvents.erase(recentEvents.begin(), recentEvents.begin() + (recentEvents.size() - 16));
    }

    if (recentChat.size() > 16)
    {
        // recentChat.RemoveAt(0, recentChat.size() - 16);
		recentChat.erase(recentChat.begin(), recentChat.begin() + (recentChat.size() - 16));
    }


    // wxDateTime dateTime = wxDateTime::Now();
    // wxDateTime dateTimeUTC = dateTime;
    // dateTimeUTC.MakeTimezone(wxDateTime::UTC);

    // wxString timeStamp;
    // timeStamp.Printf("<P>%s %sZ %sL\n%s</P>\n", dateTimeUTC.FormatISODate().c_str(), dateTimeUTC.FormatISOTime().c_str(),
    //     dateTime.FormatISOTime().c_str(), versionString.c_str());
	std::ostringstream timeStamp;
	timeStamp << "<P>TODO: Add timestamp here\n" << versionString << "</P>\n";
 
    // outFile.Write("<html>\n");
    // outFile.Write("<H2>GCB2 Server Status (gcblue.servegame.com)</H2>\n");    
    // outFile.Write(timeStamp.c_str());
	fprintf(outFile, "<html>\n");
	fprintf(outFile, "<H2>GCB2 Server Status (gcblue.servegame.com)</H2>\n");
	fprintf(outFile, "%s", timeStamp.str().c_str());
    
	// wxString s; 
	std::ostringstream s;
    // scenario
    double simTime = 0.016667 * tcSimState::Get()->GetTime();
    if (simTime > 0)
    {
        // s.Printf("<H3>Current Scenario: %s (%.0f min)</H3>\n", tcSimState::Get()->GetScenarioName(),
        //     simTime);
		s << "<H3>Current Scenario: " << tcSimState::Get()->GetScenarioName() << " (" << (int)simTime << " min)</H3>\n";
    }
    else
    {
        // s.Printf("<H3>Current Scenario: %s (not started)</H3>\n", tcSimState::Get()->GetScenarioName());
		s << "<H3>Current Scenario: " << tcSimState::Get()->GetScenarioName() << " (not started)</H3>\n";
    }
    // outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());

    // s.Printf("<P>%s</P><BR>\n", tcSimState::Get()->GetScenarioDescription());
	s.str(""); // 清空ostringstream
	s << "<P>" << tcSimState::Get()->GetScenarioDescription() << "</P><BR>\n";
    // outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());

    // players in game
    // tcAllianceInfo* allianceInfo = tcAllianceInfo::Get();
    // outFile.Write("<H3>Current Players</H3>\n");
	s.str("");
	s << "<H3>Current Players</H3>\n";
	// outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());
	
    // s = "<P>\n";
	s.str("");
	s << "<P>\n";
    std::map<int, tcPlayerStatus>::iterator iter = playerInfo.begin();

    for( ; iter != playerInfo.end(); ++iter)
    {
        tcPlayerStatus& player = iter->second;
        s << "<B>" << player.GetName() << "</B> (";
        unsigned char alliance =  player.GetAlliance();
        if (alliance != 0)
        {
            // s += allianceInfo->GetAllianceName(alliance);
			s << "Alliance " << (int)alliance; // 简化处理，实际应该获取联盟名称
        }
        else
        {
            s << "Observers";
        }
        // s += wxString::Format(") Ping: %4.0f ms\n", 1000.0f*player.ping_s);
		s << ") Ping: " << (int)(1000.0f*player.ping_s) << " ms\n";

    }
    // s += "</P><BR>\n";
	s << "</P><BR>\n";
    // outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());


    // recent log ins / log outs
    // outFile.Write("<H3>Recent Events</H3>\n");
	s.str("");
	s << "<H3>Recent Events</H3>\n";
	// outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());
	
    // s = "<P>";
	s.str("");
	s << "<P>";
    for (size_t k=0; k<recentEvents.size(); k++)
    {
        // s += recentEvents[k];
        // s += "<BR>\n";
		s << recentEvents[k] << "<BR>\n";
        
    }
    // s += "</P>\n";
	s << "</P>\n";
    // outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());

    // recent chat text
    // outFile.Write("<H3>Recent Chat</H3>\n");
	s.str("");
	s << "<H3>Recent Chat</H3>\n";
	// outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());
	
    // s = "<P>";
	s.str("");
	s << "<P>";
    for (size_t k=0; k<recentChat.size(); k++)
    {
        // s += recentChat[k];
        // s += "<BR>\n";
		s << recentChat[k] << "<BR>\n";
        
    }
    // s += "</P>\n";
	s << "</P>\n";
    // outFile.Write(s);
	fprintf(outFile, "%s", s.str().c_str());


    // outFile.Write("</html>\n");
	fprintf(outFile, "</html>\n");
	
	// if (outFile) outFile.Close();
	if (outFile) fclose(outFile);
}

tcMultiplayerInterface::tcMultiplayerInterface()
:   mpGameView(0),
    scenarioSelectView(0),
    myName("NoName"),
    tcpChat(true),
    acceptAllClients(true),
    allowAllTeamChanges(true),
    //evtHandler(0),
    entityUpdateInterval(0),
    sensorUpdateInterval(30),
    goalUpdateInterval(600),
    teamUpdateInterval(39),
    missionUpdateInterval(87),
    sendDetailedTrackInfo(false),
    lastOptionsUpdate(0)
{
    networkInterface = new tcNetworkInterface();
    assert(networkInterface);

    errorPlayerStatus.name = "error";
    errorPlayerStatus.timestamp = 0;
    
    serverPlayerStatus.SetName("SERVER");
    serverPlayerStatus.SetNameWithRank("SERVER");
    serverPlayerStatus.SetAlliance(0);
	serverPlayerStatus.isCommander = true;
	serverPlayerStatus.SetRank(tcUserInfo::RANK_GM);
    serverPlayerStatus.timestamp = 0;
    serverPlayerStatus.isAuthenticated = true;
    serverPlayerStatus.data.flags = 0xFFFF;
    serverPlayerStatus.SetConnectionId(0);
 
	updateCount = 0;
}

/**
* Copy constructor not allowed for this singleton class
*/
tcMultiplayerInterface::tcMultiplayerInterface(const tcMultiplayerInterface& source)
:   entityUpdateInterval(source.entityUpdateInterval),
    sensorUpdateInterval(source.sensorUpdateInterval),
	goalUpdateInterval(source.goalUpdateInterval),
	teamUpdateInterval(source.teamUpdateInterval),
    missionUpdateInterval(source.missionUpdateInterval)
{
    assert(false);
}

tcMultiplayerInterface::~tcMultiplayerInterface()
{
    ClearMessageMap();

    if (networkInterface)
	{
		delete networkInterface;
	}
}

END_NAMESPACE

#ifdef TC_WINDOWS_GETOBJECT_WORKAROUND_APPLIED
#pragma pop_macro("GetObject")
#undef TC_WINDOWS_GETOBJECT_WORKAROUND_APPLIED
#endif
