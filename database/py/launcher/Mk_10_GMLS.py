# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mk-10 GMLS'
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
    dbObj.childClassList=['RIM-2B','RIM-2C','RIM-2F','RIM-67A','RIM-67B','RIM-67C','RIM-67D','SAM-N-7 BT-3A','SAM-N-7 BW-1']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
