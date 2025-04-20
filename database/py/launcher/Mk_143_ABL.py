import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mk-143 ABL'
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
    dbObj.childClassList=['BGM-109 TASM','BGM-109 TLAM','BGM-109G TLAM-N']
    dbObj.childCapacityList=[4,4,4]
    dbObj.childLoadTime_s=[3600.000000,3600.000000,3600.000000]
    dbObj.childCycleTime_s=[3.000000,3.000000,3.000000]
    dbObj.CalculateParams()
    return dbObj
