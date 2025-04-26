# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='130 mm/58 (5.1in) Type 76'
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
    dbObj.childClassList=['130mm OF-42 HE-FRAG','130mm PB-42 SAP','130mm ZS-42P AA']
    dbObj.childCapacityList=[2,2,2]
    dbObj.childLoadTime_s=[6.700000,6.700000,6.700000]
    dbObj.childCycleTime_s=[0.667000,0.667000,0.667000]
    dbObj.CalculateParams()
    return dbObj
