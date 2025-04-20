import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='S-3 pylon'
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
    dbObj.childClassList=['AGM-65F','AGM-65J','AGM-84A Harpoon','AGM-84C Harpoon','AGM-84D Harpoon','AGM-84F Harpoon','Mk-36 DST','Mk-40 DST','Mk-41 DST','Mk-46 Mod5','Mk-50','Mk-54','Mk-57 Mine','Mk-59 DST','Mk-60 CAPTOR','Mk-81','Mk-82','Mk-83','Mk-84']
    dbObj.childCapacityList=[3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1]
    dbObj.childLoadTime_s=[30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000,30.000000]
    dbObj.childCycleTime_s=[10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
