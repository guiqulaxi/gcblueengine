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
#include "BasePanel.h"
#include "EditControl.h"
#include "DatabaseManager.h"
#include "TextEditControl.h"
#include "NumberEditControl.h"
#include "CheckBoxControl.h"
#include "ComboEditControl.h"
#include "BitfieldControl.h"
#include "AirCalculationControl.h"
#include "SonarCalculationControl.h"
#include "MissileCalculationControl.h"
#include "RadarCalculationControl.h"

#include "wx/sizer.h"
#include "wx/textfile.h"
#include "wx/xml/xml.h"
#include "wx/textctrl.h"

BEGIN_EVENT_TABLE(tcBasePanel, wxPanel)

END_EVENT_TABLE()

void tcBasePanel::AddControl(tcEditControl* ctrl)
{
    assert(ctrl != 0);

    if (!ctrl->IsInfoOnly())
    {
        controls.push_back(ctrl);
        fieldList.push_back(ctrl->GetFieldName());
    }
    else
    {
        infoControls.push_back(ctrl);
    }
}

void tcBasePanel::AddXmlBitfield(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string value = node->GetPropVal("value", "Error");
    std::string label = node->GetPropVal("label", "Error");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);

    int ctrlStyle = 0;
    int ctrlSizerFlags = wxALL ;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL;

    // load bit labels and values (normally all are different powers of 2 e.g. 1,2,4,8 or 8,4,2,1)
    std::vector<std::string> checkLabels;    
    std::vector<int> checkValues;
    wxXmlNode* child = node->GetChildren();
    while (child != 0)
    {
        if (child->GetName() == "bit") 
        {
            std::string bitLabel = child->GetPropVal("label", "ERR");
            std::string bitValue = child->GetPropVal("value", "0");
            long val = 0;
            bitValue.ToLong(&val);
            checkLabels.push_back(bitLabel);
            checkValues.push_back(int(val));
        }

        child = child->GetNext();
    }

    tcBitfieldControl* bitfield = new tcBitfieldControl(this, wxSize(100, -1), value, label, checkLabels, checkValues);
    AddControl(bitfield);

    int border = 2;
    int style = wxALL  | wxEXPAND;

    sizer->Add(bitfield, proportion, style, border);
}


void tcBasePanel::AddXmlCalculation(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string type = node->GetPropVal("type", "Error");
    std::string subtype = node->GetPropVal("subtype", "Error");
    std::string label = node->GetPropVal("label", "Error");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);

    int ctrlStyle = 0;
    int ctrlSizerFlags = wxALL ;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL | wxEXPAND;

	tcEditControl* newControl = 0;
	if (type == "aero")
	{
		tcAirCalculationControl* airCalc = new tcAirCalculationControl(this, wxSize(100, -1), "", 
			ctrlStyle, ctrlSizerFlags, labelTextStyle, labelTextSizerFlags);
		AddControl(airCalc);

		newControl = airCalc;
	}
	else if (type == "sonar")
	{
		tcSonarCalculationControl* sonarCalc = new tcSonarCalculationControl(this, wxSize(100, -1), "", 
			ctrlStyle, ctrlSizerFlags, labelTextStyle, labelTextSizerFlags);
		AddControl(sonarCalc);

		newControl = sonarCalc;
	}
	else if (type == "missile")
	{
		tcMissileCalculationControl* missileCalc = new tcMissileCalculationControl(this, wxSize(100, -1), "", 
			ctrlStyle, ctrlSizerFlags, labelTextStyle, labelTextSizerFlags);
		AddControl(missileCalc);

		newControl = missileCalc;
	}
    else if (type == "radar")
    {
        tcRadarCalculationControl* radarCalc = new tcRadarCalculationControl(this, wxSize(100, -1), "", "",
            ctrlStyle, ctrlSizerFlags, labelTextStyle, labelTextSizerFlags);
        radarCalc->SetCalculationType(subtype);

        AddControl(radarCalc);
        newControl = radarCalc;
    }
	else // unrecognized
	{
		return; 
	}

	if (newControl != 0)
	{		
		int border = 2;
		int style = wxALL; //  | wxEXPAND;
		sizer->Add(newControl, proportion, style, border);
	}


    
}


void tcBasePanel::AddXmlCheckBox(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string value = node->GetPropVal("value", "Error");
    std::string label = node->GetPropVal("label", "Error");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);

    int ctrlStyle = 0;
    int ctrlSizerFlags = wxALL ;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL;

    tcCheckBoxControl* checkBox = new tcCheckBoxControl(this, wxSize(100, -1), value, label, 
        ctrlStyle, ctrlSizerFlags, labelTextStyle, labelTextSizerFlags);
    AddControl(checkBox);

    int border = 2;
    int style = wxALL  | wxEXPAND;

    sizer->Add(checkBox, proportion, style, border);
}

void tcBasePanel::AddXmlComboBox(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string value = node->GetPropVal("value", "Error");
    std::string label = node->GetPropVal("label", "Error");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);
    std::string expandControl = node->GetPropVal("expand_control", "yes");
    std::string expandSizer = node->GetPropVal("expand_sizer", "yes");


    std::string updateTable = node->GetPropVal("update_table", "");
    std::string configFile = node->GetPropVal("file", "");

    int ctrlStyle = 0;
    int ctrlSizerFlags = wxALL;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL;

    std::vector<std::string> comboValues;
    std::vector<std::string> comboLabels;

    if (configFile.size() > 0)
    {
        LoadLabelValueData(configFile, comboLabels, comboValues);
    }

    if (expandControl.IsSameAs("yes", false)) ctrlSizerFlags |= wxEXPAND;

    tcComboEditControl* comboBox = new tcComboEditControl(this, wxSize(100, -1), value, label, comboValues, comboLabels);
    if (updateTable.size() > 0)
    {
        comboBox->SetUpdateFromDatabaseTable(updateTable);
    }

    // check for "update with reference" case
    wxXmlNode* child = node->GetChildren();
    std::vector<std::string> referenceTables;
    std::vector<std::string> referenceFields;
    while (child != 0)
    {
        if (child->GetName() == "update_reference") 
        {
            std::string refTable = child->GetPropVal("table", "");
            std::string refField = child->GetPropVal("field", "");
            if ((refTable.size() > 0) && (refField.size() > 0))
            {
                referenceTables.push_back(refTable);
                referenceFields.push_back(refField);
            }
        }

        child = child->GetNext();
    }
    if (referenceTables.size() > 0)
    {
        comboBox->SetUpdateFromDatabaseReferences(referenceTables, referenceFields);
        comboBox->SetInfoOnly(true);
    }



    AddControl(comboBox);

    int border = 2;
    int style = wxALL;
    if (expandSizer.IsSameAs("yes", false)) style |= wxEXPAND;

    sizer->Add(comboBox, proportion, style, border);
}


void tcBasePanel::AddXmlTextControl(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string value = node->GetPropVal("value", "Error");
    std::string label = node->GetPropVal("label", "Error");
    std::string tooltip = node->GetPropVal("tooltip", "");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);

    std::string multiline = node->GetPropVal("multiline", "no");
    std::string expandControl = node->GetPropVal("expand_control", "yes");
    std::string expandSizer = node->GetPropVal("expand_sizer", "yes");

    std::string crossRefs = node->GetPropVal("cross_reference", "");
    std::vector<std::string> crossRefTables;
    while (crossRefs.size() > 0)
    {
        std::string s = crossRefs.BeforeFirst(',');
        crossRefs = crossRefs.AfterFirst(',');
        crossRefTables.push_back(s);
    }


    int textCtrlStyle = wxTE_PROCESS_ENTER;
    int textCtrlSizerFlags = wxALL;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL;

    if (multiline.IsSameAs("yes", false)) textCtrlStyle |= wxTE_MULTILINE;

    if (expandControl.IsSameAs("yes", false)) textCtrlSizerFlags |= wxEXPAND;

    tcTextEditControl* textControl = new tcTextEditControl(this, wxSize(100, -1), value, label, 
        textCtrlStyle, textCtrlSizerFlags, labelTextStyle, labelTextSizerFlags);
    if (crossRefTables.size() > 0)
    {
        textControl->SetCrossReference(crossRefTables);
    }

    if (tooltip.size() > 0)
    {
        textControl->SetTooltipText(tooltip);
    }

    AddControl(textControl);


    int border = 2;
    int style = wxALL;
    if (expandSizer.IsSameAs("yes", false)) style |= wxEXPAND;


    sizer->Add(textControl, proportion, style, border);
}

void tcBasePanel::AddXmlNumberControl(wxXmlNode* node, wxBoxSizer* sizer)
{
    std::string value = node->GetPropVal("value", "Error");
    std::string label = node->GetPropVal("label", "Error");
    std::string tooltip = node->GetPropVal("tooltip", "");

    long proportion = 1;
    node->GetPropVal("proportion", "1").ToLong(&proportion);

    double unitFactor = 1.0;
    node->GetPropVal("unit_factor", "1.0").ToDouble(&unitFactor);

    unsigned long decimalPlaces = 4;
    node->GetPropVal("decimal_places", "4").ToULong(&decimalPlaces);

    std::string expandControl = node->GetPropVal("expand_control", "yes");
    std::string expandSizer = node->GetPropVal("expand_sizer", "yes");

    std::string crossRefs = node->GetPropVal("cross_reference", "");
    std::vector<std::string> crossRefTables;
    while (crossRefs.size() > 0)
    {
        std::string s = crossRefs.BeforeFirst(',');
        crossRefs = crossRefs.AfterFirst(',');
        crossRefTables.push_back(s);
    }


    int textCtrlStyle = 0;
    int textCtrlSizerFlags = wxALL;
    int labelTextStyle = 0;
    int labelTextSizerFlags = wxALL;

    if (expandControl.IsSameAs("yes", false)) textCtrlSizerFlags |= wxEXPAND;

    tcNumberEditControl* numberControl = new tcNumberEditControl(this, wxSize(100, -1), value, label, 
        textCtrlStyle, textCtrlSizerFlags, labelTextStyle, labelTextSizerFlags);

    numberControl->SetUnitFactor(unitFactor);
    numberControl->SetDecimalPlaces(decimalPlaces);

    if (crossRefTables.size() > 0)
    {
        numberControl->SetCrossReference(crossRefTables);
    }

    if (tooltip.size() > 0)
    {
        numberControl->SetTooltipText(tooltip);
    }

    AddControl(numberControl);


    int border = 2;
    int style = wxALL;
    if (expandSizer.IsSameAs("yes", false)) style |= wxEXPAND;


    sizer->Add(numberControl, proportion, style, border);
}

void tcBasePanel::LoadFromXml(const std::string& fileName)
{
    wxXmlDocument doc;
    if (!doc.Load(fileName)) return;

    wxXmlNode* root = doc.GetRoot();
    if (root->GetName() != "form") return;

    Freeze();

    std::string propval = root->GetPropVal("orientation", "vertical");
    
    wxBoxSizer* sizerTop;
    
    if (propval.IsSameAs("horizontal", false))
    {
        sizerTop = new wxBoxSizer(wxHORIZONTAL);
    }
    else
    {
        sizerTop = new wxBoxSizer(wxVERTICAL);
    }

    wxXmlNode* child = doc.GetRoot()->GetChildren();
    while (child != 0)
    {

        if (child->GetName() == "sizer") 
        {
            LoadXmlSizer(child, sizerTop);
        }

        child = child->GetNext();
    }

    this->SetSizer(sizerTop);
    //sizerTop->SetSizeHints(this);

    Thaw();
}

void tcBasePanel::LoadXmlSizer(wxXmlNode* node, wxBoxSizer* parent)
{
    // load sizer properties and create sizer
    wxOrientation orientation;
    long proportion;
    long labelWidth;
    long controlWidth;
    ReadSizerProperties(node, orientation, proportion, labelWidth, controlWidth);

    wxBoxSizer* sizer = new wxBoxSizer(orientation);
    int border = 3;
    int style = wxALL | wxEXPAND;
    parent->Add(sizer, proportion, style, border);

    // load and add children
    wxXmlNode* child = node->GetChildren();
    while (child != 0)
    {
        std::string childName = child->GetName();
        if (childName == "sizer") 
        {
            LoadXmlSizer(child, sizer);
        }
        else if (childName == "text")
        {
            AddXmlTextControl(child, sizer);
        }
        else if (childName == "number")
        {
            AddXmlNumberControl(child, sizer);
        }
        else if (childName == "checkbox")
        {
            AddXmlCheckBox(child, sizer);
        }
        else if (childName == "combobox")
        {
            AddXmlComboBox(child, sizer);
        }
        else if (childName == "bitfield")
        {
            AddXmlBitfield(child, sizer);
        }
		else if (childName == "calc")
		{
			AddXmlCalculation(child, sizer);
		}

        child = child->GetNext();
    }

}


bool tcBasePanel::LoadLabelValueData(const std::string& fileName, std::vector<std::string>& labels, std::vector<std::string>& values)
{
    values.clear();
    labels.clear();

    wxTextFile inFile(fileName);
    if (!inFile.Open())
    {
        values.push_back("Error");
        labels.push_back("Error");
        assert(false);
        return false;
    }

    size_t nLines = inFile.GetLineCount();
    for (size_t n=0; n<nLines; n++)
    {
        std::string line = inFile.GetLine(n);
        if (line.Contains(",") && !line.Contains("//"))
        {
            std::string labelText = line.BeforeFirst(',');
            labelText.Trim(true);
            labelText.Trim(false);

            std::string valueText = line.AfterFirst(',');
            valueText.Trim(true);
            valueText.Trim(false);

            values.push_back(valueText);
            labels.push_back(labelText);
        }
    }


    inFile.Close();

    return true;
}


void tcBasePanel::ReadSizerProperties(wxXmlNode* node, wxOrientation& orientation, long& proportion, long& labelWidth, long& controlWidth)
{
    orientation = wxVERTICAL;

    std::string propval = node->GetPropVal("orientation", "vertical");
    if (propval.IsSameAs("horizontal", false))
    {
        orientation = wxHORIZONTAL;
    }
    else
    {
        orientation = wxVERTICAL;
    }

    proportion = 1;
    node->GetPropVal("proportion", "0").ToLong(&proportion);

    labelWidth = 120;
    node->GetPropVal("label_width", "120").ToLong(&labelWidth);

    controlWidth = 120;
    node->GetPropVal("control_width", "120").ToLong(&controlWidth);

    tcEditControl::labelWidth = labelWidth;
    tcEditControl::controlWidth = controlWidth;
}

void tcBasePanel::Save()
{
    if (!ValuesHaveChanged()) return; // no need to save

    std::vector<std::string> valueList;

    for (size_t n=0; n<controls.size(); n++)
    {
        valueList.push_back(controls[n]->GetEditValue());
    }

    tcDatabaseManager* databaseManager = tcDatabaseManager::Get();
    if (!databaseManager->IsOpen()) return;

    databaseManager->UpdateDatabaseObject(table, databaseClass, fieldList, valueList);

    wxWindow::Update();
}

void tcBasePanel::SetDatabaseClass(const std::string& s)
{
    tcDatabaseManager* databaseManager = tcDatabaseManager::Get();
    if (!databaseManager->IsOpen())
    {
        databaseClass.clear();
        return;
    }

    databaseClass = s;

    for (size_t n=0; n<infoControls.size(); n++)
    {
        infoControls[n]->SetDatabaseClass(databaseClass);
        infoControls[n]->UpdateControl();
    }

	if (databaseClass.size() < 2)
	{
		return;
	}

    try
    {
        std::vector<std::string> fieldValues = databaseManager->ReadDatabaseObjectFields(table, databaseClass, fieldList);
        if (fieldValues.size() > 0)
        {
            for (size_t n=0; n<controls.size(); n++)
            {            
                controls[n]->UpdateControl();
                controls[n]->SetValue(fieldValues[n]);
            }
        }
    }
    catch (...)
    {
    }

}

bool tcBasePanel::ValuesHaveChanged() const
{
    bool changed = false;

    for (size_t n=0; (n<controls.size())&&(!changed); n++)
    {
        changed = changed || controls[n]->IsEdited();
    }
    
    return changed;
}



tcBasePanel::tcBasePanel(wxWindow* parent, const std::string& table_, const std::string& panelName) 
: wxScrolledWindow(parent, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL, panelName),
  table(table_)
{
}

/**
* This version automatically loads form from xml file
*/
tcBasePanel::tcBasePanel(wxWindow* parent, const std::string& table_, const std::string& panelName, const std::string& formPath)
: wxScrolledWindow(parent, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL, panelName),
  table(table_)
{
    LoadFromXml(formPath);

}


tcBasePanel::~tcBasePanel()
{
}