import pygcb
def CreateDBObject():
    dbObj=pygcb.tcLauncherDBObject()
    dbObj.mzClass='114mm/55(4.5in) Mark 8 Mod 0'
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
    dbObj.childClassList=['114mm N4A1 HE','114mm N4A1 HE(AA fuse)','114mm N4A1 HE-ER','114mm N4A1 HE-ER(AA fuse)']
    dbObj.childCapacityList=[16,16,16,16]
    dbObj.childLoadTime_s=[16.000000,16.000000,16.000000,16.000000]
    dbObj.childCycleTime_s=[2.000000,2.000000,2.000000,2.000000]
    dbObj.CalculateParams()
    return dbObj
