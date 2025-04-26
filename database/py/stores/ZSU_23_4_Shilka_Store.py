# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='ZSU-23-4 Shilka Store'
    dbObj.natoClass='ZSU-23-4 Shilka Store'
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
    dbObj.notes='Cannot achieve 3400rm rate of fire, so, rounds grouped into 8 round bursts, and counted as one.  Ergo a 2,000 round ammo supply is only 250 rounds in GCB.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Generic Stores'
    dbObj.capacity=250
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=15.000000
    dbObj.compatibleItems=['Gen23AA']
    dbObj.CalculateParams()
    return dbObj
