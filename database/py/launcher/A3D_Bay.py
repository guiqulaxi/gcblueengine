# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A3D Bay'
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
    dbObj.childClassList=['AP 1500','B-28*','B-43*','B-57*','B-61*','B-83*','GP MC 1000','GP MC 1900','GP MC 250','GP MC 4000','GP MC 500','M117','M118','Mk-10 Mod5 Mine','Mk-10 Mod6 Mine','Mk-25 Mine','Mk-36 DST','Mk-36 Mod1 Mine','Mk-36 Mod2 Mine','Mk-39 Mine','Mk-40 DST','Mk-41 DST','Mk-56 Mine','Mk-59 DST','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[3,2,2,8,6,1,4,2,8,1,8,6,1,2,2,2,7,2,2,2,4,2,2,5,8,8,4,2]
    dbObj.childLoadTime_s=[120.000000,3900.000000,3900.000000,5700.000000,5100.000000,3600.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,140.000000,140.000000,140.000000,120.000000,140.000000,140.000000,140.000000,120.000000,120.000000,140.000000,120.000000,120.000000,120.000000,120.000000,120.000000]
    dbObj.childCycleTime_s=[0.100000,10.000000,10.000000,10.000000,10.000000,10.000000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
