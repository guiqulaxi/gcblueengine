# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Exocet Single Launcher'
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
    dbObj.childClassList=['MM-38 Exocet','MM-40 B2 Exocet','MM-40 B3 Exocet','MM-40 Exocet']
    dbObj.childCapacityList=[1,1,1,1]
    dbObj.childLoadTime_s=[0.000000,0.000000,0.000000,0.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
