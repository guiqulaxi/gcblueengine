import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F8U FN chin'
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
    dbObj.childClassList=['50mm (2in) FFAR Rockets','68mm SNEB Rockets','AIM-9J','AIM-9L','AIM-9P','AIM-9P4','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','R.550 Magic II','R.550 Magic']
    dbObj.childCapacityList=[32,16,2,2,2,2,4,4,2,2]
    dbObj.childLoadTime_s=[180.000000,300.000000,240.000000,240.000000,240.000000,240.000000,300.000000,300.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,0.100000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
