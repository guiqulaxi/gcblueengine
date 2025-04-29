# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcItemDBObject()
    dbObj.mzClass='Fuel'
    dbObj.natoClass='Fuel'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=5.000000
    dbObj.weight_kg=1.000000
    dbObj.volume_m3=0.329060
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='fuel.jpg'
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.CalculateParams()
    return dbObj
