// ----------------------------------------------------------------------------
// CERTI - HLA RunTime Infrastructure
// Copyright (C) 2002-2005  ONERA
//
// This program is free software ; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public License
// as published by the Free Software Foundation ; either version 2 of
// the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY ; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this program ; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
// USA
//
// ----------------------------------------------------------------------------

#include "network/SocketTCPServer.hh"

#include <iostream>
#include <cassert>
#include <cerrno>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#ifndef _WIN32
#include <unistd.h>
#endif

using std::cout ;
using std::endl ;

namespace network {

// ----------------------------------------------------------------------------
SocketTCPServer::SocketTCPServer()
{
    _socket_tcp    = 0;
    _est_init_tcp  = false;
    _lastError     = 0;

    SentBytesCount = 0;
    RcvdBytesCount = 0;

#ifdef SOCKTCP_BUFFER_LENGTH
    RBLength = 0 ;
#endif
}

// ----------------------------------------------------------------------------
SocketTCPServer::~SocketTCPServer()
{// Fermeture
    if (_est_init_tcp)
        close();

#ifdef RTI_PRINTS_STATISTICS
    cout << " TCP Server Socket " ;
    cout.width(2);
    cout << _socket_tcp << " : total = " ;
    cout.width(9);
    cout << SentBytesCount << " Bytes sent " << endl ;
    cout << " TCP Server Socket " ;
    cout.width(2);
    cout << _socket_tcp << " : total = " ;
    cout.width(9);
    cout << RcvdBytesCount << " Bytes received" << endl ;
#endif
}

// ----------------------------------------------------------------------------
int SocketTCPServer::bind(in_port_t port, in_addr_t addr)
{
    long Length, Result ;

    assert(!_est_init_tcp);

    memset(&_sockIn, 0, sizeof(_sockIn));

    _sockIn.sin_family = AF_INET ;
    _sockIn.sin_addr.s_addr = addr ;
    _sockIn.sin_port = htons(port);

    Length = sizeof(_sockIn);

    int on = 1 ;
    /* Bind even if the port is in the TIME_WAIT. If the port is busy,
     * An error will be reported if the port is busy with another state. */
    if (setsockopt(_socket_tcp,
                   SOL_SOCKET, SO_REUSEADDR, (char *)&on, sizeof(on)))
        perror("setsockopt");

    Result = ::bind(_socket_tcp, (sockaddr *)&_sockIn, Length);

    if (Result != 0) {
        _lastError = errno;
        perror("bind");
        return 0;
    }
    else
        return 1;
}

// ----------------------------------------------------------------------------
void SocketTCPServer::createServer(in_port_t port, in_addr_t addr)
{
    assert(!_est_init_tcp);

    if (!open())
    {
        _lastError = errno;
        throw NetworkError(std::string("")
                           +"Cannot open port <" + std::to_string( port)
                           +"> on addr <" + addr2string(addr)
                           +"> : error =" + strerror(errno));
    }

    if (!bind(port, addr))
    {
        _lastError = errno;
        throw NetworkError(std::string("")
                           +"Cannot bind port <" +  std::to_string( port)
                           +"> on addr <" + addr2string(addr)
                           +"> : error =" + strerror(errno));
    }

    if (!listen(MAX_BACKLOG))
    {
        _lastError = errno;
        throw NetworkError(std::string("")
                           +"Cannot listen port <"  +std::to_string( port)
                           +"> on addr <" + addr2string(addr)
                           + "> : error =" + strerror(errno));
    }

    _est_init_tcp = true ;
}

// ----------------------------------------------------------------------------
SocketTCPClient* SocketTCPServer::accept()
{
    struct protoent *TCPent ;
    int optval = 1 ;

#ifdef _WIN32
    int l;
#else
    socklen_t l;
#endif

    assert(_est_init_tcp);

    l = sizeof(_sockIn);

    SOCKET new_socket = ::accept(_socket_tcp, (sockaddr*)&_sockIn, &l);
    if (new_socket < 0)
    {
        _lastError = errno;
        // No pending connections
        return nullptr;
    }

    // Create a new client socket object to wrap the accepted connection
    SocketTCPClient* client = new SocketTCPClient();
    
    // Set the TCP_NODELAY option(Server Side)
    TCPent = getprotobyname("tcp");
    if (TCPent == NULL)
    {
        cout << "Unable to retrieve TCP protocol number." << endl ;
        _lastError = errno;
        delete client;
        return nullptr;
    }

    if (setsockopt(new_socket,
                   TCPent->p_proto,
                   TCP_NODELAY,
                   (char *) &optval,
                   sizeof(optval)))
    {
        cout << "Error while calling setsockopt." << endl ;
        _lastError = errno;
        delete client;
        return nullptr;
    }

    // TODO: Properly initialize the client socket with the new connection
    // This would require access to the client's private members or a special constructor
    // For now, we're just returning a basic client object
    
    return client;
}

// ----------------------------------------------------------------------------
int SocketTCPServer::send(const unsigned char *buffer, size_t size)
{
    long total_sent = 0 ;
    long expected_size = size ;

    assert(_est_init_tcp);


    while (total_sent < expected_size)
    {
#ifdef _WIN32
        int sent = ::send(_socket_tcp, (char*) buffer + total_sent, expected_size - total_sent, 0);
#else
        int sent = ::send(_socket_tcp, buffer + total_sent, expected_size - total_sent, 0);
#endif

        if (sent < 0)
        {

#ifdef _WIN32
            if(WSAGetLastError() == WSAEINTR)
#else
            if(errno == EINTR)
#endif
                throw NetworkSignal("");
            else
            {
                _lastError = errno;
                perror("TCP Socket(EmettreTCP) ");
                throw NetworkError("Error while sending TCP message.");
            }
        }

        if (sent == 0)
        {
            _lastError = errno;
            throw NetworkError("Could not send any data on TCP socket.");
        }

        total_sent += sent ;
    }

    SentBytesCount += total_sent ;
    
    return total_sent; // Return the number of bytes sent
}

// ----------------------------------------------------------------------------
void SocketTCPServer::close()
{
    if (_est_init_tcp)
    {
#ifdef _WIN32
        ::closesocket(_socket_tcp);
#else
        ::close(_socket_tcp);
#endif
        _est_init_tcp = false ;
    }
}

// ----------------------------------------------------------------------------
bool SocketTCPServer::isOpen()
{
    return _est_init_tcp;
}

// ----------------------------------------------------------------------------
int SocketTCPServer::listen(unsigned long howMuch)
{
    assert(!_est_init_tcp);

    int result = ::listen(_socket_tcp, howMuch);
    if (result < 0) {
        _lastError = errno;
        return 0;
    }
    return 1;
}

// ----------------------------------------------------------------------------
in_addr_t SocketTCPServer::getAddr() const
{
    return(_sockIn.sin_addr.s_addr);
}

// ----------------------------------------------------------------------------
in_port_t SocketTCPServer::getPort() const
{
    return _sockIn.sin_port ;
}

// ----------------------------------------------------------------------------
/*! Return RTI_TRUE if any data as already been read from the system socket
  and is waiting in the internal buffer, else RTI_FALSE.
*/
bool SocketTCPServer::isDataReady() const
{
#ifdef SOCKTCP_BUFFER_LENGTH
    return RBLength > 0 ;
#else
    return false ;
#endif
}

// ----------------------------------------------------------------------------
int SocketTCPServer::open()
{
    _socket_tcp = socket(AF_INET,SOCK_STREAM,0);
    if (_socket_tcp < 0) {
        _lastError = errno;
        return 0;
    }
    return 1;
}

// ----------------------------------------------------------------------------
SocketTCPServer & SocketTCPServer::operator=(SocketTCPServer &theSocket)
{
    _sockIn.sin_addr.s_addr=theSocket.getAddr();
    _sockIn.sin_port =theSocket.getPort();
    _socket_tcp =theSocket.returnSocket();

    return(*this);
}

// ----------------------------------------------------------------------------
int SocketTCPServer::receive(void *buffer,size_t buf_size)
{
    // G.Out(pdGendoc,"enter SocketTCP::receive");
    assert(_est_init_tcp);

    int nReceived = 0 ;
#ifdef SOCKTCP_BUFFER_LENGTH
        nReceived = recv(_socket_tcp,
                         ReadBuffer + RBLength,
                         SOCKTCP_BUFFER_LENGTH - RBLength,
                         0);
#else
        nReceived = recv(_socket_tcp,
                         (char *) buffer ,
                         buf_size ,
                         0);
#endif

        if (nReceived < 0)
        {
#ifdef _WIN32
            if(WSAGetLastError() == WSAEINTR)
#else
            if(errno == EINTR)
#endif
                throw NetworkSignal("");
            else
            {
                _lastError = errno;
                perror("TCP Socket(RecevoirTCP) ");
                throw NetworkError("Error while receiving TCP message.");
            }
        }

        if (nReceived == 0)
        {
            _lastError = errno;
            throw NetworkError("Connection closed by client.");
        }

        RcvdBytesCount += nReceived ;


#ifdef SOCKTCP_BUFFER_LENGTH
    memcpy(buffer, (void *) ReadBuffer, size);
    memmove((void *) ReadBuffer, (void *)(ReadBuffer + size), RBLength - size);
    RBLength -= size ;
#endif
    // G.Out(pdGendoc,"exit  SocketTCP::receive");
    return nReceived;
}

// ----------------------------------------------------------------------------
SOCKET SocketTCPServer::returnSocket()
{ 
    return _socket_tcp ;
}

// ----------------------------------------------------------------------------
//! Change the port value.
void SocketTCPServer::setPort(in_port_t port)
{
    _sockIn.sin_port=port ;
}

// ----------------------------------------------------------------------------
int SocketTCPServer::lastError() const
{
    return _lastError;
}

} // namespace network