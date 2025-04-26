# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='127mm mk12/16 300 round'
    dbObj.natoClass='127mm mk12/16 300 round'
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
    dbObj.displayName='Deck Gun store'
    dbObj.capacity=300
    dbObj.maxVolume_m3=300.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=50.000000
    dbObj.compatibleItems=['127mm mk 32','127mm mk 34 AAC']
    dbObj.CalculateParams()
    return dbObj
