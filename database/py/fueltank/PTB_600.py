import pygcb
def CreateDBObject():
    dbObj=pygcb.tcFuelTankDBObject()
    dbObj.mzClass='PTB-600'
    dbObj.natoClass='PTB-600'
    dbObj.mnModelType=20
    dbObj.mnType=0
    dbObj.cost=5000.000000
    dbObj.weight_kg=20.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='fueltank.jpg'
    dbObj.mz3DModelFileName=''
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.fuelCapacity_kg=481.700012
    dbObj.CalculateParams()
    return dbObj
