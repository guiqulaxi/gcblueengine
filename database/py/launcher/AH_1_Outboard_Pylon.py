# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='AH-1 Outboard Pylon'
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
    dbObj.childClassList=['AGM-114 Hellfire','AIM-9D','AIM-9G','AIM-9H','AIM-9L','AIM-9M','AIM-9X','BGM-71A TOW','BGM-71E TOW 2','Hydra-70 rocket','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR']
    dbObj.childCapacityList=[4,1,1,1,1,1,1,4,4,19,4,4]
    dbObj.childLoadTime_s=[180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,240.000000,240.000000,180.000000,180.000000,180.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
