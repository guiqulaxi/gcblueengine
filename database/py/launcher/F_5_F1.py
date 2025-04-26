# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-5 F1'
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
    dbObj.childClassList=['120 gallon tank','300 gallon wing tank','GBU-1/B','GBU-10/B','GBU-12/B','GBU-15/B','GBU-16/B','GBU-24/B','GBU-24B/B','GBU-27','GBU-30','GBU-31*','GBU-31C(v)4','GBU-32*','GBU-39 SDB','M117','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    dbObj.childLoadTime_s=[120.000000,120.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,180.000000,180.000000,180.000000,180.000000,180.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.030000,0.030000,0.030000,0.030000,0.030000]
    dbObj.CalculateParams()
    return dbObj
