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

#ifndef CERTI_SOCKET_UDP_HH
#define CERTI_SOCKET_UDP_HH

#include "Socket.hh"

#define BUFFER_MAXSIZE 2000

namespace network {

class  SocketUDP : public Socket
{
public :
	SocketUDP();
	virtual ~SocketUDP();

	// Socket
    virtual int  send(const unsigned char *, size_t);

    virtual int receive(void *buffer,size_t buf_size) override;

	virtual bool isDataReady() const ;
	virtual int lastError() const override;

	SOCKET returnSocket();

	virtual void close();


    void createServer(unsigned int port, in_addr_t addr = INADDR_ANY);

    void attach(int opend_socket, unsigned long address, unsigned int port);

	void setDestination( in_addr_t ip, in_port_t port);

    in_port_t getPort() const override;
    in_addr_t getAddr() const override;
	// 添加：获取最近一次接收到的数据包的发送方信息
    in_addr_t getLastSenderAddr() const;   // 返回发送方IP字符串
    unsigned int getLastSenderPort() const; // 返回发送方端口号
private:
	void setPort(unsigned int port);

	int bind();
	int open();

    bool PhysicalLink ; ///< tag indicating physical or logical link

	SOCKET _socket_udp;
	struct sockaddr_in sock_local ;

	struct sockaddr_in sock_source ;

	struct sockaddr_in sock_distant ;
	struct hostent * hp_distant ;

	int _sock_local_length ;
	bool _est_init_udp ;

    size_t SentBytesCount ;
    size_t RcvdBytesCount ;
    
    int _lastError;

};

} // namespace certi

#endif // CERTI_SOCKET_UDP_HH
