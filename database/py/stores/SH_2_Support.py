# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='SH-2 Support'
    dbObj.natoClass='SH-2 Support'
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
    dbObj.displayName='SH-2 Helo Support Stores'
    dbObj.capacity=14718
    dbObj.maxVolume_m3=18.146999
    dbObj.maxWeight_kg=20120.000000
    dbObj.moveTime=45.000000
    dbObj.compatibleItems=['Fuel','DIFAR*','DICASS*','LOFAR*','120 gallon tank','Mk-50','Mk-46 Mod5','AGM-119B']
    dbObj.CalculateParams()
    return dbObj
