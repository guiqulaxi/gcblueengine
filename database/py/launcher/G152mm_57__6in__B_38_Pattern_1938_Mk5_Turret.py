import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='152mm/57 (6in) B-38 Pattern 1938 Mk5 Turret'
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
    dbObj.childClassList=['152mm AP B-35','152mm HE OF-35','152mm SAP PB-35']
    dbObj.childCapacityList=[3,3,3]
    dbObj.childLoadTime_s=[24.000000,24.000000,24.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
