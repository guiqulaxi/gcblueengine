# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Type 212 Torpedo Racks'
    dbObj.natoClass='Type 212 Torpedo Racks'
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
    dbObj.capacity=12
    dbObj.maxVolume_m3=36.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=360.000000
    dbObj.compatibleItems=['DM1','DM2A1','DM2A3','DM2A4.1','DM2A4.2','DM2A4.3','DM2A4.4','A-184']
    dbObj.CalculateParams()
    return dbObj
