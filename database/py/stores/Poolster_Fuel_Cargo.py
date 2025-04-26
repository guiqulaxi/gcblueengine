# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Poolster Fuel Cargo'
    dbObj.natoClass='Poolster Fuel Cargo'
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
    dbObj.displayName='Fuel Tank'
    dbObj.capacity=0
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=400000.000000
    dbObj.moveTime=300.000000
    dbObj.compatibleItems=['Fuel']
    dbObj.CalculateParams()
    return dbObj
