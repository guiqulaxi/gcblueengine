# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Su-17M4 Fuselage'
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
    dbObj.childClassList=['FAB-100','FAB-250','FAB-500','KAB-500Kr','S-24B 240mm','S-5K Rocket','S-5M Rocket','S-8B 80mm','S-8K 80mm']
    dbObj.childCapacityList=[12,4,4,2,2,64,64,40,40]
    dbObj.childLoadTime_s=[640.000000,360.000000,360.000000,360.000000,240.000000,240.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
