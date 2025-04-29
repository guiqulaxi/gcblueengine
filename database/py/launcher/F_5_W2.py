# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-5 W2'
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
    dbObj.childClassList=['68mm SNEB Rockets','AGM-65*','AGM-65D','AIM-120*','AIM-120C','AIM-9*','AIM-9M','GBU-1/B','GBU-12/B','GBU-15/B','GBU-16/B','GBU-30','GBU-32*','GBU-39 SDB','Hydra-70 rocket','M117','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','Mk-81','Mk-82','R-27*','R-27RE']
    dbObj.childCapacityList=[36,2,2,2,2,2,2,2,2,2,2,2,2,4,38,2,8,8,2,2,2,2]
    dbObj.childLoadTime_s=[360.000000,360.000000,360.000000,30.000000,30.000000,30.000000,30.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,360.000000,360.000000,240.000000,360.000000,360.000000,240.000000,240.000000,360.000000,360.000000]
    dbObj.childCycleTime_s=[0.030000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.030000,0.030000,0.100000,0.100000,0.030000,0.030000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
