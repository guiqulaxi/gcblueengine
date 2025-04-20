import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='100mm/70 (3.9in) CM-5 Turret'
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
    dbObj.childClassList=['100mm F-55 HE','100mm OF-55 FRAG','100mm ZS-55P AA']
    dbObj.childCapacityList=[2,2,2]
    dbObj.childLoadTime_s=[7.300000,7.300000,7.300000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
