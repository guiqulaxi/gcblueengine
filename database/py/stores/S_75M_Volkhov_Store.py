# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='S-75M Volkhov Store'
    dbObj.natoClass='S-75M Volkhov Store'
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
    dbObj.capacity=12
    dbObj.maxVolume_m3=40.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=15.000000
    dbObj.compatibleItems=['V-755']
    dbObj.CalculateParams()
    return dbObj
