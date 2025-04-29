# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='114mm/43(4.5in) Mark 6'
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
    dbObj.childClassList=['114mm/53 mk6 AA','114mm/53 mk6 HE','114mm/53 mk6 SAP']
    dbObj.childCapacityList=[16,16,16]
    dbObj.childLoadTime_s=[12.000000,12.000000,12.000000]
    dbObj.childCycleTime_s=[2.500000,2.500000,2.500000]
    dbObj.CalculateParams()
    return dbObj
