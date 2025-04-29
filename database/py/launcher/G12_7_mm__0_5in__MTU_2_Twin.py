# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='12.7 mm (0.5in) MTU-2 Twin'
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
    dbObj.childClassList=['12.7mm B-30 AP','12.7mm B-32 APi']
    dbObj.childCapacityList=[17,17]
    dbObj.childLoadTime_s=[19.000000,19.000000]
    dbObj.childCycleTime_s=[0.300000,0.300000]
    dbObj.CalculateParams()
    return dbObj
