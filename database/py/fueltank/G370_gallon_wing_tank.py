import pygcb
def CreateDBObject():
    dbObj=pygcb.tcFuelTankDBObject()
    dbObj.mzClass='370 gallon wing tank'
    dbObj.natoClass='370 gallon wing tank'
    dbObj.mnModelType=20
    dbObj.mnType=0
    dbObj.cost=5000.000000
    dbObj.weight_kg=57.000000
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
    dbObj.fuelCapacity_kg=1124.000000
    dbObj.CalculateParams()
    return dbObj
