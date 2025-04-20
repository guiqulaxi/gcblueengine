import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Mitsubishi F-2 4L-8L'
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
    dbObj.childClassList=['ASM-1','GBU-30','Mk-82']
    dbObj.childCapacityList=[2,6,6]
    dbObj.childLoadTime_s=[360.000000,360.000000,360.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000]
    dbObj.CalculateParams()
    return dbObj
