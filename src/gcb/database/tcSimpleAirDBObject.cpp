/**
**  @file tcSimpleAirDBObject.cpp
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

//#include "stdwx.h"

#if _MSC_VER > 1000
#pragma warning(disable:4786) // suppress warning for STL bug in VC6, see Q167355 in the MSDN Library.
#endif

#include "tcSimpleAirDBObject.h"
#include "tcAirObject.h"
#include "tcHeloObject.h"
#ifdef _DEBUG
#define new DEBUG_NEW
#endif



namespace database
{


tcSimpleAirDBObject::tcSimpleAirDBObject() : tcAirDBObject()
{
}

tcSimpleAirDBObject::tcSimpleAirDBObject(const tcSimpleAirDBObject& obj)
: tcAirDBObject(obj)
{
}

tcSimpleAirDBObject::~tcSimpleAirDBObject() 
{
}

 std::shared_ptr<tcGameObject> tcSimpleAirDBObject::CreateGameObject()
{
    /* these types are defined in tcDatabase.h */
    switch (this->mnModelType)
    {
    case MTYPE_FIXEDWING:
    case MTYPE_AIR:
    {
        auto obj= std::make_shared<tcAirObject>(dynamic_pointer_cast<tcSimpleAirDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;
    case MTYPE_HELO:
    {
        auto obj= std::make_shared< tcHeloObject>(dynamic_pointer_cast<tcSimpleAirDBObject>(tcDatabaseObject::shared_from_this()));
        obj->Construct();
        return obj;
    }
        break;
    default:
        fprintf(stderr, "tcSimState::CreateGameObject - "
                        "Invalid model type for Simple Air DB obj (%d)\n", this->mnModelType);
        return nullptr;
    }
}

void tcSimpleAirDBObject::WritePythonValue(std::string &valueString) const
{
    tcAirDBObject::WritePythonValue(valueString);
}

void tcSimpleAirDBObject::WritePython(std::string &valueString) const
{
    valueString+="import pygcb\n";
    valueString+="def CreateDBObject():\n";
    valueString+="    dbObj=pygcb.tcSimpleAirDBObject()\n";
    WritePythonValue(valueString);
    valueString+="    dbObj.CalculateParams()\n";
    valueString+="    return dbObj\n";
}

}
