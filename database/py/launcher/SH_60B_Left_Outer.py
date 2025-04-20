import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='SH-60B Left Outer'
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
    dbObj.childClassList=['AGM-114 Hellfire','AGM-119B','AGM-65*','Mk-46 Mod5','Mk-50','Mk-54']
    dbObj.childCapacityList=[4,1,2,1,1,1]
    dbObj.childLoadTime_s=[300.000000,300.000000,300.000000,420.000000,420.000000,420.000000]
    dbObj.childCycleTime_s=[3.000000,10.000000,3.000000,10.000000,10.000000,10.000000]
    dbObj.CalculateParams()
    return dbObj
