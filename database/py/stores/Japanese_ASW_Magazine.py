# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Japanese ASW Magazine'
    dbObj.natoClass='Japanese ASW Magazine'
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
    dbObj.displayName='ASW Magazine'
    dbObj.capacity=400
    dbObj.maxVolume_m3=120.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=45.000000
    dbObj.compatibleItems=['Mk-9 DC','Hedgehog','375mm Bofors ASRL','RUR-4A Weapon Alfa']
    dbObj.CalculateParams()
    return dbObj
