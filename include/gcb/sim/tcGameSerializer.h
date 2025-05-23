/** 
**  @file tcGameSerializer.h 
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
#ifndef _GAMESERIALIZER_H_
#define _GAMESERIALIZER_H_

#if _MSC_VER > 1000
#pragma once
#endif


class tcSimState;
class tcGameStream;
//class tcTacticalMapView;
//class tcWorldMapView;
//class wxXmlDocument;
#include "tinyxml2.h"
// using namespace tinyxml2;
class tcGameSerializer
{
public:
    
    void LoadFromBinary(const char* fileName);
    void SaveToBinary(const char* fileName);

//    void SaveToXml(wxXmlDocument& doc);
    void SaveToXml(tinyxml2::XMLDocument& doc);

//    static void AttachMapViews(tcTacticalMapView* tactical, tcWorldMapView* world);

    tcGameSerializer();
    virtual ~tcGameSerializer();

private:
    bool LoadSimObjects(tcSimState* simState, tcGameStream& stream);
    void SaveSimObjects(tcSimState* simState, tcGameStream& stream);

    bool LoadSimOther(tcSimState* simState, tcGameStream& stream);
    void SaveSimOther(tcSimState* simState, tcGameStream& stream);

//    bool LoadMapView(tcGameStream& stream);
//    void SaveMapView(tcGameStream& stream);

    bool LoadHookInfo(tcGameStream& stream);
    void SaveHookInfo(tcGameStream& stream);

    const int currentVersion;

//    static tcTacticalMapView* tacticalMap;
//    static tcWorldMapView* worldMap;
};

#endif
