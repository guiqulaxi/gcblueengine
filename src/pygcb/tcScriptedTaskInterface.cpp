/**
**  @file ScriptedTaskInterface.cpp
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

#ifndef WX_PRECOMP
////#include "wx/wx.h" 
#endif

#include "tcScriptedTaskInterface.h"
#include "BlackboardInterface.h"
#include "ScriptedTask.h"
#include "tcPlatformInterface.h"
#include "tcPlatformObject.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif 


using namespace ai;
//using namespace boost::python;
using scriptinterface::tcPlatformInterface;

bool tcScriptedTaskInterface::pythonInitialized = false;

/**
* static method that should be called once to expose class
* to Python
*/
void tcScriptedTaskInterface::InitPython()
{

}
object tcScriptedTaskInterface::GetInterface()
{

    py::module pybind11_module = py::module::import("pygcb");
    // 获取Python类的引用
    py::object  interfaceType = pybind11_module.attr("ScriptedTaskInterface");
    return interfaceType;
}
/**
* Call to safely end (remove) this task
*/
void tcScriptedTaskInterface::EndTask()
{    
    assert(task);
    if (task->IsPermanent())
    {
        task->SetAttributes(task->GetAttributes() & (~Task::PERMANENT));
    }

    task->EndTask();
}

BlackboardInterface tcScriptedTaskInterface::GetBlackboardInterface()
{
    assert(task);
    return task->GetBlackboardInterface();    
}

const std::string tcScriptedTaskInterface::GetMemoryText(const std::string& key)
{
    assert(task);    
    return task->GetMemoryText(key);
}

double tcScriptedTaskInterface::GetMemoryValue(int key)
{
    assert(task);    
    return task->GetMemoryValue(key);
}


tcPlatformInterface tcScriptedTaskInterface::GetPlatformInterface()
{
    assert(task);
    return  tcPlatformInterface(task->platform);
}


void tcScriptedTaskInterface::SetMemoryText(const std::string& key, const std::string& text)
{
    assert(task);    
    task->SetMemoryText(key, text);
}


void tcScriptedTaskInterface::SetMemoryValue(int key, double value)
{
    assert(task);    
    return task->SetMemoryValue(key, value);
}

void tcScriptedTaskInterface::SetTask(ScriptedTask* scriptedTask)
{
    task = scriptedTask;
    
    assert(task);
}

void tcScriptedTaskInterface::SetTaskAttributes(int attributes_)
{
    task->SetAttributes(attributes_);
}


void tcScriptedTaskInterface::SetUpdateInterval(float interval)
{
    assert(task);
    
    if (interval < 0.1f) interval = 0.1f; // 10 Hz maximum
    task->SetUpdateInterval(interval);
}

/**
* Default constructor is defined for Python, SetTask needs to be
* called after this constructor
*/
tcScriptedTaskInterface::tcScriptedTaskInterface()
: task(0)
{
    if (!pythonInitialized) InitPython();   
}

tcScriptedTaskInterface::tcScriptedTaskInterface(ScriptedTask* scriptedTask)
: task(scriptedTask)
{
    assert(task);
    
    if (!pythonInitialized) InitPython();
    
}



tcScriptedTaskInterface::~tcScriptedTaskInterface()
{
}



