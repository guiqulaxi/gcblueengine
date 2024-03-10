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
#ifndef _SETUPPANEL_H_
#define _SETUPPANEL_H_

#include "SetupPanel.h"
#include "BasePanel.h"

#include <vector>

class tcTextEditControl;
class wxGridEvent;
class wxGrid;
class wxButton;
class wxStaticText;
class tcComboEditControl;
class tcTextEditControl;

/**
* Class for displaying and updating platform_setup information
*/
class tcSetupPanel : public tcBasePanel
{
public:
    enum {JUMP_TO = 632, SETUP_SELECT = 491};

    virtual void Save();

    virtual void SetDatabaseClass(const std::string& s);

    static wxFrame* eventFrame;

    tcSetupPanel(wxWindow* parent, const std::string& table_, const std::string& panelName);
    virtual ~tcSetupPanel();

private:
    enum {NEW_SETUP, RENAME_SETUP, DUPLICATE_SETUP, DELETE_SETUP};
    wxFont errorFont;

    std::vector<std::string> setupFields;
    std::vector<std::vector<std::string>> setupData;
    std::vector<std::string> setupNames;
    std::string currentSetup;
    std::string launcherLoadoutName;
    std::string magazineLoadoutName;
    std::string airComplementName;

    wxStaticText* launcherTitle;
    wxGrid* launcherLoadout;
    std::vector<std::string> launcherLabels;
    std::vector<std::string> launcherFields;

    std::vector<wxStaticText*> magazineTitle;
    std::vector<wxGrid*> magazineLoadout;
    std::vector<std::string> magazineLabels;
    std::vector<std::string> magazineFields;

    wxStaticText* airComplementTitle;
    wxGrid* airComplement;
    std::vector<std::string> airComplementLabels;
    std::vector<std::string> airComplementFields;

    tcComboEditControl* setupComboBox; // for selecting setup to edit
    tcTextEditControl* initialYear;
    tcTextEditControl* finalYear;

    wxButton* newButton;
    wxButton* renameButton;
    wxButton* duplicateButton;
    wxButton* deleteButton;

    std::vector<std::string> launcherEquipmentTables;
    std::vector<std::string> storesEquipmentTables;
    std::vector<std::string> aircraftTables;

    void OnGridCellChange(wxGridEvent& event);
    void OnGridLabelRClick(wxGridEvent& event);
    void OnGridLeftDClick(wxGridEvent& event);
    void OnGridRightClick(wxGridEvent& event);
    void OnTextUpdated(wxCommandEvent& event);
    void OnNewSetup(wxCommandEvent& event);
    void OnRenameSetup(wxCommandEvent& event);
    void OnDuplicateSetup(wxCommandEvent& event);
    void OnDeleteSetup(wxCommandEvent& event);

    void InitializePanel();

    void InitializeTableControl(wxGrid* grid, const std::vector<std::string>& columnLabels);

    bool IsTableControlChanged(wxGrid* grid, const std::string& tableName, const std::string& setupDatabaseClass, 
        const std::vector<std::string>& fields, const std::string& additionalConstraint);

    void UpdateAirComplementControl(const std::string& setupName);
    void UpdateLauncherControl(const std::string& setupName);
    void UpdateMagazineControls(const std::string& setupName);
    void UpdateSetupYears(const std::string& setupName);

    void InitializeReferenceTables();
    void CheckTableReferences(wxGrid* grid, int col, const std::vector<std::string>& referenceTables_);

    void DeleteSelectedRows();
    void InsertRowAbove();

    void UpdateAllTableControls();
    void SavePlatformTable(wxGrid* grid, const std::string& tableName, const std::string& setupDatabaseClass, 
                                         const std::vector<std::string>& fields, const std::string& additionalConstraint);
    void SavePlatformTableMagazine(wxGrid* grid, const std::string& tableName, const std::string& setupDatabaseClass, 
                                         const std::vector<std::string>& fields, int magazineId);
    void SaveSetupYears();
    void AddReferenceCombo(wxXmlNode* node, wxBoxSizer* sizer);

    void UpdateSetupData();
    int GetCurrentSetupIndex();
    const std::vector<int> GetLauncherIdList();
    const std::vector<int> GetMagazineIdList();
    const std::vector<std::string>& GetMagazineNameList();
    bool HasLaunchers();
    bool HasMagazines();
    bool HasAirComplement();
    const std::string& GetNewSetupName();
    void UpdateGridRows(wxGrid* grid);
    void AddDefaultLauncherLoadout(const std::string& loadoutName);
	const std::string& GetLauncherSummary(const std::vector<std::vector<std::string>>& data);
    const std::string& GetMagazineSummary(const std::string& magazineClass, const std::vector<std::vector<std::string>>& data, bool& isOkay);

    DECLARE_EVENT_TABLE()
};












#endif