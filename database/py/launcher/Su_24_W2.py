# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Su-24 W2'
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
    dbObj.childClassList=['3000 liter tank','FAB-500','KAB-500L','Kh-59MK']
    dbObj.childCapacityList=[2,2,2,2]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
