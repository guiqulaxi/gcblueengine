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

#include "network/SocketUDP.hh"
#include <cstdlib>
#include <cstring>
#include <cstdio>

#include <iostream>
#include <assert.h>
#include <errno.h>

using std::cout;
using std::endl;

namespace network
{

    // ----------------------------------------------------------------------------
    void
    SocketUDP::attach(int opend_socket, unsigned long address, unsigned int port)
    {
        assert(!_est_init_udp);

        PhysicalLink = false;

        _socket_udp = opend_socket;
        // Building Distant Address
        memset((struct sockaddr_in *)&sock_distant, 0, sizeof(struct sockaddr_in));

        sock_distant.sin_addr.s_addr = htonl(address);
        sock_distant.sin_family = AF_INET;
        sock_distant.sin_port = port;

        _est_init_udp = true;
    }
    void SocketUDP::setDestination(in_addr_t ip, in_port_t port)
    {
        assert(_est_init_udp);

        PhysicalLink = false;
        // Building Distant Address
        memset(&sock_distant, 0, sizeof(sock_distant));

        sock_distant.sin_addr.s_addr = ip; // 已经是网络字节序
        sock_distant.sin_family = AF_INET;
        sock_distant.sin_port = htons(port); // 主机字节序转网络字节序

        _est_init_udp = true;
    }

    // ----------------------------------------------------------------------------
    int
    SocketUDP::bind()
    {
        assert(!_est_init_udp);

        long result = ::bind(_socket_udp, (sockaddr *)&sock_local,
                             sizeof(struct sockaddr_in));

        if (result != 0)
        {
            _lastError = errno;
            return 0;
        }

        return 1;
    }



    // ----------------------------------------------------------------------------
    //! create an UDP server.
    void
    SocketUDP::createServer(unsigned int port, in_addr_t addr)
    {
        assert(!_est_init_udp);

        // Building Local Address
        memset((struct sockaddr_in *)&sock_local, 0, sizeof(struct sockaddr_in));

        sock_local.sin_addr.s_addr = addr;
        sock_local.sin_family = AF_INET;
        sock_local.sin_port = htons((u_short)port);

        if (!open())
        {
            _lastError = errno;
            throw NetworkError("Cannot open UDP Socket" + std::string(strerror(errno)));
        }

        if (!bind())
        {
            _lastError = errno;
            throw NetworkError("Cannot bind UDP Socket" + std::string(strerror(errno)));
        }

        _est_init_udp = true;
    }

    // ----------------------------------------------------------------------------
    SocketUDP::SocketUDP()
    {
        _lastError = 0;

        PhysicalLink = true;

        _socket_udp = 0;

        memset(&sock_local, 0, sizeof(struct sockaddr_in));
        memset(&sock_source, 0, sizeof(struct sockaddr_in));

        memset(&sock_distant, 0, sizeof(struct sockaddr_in));
        hp_distant = NULL;

        _sock_local_length = 0;
        _est_init_udp = false;

        SentBytesCount = 0;
        RcvdBytesCount = 0;

#ifdef _WIN32 // netDot
        winsockStartup();
#endif
    }

    // ----------------------------------------------------------------------------
    SocketUDP::~SocketUDP()
    {
        // Closing the socket
        if (_est_init_udp)
            close();

#ifdef _WIN32 // netDot
        winsockShutdown();
#endif

#ifdef RTI_PRINTS_STATISTICS
        cout << " UDP Socket ";
        cout.width(2);
        cout << _socket_udp << " : total = ";
        cout.width(9);
        cout << SentBytesCount << " Bytes sent " << endl;
        cout << " UDP Socket ";
        cout.width(2);
        cout << _socket_udp << " : total = ";
        cout.width(9);
        cout << RcvdBytesCount << " Bytes received" << endl;
#endif
    }

    // ----------------------------------------------------------------------------
    int SocketUDP::send(const unsigned char *Message, size_t Size)
    {

        assert(_est_init_udp);

        int sent = sendto(_socket_udp, (char *)Message, Size, 0,
                          (struct sockaddr *)&sock_distant, sizeof(sock_distant));
        if (sent < 0)
        {
            _lastError = errno;
            perror("Sendto");
            throw NetworkError("cannot sendto");
        };
        SentBytesCount += sent;
        return sent;
    }

    // ----------------------------------------------------------------------------
    void
    SocketUDP::close()
    {
        if (_est_init_udp)
        {
            _est_init_udp = false;
            if (PhysicalLink)
            {
#ifdef _WIN32 // netDot
                ::closesocket(_socket_udp);
#else
                ::close(_socket_udp);
#endif
            }
        }
    }

    // ----------------------------------------------------------------------------
    in_addr_t SocketUDP::getLastSenderAddr() const   // 返回发送方IP字符串
    {
        return sock_source.sin_addr.s_addr;

    }
    unsigned int SocketUDP::getLastSenderPort() const
    {
        return ntohs(sock_source.sin_port);
    } // 返回发送方端口号
    in_port_t SocketUDP::getPort() const
    {
        return sock_local.sin_port;
    }
    in_addr_t SocketUDP::getAddr() const
    {
        return (sock_local.sin_addr.s_addr);
    }

    // ----------------------------------------------------------------------------
    /*! Return whether any data as already been read from the system socket
      and is waiting in the internal buffer.
    */
    bool
    SocketUDP::isDataReady() const
    {
        return RcvdBytesCount > 0;
    }

    // ----------------------------------------------------------------------------
    int SocketUDP::lastError() const
    {
        return _lastError;
    }

    // ----------------------------------------------------------------------------
    int SocketUDP::open()
    {
#ifdef _WIN32 // netDot
        assert(Socket::winsockInitialized());
#endif

        _socket_udp = socket(AF_INET, SOCK_DGRAM, 0);
        if (_socket_udp < 0)
        {
            _lastError = errno;
            return 0;
        }
        return 1;
    }

    // ----------------------------------------------------------------------------
    int SocketUDP::receive(void *buffer, size_t buf_size)
    {
#ifdef _WIN32 // netDot
        int taille = sizeof(struct sockaddr_in);
#else
        socklen_t taille = sizeof(struct sockaddr_in);
#endif

        int CR;

        assert(_est_init_udp);

        CR = recvfrom(_socket_udp,
                      (char *)buffer, buf_size, 0,
                      (struct sockaddr *)&sock_source, &taille);
        // HPUX:(struct sockaddr *)&sock_source, (int*) &taille);
        if (CR <= 0)
        {
            _lastError = errno;
            perror("Recvfrom");
            throw NetworkError("cannot recvfrom");
        }
        else
        {
            RcvdBytesCount += CR;
        }
        return CR;
    }

// ----------------------------------------------------------------------------
#ifdef _WIN32
    SOCKET SocketUDP::returnSocket()
#else
    int SocketUDP::returnSocket()
#endif
    {
        return _socket_udp;
    }

    // ----------------------------------------------------------------------------
    void
    SocketUDP::setPort(unsigned int port)
    {
        sock_local.sin_port = port;
    }

} // namespace certi
