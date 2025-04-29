# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Rafale Pylon Inner Wing'
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
    dbObj.childClassList=['1250 liter tank','2000 liter tank','AGM-119*','AGM-65*','AGM-84*','AGM-88*','AIM-120*','ALARM','AM-39 Exocet','AS-30L','Durandal','GBU-10/B','GBU-12/B','MBDA Meteor','MICA*','Mk-82','Mk-83','SCALP EG']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2,2,8,2,2,2,2,8,4,2]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
