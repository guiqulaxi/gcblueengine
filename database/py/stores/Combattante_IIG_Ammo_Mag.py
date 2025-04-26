# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Combattante IIG Ammo Mag'
    dbObj.natoClass='Combattante IIG Ammo Mag'
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
    dbObj.displayName='Ammo Magazine'
    dbObj.capacity=480
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=60.000000
    dbObj.compatibleItems=['76mm HE-MOM','76mm HE-SAPOM','40 mm L70 HE x5']
    dbObj.CalculateParams()
    return dbObj
