# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Wichita Cargo - Fuel'
    dbObj.natoClass='Wichita Cargo - Fuel'
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
    dbObj.notes='holds 160,000 barrels of fuel.  1 barrel is 42 US gallons.  Jet fuel has a mass of roughly 3.039kg per gallon, using that for now.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Cargo'
    dbObj.capacity=0
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=20422080.000000
    dbObj.moveTime=900.000000
    dbObj.compatibleItems=[]
    dbObj.CalculateParams()
    return dbObj
