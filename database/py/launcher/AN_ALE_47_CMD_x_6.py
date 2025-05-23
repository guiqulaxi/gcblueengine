# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='AN/ALE-47 CMD x 6'
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
    dbObj.childClassList=['AN/ALE-55 FOTD','Chaff-1','Flare-1']
    dbObj.childCapacityList=[24,960,192]
    dbObj.childLoadTime_s=[3600.000000,1800.000000,1800.000000]
    dbObj.childCycleTime_s=[0.010000,0.010000,0.010000]
    dbObj.CalculateParams()
    return dbObj
