# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A-10 5-7'
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
    dbObj.childClassList=['600 gallon tank','Hydra-70 rocket','M117','M118','Mk 71 Zuni WAFAR','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[2,76,8,2,8,8,6,2]
    dbObj.childLoadTime_s=[240.000000,240.000000,480.000000,240.000000,240.000000,480.000000,420.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
