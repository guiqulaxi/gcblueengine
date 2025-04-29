# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='3/50 Mark 34'
    dbObj.natoClass=''
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=0.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=0.000000
    dbObj.height_m=0.000000
    dbObj.childClassList=['76mm Mk 27 Md1 HC','76mm Mk 31 Md1 AA VT']
    dbObj.childCapacityList=[200,200]
    dbObj.childLoadTime_s=[20.000000,20.000000]
    dbObj.childCycleTime_s=[1.200000,1.200000]
    dbObj.CalculateParams()
    return dbObj
