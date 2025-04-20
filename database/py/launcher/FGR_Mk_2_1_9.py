import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='FGR.Mk.2 1-9'
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
    dbObj.childClassList=['370 gallon wing tank','AGM-45A','AGM-65D','GBU-10/B','M117','Mk-36 DST','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[2,2,2,2,6,8,12,12,6,2]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[0.200000,1.000000,1.000000,2.000000,0.200000,0.200000,0.200000,0.200000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
