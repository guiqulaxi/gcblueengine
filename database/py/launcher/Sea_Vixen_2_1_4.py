# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Sea Vixen.2 1-4'
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
    dbObj.childClassList=['68mm SNEB Rockets','FireStreak','GP MC 250','GP MC 500','Mk-81','Mk-82','RP-3 AP','RP-3 HE','Red Top']
    dbObj.childCapacityList=[36,2,2,2,2,2,8,8,2]
    dbObj.childLoadTime_s=[300.000000,360.000000,240.000000,240.000000,240.000000,240.000000,420.000000,420.000000,360.000000]
    dbObj.childCycleTime_s=[0.100000,0.200000,0.200000,0.200000,0.200000,0.200000,0.100000,0.100000,0.200000]
    dbObj.CalculateParams()
    return dbObj
