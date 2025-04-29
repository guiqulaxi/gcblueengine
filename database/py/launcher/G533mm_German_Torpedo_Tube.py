# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='533mm German Torpedo Tube'
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
    dbObj.childClassList=['A-184','DM2A1','DM2A3','DM2A4*']
    dbObj.childCapacityList=[1,1,1,1]
    dbObj.childLoadTime_s=[360.000000,360.000000,360.000000,360.000000]
    dbObj.childCycleTime_s=[4.000000,4.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
