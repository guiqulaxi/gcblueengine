import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='B-2A Bay'
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
    dbObj.childClassList=['AGM-130','AGM-158A JASSM','B-61*','B-83*','GBU-31A(v)2','GBU-31C(v)4','GBU-32A(v)2','GBU-32C(v)4','M117','M118','Mk-81','Mk-82','Mk-83','Mk-84','GBU-39 SDB']
    dbObj.childCapacityList=[8,8,8,8,8,8,8,16,26,8,40,40,18,8,40]
    dbObj.childLoadTime_s=[360.000000,480.000000,600.000000,600.000000,360.000000,360.000000,360.000000,420.000000,440.000000,360.000000,520.000000,520.000000,420.000000,360.000000,420.000000]
    dbObj.childCycleTime_s=[0.500000,1.000000,10.000000,10.000000,0.500000,0.500000,0.500000,0.500000,0.030000,0.030000,0.030000,0.030000,0.030000,0.030000,0.500000]
    dbObj.CalculateParams()
    return dbObj
