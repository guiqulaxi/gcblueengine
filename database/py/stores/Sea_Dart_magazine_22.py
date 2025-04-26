# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Sea Dart magazine 22'
    dbObj.natoClass='Sea Dart magazine 22'
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
    dbObj.displayName='Sea Dart Storage Racking'
    dbObj.capacity=22
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['Sea Dart Mod0','Sea Dart Mod2']
    dbObj.CalculateParams()
    return dbObj
