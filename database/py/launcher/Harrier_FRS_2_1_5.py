# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Harrier FRS.2 1-5'
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
    dbObj.childClassList=['AIM-120*','AIM-120B','AIM-9*','AIM-9L','ASRAAM']
    dbObj.childCapacityList=[2,2,4,4,4]
    dbObj.childLoadTime_s=[360.000000,360.000000,420.000000,420.000000,420.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
