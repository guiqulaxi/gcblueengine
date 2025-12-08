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

#ifndef CERTI_SOCKET_HH
#define CERTI_SOCKET_HH

#include "Exception.hh"
#include <cstdint>
#ifdef _WIN32
# ifndef NOMINMAX
# define NOMINMAX
# endif
# include <winsock2.h>
# include <ws2tcpip.h>
typedef u_long         in_addr_t;
typedef unsigned short in_port_t;
#else
# include <sys/types.h>
# include <sys/socket.h>
# include <netinet/in.h>
# include <netinet/tcp.h>
# include <netdb.h>
typedef int SOCKET;
#include <unistd.h>
#endif

#ifndef MAXHOSTNAMELEN
#define MAXHOSTNAMELEN 4096
#endif

#include <cstring>
#include <cerrno>
#include <string>
#include <sstream>

const int MAX_BACKLOG = 256;

namespace network
{

class Socket
{
public:
    virtual ~Socket() {};
#ifdef _WIN32
    static bool winsockStartup();

    static void winsockShutdown();
    static bool winsockInitialized();
#endif

    virtual int send(const unsigned char *, size_t) = 0;
    virtual int receive(void *buffer, size_t buf_size) = 0;
    virtual void close() = 0;

    // This method may be used for implementation using Read Buffers,
    // because in that case 'select' system calls are not trustworthy.
    // See Important Note in SocketTCP.hh
    virtual bool isDataReady() const = 0;

    virtual SOCKET returnSocket() = 0;

    virtual in_addr_t getAddr() const = 0;

    virtual in_port_t getPort() const = 0;
    virtual int lastError() const = 0;

    /**
     * This function builds a string which represents
     * the provided IPv4 address as a "w.x.y.z".
     * @param[in] addr, the IPv4 address
     * @return the string "w.x.y.z"
     */
    static const std::string addr2string(in_addr_t addr);

    /**
     * This function builds an IP address out of an hostname.
     */
    static void host2addr(const std::string &hostName, in_addr_t &addr);

    /**
         * Get the IP address corresponding to the first interface of the host.
         */
    static void getMyFirstIPaddr(in_addr_t &addr);

private:
#ifdef _WIN32
    static int winsockInits;
#endif
};


} // namespace certi

#endif // CERTI_SOCKET_HH
