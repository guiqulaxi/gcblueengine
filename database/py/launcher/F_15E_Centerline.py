# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-15E-Centerline'
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
    dbObj.childClassList=['GBU-10/B','GBU-12/B','GBU-28B/B','GBU-30','GBU-31(V)1/B','GBU-31A(v)2','GBU-31C(v)4','GBU-32','GBU-32A(v)2','GBU-32B(v)2','GBU-32C(v)4','GBU-39 SDB']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,1,1,1,1,4]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,900.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
