import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='100 mm/70 (3.9in) AK-100'
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
    dbObj.childClassList=['100mm OF-58 FRAG','100mm ZS-58 AA','100mm ZS-58P AA']
    dbObj.childCapacityList=[46,46,46]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[1.090910,1.090910,1.090910]
    dbObj.CalculateParams()
    return dbObj
