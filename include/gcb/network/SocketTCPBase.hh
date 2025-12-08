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
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
// ----------------------------------------------------------------------------

#ifndef CERTI_SOCKET_TCP_BASE_HH
#define CERTI_SOCKET_TCP_BASE_HH

#include "Socket.hh"

// This is the read buffer of TCP sockets. It must be at least as long
// as the longest data ever received by a socket.
// If the next line is commented out, no buffer will be used at all.
//#define SOCKTCP_BUFFER_LENGTH 4096

namespace network {

/** This is the base class for TCP socket implementations.
  It defines the common interface and shared functionality for both
  client and server TCP sockets.
*/
class SocketTCPBase : public Socket
{
public :
    virtual ~SocketTCPBase(){};
    
    virtual void close() = 0;
    virtual bool isOpen() = 0;
    virtual int send(const unsigned char *, size_t) = 0;
    virtual int receive(void *buffer,size_t buf_size) = 0;
    virtual bool isDataReady() const = 0;
    virtual in_port_t getPort() const = 0;
    virtual in_addr_t getAddr() const = 0;
    virtual SOCKET returnSocket() = 0;
    virtual int lastError() const = 0;



protected:
    SocketTCPBase(){};
    
    int timeoutTCP(int, int);

    size_t SentBytesCount;
    size_t RcvdBytesCount;
#ifdef SOCKTCP_BUFFER_LENGTH
    // This class can use a buffer to reduce the number of systems calls
    // when reading a lot of small amouts of data. Each time a Receive
    // is made, it will try to read SOCKTCP_BUFFER_LENGTH
    char ReadBuffer[SOCKTCP_BUFFER_LENGTH] ;
    unsigned long RBLength ;
#endif
};

} // namespace network

#endif // CERTI_SOCKET_TCP_BASE_HH
