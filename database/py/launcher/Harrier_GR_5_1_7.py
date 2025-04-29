# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Harrier GR.5 1-7'
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
    dbObj.childClassList=['68mm SNEB Rockets','AIM-9*','AIM-9L','M117','Mk-81','Mk-82','Mk-83']
    dbObj.childCapacityList=[36,2,2,2,4,4,2]
    dbObj.childLoadTime_s=[240.000000,300.000000,300.000000,240.000000,360.000000,360.000000,240.000000]
    dbObj.childCycleTime_s=[0.100000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
