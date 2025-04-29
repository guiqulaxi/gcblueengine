# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='660mm Seawolf Tube'
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
    dbObj.childClassList=['Mk-48 Mod6','Mk-57 Mine','Mk-60 CAPTOR','Mk-67 SLMM','UGM-109C','UGM-84D Harpoon']
    dbObj.childCapacityList=[1,1,1,1,1,1]
    dbObj.childLoadTime_s=[300.000000,300.000000,300.000000,300.000000,300.000000,300.000000]
    dbObj.childCycleTime_s=[4.000000,10.000000,10.000000,10.000000,4.000000,4.000000]
    dbObj.CalculateParams()
    return dbObj
