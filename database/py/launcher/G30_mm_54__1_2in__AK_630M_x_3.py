import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='30 mm/54 (1.2in) AK-630M x 3'
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
    dbObj.childClassList=['30mm OF-84 HE-FRAG AK-630M','30mm OP-84 FRAG Tracer AK-630M']
    dbObj.childCapacityList=[354,354]
    dbObj.childLoadTime_s=[30.000000,30.000000]
    dbObj.childCycleTime_s=[0.400000,0.400000]
    dbObj.CalculateParams()
    return dbObj
