# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Tornado F3 wing shoulder'
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
    dbObj.childClassList=['AIM-9L','AIM-9M','ASRAAM','AIM-132 ASRAAM']
    dbObj.childCapacityList=[4,4,4,4]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
