# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='S-400 Triumf Store'
    dbObj.natoClass='S-400 Triumf Store'
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
    dbObj.notes='Generic stores'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Generic Stores'
    dbObj.capacity=288
    dbObj.maxVolume_m3=72.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=15.000000
    dbObj.compatibleItems=['48N6DM','48N6D','9M96','9M96E','9M96E2','40N6','40N6D']
    dbObj.CalculateParams()
    return dbObj
