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
#ifndef _GRIDPANEL_H_
#define _GRIDPANEL_H_

#include "BasePanel.h"

#include <map>
#include <vector>

class tcTextEditControl;
class wxGridEvent;
class wxGrid;
class tcComboEditControl;

/**
* Class for displaying and updating tcPlatformDatabaseObject generic parameters
*/
class tcGridPanel : public tcBasePanel
{
public:
    enum {JUMP_TO = 632};

    virtual void Save();

    virtual void SetDatabaseClass(const std::string& s);

    static wxFrame* eventFrame;

    tcGridPanel(wxWindow* parent, const std::string& table_, const std::string& panelName, const std::string& xmlPath);
    virtual ~tcGridPanel();

private:

    wxFont errorFont;

    wxGrid* tableCtrl;
    tcComboEditControl* referenceComboBox;

    std::vector<std::string> tableLabels;
    std::vector<std::string> tableFields;

    std::vector<std::string> referenceTables;
	std::map<long, bool> isDateField;

    void OnGridCellChange(wxGridEvent& event);
    void OnGridLabelRClick(wxGridEvent& event);
    void OnGridLeftDClick(wxGridEvent& event);
    void OnGridRightClick(wxGridEvent& event);

    void LoadFromXml(const std::string& fileName);

    void InitializeTableControl(wxGrid* grid, const std::vector<std::string>& columnLabels);

    bool IsTableControlChanged(wxGrid* grid, const std::string& tableName, const std::vector<std::string>& fields);
    void UpdateTableControl(wxGrid* grid, const std::string& tableName, const std::vector<std::string>& fields);
    void CheckTableReferences(wxGrid* grid, const std::vector<std::string>& referenceTables_);
    const std::vector<std::string>& GetReferenceTables(wxGrid* grid) const;

    void DeleteSelectedRows();
    void InsertRowAbove();

    void UpdateAllTableControls();
    void SavePlatformTable(wxGrid* grid, const std::string& tableName, const std::vector<std::string>& fields);

    void AddReferenceCombo(wxXmlNode* node, wxBoxSizer* sizer);

    DECLARE_EVENT_TABLE()
};












#endif