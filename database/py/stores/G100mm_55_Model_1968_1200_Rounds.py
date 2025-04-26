# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='100mm/55 Model 1968 1200 Rounds'
    dbObj.natoClass='100mm/55 Model 1968 1200 Rounds'
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
    dbObj.capacity=1200
    dbObj.maxVolume_m3=1200.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['100mm OEA F1 HE','100mm OPF F4 PFHE']
    dbObj.CalculateParams()
    return dbObj
