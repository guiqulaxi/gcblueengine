# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-117-Bays'
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
    dbObj.childClassList=['GBU-10/B','GBU-12/B','GBU-16/B','GBU-27','GBU-30','GBU-31A(v)2','GBU-31C(v)4','AGM-65*','AGM-88*','AGM-158A JASSM']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
