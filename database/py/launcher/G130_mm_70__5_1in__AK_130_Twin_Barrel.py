import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='130 mm/70 (5.1in) AK-130 Twin Barrel'
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
    dbObj.childClassList=['130mm F-44 HE','130mm ZS-44 AA','130mm ZS-44P AA']
    dbObj.childCapacityList=[100,100,100]
    dbObj.childLoadTime_s=[50.000000,50.000000,50.000000]
    dbObj.childCycleTime_s=[1.500000,1.500000,1.500000]
    dbObj.CalculateParams()
    return dbObj
