# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Tornado IDS 2-8'
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
    dbObj.childClassList=['330 gallon wing tank','AGM-65D','AGM-88B','AS.34 Kormoran','AS.34 Kormoran II','Taurus KEPD 350P','Mk-81','Mk-82','Mk-83']
    dbObj.childCapacityList=[1,1,1,1,1,1,3,2,1]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.100000,0.500000,0.500000,0.500000,0.500000,0.500000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
