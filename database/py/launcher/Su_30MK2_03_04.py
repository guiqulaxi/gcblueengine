import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='Su-30MK2 03-04'
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
    dbObj.childClassList=['KAB-500Kr','R-27R','R-77','R-77T','Kh-29T','Kh-31A','Kh-31P']
    dbObj.childCapacityList=[2,2,2,2,2,2,2]
    dbObj.childLoadTime_s=[1200.000000,600.000000,600.000000,600.000000,1200.000000,1200.000000,1200.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,2.000000,2.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
