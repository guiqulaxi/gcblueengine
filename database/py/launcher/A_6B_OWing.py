# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A-6B OWing'
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
    dbObj.childClassList=['Mk-84','Mk-83','Mk-82','Mk-81','M118','M117','AGM-45A','AGM-45B','AGM-78A','AGM-78B','AGM-78C','AGM-78D','300 gallon tank']
    dbObj.childCapacityList=[2,6,12,12,2,4,2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,120.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
