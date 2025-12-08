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

#ifndef CERTI_SOCKET_TCP_SERVER_HH
#define CERTI_SOCKET_TCP_SERVER_HH

#include "SocketTCPBase.hh"
#include "SocketTCPClient.hh"

namespace network {

/** This TCP socket implementation is specialized for server operations.
  It provides methods for binding to ports, listening for connections,
  and accepting client connections.
*/
class SocketTCPServer : public SocketTCPBase
{
public :
    SocketTCPServer();
    virtual ~SocketTCPServer();
    
    virtual void close();
    virtual bool isOpen();
    virtual int send(const unsigned char *, size_t);
    virtual int receive(void *buffer,size_t buf_size) override;
    virtual bool isDataReady() const;
    virtual in_port_t getPort() const override;
    virtual in_addr_t getAddr() const override;
    virtual SOCKET returnSocket();
    virtual int lastError() const override;

    void createServer(in_port_t port = 0, in_addr_t addr = INADDR_ANY);
    
    SocketTCPClient* accept();
    
    SocketTCPServer &operator=(SocketTCPServer &theSocket);

protected:
    int listen(unsigned long howMuch=5);
    int bind(in_port_t port=0, in_addr_t addr=INADDR_ANY);
    int open();

private:
    void setPort(in_port_t port);

    SOCKET _socket_tcp;
    bool _est_init_tcp;
    struct sockaddr_in _sockIn;
    int _lastError;
};

} // namespace network

#endif // CERTI_SOCKET_TCP_SERVER_HH