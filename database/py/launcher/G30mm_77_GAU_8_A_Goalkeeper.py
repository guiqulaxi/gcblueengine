# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='30mm/77 GAU-8/A Goalkeeper'
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
    dbObj.childClassList=['30mm PGU-13/B HE-I','30mm PGU-14/B API']
    dbObj.childCapacityList=[79,79]
    dbObj.childLoadTime_s=[1200.000000,1200.000000]
    dbObj.childCycleTime_s=[0.214300,0.241300]
    dbObj.CalculateParams()
    return dbObj
