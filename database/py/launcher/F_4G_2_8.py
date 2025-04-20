import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='F-4G 2-8'
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
    dbObj.childClassList=['AGM-12C','AGM-45A','AGM-45B','AGM-65D','AGM-78A','AGM-78B','AGM-78C','AGM-78D','AGM-88A','AGM-88B','AIM-4','AIM-4A','AIM-4C','AIM-4D','AIM-4E','AIM-4F','AIM-4G','AIM-9B','AIM-9D','AIM-9E','B-28*','B-43*','B-57*','B-61*','GBU-1/B','GBU-10/B','GBU-11/B','GBU-12/B','Mk-36 DST','Mk-81','Mk-82','Mk-83']
    dbObj.childCapacityList=[2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,2,2,2,2,4,2,2,2,6,6,6,6]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,1.000000,1.000000,1.000000,1.000000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000,0.200000]
    dbObj.CalculateParams()
    return dbObj
