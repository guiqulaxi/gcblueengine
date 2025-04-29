# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='P-3 9-18'
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
    dbObj.childClassList=['AIM-9*','Hydra-70 rocket','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-36 DST','Mk-40 DST','Mk-44','Mk-46 Mod5','Mk-50','Mk-54']
    dbObj.childCapacityList=[2,38,8,8,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[360.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,0.100000,0.100000,0.100000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
