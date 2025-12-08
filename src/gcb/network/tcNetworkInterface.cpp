/** @file tcNetworkInterface.cpp */
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

#include "network/tcNetworkInterface.h"
#include "network/tcTextMessageHandler.h"
#include "tcTime.h"
#include <iostream>
#include <string>
#include <cerrno>
#include <cassert>

#ifdef _WIN32
#include <winsock2.h>
#endif

BEGIN_NAMESPACE(network)


/**
* Creates new connection using <socket>
* A new id is assigned. The new connection is added to the peerMap
* and connectionList.
*/
void tcNetworkInterface::AddConnection(SocketTCPClient *socket)
{
    tcConnectionData* cdata = new tcConnectionData;

    cdata->SetSocket(socket);
    cdata->idString = Socket::addr2string(socket->getAddr());


    cdata->timestamp = tcTime::Get()->Get30HzCount();
    cdata->id = connectionIndex++;


    connectionData[cdata->id] = cdata;

    peerMap[std::string(cdata->idString.c_str())] = cdata->id;

    connectionList.push_back(cdata->id);

    fprintf(stdout, "New connection: %s : %d\n", Socket::addr2string(socket->getAddr()).c_str(), socket->getPort());
    connectState = IS_CONNECTED;
}

void tcNetworkInterface::RemoveConnection(int id)
{
    std::map<int, tcConnectionData*>::iterator iter = connectionData.find(id);
    if (iter == connectionData.end())
    {
        fprintf(stderr, "Connection id: %d not found in map\n", id);
        return;
    }
    tcConnectionData* connection = iter->second;
    
    // remove from peerMap
    {
        std::string peerName = connection->GetIdString();
        
        std::map<std::string, int>::iterator peerMapIter = peerMap.find(peerName);
        if (peerMapIter != peerMap.end())
        {
            peerMap.erase(peerMapIter);
        }
        else
        {
            fprintf(stderr, "Connection id: %d not found in peerMap\n", id); 
        }
    }
    
    // remove from connectionList
    connectionList.remove(id);
    
    // 获取 socket 并确保它被正确关闭
    SocketTCPClient* socket = connection->GetSocket();
    if (socket ) {
        socket->close();
    }
    
    // remove from connectionData
    delete connection;
    connectionData.erase(iter);
    
    if (connectionData.size() == 0)
    {
        connectState = NOT_CONNECTED;
    }

    // re-init client sock if client
    if (!isServer)
    {
        // 确保旧的 clientSock 被删除
        if (clientSock) {
            delete clientSock;
        }
        clientSock = new SocketTCPClient();
        InitializeUDP();
    }
}

/**
* Destroy all sockets
*/
void tcNetworkInterface::Clear()
{        
    // delete all connections first
    std::map<int, tcConnectionData*>::iterator iter = connectionData.begin();
    for ( ; iter != connectionData.end(); ++iter)
    {
        delete iter->second;
    }
    connectionData.clear();
    peerMap.clear();
    connectionList.clear();
    
    if (clientSock)
    {
        delete clientSock;
        clientSock = nullptr;
    }
    
    if (serverSock)
    {
        delete serverSock;
        serverSock = nullptr;
    }

    if (datagramSock)
    {
        delete datagramSock;
        datagramSock = nullptr;
    }

    ResetMessageBuffer();

    connectState = NOT_CONNECTED;
}

/** 
* Free (return to buffer) all queued messages in connection data
*/
void tcNetworkInterface::ClearConnectionMessages(int id)
{
    tcConnectionData* connection = GetConnection(id);

    // wxASSERT(connection);
    assert(connection);
    if (connection == 0)
    {
        fprintf(stderr, "Error - Bad id (%d) passed to ClearConnectionMessages\n", id);
        return;
    }

    connection->ClearAllMessages();
}

/**
* Complement of OpenConnection, used by client to close connection to
* server.
*/
void tcNetworkInterface::CloseConnection()
{
    if (isServer)
    {
        fprintf(stderr, 
                "Error - tcNetworkInterface::CloseConnection called in server mode\n");
        return;
    }
    
    if (connectState == NOT_CONNECTED)
    {
        fprintf(stderr,
                "Error - tcNetworkInterface::CloseConnection called while not connected\n");
        return;
    }

    // 使用 socket 的 close() 方法来断开连接
    if (clientSock) {
        clientSock->close();
    }
    
    Clear();
}

const std::list<int>& tcNetworkInterface::GetConnectionList() const
{
    // wxASSERT(connectionList.size() == connectionData.size());
    return connectionList;
}

/**
* For iterating through connections. (Need this?)
*/
const std::map<int, tcConnectionData*>& tcNetworkInterface::GetConnectionMap()
{
    return connectionData;
}



const std::string& tcNetworkInterface::GetConnectionStatus(int id, int detailLevel)
{
    static std::string s;

    unsigned timeCount = tcTime::Get()->Get30HzCount();

    if (connectState == IS_CONNECTING)
    {
        s = "Connecting to " + Socket::addr2string(hostAddress);
        
        // display "animated" dots while connecting to indicate something is happening
        unsigned animateCount = timeCount % 40;
        if (animateCount >= 10) s += ". ";
        if (animateCount >= 20) s += ". ";
        if (animateCount >= 30) s += ".";

        return s;
    }

    //if (connectionIdx >= GetNumConnections()) return "Error";

    tcConnectionData* connData = GetConnection(id);
    // wxASSERT(connData);
    if (connData == 0)
    {
        s = "Error";
        return s;
    }


    float dt_sec = (1.0f/30.0f)*(float)(timeCount - connData->timestamp);
    
    unsigned int bytesIn = connData->GetReadCountSec();
    unsigned int bytesOut = connData->GetWriteCountSec();

    char status[512];
    if (detailLevel == 0)
    {
        sprintf(status, "%s (%.0f ms)", connData->GetIdString(), 
                1000.0f*connData->GetPingTime());
    }
    else if (detailLevel == 1)
    {
        sprintf(status, "%s (%.0f ms) In: %d B/s Out: %d B/s", 
                connData->GetIdString(), 1000.0f*connData->GetPingTime(),
                bytesIn, bytesOut);
    }
    else
    {
        sprintf(status, "%s (%.0f ms) Age: %.0f s In: %d B/s Out: %d B/s", 
                connData->GetIdString(), 1000.0f*connData->GetPingTime(),
                dt_sec, bytesIn, bytesOut);
    }
    s = std::string(status);

    return s;
}



/**
* Obtains message buffer if available.
* @return valid id if message buffer is available, -1 otherwise
*/
int tcNetworkInterface::CheckoutMessage()
{
    if (available.empty()) return -1;
    int idx = (int)available.front();
    available.pop();
    return idx;
}

tcConnectionData *tcNetworkInterface::GetConnection(SocketTCPClient * socket)
{
    std::map<int, tcConnectionData*>::iterator iter = connectionData.begin();

    for (; iter!=connectionData.end(); ++iter) {
        if(iter->second->GetSocket()==socket)
        {
            return iter->second;
        }
    }
    return nullptr;
}

/**
* @return 0 if id is invalid, pointer to connection data otherwise
*/
tcConnectionData* tcNetworkInterface::GetConnection(int id)
{
    std::map<int, tcConnectionData*>::iterator iter = connectionData.find(id);
    
    if (iter != connectionData.end())
    {
        return iter->second;
    }
    else
    {
        return 0; 
    }
}



/**
* Lookup connection by peerName and return pointer to connection data
* @return 0 if idx is invalid, pointer to connection data otherwise
*/
tcConnectionData* tcNetworkInterface::GetConnection(const std::string& peerName)
{
    std::map<std::string, int>::const_iterator mapIter =
        peerMap.find(peerName);
    if (mapIter != peerMap.end()) 
    {
        return GetConnection(mapIter->second);
    }
    else
    {
        return 0;
    }
}



tcMessage* tcNetworkInterface::GetMessage(int id)
{
    if ((id < 0)||(id >= (int)messageBuffer.size())) return 0;
    return &messageBuffer[id];
}

unsigned int tcNetworkInterface::GetNumConnections()
{
    if (isServer)
    {
        return (unsigned int)connectionData.size();
    }
    else
    {
        if (connectState == IS_CONNECTED)
        {
            // client mode has one connection to server if connected
            // wxASSERT(connectionData.size() == 1);
            // wxASSERT(connectionList.size() == 1);
            return 1;
        }
        else if (connectState == NOT_CONNECTED)
        {
            return 0;
        }
        else if (connectState == IS_CONNECTING)
        {
            return 1; // attempted connection counted
        }
        else
        {
            // wxASSERT(false);
            return 0;
        }
    }
}

/**
* Initializes UDP datagram socket
*/
void tcNetworkInterface::InitializeUDP()
{
    if (datagramSock) return; // already initialized

    // Create UDP socket and bind to port
    datagramSock = new SocketUDP();
    datagramSock->createServer(UDP_PORT);


    fprintf(stdout, "Created datagram socket on port %d\n", UDP_PORT);
}


bool tcNetworkInterface::IsConnecting() const
{
    return (connectState == IS_CONNECTING);
}

/**
* @return true if this interface is acting as a server
*/
bool tcNetworkInterface::IsServer() const
{
    return isServer;
}



/**
* Destroy all old sockets and initialize clientSock
*/
void tcNetworkInterface::MakeClient()
{   
    Clear();

    isServer = false;
    
    // create the socket
    clientSock = new SocketTCPClient();

    InitializeUDP();
}

void tcNetworkInterface::MakeServer()
{
    Clear();

    isServer = true;

    serverSock = new SocketTCPServer();
    fprintf(stdout, "Server listening at port %d\n", TCPIP_PORT);

    InitializeUDP();
}

/**
* Handles socket events from the underlying network system.
* This method has been adapted to work without wxWidgets event system,
* using direct socket polling instead.
*/
void tcNetworkInterface::OnSocketEvent(/*SocketEvent& event*/)
{
    // This method is kept for compatibility but is no longer used
    // Event handling is done through polling in Update methods
}

/**
* Opens connection with server specified by hostName.
* @param hostName server address--can be a host name or an IP-style address in dot notation (a.b.c.d)
*/
void tcNetworkInterface::OpenConnection(const std::string& hostName)
{
    if (isServer)
    {
        std::cerr << "Error - tcNetworkInterface::OpenConnection called in server mode." << std::endl;
        return;
    }
    if (connectState != NOT_CONNECTED)
    {
        std::cerr << 
            "Error - tcNetworkInterface::OpenConnection called while connected or connecting."
                  << std::endl;
        return;
    }
    if (clientSock == NULL)
    {
        std::cerr << 
            "Error - tcNetworkInterface::OpenConnection called with NULL clientSock."
                  << std::endl;
        return;
    }

    connectState = IS_CONNECTING;
    connectionStartTime = tcTime::Get()->Get30HzCount();

    clientSock->createConnection(hostName.c_str(),TCPIP_PORT);



    connectState=IS_CONNECTED;
    fprintf(stdout, "Connecting to %s\n", hostName.c_str());
}


/**
* Remove connections that don't have UDP pings, or have other TBD issues
*/
void tcNetworkInterface::RemoveBadConnections()
{
    std::list<int>::iterator iter = connectionList.begin();
    while (iter != connectionList.end())
    {
        tcConnectionData* connection = GetConnection(*iter);
        // wxASSERT(connection);
        if (connection == 0)
        {
            fprintf(stderr, "Error - bad connection id in connectionList\n");
            return;
        }
        // wxASSERT(connection->GetSocket());
        // Note: Original code checked socket state with sockpp methods
        // We'll skip this check since our SocketTCP implementation doesn't have these methods
        ++iter;
    }
}


/**
* Remove connections that have disconnected from connectionData
*/
void tcNetworkInterface::RemoveDeadConnections()
{
    std::vector<int> deadConnections;

    std::map<int, tcConnectionData*>::iterator iter = connectionData.begin();
    
    for( ; iter != connectionData.end(); ++iter)
    {
        tcConnectionData* connection = iter->second;
        if (!connection->GetSocket()||!connection->GetSocket()->isOpen())
        {
            deadConnections.push_back(iter->first);
        }
    }
    
    size_t nDead = deadConnections.size();
    for (size_t n=0; n<nDead; n++)
    {
        RemoveConnection(deadConnections[n]);
    }
}


/**
* Clears and re-initializes messageBuffer. Clears all 
* queued read/write/ack messages.  This should be
* called at least once at startup.
*/
void tcNetworkInterface::ResetMessageBuffer()
{
    std::map<int, tcConnectionData*>::iterator iter = connectionData.begin();
    
    for ( ; iter != connectionData.end(); ++iter)
    {
        iter->second->ClearAllMessages();
    }

    messageBuffer.clear();
    while(!available.empty()) available.pop();

    for(unsigned i=0;i<MESSAGE_BUFFER_SIZE;i++)
    {
        tcMessage message;
        messageBuffer.push_back(message);
        available.push(i); // add index to available fifo
    }

}

/**
* return message idx to available 
*/
void tcNetworkInterface::ReturnMessage(unsigned int idx)
{
    available.push(idx);
    messageBuffer[idx].Reset();
}

void tcNetworkInterface::ReturnMessagesFromQueue(std::queue<unsigned int>& q)
{
    while (!q.empty())
    {
        ReturnMessage(q.front());
        q.pop();
    }
}

/**
* @return Pointer to message data if successful, 0 otherwise. messageSize
*    and messageId are set if return is successful.
*/
const unsigned char* tcNetworkInterface::ReceiveMessage(int connectionId, int& messageId, unsigned& messageSize, 
                                                        int protocol)
{
    tcConnectionData* connection = GetConnection(connectionId);
    if (connection == 0)
    {
        fprintf(stderr, "Error - Invalid connection id (%d) in tcNetworkInterface::ReceiveMessage\n", 
                connectionId);
        return 0;
    }

    std::queue<unsigned int> *readQueue = 0;

    if (protocol == TCP)
    {
        readQueue = &connection->readQueueTCP;
    }
    else if (protocol == UDP)
    {
        readQueue = &connection->readQueueUDP;
    }
    else
    {
        // wxASSERT(false);
        return 0;
    }

    if (readQueue->empty()) return 0;

    unsigned int idx = readQueue->front();
    tcMessage *message = GetMessage(idx);
    if (message == 0)
    {
        // wxASSERT(false);
        return 0;
    }
    else
    {
        // messageId = message->GetMessageId();
        // messageSize = message->GetMessageSize();
        readQueue->pop();
        return message->GetMessageData();
    }
}

void tcNetworkInterface::RouteUDP()    
{    
    static unsigned char buff[MAX_UDP_SIZE];
    unsigned int messageSize;

    messageSize = MAX_UDP_SIZE;

    if (!datagramSock) {
        std::cerr << "Error - RouteUDP() datagram socket not initialized" << std::endl;
        return;
    }
    
    int result =datagramSock->receive(buff, messageSize);
    
    
    if (result < 0) {

        return;
    }
    
    // Get the actual number of bytes received
    size_t readCount = static_cast<size_t>(result);
    
    // Create a peer identifier from the source address
    std::string peerName = Socket::addr2string(datagramSock->getLastSenderAddr());
    
    tcConnectionData *conn = GetConnection(peerName);
    if (conn == NULL)
    {
        // Create a new connection for this peer if it doesn't exist
        // This is a simplified approach - in a real implementation you might want to handle this differently
        std::cerr << "Warning - RouteUDP() peer " << peerName << " not found, creating temporary connection" << std::endl;
        return;
    }
    conn->ReadNextMessageUDP(readCount, buff);
}

/**
* Normally called from tcMultiplayerInterface, here to allow special disconnect messages
* to be sent to client before disconnect
*/
void tcNetworkInterface::SendChatText(int destination, const std::string& message)
{
    char buff[256];
    unsigned messageLength;

    int protocol = tcNetworkInterface::TCP;

    tcTextMessageHandler::CreateMessage(messageLength, (unsigned char*)buff, message, 255);

    // MSG_CHATTEXT == 1
    SendMessage(destination, 1, 
                messageLength, (unsigned char*)buff, protocol);
}


bool tcNetworkInterface::SendMessage(int connectionId, int messageId, unsigned messageSize, 
                                     const unsigned char *data, int protocol)
{
    tcConnectionData* connection = GetConnection(connectionId);
    if (connection == 0)
    {
        fprintf(stderr, "Error - Invalid connection id (%d) in tcNetworkInterface::SendMessage\n", 
                connectionId);
        return false;
    }

    if (protocol == TCP)
    {
        int bufferId = CheckoutMessage();
        if (bufferId < 0) 
        {
            std::cerr << "Error - Message buffer full, send message lost" << std::endl;
            return false;
        }
        tcMessage *message = GetMessage(bufferId);
        connection->SendTCP(bufferId);
        return true;
    }
    else if ((protocol == UDP)||(protocol == UDP_ACK))
    {
        int bufferId = CheckoutMessage();
        if (bufferId < 0) 
        {
            std::cerr << "Error - Message buffer full, send message lost" << std::endl;
            return false;
        }
        tcMessage *message = GetMessage(bufferId);
        // Note: Original code tried to use connection->SendUDP() which is not implemented
        // Actual message sending should be done through appropriate SocketUDP methods
        connection->SendUDP(bufferId);
        return true;
    }
    else
    {
        // wxASSERT(false);
        return false;
    }
}

/**
* Sets ping time associated with connection
*/
void tcNetworkInterface::SetPingTime(int connectionId, float ping_s)
{
    if (tcConnectionData* conn = GetConnection(connectionId))
    {
        conn->SetPingTime(ping_s);
    }
}


/** 
* Called regularly to poll socket methods. This is done this 
* way to avoid dependencies on the wxWindows event system to 
* make integration easier with non-wxWindows software.
*/
void tcNetworkInterface::Update()
{
    /*
    static unsigned lastUpdate = tcTime::Get()->Get30HzCount();

    if ((tcTime::Get()->Get30HzCount() - lastUpdate) < 15) return;
    lastUpdate = tcTime::Get()->Get30HzCount();
    */
    if (isServer)
    {
        UpdateServer();
    }
    else
    {
        UpdateClient();
    }
}

void tcNetworkInterface::UpdateClient()
{
    if (connectState == NOT_CONNECTED)
    {
        return;
    }
    if (connectState == IS_CONNECTING)
    {
        UpdateClientConnection();
        return;
    }
    
    RemoveDeadConnections();

    UpdateConnections();

}

void tcNetworkInterface::UpdateClientConnection()
{
    if (connectState != IS_CONNECTING) return;
    
    bool timedOut = tcTime::Get()->GetUpdated30HzCount() - connectionStartTime > 30*5;
    if (timedOut)
    {
        connectState = NOT_CONNECTED;
        std::cerr << "Error - Connection timed out." << std::endl;
        return;
    }
    
    // Check if connection is established
    if (clientSock->isOpen()) {
        connectState = IS_CONNECTED; // success
        AddConnection(clientSock);
        return;
    }
    
    // For non-blocking connect, check for errors to determine connection status
    if (clientSock->lastError() != 0 && clientSock->lastError() != EINPROGRESS && clientSock->lastError() != EWOULDBLOCK) {
        connectState = NOT_CONNECTED;
        std::cerr << "Error - Connection failed with error: " << clientSock->lastError() << std::endl;
        return;
    }
    
    // Still connecting, do nothing
}

void tcNetworkInterface::UpdateConnections()
{
    std::map<int, tcConnectionData*>::iterator iter = connectionData.begin();
    
    for ( ; iter != connectionData.end(); ++iter)
    {
        iter->second->Update(); 
    }
    
    // Handle UDP traffic
    RouteUDP();
}



void tcNetworkInterface::UpdateServer()
{
    static unsigned lastBadCheck = 0;
    
    unsigned t = tcTime::Get()->Get30HzCount();

    RemoveDeadConnections();

    if (t - lastBadCheck > 150)
    {
        RemoveBadConnections();
        lastBadCheck = t;
    }


    UpdateConnections();


    const SOCKET tcp_server_fd(serverSock->returnSocket());
    const SOCKET udp_server_fd(datagramSock->returnSocket());
    int max_fd = 0; // not used for _WIN32

    int result = 0;	// Wait for an incoming message.
    while (!result)
    {
        int test;

        FD_ZERO(&fdset);
        FD_SET(tcp_server_fd, &fdset);
        FD_SET(udp_server_fd, &fdset);

        //  将所有客户端连接加入监控
        SOCKET current_max_fd = std::max(tcp_server_fd, udp_server_fd);
        // for (SocketTCPClient* sock : socketTCPClients) {
        //     SOCKET fd = sock->returnSocket();
        //     FD_SET(fd, &fdset);
        //     if (fd > current_max_fd)
        //         current_max_fd = fd;
        // }
        for (auto kv:connectionData) {
            SocketTCPClient* sock=kv.second->GetSocket();
            if(sock)
            {
                SOCKET fd = sock->returnSocket();
                FD_SET(fd, &fdset);
                if (fd > current_max_fd)
                    current_max_fd = fd;
            }
        }
#ifndef _WIN32
        max_fd = std::max(max_fd, std::max(tcp_server_fd, udp_server_fd));
#endif

        timeval		timeout;
        timeout.tv_sec= 0;
        timeout.tv_usec= 50000L;
#ifdef _WIN32
        result = select(0, &fdset, NULL, NULL, &timeout);
        if (result < 0) {
#ifdef _WIN32
            if (WSAGetLastError() == WSAEINTR)
#else
            if (errno == EINTR)
#endif
            {
                throw NetworkSignal("EINTR on select");
            }
            else {
                throw NetworkError("Unexpected errno on select");
            }
        }
#else
        result = select(max_fd+1, &fdset, NULL, NULL, &timeout);
        if (result < 0) {
#ifdef _WIN32
            if (WSAGetLastError() == WSAEINTR)
#else
            if (errno == EINTR)
#endif
            {
                throw NetworkSignal("EINTR on select");
            }
            else {
                throw NetworkError("Unexpected errno on select");
            }
        }
#endif

    }

    for (auto kv:connectionData) {
        {
            SocketTCPClient* link=kv.second->GetSocket();
            //获得准备好的
            if (link != NULL) {
                try {
                    do {
                        //从SocketTCPClient转为connectionData
                        tcConnectionData * conn =GetConnection(link);
                        if(conn)
                        {
                            conn->ReadNextMessageTCP();
                        }
                    } while (link->isDataReady());
                }
                catch (NetworkError &e) {
                    if (!e._reason.empty())
                        std::cout << "Catching Network Error, reason : "<<e._reason<< std::endl;
                    else
                        std::cout << "RTIG dropping client connection " << link->returnSocket()
                                  << '.' << std::endl ;
                    link->close();
                    link = NULL ;
                }
            }
        }

        if (FD_ISSET(tcp_server_fd, &fdset))//来了新的TCP连接
        {
            SocketTCPClient *newLink = serverSock->accept();
            AddConnection(newLink);
            max_fd = std::max<decltype(max_fd)>(max_fd, newLink->returnSocket());
        }
        else if (FD_ISSET(udp_server_fd, &fdset)) {//来了新的UDP连接 直接读了
            tcMessage tcMessage;
            datagramSock->receive(tcMessage.GetMessageData(),tcMessage::BUFFER_SIZE);
        }


    }
}


tcNetworkInterface::tcNetworkInterface()
    :connectionIndex(1),
    isServer(false),
    connectionStartTime(0),
    hostAddress(0),
    clientSock(nullptr),
    serverSock(nullptr),
    datagramSock(nullptr)
{
    tcConnectionData::networkInterface = this;
    connectState = NOT_CONNECTED;
    ResetMessageBuffer();
}

tcNetworkInterface::~tcNetworkInterface()
{
    Clear();
}

END_NAMESPACE
