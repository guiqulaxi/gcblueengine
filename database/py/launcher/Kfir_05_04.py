import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Kfir 05-04'
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
    dbObj.childClassList=['Derby','Gabriel Mk3A/S','Mk-83','Python 5','SPICE-1000','Tanque de 300 galones']
    dbObj.childCapacityList=[2,2,4,2,2,2]
    dbObj.childLoadTime_s=[600.000000,1200.000000,1200.000000,600.000000,1200.000000,1200.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,1.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
