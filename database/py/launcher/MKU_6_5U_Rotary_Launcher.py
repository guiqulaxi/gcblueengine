# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='MKU-6-5U Rotary Launcher'
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
    dbObj.childClassList=['GB-500','KAB-1500L','Kh-15','Kh-15A','Kh-15P','Kh-55SE']
    dbObj.childCapacityList=[36,12,6,6,6,6]
    dbObj.childLoadTime_s=[10800.000000,10800.000000,10800.000000,10800.000000,10800.000000,10800.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,5.000000,5.000000,5.000000,5.000000]
    dbObj.CalculateParams()
    return dbObj
