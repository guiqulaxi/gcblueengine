# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='AS565 Launcher'
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
    dbObj.childClassList=['20x102 mm burst','750 litre tank','A-244S','AS-30L','MU-90','Mistral','Mk-46 Mod5','Mk-50','Mk-54','Stingray']
    dbObj.childCapacityList=[50,1,1,1,1,8,1,1,1,1]
    dbObj.childLoadTime_s=[300.000000,600.000000,600.000000,600.000000,600.000000,300.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.250000,3.000000,3.000000,3.000000,3.000000,0.500000,3.000000,3.000000,3.000000,3.000000]
    dbObj.CalculateParams()
    return dbObj
