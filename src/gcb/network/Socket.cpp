#include "Socket.hh"

namespace network
{
#ifdef _WIN32
    int Socket::winsockInits = 0;
    bool Socket::winsockStartup()
    {
        WORD wVersionRequested;
        WSADATA wsaData;
        int lError;

        if (winsockInits > 0)
        {
            winsockInits++;
            return true;
        }
        else if (winsockInits < 0)
        {
            return false;
        }

        wVersionRequested = MAKEWORD(2, 0);
        lError = WSAStartup(wVersionRequested, &wsaData);
        if (lError != 0)
        {
            winsockInits = -1;
            return false;
        }

        if (LOBYTE(wsaData.wVersion) != 2 || HIBYTE(wsaData.wVersion) != 0)
        { // Tell the user that we couldn't find a usable WinSock DLL.
            WSACleanup();
            winsockInits = -1;
            return false;
        }

        winsockInits = 1;
        return true;
    }

    void Socket::winsockShutdown()
    {
        winsockInits--;
        if (winsockInits == 0)
            WSACleanup();
    }
    bool Socket::winsockInitialized() { return (winsockInits > 0); }

#endif
    /**
     * This function builds a string which represents
     * the provided IPv4 address as a "w.x.y.z".
     * @param[in] addr, the IPv4 address
     * @return the string "w.x.y.z"
     */
     const std::string Socket::addr2string(in_addr_t addr)
    {
        typedef union
        {
            uint32_t addr;
            uint8_t parts[4];
        } addr_union_t;
        std::stringstream msg;

        addr_union_t uaddr;
        uaddr.addr = (uint32_t)ntohl((uint32_t)(addr));
        msg << "" << static_cast<int>(uaddr.parts[3])
            << "." << static_cast<int>(uaddr.parts[2])
            << "." << static_cast<int>(uaddr.parts[1])
            << "." << static_cast<int>(uaddr.parts[0]);
        return msg.str();
    }
/**
     * This function builds an IP address out of an hostname.
     */
     void Socket::host2addr(const std::string &hostName, in_addr_t &addr)
    {
        addr = 0;
        // get host information from server name
        // this may perform DNS query
        struct hostent *hptr = gethostbyname(hostName.c_str());
        // FIXME we should probably use getaddrinfo instead
        if (NULL == hptr)
        {
            throw NetworkError(std::string("") +
                               +"gethostbyname gave NULL answer for hostname <" + hostName + "> with error <" + strerror(errno) + ">");
        }
        memcpy((void *)&addr, (void *)hptr->h_addr, hptr->h_length);
        ;
    }

    /**
         * Get the IP address corresponding to the first interface of the host.
         */
     void Socket::getMyFirstIPaddr(in_addr_t &addr)
    {
        char name[MAXHOSTNAMELEN + 1];
        /* FIXME gethostname is deprecated
             * we should use getnameinfo and getaddrinfo
             */
        if (0 != gethostname(name, 1024))
        {
            throw NetworkError(std::string("") + "gethostname FAILED" + " with error <" + strerror(errno) + ">");
        }
        Socket::host2addr(name, addr);
    }
} // namespace certi
