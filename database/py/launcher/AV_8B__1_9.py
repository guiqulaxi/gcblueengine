# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='AV-8B+ 1-9'
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
    dbObj.childClassList=['AIM-9*','GBU-31A(v)2','GBU-31C(v)4','GBU-32A(v)2','GBU-32C(v)4','GBU-39 SDB','Hydra-70 rocket','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-40 FFAR','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[4,2,2,2,2,6,38,8,8,72,4,4,2,2]
    dbObj.childLoadTime_s=[360.000000,300.000000,300.000000,300.000000,300.000000,360.000000,240.000000,240.000000,240.000000,240.000000,360.000000,360.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.100000,0.200000,0.200000,0.100000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
