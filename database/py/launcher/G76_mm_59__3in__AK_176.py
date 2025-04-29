# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='76 mm/59 (3in) AK-176'
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
    dbObj.childClassList=['76.2mm OS-62 FRAG','76.2mm ZS-63 AA']
    dbObj.childCapacityList=[152,152]
    dbObj.childLoadTime_s=[0.000000,0.000000]
    dbObj.childCycleTime_s=[0.461500,0.461500]
    dbObj.CalculateParams()
    return dbObj
