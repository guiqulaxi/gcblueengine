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
#ifndef _EDITCONTROL_H_
#define _EDITCONTROL_H_

#include "wx/panel.h"
#include <vector>


/**
* Base class for edit controls for editing individual database record fields
*/
class tcEditControl : public wxPanel
{
public:
    virtual void SetValue(const std::string& s);
    virtual void UpdateControl();
    virtual void SetDatabaseClass(const std::string& s);

    const std::string& GetFieldName() const;
    const std::string& GetInitialValue() const;
    virtual const std::string& GetEditValue() const;

    bool IsInfoOnly() const;
    void SetInfoOnly(bool state);

    void SetTooltipText(const std::string& s);

    virtual bool IsEdited() const;

    tcEditControl(wxWindow* parent, const wxSize& size, const std::string& fieldName_, const std::string& label_);
    virtual ~tcEditControl();

    static int labelWidth;
    static int controlWidth;
    
    static wxFont normalFont;
    static wxFont errorFont;

protected:
    bool infoOnly; ///< true if this control is just for displaying info, doesn't update database
    std::string databaseClass; ///< for controls that need to be aware of databaseClass

    std::string fieldName;
    std::string label; ///< label for this field
    std::string initialValue;
    std::string editValue;

    std::string tooltip;

    DECLARE_EVENT_TABLE()
};












#endif