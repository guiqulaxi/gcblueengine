import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='30 mm/63 (1.2in) AK-230'
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
    dbObj.childClassList=['30mm Br-83 AP','30mm F-33 HE','30mm OF-83 HE-FRAG']
    dbObj.childCapacityList=[250,250,250]
    dbObj.childLoadTime_s=[600.000000,600.000000,600.000000]
    dbObj.childCycleTime_s=[0.240000,0.240000,0.240000]
    dbObj.CalculateParams()
    return dbObj
