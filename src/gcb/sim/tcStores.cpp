/** 
** @file tcStores.cpp
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

//#include "stdwx.h" // precompiled header file

#include "tcStores.h"

#include "tcLauncher.h"
////#include "tcMessageInterface.h"
#include "tcGameObject.h"
#include "tcPlatformObject.h"
#include "tcAirObject.h"
#include "tcStoresDBObject.h"
#include <iostream>
#include "common/tcObjStream.h"
#include "tcGameStream.h"
#include "tcDatabase.h"
#include "tcAirDBObject.h"
#include "tcPlatformDBObject.h"
#include "tcFuelTankDBObject.h"
#include "tcCounterMeasureDBObject.h"
#include "tcWeaponDBObject.h"
#include "tcMissileDBObject.h"
#include "tcTorpedoDBObject.h"
#include "tcBallisticDBObject.h"
#include "tcFlightOpsObject.h"
#include "tcFlightPort.h"
#include "tcScenarioLogger.h"
#include "tcSimState.h"
#include <limits>
#include <cassert>
#ifdef _DEBUG
#define new DEBUG_NEW
#endif

std::shared_ptr<tcDatabaseObject> tcStores::StoreItem::GetDatabaseObject() const
{
    return databaseObj;
}

std::shared_ptr<tcDatabaseObject> tcStores::StoreItem::GetOrLoadDatabaseObject()
{
    if (databaseObj != 0)
    {
        return databaseObj;
    }
    else
    {
        LoadDatabaseObject();
        return databaseObj;
    }
}

void tcStores::StoreItem::SetDatabaseObject(std::shared_ptr<tcDatabaseObject> obj)
{
	databaseObj = obj;
}

/**
* Set pointer to database object associated with
* this item.
*/
void tcStores::StoreItem::LoadDatabaseObject()
{
    databaseObj = tcDatabase::Get()->GetObject(className);
    
    if (databaseObj == 0)
    {
        fprintf(stderr, "tcStores::StoreItem::LoadDatabaseObject - "
            "Can't find %s in database\n", className.c_str());
        assert(false);
    }
}

tcStores::StoreItem::StoreItem()
:   databaseObj(0),
    quantity(0),
    itemId(0)
{
}

tcStores::StoreItem::StoreItem(const StoreItem& src)
:   className(src.className), 
    quantity(src.quantity),
    databaseObj(src.databaseObj),
    itemId(src.itemId)
{
}

tcStores::StoreItem::StoreItem(const std::string& name, unsigned long qty, unsigned int id)
:   className(name), 
    quantity(qty),
    itemId(id)
{
    LoadDatabaseObject();
}


std::shared_ptr<tcGameObject> tcStores::StoreOperation::GetObj()
{   
    if (std::shared_ptr<tcGameObject> obj = tcSimState::Get()->GetObject(platformId))
    {
        if (childId == -1)
        {
            return obj;
        }
        else
        {
            return obj->GetChildById(long(childId));
        }
    }
    else
    {
        return 0;
    }
}



/**
*
*/
tcCreateStream& tcStores::operator<<(tcCreateStream& stream)
{
    return stream;
}


/**
*
*/
tcCreateStream& tcStores::operator>>(tcCreateStream& stream)
{

    return stream;
}


/**
* Loads state from update stream
*/
tcUpdateStream& tcStores::operator<<(tcUpdateStream& stream)
{
	tcDatabase* database = tcDatabase::Get();

	/* delete and rebuild stores for each update
	** might be more efficient to search and selectively update?
	*/
	stores.clear();

	unsigned char nItems;
	stream >> nItems;

	for (unsigned char n=0; n<nItems; n++)
	{
		long id;
		stream >> id;
		
		unsigned long quantity;
		stream >> quantity;

        unsigned int itemId;
        stream >> itemId;

		std::shared_ptr<tcDatabaseObject> databaseObj = database->GetObject(id);
		
		if (databaseObj == 0)
		{
			assert(false);
			fprintf(stderr, "tcStores::operator<<(tcUpdateStream& stream) - not found in DB\n");
			return stream;
		}

		std::string itemName(databaseObj->mzClass.c_str());
		AddItemsForceId(itemName, quantity, itemId);
	}

    return stream;
}

/**
* Saves state to update stream
*/
tcUpdateStream& tcStores::operator>>(tcUpdateStream& stream)
{
	unsigned char nItems = stores.size();
	stream << nItems;
	for (unsigned char n=0; n<nItems; n++)
	{
		std::shared_ptr<tcDatabaseObject> databaseObj = stores[n].GetDatabaseObject();
		long databaseId = databaseObj->mnKey;
		unsigned long quantity = stores[n].quantity;
        unsigned int itemId = stores[n].itemId;
		
		stream << databaseId;
		stream << quantity;
        stream << itemId;
	}

    return stream;
}





/**
* Load from command stream
*/
tcCommandStream& tcStores::operator<<(tcCommandStream& stream)
{
    unsigned char nCommands;
	stream >> nCommands;

	for (unsigned char n=0; n<nCommands; n++)
	{
		short int id;
		unsigned char op;
		long itemId = -1;
		unsigned long quantity = 0;
        unsigned char launcherIdx = 99;
		std::string type;

        stream >> id;
		stream >> op;

		if (op != StoreOperation::AUTOMATION)
		{
			stream >> itemId;
			stream >> quantity;
			stream >> launcherIdx;
		}
		else
		{
			stream >> type;
		}
		
		bool ok = true;
		std::shared_ptr<tcGameObject> obj = 0;
		if (id != -1)
		{
            obj = parent->GetChildById(id);
            if (obj == 0) ok = false;
        }

		if (ValidateOpObject(obj) == false)
		{
			ok = false;
		}
		

        std::string item;
		if ((op != StoreOperation::UNLOAD) && (op != StoreOperation::AUTOMATION))
        {
            std::shared_ptr<tcDatabaseObject> databaseObj = tcDatabase::Get()->GetObject(itemId);
            if (databaseObj == 0)
            {
                ok = false;
            }
            else
            {
                item = databaseObj->mzClass.c_str();
            }
        }

        if (ok)
        {
			if (op == StoreOperation::AUTOMATION)
			{
				AddAutomationOp(type, obj);
			}
            else if (op == StoreOperation::LOAD)
            {
                LoadLauncher(launcherIdx, item, obj);
            }
            else if (op == StoreOperation::UNLOAD)
            {
                UnloadLauncher(launcherIdx, obj); 
            }
            else if (op == StoreOperation::REFUEL)
            {
                LoadOther(item, quantity, obj);
            }
            else
            {
                fprintf(stderr, "tcStores::operator<< -- Bad op (%d)\n", op);
                assert(false);
            }
        }
        
	}
        
    return stream;
}

/**
* Save to command stream
*/
tcCommandStream& tcStores::operator>>(tcCommandStream& stream)
{
	unsigned char nCommands = commandList.size();
	stream << nCommands;

	for (unsigned char n=0; n<nCommands; n++)
	{
        CommandInfo& cmd = commandList[n];
        
 		stream << cmd.id;
		stream << cmd.op;
		if (cmd.op != StoreOperation::AUTOMATION)
		{
			stream << cmd.itemId;
			stream << cmd.quantity;
			stream << cmd.launcherIdx;
		}
		else
		{
			stream << cmd.type;
		}
	}

    return stream;
}


/**
* Loads state from game stream
*/
tcGameStream& tcStores::operator<<(tcGameStream& stream)
{
    stream >> errorCode;
    stream >> lastUpdate;

	tcDatabase* database = tcDatabase::Get();

    // ---------- load stores ----------
	stores.clear();
	unsigned char nItems;
	stream >> nItems;
	for (unsigned char n=0; n<nItems; n++)
	{
        std::string itemName;
		stream >> itemName;
		
		unsigned long quantity;
		stream >> quantity;

		std::shared_ptr<tcDatabaseObject> databaseObj = database->GetObject(itemName);
		
		if (databaseObj == 0)
		{
			assert(false);
            fprintf(stderr, "tcStores::operator<<(tcUpdateStream& stream) - Warning, %s not found in DB\n", itemName.c_str());
		}

		AddItems(itemName, quantity);
	}

    // ---------- load store operations ----------
    ops.clear();
    unsigned char nOps;
    stream >> nOps;
    for (unsigned char n=0; n<nOps; n++)
    {
        StoreOperation op;
        stream >> op.item;        
        stream >> op.quantity; ///< quantity of item
        stream >> op.timeToComplete; ///< time left for op to complete [s]
        stream >> op.timeElapsed;
        stream >> op.launcherIdx; ///< launcher idx to transfer to/from
        stream >> op.transferType; ///< UNLOAD or LOAD

        stream >> op.platformId;
        stream >> op.childId;

        //long objId; // = (ops[n].obj == 0) ? -1 : ops[n].obj->mnID;
        //stream >> objId;
        //if (objId == -1)
        //{
        //    op.obj = 0;
        //}
        //else
        //{
        //    op.obj = parent->GetChildById(objId);
        //    assert(op.obj != 0);
        //}

        ops.push_back(op);
    }

    // ---------- load automation operations ----------
    automationOps.clear();
    unsigned char nAutomationOps;
    stream >> nAutomationOps;
    for (unsigned char n=0; n<nAutomationOps; n++)
    {
        AutomationOperation autoOp;
        stream >> autoOp.type;
        stream >> autoOp.stage;

        long objId; // = (automationOps[n].obj == 0) ? -1 : automationOps[n].obj->mnID;
        stream >> objId;
        if (objId == -1)
        {
            autoOp.obj = 0;
        }
        else
        {
            autoOp.obj = parent->GetChildById(objId);
            assert(autoOp.obj != 0);
        }

        automationOps.push_back(autoOp);
    }

    // ---------- load command list ----------
    commandList.clear();
    unsigned char nCommands;
    stream >> nCommands;
    for (unsigned char n=0; n<nCommands; n++)
    {
        CommandInfo cmd;
		stream >> cmd.id;
		stream >> cmd.op;
		stream >> cmd.itemId;
		stream >> cmd.quantity;
		stream >> cmd.launcherIdx;
		stream >> cmd.type;

        commandList.push_back(cmd);
    }

    stream.ReadCheckValue(9876);

    return stream;
}

/**
* Saves state to game stream
*/
tcGameStream& tcStores::operator>>(tcGameStream& stream)
{
    stream << errorCode;
    stream << lastUpdate;

    assert(stores.size() < 256);
	unsigned char nItems = stores.size();
	stream << nItems;
	for (unsigned char n=0; n<nItems; n++)
	{
		//std::shared_ptr<tcDatabaseObject> databaseObj = stores[n].GetDatabaseObject();
        std::string itemName = stores[n].className;
		unsigned long quantity = stores[n].quantity;
		
		stream << itemName;
		stream << quantity;
	}

    assert(ops.size() < 256);
    unsigned char nOps = ops.size();
    stream << nOps;
    for (unsigned char n=0; n<nOps; n++)
    {
        stream << ops[n].item;        
        stream << ops[n].quantity; ///< quantity of item
        stream << ops[n].timeToComplete; ///< time left for op to complete [s]
        stream << ops[n].timeElapsed;
        stream << ops[n].launcherIdx; ///< launcher idx to transfer to/from
        stream << ops[n].transferType; ///< UNLOAD or LOAD

        stream << ops[n].platformId;
        stream << ops[n].childId;

        //long objId = (ops[n].obj == 0) ? -1 : ops[n].obj->mnID;
        //stream << objId;
    }

    assert(automationOps.size() < 256);
    unsigned char nAutomationOps = automationOps.size();
    stream << nAutomationOps;
    for (unsigned char n=0; n<nAutomationOps; n++)
    {
        stream << automationOps[n].type;
        stream << automationOps[n].stage;

        long objId = (automationOps[n].obj == 0) ? -1 : automationOps[n].obj->mnID;
        stream << objId;
    }

    assert(commandList.size() < 256);
    unsigned char nCommands = commandList.size();
    stream << nCommands;
    for (unsigned char n=0; n<nCommands; n++)
    {
		stream << commandList[n].id;
		stream << commandList[n].op;
		stream << commandList[n].itemId;
		stream << commandList[n].quantity;
		stream << commandList[n].launcherIdx;
		stream << commandList[n].type;
    }

    stream.WriteCheckValue(9876);

    return stream;
}




void tcStores::ClearNewCommand()
{
	commandList.clear();
}

bool tcStores::HasNewCommand() const
{
	return (commandList.size() > 0);
}


/**
* Adds new automation operation used to set platform to one of several generic
* configurations.
* @param type "Empty" empty all launchers, "AAW" anti-air warfare, "ASuW" antisurface warfare, "ASW" antisubmarine warfare, "Strike" ground strike
*/
void tcStores::AddAutomationOp(const std::string& type, std::shared_ptr<tcGameObject> child)
{
	if (type == "Error")
	{
		assert(false);
		return;
	}

	if (parent->IsClientMode())
	{
		CommandInfo cmd;

		if (child->parent != 0)
		{
			cmd.id = child->mnID;
		}
		else
		{
			cmd.id = -1;
		}

		cmd.op = StoreOperation::AUTOMATION;
		cmd.itemId = -1;
		cmd.quantity = 0;
		cmd.launcherIdx = 0;
		cmd.type = type;

		commandList.push_back(cmd);

		return;
	}

	// first search for any existing ops with this child and remove
	std::vector<AutomationOperation> temp;
	for (size_t n=0; n<automationOps.size(); n++)
	{
		if (automationOps[n].obj != child)
		{
			temp.push_back(automationOps[n]);
		}
		else if (automationOps[n].type == type)
		{
			return; // op already exists, don't add again
		}
	}
	automationOps = temp;


	AutomationOperation op;
	op.type = type;
	op.obj = child;
	op.stage = 0;

	automationOps.push_back(op);
}


/**
*
*/
bool tcStores::AddItems(const std::string& item, unsigned long quantity)
{
    std::shared_ptr<tcDatabaseObject> databaseObject = tcDatabase::Get()->GetObject(item);

    if (databaseObject == 0)
    {
        fprintf(stderr, "tcStores::AddItems -- not found (%s)\n", item.c_str());
        return false; // not found in database
    }

    unsigned long freeCapacity = GetFreeCapacityForItem(databaseObject->weight_kg, databaseObject->volume_m3);

    if ((freeCapacity > 0) && IsCompatible(item))
    {
        if (quantity > (unsigned)freeCapacity) quantity = (unsigned)freeCapacity;

        for (size_t n=0; n<stores.size(); n++)
        {
            if (stores[n].className == item)
            {
                stores[n].quantity += quantity;
                UpdateWeightAndVolume();
                return true;
            }
        }

		if (quantity > 0)
		{
			stores.push_back(StoreItem(item, quantity, nextItemId++));
		}
        UpdateWeightAndVolume();
		return true;
    }
	else
	{
		return false;
	}
}

bool tcStores::AddItemsForceId(const std::string& item, unsigned long quantity, unsigned int itemId)
{
    std::shared_ptr<tcDatabaseObject> databaseObject = tcDatabase::Get()->GetObject(item);

    if (databaseObject == 0)
    {
        fprintf(stderr, "tcStores::AddItemsForceId -- not found (%s)\n", item.c_str());
        return false; // not found in database
    }

    unsigned long freeCapacity = GetFreeCapacityForItem(databaseObject->weight_kg, databaseObject->volume_m3);
    if ((freeCapacity > 0) && IsCompatible(item))
    {
        if (quantity > (unsigned)freeCapacity) quantity = (unsigned)freeCapacity;

        stores.push_back(StoreItem(item, quantity, itemId));
        UpdateWeightAndVolume();
        return true;
    }
    else
    {
        return false;
    }
}


void tcStores::RemoveAllItems()
{
    stores.clear();
    ops.clear();
	automationOps.clear();
    commandList.clear();

    weight_kg = 0;
    volume_m3 = 0;
}

/**
* Removes specified items from stores.
* @return true if any of specified type were removed
*/
bool tcStores::RemoveItems(const std::string& item, unsigned long quantity)
{
    assert(quantity > 0); // technically not a problem, but this shouldn't happen

    bool found = false;
    int nStores = (int)stores.size();
    unsigned long removeQuantity = 0;
    for (int k=nStores-1; (k>=0) && !found; k--)
    {
        if (stores[k].className == item)
        {
            found = true;
            assert(stores[k].quantity);
            if (stores[k].quantity >= (unsigned)quantity)
            {
                removeQuantity = (unsigned)quantity;
            }
            else
            {
                removeQuantity = stores[k].quantity;
            }
            stores[k].quantity -= removeQuantity;
            if (stores[k].quantity == 0)
            {
                stores.erase(stores.begin()+k);
            }

            UpdateWeightAndVolume();
        }
    }

    return found;
}


bool tcStores::AddOperation(const std::string& itemName, unsigned int launcherIdx, unsigned long quantity, float transferTime_s,
							int opType, std::shared_ptr<tcGameObject> obj)
{
	/* Search for existing op with launcher (or platform for REFUEL)
	** opType 
	** LOAD - Search for existing LOAD and UNLOAD ops
	**        If existing op is UNLOAD, then ignore this add request and return
	**        If existing op is LOAD and item is the same, then ignore and return
	**        If existing op is LOAD and item is different, then switch to new item (new items already removed from stores)
	** UNLOAD - Search for existing LOAD and UNLOAD ops
	**        If existing op is UNLOAD, then ignore this add request and return
	**        If existing op is LOAD then cancel the load op and return items to stores
	** REFUEL - Search for existing REFUEL or DEFUEL ops
	**        If found then ignore this add request and return
	** DEFUEL - Search for existing REFUEL or DEFUEL ops
	**        If found then ignore this add request and return
	*/

	if (parent->IsClientMode())
	{
		CommandInfo cmd;

		std::shared_ptr<tcDatabaseObject> databaseObj = tcDatabase::Get()->GetObject(itemName);
		if (databaseObj == 0)
		{
			assert(false);
			return false;
		}
        
        
		cmd.id = ((obj != 0) && (obj->parent != 0)) ? obj->mnID : -1;
		cmd.op = opType;
		cmd.itemId = databaseObj->mnKey;
		cmd.quantity = quantity;
		cmd.launcherIdx = launcherIdx;

		commandList.push_back(cmd);
		return true;
	}


	bool isLoadOp = (opType == StoreOperation::LOAD);
	bool isUnloadOp = (opType == StoreOperation::UNLOAD);
    bool isFuelOp = (opType == StoreOperation::REFUEL) || (opType == StoreOperation::DEFUEL);
    //bool isMoveOp = (opType == StoreOperation::MOVE);

    bool found = false;
    std::vector<StoreOperation>::iterator opIter;
    std::vector<StoreOperation>::iterator matchIter;
    for (opIter = ops.begin(); (opIter != ops.end()) && (!found); ++opIter)
    {
        bool allowMatch = (isLoadOp && (opIter->transferType != StoreOperation::REFUEL) && (opIter->transferType != StoreOperation::DEFUEL)) ||
			              (isUnloadOp && (opIter->transferType != StoreOperation::REFUEL) && (opIter->transferType != StoreOperation::DEFUEL)) ||
			              (isFuelOp && (opIter->transferType == StoreOperation::REFUEL)) ||
                          (isFuelOp && (opIter->transferType == StoreOperation::DEFUEL));

        if ((opIter->GetObj() == obj) && (allowMatch) && (opIter->launcherIdx == launcherIdx))
        {
            matchIter = opIter;
            found = true;
        }
    }

	bool success = false;
	std::string msg;

    if (found) // do nothing, modify existing op, or cancel existing op
    {
		if (matchIter->transferType == StoreOperation::UNLOAD)
		{            
			msg = strutil::format("%s (%s) - Unload of %s to %s must finish\n", 
				obj->mzUnit.c_str(), obj->mzClass.c_str(), 
				matchIter->item.c_str(), storesDBObj->displayName.c_str());
		}
		else if (matchIter->transferType == StoreOperation::LOAD)
		{
			if (isLoadOp && (matchIter->item == itemName))
			{
				msg = strutil::format("%s (%s) - Already loading %s\n", 
				    obj->mzUnit.c_str(), obj->mzClass.c_str(), itemName.c_str());
			}
			else if (isLoadOp)
			{
				msg = strutil::format("%s (%s) - load in progress, cant load %s\n", 
				    obj->mzUnit.c_str(), obj->mzClass.c_str(), itemName.c_str());
			}
			else // isUnloadOp
			{
				msg = strutil::format("%s (%s) - load in progress, cant unload\n", 
				    obj->mzUnit.c_str(), obj->mzClass.c_str());
			}
		}
		else // if (matchIter->transferType == REFUEL) || (matchIter->transferType == DEFUEL)
		{
			msg = strutil::format("%s (%s) - Already refueling or defueling\n", 
				obj->mzUnit.c_str(), obj->mzClass.c_str());
		}   
    }
	else // add new operation
	{
		StoreOperation op;

		op.item = itemName;
		op.launcherIdx = launcherIdx;
		op.quantity = quantity;
		op.timeToComplete = transferTime_s;
        op.timeElapsed = 0;
		op.transferType = opType;
        op.opId = nextItemId++;

        if (obj == 0)
        {
            op.platformId = parent->mnID;
            op.childId = -1;
        }
        else if (obj->parent != 0)
        {
            op.platformId = obj->parent->mnID;
            op.childId = obj->mnID;
        }
        else
        {
            op.platformId = obj->mnID;
            op.childId = -1;
        }

		ops.push_back(op);

		msg = strutil::format("%s (%s) - Starting op with %s\n", 
			obj->mzUnit.c_str(), obj->mzClass.c_str(), op.item.c_str());

		success = true;
	}

//	//tcMessageInterface::Get()->ChannelMessage("Info", msg, obj->GetAlliance());
	
	return success;
}

/**
* @return true if operation found and canceled, false otherwise
*/
bool tcStores::CancelOperation(unsigned char id)
{
    int nOps = (int)ops.size();
    for (int n=nOps-1; n>=0; n--)
    {
        if (ops[n].opId == id)
        {
            switch (ops[n].transferType)
            {
            case StoreOperation::MOVE:
                {
                // add op to move items back into this stores
                unsigned int myIndex = GetMyStoresIndex();
                float transferTime_s = ops[n].timeElapsed;
                AddOperation(ops[n].item, myIndex, ops[n].quantity, transferTime_s, StoreOperation::MOVE, parent);
                }
                break;
            case StoreOperation::REFUEL: 
            case StoreOperation::LOAD:
                AddItems(ops[n].item, ops[n].quantity); // instant cancel for these for now
                break;
            case StoreOperation::UNLOAD:
                break; // instant cancel for unload for now
            }

            ops.erase(ops.begin()+n);
            return true;
        }
    }

    return false;
}

/**
* Complete load or unload operation, updating stores and launcher
*/
void tcStores::CompleteOperation(tcStores::StoreOperation& op)
{
    std::shared_ptr<tcGameObject> obj = op.GetObj();
    

    if (obj == 0) // object left or destroyed
    {
        AddItems(op.item, op.quantity);
        return;
    }

    if (op.transferType == StoreOperation::MOVE)
    {
        CompleteMoveOperation(op, obj);
        return;
    }
     
    std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(op.launcherIdx);
    assert(launcher || (op.transferType == StoreOperation::REFUEL));
    if (!launcher && (op.transferType != StoreOperation::REFUEL)) return;

    if (op.transferType == StoreOperation::LOAD)
    {
		launcher->SetChildQuantity(launcher->mnCurrent + op.quantity);
    }
	else if (op.transferType == StoreOperation::REFUEL)
	{
		if (std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(obj))
		{
			platform->fuel_kg += float(op.quantity);
			float fuelCapacity_kg = platform->GetFuelCapacity();
			if (platform->fuel_kg > fuelCapacity_kg)
			{
				platform->fuel_kg = fuelCapacity_kg;
			}
			platform->SetRefueling(false);
		}
	}
    else if (op.transferType == StoreOperation::DEFUEL)
    {
		if (std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(obj))
		{
			platform->fuel_kg -= float(op.quantity);
			if (platform->fuel_kg < 0)
			{
				platform->fuel_kg = 0;
			}
			platform->SetRefueling(false);
            AddItems(op.item, op.quantity);
		}
    }
    else // (op.transferType == StoreOperation::UNLOAD)
    {
        assert(op.transferType == StoreOperation::UNLOAD);
        assert(op.quantity < std::numeric_limits<short>::max());
        assert(launcher->mnCurrent >= short(op.quantity));
        op.quantity = std::min(op.quantity, (unsigned long)launcher->mnCurrent);
        AddItems(op.item, op.quantity);
        launcher->SetChildQuantity(launcher->mnCurrent - short(op.quantity));
    }

}

void tcStores::CompleteMoveOperation(tcStores::StoreOperation& op, std::shared_ptr<tcGameObject> obj)
{
    std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(obj);
    if (platform == 0)
    {
        assert(false);
        AddItems(op.item, op.quantity);
        return;
    }

    std::shared_ptr<tcStores> stores = platform->GetMagazine(op.launcherIdx);

    if (stores == 0)
    {
        assert(false);
        AddItems(op.item, op.quantity);
        return;
    }

    if (!stores->IsCompatible(op.item))
    {
        assert(false); // should have already check for this
        AddItems(op.item, op.quantity);
        return;
    }

    stores->AddItems(op.item, op.quantity);
}

/**
* @return current quantity of item available in magazine
* Modified to use mask with ? and * characters. If more than one item match, this only returns info
* on the first match
*/
unsigned long tcStores::CurrentItemQuantity(const std::string& itemMask, std::string& matchingItem) const
{
    std::string s;

    for (size_t n=0; n<stores.size(); n++)
    {
        s = stores[n].className.c_str();

//        if (s.Matches(itemMask.c_str()))
        if(strutil::wildcard_match(s,itemMask))
        {
            matchingItem = s.c_str(); // handles soft match with ?,*
            return stores[n].quantity;
        }
    }

    return 0;
}

/**
* @return current quantity of stores, not including incoming unloads
* @see tcStores::IncomingQuantity
*/
unsigned long tcStores::CurrentQuantity() const
{
    unsigned long currentCount = 0;
    for (size_t n=0; n<stores.size(); n++)
    {
        currentCount += stores[n].quantity;
    }

    return currentCount;
}


/**
* Helper method to support operations between tcStores and 
* child object of parent. 
* @return host parent (of stores) if child is 0, child if child is valid (if e.g. this is flightport stores and child is an aircraft in the flightport), 0 otherwise
*/
std::shared_ptr<tcGameObject> tcStores::GetChildOrParent(std::shared_ptr<tcGameObject> child)
{
    assert(parent);
    
    if ((child == 0) || (child == parent))
    {
        return parent;
    }
    else if (parent->IsChild(child))
    {
        return child;
    }
    else
    {
        fprintf(stderr, "tcStores::GetChildOrParent - Child not found\n"); 
        return 0;
    }
}

/**
* @return true if stores operation is allowed between this stores obj and destination obj 
*/
bool tcStores::StoresOperationAllowed(std::shared_ptr<tcPlatformObject> destination) const
{
    assert(parent != 0);

    return (destination == parent) || 
        ((destination != 0) && (destination->IsChild(parent) || parent->IsChild(destination)));
}

std::shared_ptr<tcStoresDBObject> tcStores::GetDatabaseObject() const
{
	return storesDBObj;
}

/**
* Uses linear search
* @return database object for item or 0 if not found
*/
std::shared_ptr<tcDatabaseObject> tcStores::GetDatabaseObjectForItem(const std::string& item) const
{
    for (size_t n=0; n<stores.size(); n++)
    {
        if (stores[n].className == item)
        {
            return stores[n].GetDatabaseObject();
        }
    }

    return 0;    
}

const std::string& tcStores::GetDisplayName() const
{
	assert(storesDBObj != 0);

	return storesDBObj->displayName;
}

const std::string& tcStores::GetFilledStatusString() const
{
    static std::string s;

    s.clear();

    if (storesDBObj->capacity > 0)
    {
        s += strutil::format("C: %03.1f%%", 100.0f*float(CurrentQuantity())/float(storesDBObj->capacity));
    }

    if (storesDBObj->maxVolume_m3 > 0)
    {
        s += strutil::format(" V: %03.1f%%", 100.0f*volume_m3/float(storesDBObj->maxVolume_m3));
    }

    if (storesDBObj->maxWeight_kg > 0)
    {
        s += strutil::format(" W: %03.1f%%", 100.0f*weight_kg/float(storesDBObj->maxWeight_kg));
    }

    return s;
}

unsigned long tcStores::GetFreeCapacityForItem(float itemWeight_kg, float itemVolume_m3) const
{
    assert(storesDBObj);
	assert((storesDBObj->capacity >= CurrentQuantity()) || (storesDBObj->capacity == 0));

    long countCapacity = (storesDBObj->capacity > 0) ? (long)storesDBObj->capacity : std::numeric_limits<long>::max();
        
    long freeCapacity = countCapacity - CurrentQuantity();

    long volumeCapacity = std::numeric_limits<long>::max();
    if ((storesDBObj->maxVolume_m3 > 0) && (itemVolume_m3 > 0))
    {
        volumeCapacity = floorf((storesDBObj->maxVolume_m3 - volume_m3) / itemVolume_m3);
        freeCapacity = std::min(freeCapacity, volumeCapacity);
    }

    long weightCapacity = std::numeric_limits<long>::max();
    if ((storesDBObj->maxWeight_kg > 0) && (itemWeight_kg > 0))
    {
        weightCapacity = floorf((storesDBObj->maxWeight_kg - weight_kg) / itemWeight_kg);
        freeCapacity = std::min(freeCapacity, weightCapacity);
    }

    return (freeCapacity >= 0) ? (unsigned long)freeCapacity : 0;
}

const tcStores::StoreItemInfo& tcStores::GetItemInfo(size_t idx) const
{
    static StoreItemInfo info;
    if (idx < stores.size())
    {
        info.className = stores[idx].className;
        info.quantity = stores[idx].quantity;
        info.id = stores[idx].itemId;
        return info;
    }
    else
    {
        info.className.clear();
        info.quantity = 0;
        info.id = 0;
        return info;
    }

}

const std::string& tcStores::GetItemName(unsigned int idx) const
{
	static std::string errorString = "Error";

	if (idx >= stores.size())
	{
		return errorString;
	}
	else
	{
		return stores[idx].className;
	}
}

/**
* @return list of items/qtys of ongoing move operations
*/
const std::vector<tcStores::StoreItemInfo>& tcStores::GetMoveSummary() const
{
    static std::vector<tcStores::StoreItemInfo> moveSummary;
    moveSummary.clear();

    if (parent->IsEditMode()) return moveSummary;

    int nOps = (int)ops.size();
    for (int n=nOps-1; n>=0; n--)
    {
        if ((ops[n].transferType == StoreOperation::MOVE) && (ops[n].timeToComplete > 0))
        {
            StoreItemInfo info;
            info.className = ops[n].item;
            info.quantity = ops[n].quantity;
            info.id = ops[n].opId;

            moveSummary.push_back(info);
        }
    }

    return moveSummary;
}

/**
* @return index of this stores within parent
*/
size_t tcStores::GetMyStoresIndex() const
{
    assert(parent != 0);

    size_t nStores = parent->GetMagazineCount();
    for (size_t n=0; n<nStores; n++)
    {
        if (parent->GetMagazine(n) == shared_from_this())
        {
            return n;
        }
    }

    assert(false); // not found
    return 99;
}


unsigned int tcStores::GetNumberItemTypes() const
{
	return stores.size();
}


std::shared_ptr<tcGameObject> tcStores::GetParent() const
{
    return parent;
}

/**
* @return quantity of stores being unloaded into stores
* @see tcStores::CurrentQuantity
*/
unsigned long tcStores::IncomingQuantity() const
{
    unsigned long currentCount = 0;

    for (size_t k=0; k<ops.size(); k++)
    {
        if (ops[k].transferType == StoreOperation::UNLOAD)
        {
            currentCount += ops[k].quantity;
        }
    }

	return currentCount;
}

/**
*
*/
bool tcStores::IsCompatible(const std::string& item) const
{
    assert(storesDBObj);
    
    size_t nCompatible = storesDBObj->compatibleItems.size();
    
    /* if no compatible items are entered, all items are compatible.
    ** This can be used for airfield depots or other general storage */
    if (nCompatible == 0) return true;
    
    for (size_t n=0; n<nCompatible; n++)
    {
        if (storesDBObj->compatibleItems[n] == item) return true;
    }
    return false;
}

/**
* Only checks quantity restrictions, not weight or volume. Stores capacity of zero means unlimited capacity.
*/
bool tcStores::IsFull() const
{
    unsigned long currentQuantity = CurrentQuantity();
	unsigned long incomingQuantity = IncomingQuantity();

    return (storesDBObj->capacity > 0) && ((currentQuantity + incomingQuantity) >= storesDBObj->capacity);
}

/**
* Loads exactly one item into launcher
*/
bool tcStores::LoadLauncher(unsigned int idx, const std::string& item, 
        std::shared_ptr<tcGameObject> child, unsigned int maxToLoad)
{
    if (item.size() == 0) return false;

    if ( std::shared_ptr<tcAirObject> air = std::dynamic_pointer_cast<tcAirObject>(child))
    {
        if (air->MaintenanceHold()) return false;
    }

    std::shared_ptr<tcGameObject> obj = GetChildOrParent(child);
    
    if (obj == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot load launcher, no access to magazine\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());

		return false;
	}


    std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(idx);
    assert(launcher);
    if (!launcher) return false;

    if ((obj->parent == 0) && (!launcher->isReloadable))
    {
        std::string s = strutil::format("%s (%s) - Launcher doesnt allow underway reload\n",
            obj->mzUnit.c_str(), obj->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // launcher not empty
    }

	if (launcher->mnCurrent)
	{
		/* For non-empty launcher, same type can be loaded to "top off" launcher.
		** TODO In some cases partial loads should be restricted.
		*/
		if (launcher->GetChildClassName() != item)
		{
            std::string s = strutil::format("%s (%s) - Cannot load non-empty launcher\n",
                obj->mzUnit.c_str(), obj->mzClass.c_str());
//            //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

			return false; // launcher not empty
		}
    }

    float loadTime_s = 0;
    float cycleTime_s = 0;
    unsigned int launcherCapacity = launcher->GetCapacityForItem(item, loadTime_s, cycleTime_s);
    
    if (launcherCapacity == 0)
    {
        std::string s = strutil::format("%s (%s) - Incompatible item for launcher\n",
            obj->mzUnit.c_str(), obj->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // item not compatible with launcher  
    }

	int maxLoadQuantity = (int)launcherCapacity - launcher->mnCurrent;
	if (maxLoadQuantity <= 0)
	{
        std::string s = strutil::format("%s (%s) - Launcher full\n",
            obj->mzUnit.c_str(), obj->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

		return false;
	}

    if (maxLoadQuantity > (int)maxToLoad) maxLoadQuantity = (int)maxToLoad;



    std::vector<StoreItem>::iterator iter;
    bool found = false;
    int nStores = (int)stores.size();
    unsigned long loadQuantity = 0;
    for (int k=nStores-1; (k>=0) && !found; k--)
    {
        if (stores[k].className == item)
        {
            found = true;
            assert(stores[k].quantity);
            if (stores[k].quantity >= (unsigned)maxLoadQuantity)
            {
                loadQuantity = (unsigned)maxLoadQuantity;
            }
            else
            {
                loadQuantity = stores[k].quantity;
            }
            stores[k].quantity -= loadQuantity;
            if (stores[k].quantity == 0)
            {
                stores.erase(stores.begin()+k);
            }
        }
    }

    if (!found)
    {
        std::string s = strutil::format("%s (%s) - No %s in %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // stores not available
    }

	float databaseLoadTime_s = (loadTime_s + storesDBObj->moveTime);
	float transferTime_s = (tcOptions::Get()->fastLoad == 0) ? databaseLoadTime_s : std::min(30.0f, databaseLoadTime_s);
	bool result = AddOperation(item, idx, loadQuantity, transferTime_s, StoreOperation::LOAD, obj);


	if (result == true)
	{
        std::string s = strutil::format("%s (%s) - Loading %s in %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

		// SetChildClass empties launcher, so save current quantity, call SetChildClass,
		// then call SetChildQuantity to restore
		int currentLauncherQuantity = launcher->mnCurrent;
		launcher->SetChildClass(item);
		launcher->SetChildQuantity(currentLauncherQuantity); // note this calls SetLoadState(false)

		launcher->SetLoadState(true);
	}

    return result;
}

/**
* @return quantity to move
* Used to transfer items from one stores to another
*/
unsigned int tcStores::MoveStores(const std::string& item, unsigned int quantity, std::shared_ptr<tcPlatformObject> destination, unsigned int storesIdx)
{
    bool moveAllowed = StoresOperationAllowed(destination);
    
    if (!moveAllowed)
	{
        std::string s = strutil::format("%s (%s) - Cannot transfer item, no access to destination stores\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
		return 0;
	}

    assert(destination != 0); // checked by StoresOperationsAllowed
    std::shared_ptr<tcStores> destStores = destination->GetMagazine(storesIdx);
    if (destStores == 0)
    {
        assert(false);
        std::string s = strutil::format("%s (%s) - Cannot transfer item, invalid stores idx\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
		return 0;
    }

    if (destStores->IsCompatible(item))
    {
        std::shared_ptr<tcDatabaseObject> itemData = tcDatabase::Get()->GetObject(item);

        if (itemData == 0)
        {
            fprintf(stderr, "tcStores::MoveStores -- item not found in database (%s)\n", item.c_str());
            return 0; // not found in database
        }

        unsigned long freeCapacity = destStores->GetFreeCapacityForItem(itemData->weight_kg, itemData->volume_m3);        
        unsigned int moveQuantity = (unsigned int)std::min((unsigned long)quantity, freeCapacity);

        float transferTime_s = storesDBObj->moveTime + destStores->GetDatabaseObject()->moveTime;
        RemoveItems(item, moveQuantity);

        AddOperation(item, storesIdx, moveQuantity, transferTime_s, StoreOperation::MOVE, destination);

        return moveQuantity;
    }
    else
    {
        std::string s = strutil::format("%s (%s) - Cannot transfer item, not compatible with destination stores\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
        return 0;
    }


}


/**
* Used to load a non-launcher item (e.g. fuel) from stores to platform
*/
bool tcStores::LoadOther(const std::string& item, unsigned long quantity, std::shared_ptr<tcGameObject> child)
{
    long maxWeightFuel_kg = 9999999;
    if ( std::shared_ptr<tcAirObject> air = std::dynamic_pointer_cast<tcAirObject>(child))
    {
        if (air->MaintenanceHold()) return false;
        maxWeightFuel_kg = long(air->mpDBObject->maxTakeoffWeight_kg - air->GetTotalWeight());
    }

    std::shared_ptr<tcGameObject> obj = GetChildOrParent(child);
    
    if (obj == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot load item, no access to stores\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());

		return false;
	}
	
	std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(obj);
	if (platform == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot load item, not platform object\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

		return false;
	}

	// only support refueling right now
	if (item != "Fuel")
	{
		assert(false);
		return false;
	}

	long fuelNeeded_kg = long(ceilf((platform->GetFuelCapacity() - platform->fuel_kg)));
    fuelNeeded_kg = std::min(fuelNeeded_kg, maxWeightFuel_kg);

    if (fuelNeeded_kg <= 0)
    {
        std::string s;
        if (fuelNeeded_kg != maxWeightFuel_kg)
        {
            s = strutil::format("%s (%s) - platform already refueled\n",
                obj->mzUnit.c_str(), obj->mzClass.c_str());
        }
        else
        {
            s = strutil::format("%s (%s) - additional fuel would exceed max takeoff weight\n",
                obj->mzUnit.c_str(), obj->mzClass.c_str());
        }
        
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // item not compatible with launcher  
    }

	fuelNeeded_kg = std::min((unsigned long)fuelNeeded_kg, quantity);

    std::vector<StoreItem>::iterator iter;
    bool found = false;
    int nStores = (int)stores.size();
    unsigned long loadQuantity = 0;
    for (int k=nStores-1; (k>=0) && !found; k--)
    {
        if (stores[k].className == item)
        {
            found = true;
            assert(stores[k].quantity);
            if (stores[k].quantity >= (unsigned long)fuelNeeded_kg)
            {
                loadQuantity = fuelNeeded_kg;
            }
            else
            {
                loadQuantity = stores[k].quantity;
            }
            stores[k].quantity -= loadQuantity;
            if (stores[k].quantity == 0)
            {
                stores.erase(stores.begin()+k);
            }
        }
    }

    if (!found)
    {
        std::string s = strutil::format("%s (%s) - No %s in %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // stores not available
    }

    float transferTime_s = loadQuantity * 0.02f; // 50 kg/s refuel rate, hard-coded
	bool result = AddOperation(item, 0, loadQuantity, transferTime_s, StoreOperation::REFUEL, obj);

    if (result == true)
    {
        std::string s = strutil::format("%s (%s) - Refueling\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

		platform->SetRefueling(true);
	}

    return result;
}


/**
* Used to unload a non-launcher item (e.g. fuel) from platform to stores
*/
bool tcStores::UnloadOther(const std::string& item, unsigned long quantity, std::shared_ptr<tcGameObject> child)
{
    std::shared_ptr<tcGameObject> obj = GetChildOrParent(child);
    
    if (obj == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot unload item, no access to stores\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
		return false;
	}
	
	std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(obj);
	if (platform == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot unload item, not platform object\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());
		return false;
	}

	// only support defueling right now
	if (item != "Fuel")
	{
		assert(false);
		return false;
	}

    if (!IsCompatible("Fuel")) return false;

    // don't defuel external tanks
    long maxDefuel_kg = long(ceilf(std::min(platform->mpDBObject->GetInternalFuelCapacity(), (float)platform->fuel_kg)));
    long defuel_kg = std::min(maxDefuel_kg, (long)quantity);


    float transferTime_s = float(defuel_kg) * 0.02f; // 50 kg/s refuel rate, hard-coded
	bool result = AddOperation(item, 0, defuel_kg, transferTime_s, StoreOperation::DEFUEL, obj);

    if (result == true)
    {
        std::string s = strutil::format("%s (%s) - Defueling\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());
		platform->SetRefueling(true);
	}

    return result;
}



void tcStores::SaveToPython(scriptinterface::tcScenarioLogger& logger)
{
	std::string s;

	for (size_t k=0; k<stores.size(); k++)
	{
		s=strutil::format("SM.AddToUnitMagazine(\"%s\", '%s', %d)", parent->mzUnit.c_str(),
			stores[k].className.c_str(), stores[k].quantity);
		logger.AddScenarioText(s);
	}
}

/**
*
*/
void tcStores::SetParent(std::shared_ptr<tcPlatformObject> obj)
{
    parent = obj;
}

/**
* Unloads all items from launcher
*/
bool tcStores::UnloadLauncher(unsigned int idx, std::shared_ptr<tcGameObject> child, unsigned long maxToUnload)
{
    std::shared_ptr<tcGameObject> obj = GetChildOrParent(child);
    
    if (obj == 0)
	{
        std::string s = strutil::format("%s (%s) - Cannot unload launcher, no access to magazine\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
//        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());

		return false;
	}

    std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(idx);    
    assert(launcher);
    if (!launcher) return false;

    if (launcher->mnCurrent == 0)
    {
        std::string s = strutil::format("%s (%s) - Cannot unload empty launcher\n",
            obj->mzUnit.c_str(), obj->mzClass.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // launcher not empty
    }

    if ((obj->parent == 0) && (!launcher->isReloadable))
    {
        std::string s = strutil::format("%s (%s) - Launcher doesnt allow underway unload\n",
            obj->mzUnit.c_str(), obj->mzClass.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false; // launcher not empty
    }

    std::string item = launcher->GetChildClassName();

    if (!IsCompatible(item))
    {
        std::string s = strutil::format("%s (%s) - No magazine to hold %s from %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false;
    }


    if (IsFull())
    {
        std::string s = strutil::format("%s (%s) - Magazine full, cannot unload %s from %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

        return false;
    }

	float transferTime_s = (tcOptions::Get()->fastLoad == 0) ? storesDBObj->moveTime : std::min(10.0f, storesDBObj->moveTime);
    bool result = AddOperation(item, idx, std::min((unsigned long)launcher->mnCurrent, maxToUnload), transferTime_s, StoreOperation::UNLOAD, obj);

	if (result == true)
	{
		launcher->SetLoadState(true);

        std::string s = strutil::format("%s (%s) - Unloading %s to %s\n", 
            obj->mzUnit.c_str(), obj->mzClass.c_str(), 
            item.c_str(), storesDBObj->displayName.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, obj->GetAlliance());

	}

    return result;
}

/**
*
*/
void tcStores::Update(double t)
{
    float dt = float(t - lastUpdate);
    if ((dt < 1.0) && (!parent->IsEditMode())) return;
    
	UpdateAutomation();

    lastUpdate = t;

    int nOps = (int)ops.size();
    for (int n=nOps-1; n>=0; n--)
    {
        ops[n].timeToComplete -= dt;
        ops[n].timeElapsed += dt;
        if ((ops[n].timeToComplete <= 0) || (parent->IsEditMode()))
        {
            CompleteOperation(ops[n]);
            ops.erase(ops.begin()+n);
        }
    }

}

void tcStores::UpdateAutomation()
{
    const int finishOp = 86; // 定义一个常量，表示操作完成的阶段

    // 首先验证有效的操作目标，否则将阶段设置为finishOp
    for (size_t n=0; n<automationOps.size(); n++) // 遍历所有的自动化操作
    {
        AutomationOperation& op = automationOps[n]; // 获取当前操作的引用
        std::shared_ptr<tcGameObject> obj = GetChildOrParent(op.obj); // 获取操作目标对象
        if (obj == 0) op.stage = finishOp; // 如果对象无效，将操作阶段设置为完成
    }

    for (size_t n=0; n<automationOps.size(); n++) // 再次遍历所有的自动化操作
    {
        AutomationOperation& op = automationOps[n]; // 获取当前操作的引用
        if (op.stage == 0) // 如果操作处于初始阶段
        {
            // 所有操作都从完全卸载平台开始
            if (UnloadPlatform(op.obj)) // 尝试卸载平台
            {
                op.stage = 1;	// 如果成功，将阶段设置为1
            }
            else
            {
                op.stage = finishOp; // 如果失败，将阶段设置为完成
            }
        }
        else if (op.stage == 1) // 如果操作处于阶段1
        {
            if (AllLaunchersEmpty(op.obj)) // 如果所有发射器都为空
            {
                if (op.type == "Empty") // 如果操作类型为"Empty"
                {
                    op.stage = finishOp; // 将阶段设置为完成
                }
                else
                {
                    if (LoadPlatform(op.obj, op.type)) // 尝试加载平台
                    {
                        op.stage = 2; // 如果成功，将阶段设置为2
                    }
                    else
                    {
                        op.stage = finishOp; // 如果失败，将阶段设置为完成
                    }
                }
            }
        }
        else if (op.stage == 2) // 如果操作处于阶段2
        {
            if (AllLaunchersReady(op.obj)) // 如果所有发射器都已准备好
            {
                op.stage = finishOp; // 将阶段设置为完成
            }
        }
        else
        {
            op.stage = finishOp; // 对于其他阶段，也将阶段设置为完成
        }
    }

    // 移除所有处于完成阶段（op.stage == finishOp）的自动化操作
    std::vector<AutomationOperation> temp; // 创建一个临时向量用于存储未完成的操作

    for (size_t n=0; n<automationOps.size(); n++) // 遍历所有的自动化操作
    {
        if (automationOps[n].stage != finishOp) // 如果操作未完成
        {
            temp.push_back(automationOps[n]); // 将操作添加到临时向量中
        }
        else
        {
            // 构造一个消息字符串，表示操作已完成
            std::string s = strutil::format("%s (%s) - Completed loadout automation (%s)\n",
                                            parent->mzUnit.c_str(), parent->mzClass.c_str(), automationOps[n].type.c_str());
            // 下面的代码被注释掉了，原本用于发送消息到某个频道
            //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
        }
    }
    automationOps = temp; // 将未完成的操作从临时向量复制回原始向量


}
/**
* Gets best calculated generic loadout based on target type
* @param type "AAW" targetMask = AIR_TARGET; "ASuW" targetMask = SURFACE_TARGET; "ASW" targetMask = SUBSURFACE_TARGET;
*	"Strike" targetMask = LAND_TARGET; "Nuclear"
*/
/**
 * 根据目标类型获取最佳通用装备配置
 * @param obj 平台对象指针
 * @param type 目标类型字符串，如"AAW"、"ASuW"、"ASW"、"Strike"、"Nuclear"
 * @param bestForLauncher 存储每个发射器的最佳武器信息的向量
 * @return 如果成功获取配置，则返回true；否则返回false
 */
bool tcStores::GetBestGenericLoadout(std::shared_ptr<tcPlatformObject> obj, const std::string& type, std::vector<WeaponInfo>& bestForLauncher)
{
    // 断言确保对象不为空，若为空则直接返回false
    assert(obj != 0);
    if (obj == 0) return false;

    int targetMask = 0; // 目标掩码，用于筛选武器
    bool allowNuclear = false; // 是否允许使用核武器

    // 根据目标类型设置目标掩码和核武器使用权限
    if (type == "AAW") targetMask = AIR_TARGET; // 空中目标
    else if (type == "ASuW") targetMask = SURFACE_TARGET; // 水面目标
    else if (type == "ASW") targetMask = SUBSURFACE_TARGET; // 水下目标
    else if (type == "Strike") targetMask = LAND_TARGET; // 陆地目标
    else if (type == "Nuclear")
    {
        targetMask = (AIR_TARGET | SURFACE_TARGET | LAND_TARGET); // 所有类型目标
        allowNuclear = true; // 允许使用核武器
    }

    // 用于装载干扰弹和照明弹的标志
    bool haveFlares = false;
    bool haveChaff = false;

    // 清空最佳武器信息向量
    bestForLauncher.clear();
    // 获取发射器数量
    size_t nLaunchers = obj->GetLauncherCount();

    // 遍历每个发射器
    for (size_t n=0; n<nLaunchers; n++)
    {
        std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n); // 获取当前发射器
        size_t nTypes = launcher->GetCompatibleCount(); // 获取当前发射器兼容的武器类型数量
        assert(nTypes > 0); // 断言确保至少有一种兼容的武器类型

        // 初始化最佳武器信息
        WeaponInfo best;
        best.capacity = launcher->GetCompatibleQuantity(0); // 设置初始容量为第一种兼容武器的数量
        best.quantity = CurrentItemQuantity(launcher->GetCompatibleName(0), best.name); // 获取当前存储数量

        GetWeaponInfo(best); // 获取最佳武器的详细信息

        // 遍历其他武器类型并进行比较
        for (size_t k=1; k<nTypes; k++)
        {
            WeaponInfo candidate; // 候选武器信息
            candidate.capacity = launcher->GetCompatibleQuantity(k); // 设置候选武器的容量
            candidate.quantity = CurrentItemQuantity(launcher->GetCompatibleName(k), candidate.name); // 获取候选武器的当前存储数量
            GetWeaponInfo(candidate); // 获取候选武器的详细信息

            // 判断候选武器是否更适合当前任务
            bool betterMissionFit = ((best.targetFlags & targetMask) == 0) &&
                                    ((candidate.targetFlags & targetMask) != 0); // 最佳武器不适合而候选武器适合
            bool worseMissionFit = ((best.targetFlags & targetMask) != 0) &&
                                   ((candidate.targetFlags & targetMask) == 0); // 最佳武器适合而候选武器不适合
            bool betterRange = candidate.range_km > best.range_km; // 候选武器射程更远
            bool isAvailable = (candidate.quantity > 0) && (!candidate.isNuclear || allowNuclear); // 候选武器可用且符合核武器使用权限

            bool betterNuclear = allowNuclear && (!best.isNuclear && candidate.isNuclear); // 允许使用核武器且候选武器是核武器而最佳武器不是

            // 判断候选武器是否优于最佳武器
            bool better = isAvailable &&
                          (betterMissionFit || (!worseMissionFit && betterRange) ||
                           (!worseMissionFit && betterNuclear));

            // 如果需要装载干扰弹和照明弹，则进行特殊处理
            if (candidate.miscType.size() > 0)
            {
                bool isChaff = (candidate.miscType == "Chaff"); // 是否为干扰弹
                bool isFlares = (candidate.miscType == "Flare"); // 是否为照明弹

                // 如果尚未装载干扰弹且当前候选为干扰弹，则标记为已装载并认为候选更优
                if (isChaff && (!haveChaff))
                {
                    haveChaff = true;
                    better = true;
                }
                // 如果尚未装载照明弹且当前候选为照明弹，则标记为已装载并认为候选更优
                if (isFlares && (!haveFlares))
                {
                    haveFlares = true;
                    better = true;
                }
            }

            // 如果候选武器更优，则更新最佳武器信息
            if (better)
            {
                best = candidate;
            }
        }

        // 将最佳武器信息添加到向量中
        bestForLauncher.push_back(best);
    }

    // 如果对象是飞行器，则进行起飞重量检查
    if ( std::shared_ptr<tcAirObject> air = std::dynamic_pointer_cast<tcAirObject>(obj))
    {
        // 计算最大起飞重量（假设已加满燃油）
        float maxLoadWeight_kg = air->mpDBObject->maxTakeoffWeight_kg - air->mpDBObject->weight_kg -
                                 air->mpDBObject->mfFuelCapacity_kg;

        // 如果超重，则迭代移除最大容量的物品直到重量符合要求
        bool iteratingForWeight = true;
        unsigned int nIterations = 0; // 迭代次数
        const unsigned int maxIterations = 32; // 最大迭代次数

        while (iteratingForWeight && (nIterations++ < maxIterations))
        {
            float loadWeight_kg = 0; // 当前装载重量
            size_t bestIdx = 0; // 最佳移除索引
            size_t bestCapacity = 0; // 最佳移除容量
            float bestWeight = 99999.9f; // 最佳移除物品的单重（用于比较）

            // 遍历每个发射器的最佳武器信息，计算总重量并找出最佳移除项
            for (size_t n=0; n<nLaunchers; n++)
            {
                // std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n); // 已在外部循环中获取，此处省略

                size_t capacity = bestForLauncher[n].capacity; // 当前武器的容量
                float weight_kg = bestForLauncher[n].weight_kg; // 当前武器的单重
                loadWeight_kg += weight_kg * float(capacity); // 计算当前武器的总重量并累加到总装载重量中

                // 找出容量最大或（容量相同但单重最轻）的物品作为最佳移除项
                if ((capacity > bestCapacity) || ((capacity == bestCapacity) && (weight_kg < bestWeight)))
                {
                    bestIdx = n;
                    bestCapacity = capacity;
                    bestWeight = weight_kg;
                }

            }

            // 如果当前装载重量不超过最大起飞重量，则停止迭代
            if (loadWeight_kg <= maxLoadWeight_kg)
            {
                iteratingForWeight = false;
            }
            else
            {
                // 如果最佳移除项的容量大于0，则减少其容量
                if (bestForLauncher[bestIdx].capacity > 0) bestForLauncher[bestIdx].capacity--;
            }

        }

        // 如果达到最大迭代次数仍未找到满足条件的装载配置，则输出错误信息并返回false
        if (nIterations >= maxIterations)
        {
            fprintf(stderr, "(%s: %s) 未能找到满足起飞重量限制的装载配置。可能是数据库错误。\n",
                    air->mzClass.c_str(), air->mzUnit.c_str());
            return false;
        }
    }

    // 成功获取装载配置，返回true
    return true;
}


/**
* @param type is either an auto-setup name like Empty, AAW, etc.; or a reference to
* a SetupName in the platform_setup table
*/
bool tcStores::LoadPlatform(std::shared_ptr<tcGameObject> child, const std::string& type)
{
    std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(child));

    // check that magazine is accessible (child hasn't taken off yet)
    if (obj == 0)
    {
        std::string s = strutil::format("%s (%s) - Automation failed: Cannot load platform, no access to magazine\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
        return false;
    }

    // verify all launchers are empty
    if (!AllLaunchersEmpty(child))
    {
        std::string s = strutil::format("%s (%s) - Automation failed: Cannot load platform, launchers not empty\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
        return false;
    }

    // verify launchers are all valid
    size_t nLaunchers = obj->GetLauncherCount();
    for (size_t n=0; n<nLaunchers; n++)
    {
        std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);    
        assert(launcher);

        if (launcher == 0)
        {
            std::string s = strutil::format("%s (%s) - Automation failed: Cannot load platform, corrupt launcher\n",
                parent->mzUnit.c_str(), parent->mzClass.c_str());
            //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
            return false;
        }
    }


    bool genericLoadout = 
        (type == "AAW") || 
        (type == "ASuW") ||
        (type == "ASW") ||
        (type == "Strike") ||
        (type == "Nuclear");

    if (!genericLoadout)
    {   // assume DB platform_setup loadout
        return LoadAirLoadout(child, type);
    }

    std::vector<WeaponInfo> bestForLauncher;
    bool success = GetBestGenericLoadout(obj, type, bestForLauncher);
    if (success)
    {
        // load launcher with best results
        for (size_t n=0; n<nLaunchers; n++)
        {
            // load launcher with best results
            LoadLauncher(n, bestForLauncher[n].name, child, bestForLauncher[n].capacity);
        }


        obj->SetLoadoutTag(type);
        return true;
    }
    else
    {
        return false;
    }
}


/**
* Intended to be called in edit mode, mirroring behavior of LoadPlatform, except with no
* limits on "stores" quantity of items available
*/
bool tcStores::LoadPlatformEditMode(std::shared_ptr<tcGameObject> child, const std::string& type)
{
	std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(child);
	
    if (!tcGameObject::IsEditMode()) return false;

	// verify launchers are all valid
	size_t nLaunchers = obj->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);    
		assert(launcher);
		if (launcher == 0) return false;
	}


	// for each launcher find the best loadout based on mission type, weapon range, weapon availability
	int targetMask = 0;
    bool allowNuclear = false;
	
	if (type == "AAW") targetMask = AIR_TARGET;
	else if (type == "ASuW") targetMask = SURFACE_TARGET;
	else if (type == "ASW") targetMask = SUBSURFACE_TARGET;
	else if (type == "Strike") targetMask = LAND_TARGET;
    else if (type == "Nuclear")
    {
        targetMask = (AIR_TARGET | SURFACE_TARGET | LAND_TARGET);
        allowNuclear = true;
    }
	else 
    {   // assume DB air loadout
        return LoadAirLoadoutEditMode(child, type);
    }

    // to load an assortment of CM
    bool haveFlares = false;
    bool haveChaff = false;

    const size_t nLots = 9999;

    std::vector<WeaponInfo> bestForLauncher;

	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   
		size_t nTypes = launcher->GetCompatibleCount();
		assert(nTypes > 0);

        WeaponInfo best;
        best.name = launcher->GetCompatibleName(0);
        best.capacity = launcher->GetCompatibleQuantity(0);
        best.quantity = nLots;

		GetWeaponInfo(best);

		// cycle through other types and compare
		for (size_t k=1; k<nTypes; k++)
		{
            WeaponInfo candidate;
            candidate.name = launcher->GetCompatibleName(k);
            candidate.capacity = launcher->GetCompatibleQuantity(k);
            candidate.quantity = nLots;
			GetWeaponInfo(candidate);

			bool betterMissionFit = ((best.targetFlags & targetMask) == 0) && 
				((candidate.targetFlags & targetMask) != 0);
			bool worseMissionFit = ((best.targetFlags & targetMask) != 0) &&
				((candidate.targetFlags & targetMask) == 0);
//			bool fitsMission = ((candidate.targetFlags & targetMask) != 0);
			bool betterRange = candidate.range_km > best.range_km;
            bool isAvailable = (candidate.quantity > 0) && (!candidate.isNuclear || allowNuclear);
            
            bool betterNuclear = allowNuclear && (!best.isNuclear && candidate.isNuclear);

			bool better = isAvailable && 
				         (betterMissionFit || (!worseMissionFit && betterRange) || 
                         (!worseMissionFit && betterNuclear));

            // section to load both chaff and flares
            if (candidate.miscType.size() > 0)
            {
                bool isChaff = (candidate.miscType == "Chaff");
                bool isFlares = (candidate.miscType == "Flare");
               
                if (isChaff && (!haveChaff))
                {
                    haveChaff = true;
                    better = true;
                }
                if (isFlares && (!haveFlares))
                {
                    haveFlares = true;
                    better = true;
                }
            }

			if (better)
			{
                best = candidate;
			}
		}

        bestForLauncher.push_back(best);
	}

    if ( std::shared_ptr<tcAirObject> air = std::dynamic_pointer_cast<tcAirObject>(obj))
    {
        // check if overweight for takeoff (assuming fully fueled)
        float maxLoadWeight_kg = air->mpDBObject->maxTakeoffWeight_kg - air->mpDBObject->weight_kg -
            air->mpDBObject->mfFuelCapacity_kg;

        // if overweight, iterate through, removing one of biggest capacity item until weight is okay
        bool iteratingForWeight = true;
        unsigned int nIterations = 0;
        const unsigned int maxIterations = 32;

        while (iteratingForWeight && (nIterations++ < maxIterations))
        {
            float loadWeight_kg = 0;
            size_t bestIdx = 0;
            size_t bestCapacity = 0;
            float bestWeight = 99999.9f;

            for (size_t n=0; n<nLaunchers; n++)
            {
//                std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   

                size_t capacity = bestForLauncher[n].capacity;
                float weight_kg = bestForLauncher[n].weight_kg;
                loadWeight_kg += weight_kg * float(capacity);
                
                if ((capacity > bestCapacity) || ((capacity == bestCapacity) && (weight_kg < bestWeight)))
                {
                    bestIdx = n;
                    bestCapacity = capacity;
                    bestWeight = weight_kg;
                }

            }
            
            if (loadWeight_kg <= maxLoadWeight_kg)
            {
                iteratingForWeight = false;
            }
            else
            {
                if (bestForLauncher[bestIdx].capacity > 0) bestForLauncher[bestIdx].capacity--;
            }

        }

        if (nIterations >= maxIterations)
        {
            fprintf(stderr, "LoadPlatformEditMode: (%s: %s) Failed to find loadout satisfying takeoff weight restriction."
                " Could be caused by database error\n", 
                air->mzClass.c_str(), air->mzUnit.c_str());
            return false;
        }
        
    }

    // load launcher with best results
    for (size_t n=0; n<nLaunchers; n++)
	{
        std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);
        assert(launcher != 0);

		// load launcher with best results
        std::string item = bestForLauncher[n].name;
        unsigned int launcherCapacity = launcher->GetCapacityForItem(item);

        launcher->SetChildClass(item);
		launcher->SetChildQuantity(launcherCapacity); // note this calls SetLoadState(false)
	}

	return true;
}

/**
* @param groupSize multiplier to ensure that quantity is available for all platforms in group
* @return true if loadout found, false if no loadout satisfying weight restriction
*/
bool tcStores::GetBestLoadout(std::shared_ptr<tcAirObject> obj, const std::vector<LauncherLoadout>& launcherLoadout,
                              std::vector<WeaponInfo>& bestForLauncher, unsigned int groupSize)
{
    bestForLauncher.clear();
    assert(obj != 0);
    if (obj == 0) return false;



    size_t nLaunchers = (size_t)obj->GetLauncherCount();
        
    for (size_t n=0; n<nLaunchers; n++)
	{
        unsigned int launcherId = obj->mpDBObject->launcherId[n]; // launcher id for this launcher
        WeaponInfo weaponInfo;
//		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   
		
        // search through each entry in the launcherLoadout list, checking for multiple entries for alternate loads
        bool searching = true;
        for (size_t opt=0; (opt<launcherLoadout.size()) && searching; opt++)
        {
            if (launcherLoadout[opt].launcherId == launcherId)
            {
                std::string itemName = launcherLoadout[opt].item;
                if ((itemName != "Empty") && (itemName.size() > 0))
                {
                    weaponInfo.capacity = launcherLoadout[opt].quantity;
                    weaponInfo.quantity = CurrentItemQuantity(launcherLoadout[opt].item, weaponInfo.name);
                    if (weaponInfo.quantity >= groupSize*weaponInfo.capacity)
                    {
                        searching = false;
                        GetWeaponInfo(weaponInfo);
                    }
                }
                else
                {
                    weaponInfo.name = "Empty";
                    weaponInfo.capacity = 0;
                    weaponInfo.weight_kg = 0;
                    searching = false;
                }
            }
        }

        bestForLauncher.push_back(weaponInfo);
    }

    // check if overweight for takeoff (assuming fully fueled)
    float maxLoadWeight_kg = obj->mpDBObject->maxTakeoffWeight_kg - obj->mpDBObject->weight_kg -
        obj->mpDBObject->mfFuelCapacity_kg;

    float loadWeight_kg = 0;

    for (size_t n=0; n<nLaunchers; n++)
    {
//        std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   

        size_t capacity = bestForLauncher[n].capacity;
        float weight_kg = bestForLauncher[n].weight_kg;
        loadWeight_kg += weight_kg * float(capacity);
    }

    if (loadWeight_kg > maxLoadWeight_kg)
    {
        fprintf(stderr, "(%s: %s) Failed to find loadout satisfying takeoff weight restriction."
            " Could be caused by database error (loadout name: %s)\n", 
            obj->mzClass.c_str(), obj->mzUnit.c_str(), "unavailable");
        return false;
    }
    else
    {
        return true;
    }

}

/**
* Loads an air loadout according to database data
* Only applies to air platforms
*/
bool tcStores::LoadAirLoadout(std::shared_ptr<tcGameObject> child, const std::string& type)
{
	std::shared_ptr<tcAirObject> obj = std::dynamic_pointer_cast<tcAirObject>(GetChildOrParent(child));
    if (obj == 0) return false;

    // assume that we've already done checks for magazine accessible, launcher empty, launchers valid
	// assume that we've checked for auto-loadout type

    const tcLoadoutData* loadoutInfo = obj->mpDBObject->GetLoadout(type);
    if (loadoutInfo == 0)
    {
        fprintf(stderr, "tcStores::LoadAirLoadout - Loadout not found, air unit: %s, loadout: %s\n",
            obj->mzUnit.c_str(), type.c_str());
        assert(false);
        return false;
    }

	// for each launcher find the first available option
    std::vector<WeaponInfo> bestForLauncher;
    bool success = GetBestLoadout(obj, loadoutInfo->launcherLoadout, bestForLauncher);
    if (!success)
    {
        return false;
    }

    size_t nLaunchers = (size_t)obj->GetLauncherCount();
    assert(bestForLauncher.size() == nLaunchers);

    // load launcher with best results
    for (size_t n=0; n<nLaunchers; n++)
	{
//		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   

		// load launcher with best results
        LoadLauncher(n, bestForLauncher[n].name, child, bestForLauncher[n].capacity);
	}

    obj->SetLoadoutTag(type);

	return true;
}

/**
* Loads an air loadout according to database data
* Only applies to air platforms
* Edit mode version that doesn't check stores availability
*/
bool tcStores::LoadAirLoadoutEditMode(std::shared_ptr<tcGameObject> child, const std::string& type)
{
    std::shared_ptr<tcAirObject> obj = std::dynamic_pointer_cast<tcAirObject>(child);
    if (obj == 0) return false;

    if (!tcGameObject::IsEditMode()) return false;

    // assume that we've already done checks for magazine accessible, launcher empty, launchers valid
	// assume that we've checked for auto-loadout type

    const tcLoadoutData* loadoutInfo = obj->mpDBObject->GetLoadout(type);
    if (loadoutInfo == 0)
    {
        fprintf(stderr, "tcStores::LoadAirLoadout - Loadout not found, air unit: %s, loadout: %s\n",
            obj->mzUnit.c_str(), type.c_str());
        assert(false);
        return false;
    }

	// for each launcher find the first available option
    std::vector<WeaponInfo> bestForLauncher;
    
    size_t nLaunchers = (size_t)obj->GetLauncherCount();
        
    for (size_t n=0; n<nLaunchers; n++)
	{
        unsigned int launcherId = obj->mpDBObject->launcherId[n]; // launcher id for this launcher
        WeaponInfo weaponInfo;
//		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   
		
        // search through each entry in the launcherLoadout list, checking for multiple entries for alternate loads
        bool searching = true;
        for (size_t opt=0; (opt<loadoutInfo->launcherLoadout.size()) && searching; opt++)
        {
            if (loadoutInfo->launcherLoadout[opt].launcherId == launcherId)
            {
                std::string itemName = loadoutInfo->launcherLoadout[opt].item;
                if ((itemName != "Empty") && (itemName.size() > 0))
                {
                    weaponInfo.name = itemName;
                    weaponInfo.capacity = loadoutInfo->launcherLoadout[opt].quantity;
                    weaponInfo.quantity = 99999;
                    if (weaponInfo.quantity >= weaponInfo.capacity)
                    {
                        searching = false;
                        GetWeaponInfo(weaponInfo);
                    }
                }
                else
                {
                    weaponInfo.name = "Empty";
                    weaponInfo.capacity = 0;
                    weaponInfo.weight_kg = 0;
                    searching = false;
                }
            }
        }

        bestForLauncher.push_back(weaponInfo);
    }


    // load launcher with best results
    for (size_t n=0; n<nLaunchers; n++)
	{
        std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);
        assert(launcher != 0);

		// load launcher with best results
        std::string item = bestForLauncher[n].name;
        unsigned int launcherCapacity = launcher->GetCapacityForItem(item);

        launcher->SetChildClass(item);
		launcher->SetChildQuantity(launcherCapacity); // note this calls SetLoadState(false)
	}

	return true;
}


void tcStores::GetWeaponInfo(WeaponInfo& info)
{
	info.range_km = 0;
	info.targetFlags = 0;
    info.miscType.clear();
    info.isNuclear = false;
    info.weight_kg = 0;

    tcDatabase* database = tcDatabase::Get();
	std::shared_ptr<tcDatabaseObject> databaseObj = database->GetObject(info.name);
	if (databaseObj == 0) return;

    info.weight_kg = databaseObj->weight_kg;

    if (std::shared_ptr<tcWeaponDBObject> weaponObj =  std::dynamic_pointer_cast<tcWeaponDBObject>(databaseObj))
	{
		info.targetFlags = weaponObj->targetFlags;
        info.range_km = weaponObj->maxRange_km;

        // check if this is nuclear based on weapon energy
        info.isNuclear = weaponObj->IsNuclear();
	}
    else if (std::shared_ptr<tcFuelTankDBObject> fuelTank =  std::dynamic_pointer_cast<tcFuelTankDBObject>(databaseObj))
    {
        info.weight_kg += fuelTank->fuelCapacity_kg; // assume will be fully fueled
    }
    else if (std::shared_ptr<tcCounterMeasureDBObject> cm =  std::dynamic_pointer_cast<tcCounterMeasureDBObject>(databaseObj))
    {
        info.miscType = cm->subType;
    }


}

float tcStores::GetWeightKg() const
{
	return weight_kg;
}


bool tcStores::UnloadPlatform(std::shared_ptr<tcGameObject> child)
{
	std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(child));
    
    if (obj == 0)
    {
        std::string s = strutil::format("%s (%s) - Automation failed: Cannot unload platform, no access to magazine\n",
            parent->mzUnit.c_str(), parent->mzClass.c_str());
        //tcMessageInterface::Get()->ChannelMessage("Info", s, parent->GetAlliance());
        return false;
	}
	
	size_t nLaunchers = obj->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);    
		assert(launcher);

		if ((launcher != 0) && (launcher->mnCurrent > 0))
		{
			UnloadLauncher(n, child);
		}
	}

	obj->SetLoadoutTag("Empty");

	return true;
}

/**
* @return true if any ops for child are active
*/
bool tcStores::HasActiveOp(std::shared_ptr<tcGameObject> child) const
{
	std::vector<AutomationOperation>::const_iterator opIter;
    for (opIter = automationOps.begin(); opIter != automationOps.end(); ++opIter)
    {
        if (opIter->obj == child)
        {
			return true;
        }
    }

	return false;
}

/**
* @return true if all launchers of child are empty
*/
bool tcStores::AllLaunchersEmpty(std::shared_ptr<tcGameObject> child)
{
	std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(child));
    if (obj == 0)
    {
        return false;
    }

	size_t nLaunchers = obj->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);    
		assert(launcher);

		if ((launcher != 0) && (launcher->mnCurrent > 0))
		{
			return false;
		}
	}

	return true;
}

/**
* @return true if all launchers of child are full and ready
*/
bool tcStores::AllLaunchersReady(std::shared_ptr<tcGameObject> child)
{
	std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(child));
    if (obj == 0)
    {
        return false;
    }

	size_t nLaunchers = obj->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);    
		assert(launcher);

		if ((launcher != 0) && ((launcher->mnCurrent == 0) || (launcher->IsLoading())))
		{
			return false;
		}
	}

	return true;
}

/**
* @return true if op found
*/
bool tcStores::FindLauncherOp(std::shared_ptr<tcGameObject> obj, unsigned int launcherIdx, unsigned int& opId)
{
    for (size_t n=0; n<ops.size(); n++)
    {
        if ((ops[n].GetObj() == obj) && (ops[n].launcherIdx == launcherIdx))
        {
            opId = ops[n].opId;
            return true;
        }
    }

    opId = 0;
    return false;
}

const tcStores::StoreOperation* tcStores::FindOpById(unsigned int opId) const
{
    for (size_t n=0; n<ops.size(); n++)
    {
        if (ops[n].opId == opId)
        {
            return &ops[n];
        }
    }
    return 0;
}

/**
* @param nuclear true to only look at nuclear weapons
* @return bitwise OR of all target flags from weapons available in stores that
* are compatible with child's launchers
*/
int tcStores::GetAvailableTargetFlags(std::shared_ptr<tcGameObject> child, bool nuclear)
{
	std::shared_ptr<tcPlatformObject> obj = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(child));
    
	// check that magazine is accessible (child hasn't taken off yet)
    if (obj == 0) return 0;
	
	size_t nLaunchers = obj->GetLauncherCount();

	int netTargetFlags = 0;

	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = obj->GetLauncher(n);   

		size_t nTypes = launcher->GetCompatibleCount();
		for (size_t k=0; k<nTypes; k++)
		{
            WeaponInfo info;
            info.quantity = CurrentItemQuantity(launcher->GetCompatibleName(k), info.name);
			if (info.quantity > 0)
			{
				GetWeaponInfo(info);

                if (!nuclear)
                {
				    netTargetFlags |= info.targetFlags;
                }
                else if (info.isNuclear)
                {
                    netTargetFlags |= info.targetFlags;
                }
			}
		}
	}

	return netTargetFlags;
}

bool tcStores::HasNuclearWeapons()
{
    for (size_t n=0; n<stores.size(); n++)
    {
        std::shared_ptr<tcDatabaseObject> databaseObj = stores[n].GetOrLoadDatabaseObject();
        
        if (std::shared_ptr<tcWeaponDBObject> weaponObj =  std::dynamic_pointer_cast<tcWeaponDBObject>(databaseObj))
	    {
            if (weaponObj->IsNuclear()) return true;
        }
    }

    return false;
}


/**
* Used for good guess as to which magazine should manage automation operation
* for obj.
* @return true if stores has any items that are compatible with obj
*/
bool tcStores::HasStoresForThisObject(std::shared_ptr<tcGameObject> obj)
{
	std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(obj));
	if (platform == 0)
	{
		assert(false);
		return false;
	}

    std::string s;
	size_t nLaunchers = platform->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(n);    
		assert(launcher);
		
		size_t nCompatible = launcher->GetCompatibleCount();
		for (size_t k=0; k<nCompatible; k++)
		{
			if (CurrentItemQuantity(launcher->GetCompatibleName(k), s) > 0)
			{
				return true;
			}
		}
	}

	return false;
}

/**
* @return true if any of obj items are compatible with stores
*/
bool tcStores::CanUnloadThisObject(std::shared_ptr<tcGameObject> obj)
{
	std::shared_ptr<tcPlatformObject> platform = std::dynamic_pointer_cast<tcPlatformObject>(GetChildOrParent(obj));
	if (platform == 0)
	{
		assert(false);
		return false;
	}

    std::string s;
	size_t nLaunchers = platform->GetLauncherCount();
	for (size_t n=0; n<nLaunchers; n++)
	{
		std::shared_ptr<tcLauncher> launcher = platform->GetLauncher(n);    
		assert(launcher);

        if ((launcher->mnCurrent > 0) && IsCompatible(launcher->GetChildClassName()))
        {
            return true;
        }
		
	}

	return false;
}


/**
* @return true if adequate stores present to supply loadout
* Entire quantity (or alternate item quantity) must be available, otherwise returns false
*/
bool tcStores::HasStoresForLoadout(const tcLoadoutData& loadoutData) const
{
    std::map<unsigned int, bool> hasStores;

    for (size_t n=0; n<loadoutData.launcherLoadout.size(); n++)
    {
        hasStores[loadoutData.launcherLoadout[n].launcherId] = false;
    }

    for (size_t n=0; n<loadoutData.launcherLoadout.size(); n++)
    {
        if (!hasStores[loadoutData.launcherLoadout[n].launcherId])
        {
            std::string itemName = loadoutData.launcherLoadout[n].item;
            std::string matchingItem;
            unsigned int nAvailable = CurrentItemQuantity(itemName, matchingItem);
            if (nAvailable >= loadoutData.launcherLoadout[n].quantity)
            {
                hasStores[loadoutData.launcherLoadout[n].launcherId] = true;
            }
        }
    }

    std::map<unsigned int, bool>::iterator iter;
    for (iter = hasStores.begin(); iter != hasStores.end(); ++iter)
    {
        if (iter->second == false)
        {
            return false;
        }
    }

    return true;
}

/**
* Update weight and volume occupied by current stores, should be
* called whenever stores have changed
*/
void tcStores::UpdateWeightAndVolume()
{
    volume_m3 = 0;
    weight_kg = 0;

    for (size_t n=0; n<stores.size(); n++)
    {
        std::shared_ptr<tcDatabaseObject> databaseObj = stores[n].GetOrLoadDatabaseObject();

	    if (databaseObj != 0)
        {
            weight_kg += float(stores[n].quantity) * databaseObj->weight_kg;
            volume_m3 += float(stores[n].quantity) * databaseObj->volume_m3;
        }
    }
}

/**
* For multiplayer, for obj's that are flightport objects, only objects in
* the ALERT15 position are allowed to interact with the stores
* (partially a bandwidth issue vs. realism)
* @returns true if op is allowed
*/
bool tcStores::ValidateOpObject(std::shared_ptr<tcGameObject> obj)
{
	if (obj == 0) return true;

	/* if parent of this stores has a flightport, and obj is a child of parent,
    ** then return true if child is in a ALERT15 position, otherwise return true always
	*/
    std::shared_ptr<tcFlightOpsObject> flightOps =  parent->GetComponent<tcFlightOpsObject>();
	if (flightOps == 0) return true;

	tcFlightPort* flightPort = flightOps->GetFlightPort();
	if (flightPort == 0) return true;

	int idx = flightPort->GetAirStateIdx(obj->mnID);
	if (idx < 0) return true;

	if (tcAirState* airState = flightPort->GetAirState(idx))
	{
		return (airState->current_location == ALERT15);
	}
	else
	{
		return true;
	}

}


/**
*
*/
tcStores::tcStores(std::shared_ptr<tcStoresDBObject> dbObj)
: storesDBObj(dbObj), lastUpdate(0), parent(0),
  volume_m3(0), weight_kg(0), nextItemId(1)
{
    assert(storesDBObj);
}

/**
*
*/
tcStores::~tcStores()
{
}


