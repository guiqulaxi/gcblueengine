import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='B-52 Internal'
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
    dbObj.childClassList=['B-61 170kT','B-61*','B-83 400kT','B-83*','GBU-32A(v)2','GBU-32C(v)4','M117','M118','Mk-60 CAPTOR','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[8,8,8,8,6,6,27,7,8,27,27,18,9]
    dbObj.childLoadTime_s=[3600.000000,3600.000000,3600.000000,3600.000000,300.000000,300.000000,420.000000,300.000000,300.000000,420.000000,420.000000,360.000000,300.000000]
    dbObj.childCycleTime_s=[10.000000,10.000000,10.000000,10.000000,0.500000,0.500000,0.030000,0.030000,0.500000,0.030000,0.030000,0.030000,0.030000]
    dbObj.CalculateParams()
    return dbObj
