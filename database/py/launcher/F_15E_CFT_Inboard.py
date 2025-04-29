# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-15E-CFT-Inboard'
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
    dbObj.childClassList=['AIM-7F','AIM-7M','AIM-7P','AIM-7*','AIM-120A','AIM-120B','AIM-120C','AIM-120C5','AIM-120C7','AIM-120D','AIM-120*','GBU-10/B','GBU-12/B','GBU-24/B','GBU-24B/B','GBU-30','GBU-31A(v)2','GBU-31B(v)2','GBU-31C(v)4','GBU-32A(v)2','GBU-32B(v)2','GBU-32C(v)4','GBU-39 SDB','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[4,4,4,4,4,4,4,4,4,4,4,2,4,2,2,4,4,4,4,4,4,4,8,6,6,4,4]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
