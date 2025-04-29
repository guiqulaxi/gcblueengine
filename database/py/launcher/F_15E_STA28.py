# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-15E-STA28'
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
    dbObj.childClassList=['600 gallon tank','GBU-10/B','GBU-15/B','GBU-24/B','GBU-24B/B','GBU-30','GBU-31(V)1/B','GBU-31A(v)2','GBU-31B(v)2','GBU-31C(v)4','GBU-32','GBU-32A(v)2','GBU-32B(v)2','GBU-39 SDB','Mk-81','Mk-82','Mk-83','Mk-84','AGM-65A','AGM-65B','AGM-65D','AGM-65E','AGM-65F','AGM-65G','AGM-65J','AGM-65K','AGM-130']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2,2,2,2,2,8,6,4,2,2,2,2,2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.100000]
    dbObj.CalculateParams()
    return dbObj
