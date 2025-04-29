# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Helix Torpedo Launcher'
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
    dbObj.childClassList=['APR-2E','AT-1','VTT-1','Yu-7']
    dbObj.childCapacityList=[2,2,2,2]
    dbObj.childLoadTime_s=[720.000000,720.000000,720.000000,720.000000]
    dbObj.childCycleTime_s=[15.000000,15.000000,15.000000,15.000000]
    dbObj.CalculateParams()
    return dbObj
