# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A-4M 1-5'
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
    dbObj.childClassList=['50mm (2in) FFAR Rockets','AGM-12A','AGM-12B','AGM-45A','AGM-45B','AGM-65A','AGM-65B','AGM-65D','AGM-65E','AGM-65F','AGM-65G','AGM-65J','AGM-65K','AIM-9B','AIM-9D','AIM-9E','AIM-9G','AIM-9H','AIM-9J','AIM-9L','AIM-9M','AIM-9N','AIM-9P','AIM-9P4','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-81','Mk-82']
    dbObj.childCapacityList=[114,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,8,4,2]
    dbObj.childLoadTime_s=[480.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,420.000000,420.000000,480.000000,480.000000]
    dbObj.childCycleTime_s=[0.100000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
