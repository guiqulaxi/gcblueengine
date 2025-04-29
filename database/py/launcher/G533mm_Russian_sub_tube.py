# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='533mm Russian sub tube'
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
    dbObj.childClassList=['3M10 Granat','3M10 Granat(n)','3M54E Klub Alfa','3M80M Moskit-M','53-56','53-56V','53-65KE','53-65M','RPK-6 Vodopod','SAET-60M','SET-65','SET-65M','Shkval','TEST-71','TEST-71ME','TEST-71MKE','USET-80']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    dbObj.childLoadTime_s=[480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000,480.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
