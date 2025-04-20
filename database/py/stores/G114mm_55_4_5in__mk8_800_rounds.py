import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='114mm/55(4.5in) mk8 800 rounds'
    dbObj.natoClass='114mm/55(4.5in) mk8 800 rounds'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=0.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='114mm/55(4.5in) mk6 mod0 Mag'
    dbObj.capacity=800
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=30.000000
    dbObj.compatibleItems=['114mm N4A1 HE','114mm N4A1 HE-ER','114mm N4A1 HE(AA fuse)','114mm N4A1 HE-ER(AA fuse)']
    dbObj.CalculateParams()
    return dbObj
