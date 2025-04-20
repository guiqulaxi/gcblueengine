import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='100mm/55 (3.9in) model 1964'
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
    dbObj.childClassList=['100mm OEA F1 HE','100mm OPF F4 PFHE']
    dbObj.childCapacityList=[35,35]
    dbObj.childLoadTime_s=[30.000000,30.000000]
    dbObj.childCycleTime_s=[0.769000,0.769000]
    dbObj.CalculateParams()
    return dbObj
