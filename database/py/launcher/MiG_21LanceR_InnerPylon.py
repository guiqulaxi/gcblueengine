import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='MiG-21LanceR InnerPylon'
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
    dbObj.childClassList=['AIM-9L','FAB-100','FAB-250','GBU-32A(v)2','GBU-32C(v)4','Kh-66','Python 3','R-60','R-60M','S-24B 240mm','S-5K 57mm','S-5K Rocket','S-5M Rocket']
    dbObj.childCapacityList=[1,1,1,1,1,1,1,2,2,1,16,16,16]
    dbObj.childLoadTime_s=[360.000000,180.000000,180.000000,240.000000,240.000000,240.000000,360.000000,360.000000,360.000000,180.000000,240.000000,240.000000,240.000000]
    dbObj.childCycleTime_s=[1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,1.000000,0.100000,0.100000,0.100000]
    dbObj.CalculateParams()
    return dbObj
