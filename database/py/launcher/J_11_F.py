# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='J-11 F'
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
    dbObj.childClassList=['FAB-100','FAB-250','FAB-500','PL-12','PL-8*','R-27R','R-73M']
    dbObj.childCapacityList=[8,4,4,4,4,4,4]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
