# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='688 VLS Bank'
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
    dbObj.childClassList=['UGM-109A','UGM-109B','UGM-109C','UGM-84C Harpoon']
    dbObj.childCapacityList=[6,6,6,6]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[15.000000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
