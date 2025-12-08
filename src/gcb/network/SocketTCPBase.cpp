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

#include "network/SocketTCPBase.hh"

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
int SocketTCPBase::timeoutTCP(int sec, int usec)
{
    struct timeval time_out ;
    time_out.tv_sec = sec ;
    time_out.tv_usec = usec ;

    // Note: This is a simplified implementation. In a real implementation,
    // we would need access to the socket file descriptor.
    // This method might need to be restructured depending on how it's used.

    cout << "Warning: timeoutTCP is not fully implemented in base class" << endl;
    return 0;
}

} // namespace network