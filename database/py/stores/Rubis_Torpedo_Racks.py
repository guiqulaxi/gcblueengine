# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Rubis Torpedo Racks'
    dbObj.natoClass='Rubis Torpedo Racks'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Torpedo Racks'
    dbObj.capacity=21
    dbObj.maxVolume_m3=42.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=360.000000
    dbObj.compatibleItems=['F-17','F-17 Mod1','F-17 Mod2','SM-39 Exocet']
    dbObj.CalculateParams()
    return dbObj
