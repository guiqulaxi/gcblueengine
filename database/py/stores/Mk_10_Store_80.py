# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Mk-10 Store 80'
    dbObj.natoClass='Mk-10 Store 80'
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
    dbObj.notes='Mk-10 Rotary Store'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Mk-10 Missile Store'
    dbObj.capacity=80
    dbObj.maxVolume_m3=80.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-2B','RIM-2C','RIM-2F','SAM-N-7 BT-3A','SAM-N-7 BW-1','RIM-67A','RIM-67B','RIM-67C','RIM-67D']
    dbObj.CalculateParams()
    return dbObj
