import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='A-6C IWing'
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
    dbObj.childClassList=['Mk-84','Mk-83','Mk-82','Mk-81','M118','M117','AGM-12A','AGM-12B','AGM-12C','AGM-45A','AGM-45B','AIM-9D','AIM-9E','AIM-9L','AIM-9*','Mk-40 FFAR','Mk 16 Zuni FFAR','Mk 71 Zuni WAFAR','300 gallon tank','Mk-25 Mine','Mk-36 Mod1 Mine','Mk-36 Mod2 Mine','Mk-39 Mine','Mk-56 Mine','Mk-36 DST','Mk-40 DST','Mk-41 DST','Mk-59 DST','B-28*','B-43*','B-57*','B-61*']
    dbObj.childCapacityList=[2,6,12,12,2,4,2,2,2,4,4,2,2,2,2,38,8,8,2,2,2,2,2,2,12,12,2,6,2,2,2,2]
    dbObj.childLoadTime_s=[240.000000,240.000000,240.000000,240.000000,240.000000,240.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,180.000000,180.000000,180.000000,120.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,3600.000000,3600.000000,3600.000000,3600.000000]
    dbObj.childCycleTime_s=[0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,0.100000,1.000000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,0.100000,10.000000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
