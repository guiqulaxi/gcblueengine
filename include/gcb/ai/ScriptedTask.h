/**
**  @file ScriptedTask.h
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

#ifndef _SCRIPTEDTASK_H_
#define _SCRIPTEDTASK_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include "ai/Task.h"

#include <map>
#include <string>
#include <vector>

class tcGameStream;

namespace ai
{

class Blackboard;

/**
* Task that is scripted through Python
*/
class ScriptedTask : public Task
{
public:
    const std::string& GetMemoryText(const std::string& key);
    void SetMemoryText(const std::string& key, const std::string& text);
    
    double GetMemoryValue(int key);
    void SetMemoryValue(int key, double value);
    
    void Update(double t);   
       
    virtual tcGameStream& operator<<(tcGameStream& stream);
	virtual tcGameStream& operator>>(tcGameStream& stream);

    ScriptedTask(std::shared_ptr<tcPlatformObject> platform_, Blackboard* bb, 
        long id_, double priority_, int attributes_, const std::string& scriptName_);
    ~ScriptedTask();
    
protected:
    std::map<std::string, std::string> textMemory;
    std::map<int, double> numberMemory;


    const char* GetCommandString();
private:
    std::string commandString;
};

}

#endif
