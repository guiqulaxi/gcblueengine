/**
**  @file tcPlatformDBInterface.h
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

#ifndef __tcPlatformDBInterface_h__
#define __tcPlatformDBInterface_h__

#if _MSC_VER > 1000
#pragma once
#endif

#include "tcPlatformDBObject.h"
#include "tcStringArray.h"

#include <pybind11-global/pybind11/pybind11.h>
#include <pybind11-global/pybind11/eval.h>
#include <pybind11-global/pybind11/embed.h>


namespace py = pybind11;
using namespace py;

namespace scriptinterface {
/**
    * Database interface class for Python - provides access to platform database objects
    * This class is specifically designed for querying platform database objects by name
    */
class tcPlatformDBInterface
{
public:
    // static void InitPythonClasses();
    // static py::object InitPythonDBInterface();
    static py::object GetPlatformDBInterface();

    /// Constructor with platform class name
    tcPlatformDBInterface();
    ~tcPlatformDBInterface();

    // Database query methods
    bool IsValid() const;
    std::string GetClassName() const;
    void SetClassName(const std::string &);
    std::shared_ptr<database::tcPlatformDBObject> GetPlatformDBObject() const;

    // Static database queries
    static bool PlatformDBObjectExists(const std::string& className);
    static std::shared_ptr<database::tcPlatformDBObject> GetPlatformObject(const std::string& className);

private:
    std::shared_ptr<database::tcPlatformDBObject> databaseObject;
    std::string className;


};
}

#endif
