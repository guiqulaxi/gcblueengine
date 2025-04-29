# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='533mm French L Torp Tubes x5'
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
    dbObj.childClassList=['L3 Mod2','L3','L5 Mod 4','L5 Mod4']
    dbObj.childCapacityList=[5,5,5,5]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[4.000000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
