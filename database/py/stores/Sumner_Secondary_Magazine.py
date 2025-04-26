# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Sumner Secondary Magazine'
    dbObj.natoClass='Sumner Secondary Magazine'
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
    dbObj.displayName='Secondary Amunition Magazine'
    dbObj.capacity=8500
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=28320.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['20mm HE-T','20mm HE-T x2','40mm HE Mk1 Md1 x2','76mm Mk 31 Md1 AA VT']
    dbObj.CalculateParams()
    return dbObj
