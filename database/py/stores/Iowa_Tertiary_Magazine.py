# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Iowa Tertiary Magazine'
    dbObj.natoClass='Iowa Tertiary Magazine'
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
    dbObj.notes='20k rounds of 40mm.  500 per gun for 20mm, and 50 rounds, so 25k 20mm.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Tertiary Amunition Bunker'
    dbObj.capacity=45000
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['20mm HE-T x10','40mm HE Mk1 Md1 x8']
    dbObj.CalculateParams()
    return dbObj
