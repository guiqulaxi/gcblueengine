# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F8U-2NE wings'
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
    dbObj.childClassList=['50mm (2in) FFAR Rockets','AGM-12A','AGM-12B','AGM-12C','M117','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[38,2,2,2,6,8,8,8,2,2]
    dbObj.childLoadTime_s=[180.000000,240.000000,240.000000,240.000000,240.000000,300.000000,300.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[0.100000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
