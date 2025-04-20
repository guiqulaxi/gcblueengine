import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='B-1B Bay'
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
    dbObj.childClassList=['B-83*','GBU-31A(v)2','GBU-31C(v)4','Mk-82','Mk-84']
    dbObj.childCapacityList=[8,8,8,27,8]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[10.000000,0.100000,0.100000,0.030000,0.100000]
    dbObj.CalculateParams()
    return dbObj
