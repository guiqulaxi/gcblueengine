# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='STWS Mk2 Triple'
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
    dbObj.childClassList=['Mk-46 LWT Mod2']
    dbObj.childCapacityList=[3]
    dbObj.childLoadTime_s=[30.000000]
    dbObj.childCycleTime_s=[15.000000]
    dbObj.CalculateParams()
    return dbObj
