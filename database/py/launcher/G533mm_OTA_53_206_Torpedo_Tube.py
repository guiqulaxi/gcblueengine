# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='533mm OTA-53-206 Torpedo Tube'
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
    dbObj.childClassList=['53-56','53-56V','53-56VA','53-65K','53-65','USET-80']
    dbObj.childCapacityList=[1,1,1,1,1,1]
    dbObj.childLoadTime_s=[900.000000,900.000000,900.000000,900.000000,900.000000,900.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
