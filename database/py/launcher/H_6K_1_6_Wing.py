import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='H-6K 1-6 Wing'
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
    dbObj.childClassList=['KD-63','YJ-1','YJ-61','YJ-62K','YJ-82K','YJ-83K','YJ-85K']
    dbObj.childCapacityList=[2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000]
    dbObj.childCycleTime_s=[0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000]
    dbObj.CalculateParams()
    return dbObj
