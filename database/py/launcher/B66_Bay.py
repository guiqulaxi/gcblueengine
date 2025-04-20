import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='B66 Bay'
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
    dbObj.childClassList=['AP 1500','B-28*','B-39*','B-43*','B-53*','B-57*','B-61*','B-83*','GP HC 8000','GP MC 1000','GP MC 1900','GP MC 250','GP MC 4000','GP MC 500','M117','M118','Mk-10 Mod5 Mine','Mk-10 Mod6 Mine','Mk-25 Mine','Mk-36 DST','Mk-36 Mod1 Mine','Mk-36 Mod2 Mine','Mk-39 Mine','Mk-40 DST','Mk-41 DST','Mk-56 Mine','Mk-59 DST','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[7,5,1,5,1,14,14,4,1,10,6,14,2,14,14,3,6,6,5,14,5,5,5,10,5,5,12,14,14,10,5]
    dbObj.childLoadTime_s=[120.000000,4500.000000,3600.000000,4500.000000,3600.000000,6900.000000,6900.000000,4200.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,120.000000,140.000000,140.000000,140.000000,120.000000,140.000000,140.000000,140.000000,120.000000,120.000000,140.000000,120.000000,120.000000,120.000000,120.000000,120.000000]
    dbObj.childCycleTime_s=[0.100000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
