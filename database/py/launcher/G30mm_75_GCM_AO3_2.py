# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='30mm/75 GCM-AO3-2'
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
    dbObj.childClassList=['30mm/75 GCM-AO3-2 APDS','30mm/75 GCM-AO3-2 HE']
    dbObj.childCapacityList=[83,83]
    dbObj.childLoadTime_s=[120.000000,120.000000]
    dbObj.childCycleTime_s=[0.276900,0.276900]
    dbObj.CalculateParams()
    return dbObj
