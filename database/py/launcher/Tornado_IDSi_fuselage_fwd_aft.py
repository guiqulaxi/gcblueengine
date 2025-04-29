# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Tornado IDSi fuselage fwd/aft'
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
    dbObj.childClassList=['AGM-65D','AGM-88B','AS.34 Kormoran','AS.34 Kormoran II','Storm Shadow','GBU-10/B','GBU-15/B','GBU-16/B','GBU-24/B','GBU-24B/B','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[2,1,1,1,1,1,2,2,1,1,4,4,2,2]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
