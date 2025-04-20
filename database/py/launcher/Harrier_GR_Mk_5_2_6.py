import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Harrier GR.Mk.5 2-6'
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
    dbObj.childClassList=['AIM-9*','AIM-9B','AIM-9D','AIM-9E','AIM-9G','AIM-9H','AIM-9L','AIM-9M','AIM-9N','AIM-9P','AIM-9X','GBU-1/B','GBU-12/B','GBU-16/B','GBU-24/B','GBU-24B/B','GBU-27','GBU-28B/B','GBU-31A(v)2','GBU-31C(v)4','GBU-32A(v)2','GBU-32C(v)4','M117','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2,2,2,6,6,4,2,2,2,6,2,2,2,2,6,6,6,4,2]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
