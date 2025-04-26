# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='P-3 Bay'
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
    dbObj.childClassList=['Mk-36 DST','Mk-40 DST','Mk-41 DST','Mk-44','Mk-46 Mod5','Mk-50','Mk-54','Mk-82','Mk-83']
    dbObj.childCapacityList=[6,3,2,8,8,8,8,8,8]
    dbObj.childLoadTime_s=[300.000000,300.000000,300.000000,660.000000,660.000000,660.000000,660.000000,660.000000,660.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
