import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Alpha2'
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
    dbObj.childClassList=['*Magic*','310 liter tank','450 liter tank','68mm SNEB Rockets','AGM-65*','AIM-9*','Durandal','Hydra-70 rocket','IRIS-T','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[2,2,2,72,2,2,2,38,2,2,2,2]
    dbObj.childLoadTime_s=[360.000000,240.000000,240.000000,240.000000,360.000000,360.000000,240.000000,240.000000,360.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,0.100000,1.000000,1.000000,0.050000,0.100000,1.000000,0.050000,0.050000,0.050000]
    dbObj.CalculateParams()
    return dbObj
