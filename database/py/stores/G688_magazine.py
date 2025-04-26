# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='688 magazine'
    dbObj.natoClass='688 magazine'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='null'
    dbObj.iconFileName='null'
    dbObj.mz3DModelFileName='null'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Torpedo Mag'
    dbObj.capacity=20
    dbObj.maxVolume_m3=61.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=180.000000
    dbObj.compatibleItems=[]
    dbObj.CalculateParams()
    return dbObj
