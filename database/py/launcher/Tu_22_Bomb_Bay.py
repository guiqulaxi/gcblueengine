import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Tu-22 Bomb Bay'
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
    dbObj.childClassList=['FAB-100','FAB-1500','FAB-250','FAB-3000','FAB-500','Kh-22M','Kh-22MP','Kh-22N']
    dbObj.childCapacityList=[36,8,36,4,24,1,1,1]
    dbObj.childLoadTime_s=[510.000000,390.000000,510.000000,300.000000,450.000000,360.000000,360.000000,360.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
