# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mk-12 GMLS'
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
    dbObj.childClassList=['RIM-8A','RIM-8C','RIM-8E','RIM-8F','RIM-8J','SAM-N-6b','SAM-N-6b1','SAM-N-6b1(CW)','SAM-N-6c1']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[22.000000,22.000000,22.000000,22.000000,22.000000,22.000000,22.000000,22.000000,22.000000]
    dbObj.childCycleTime_s=[3.000000,3.000000,3.000000,3.000000,3.000000,3.000000,3.000000,3.000000,3.000000]
    dbObj.CalculateParams()
    return dbObj
