# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcItemDBObject()
    dbObj.mzClass='Spare parts'
    dbObj.natoClass='Spare parts'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=10000.000000
    dbObj.weight_kg=100.000000
    dbObj.volume_m3=2.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='null'
    dbObj.iconFileName='unknown.jpg'
    dbObj.mz3DModelFileName='null'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.CalculateParams()
    return dbObj
