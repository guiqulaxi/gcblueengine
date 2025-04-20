import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mk-137 SRBOC Launcher'
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
    dbObj.childClassList=['Chaff-2','Chaff-Round-1','Flare-2','Mk-186 TORCH Flare']
    dbObj.childCapacityList=[6,6,6,6]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.500000,0.500000,0.500000,0.500000]
    dbObj.CalculateParams()
    return dbObj
