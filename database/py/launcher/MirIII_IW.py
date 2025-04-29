# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='MirIII IW'
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
    dbObj.childClassList=['AIM-9M','GB-200','GB-500','R.550 Magic']
    dbObj.childCapacityList=[2,4,2,2]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[0.000000,0.000000,0.000000,0.000000]
    dbObj.CalculateParams()
    return dbObj
