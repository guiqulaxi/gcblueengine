# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='MiG-21Bison OuterPylon'
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
    dbObj.childClassList=['FAB-100','FAB-250','FAB-500','KAB-500Kr','Kh-25MP','Kh-31P','Kh-66','PTB-400','PTB-490','R-27RE','R-27TE','R-3*','R-60','R-60M','R-73E','R-77','S-24B 240mm','S-5K 57mm','S-5K Rocket','S-5M Rocket']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,32,32,32]
    dbObj.childLoadTime_s=[180.000000,180.000000,180.000000,360.000000,360.000000,360.000000,240.000000,180.000000,180.000000,300.000000,300.000000,240.000000,360.000000,360.000000,300.000000,300.000000,180.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
