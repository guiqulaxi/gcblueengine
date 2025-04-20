import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='USCGS Helo Support'
    dbObj.natoClass='USCGS Helo Support'
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
    dbObj.displayName='Helo Fuel'
    dbObj.capacity=38294
    dbObj.maxVolume_m3=12601.179688
    dbObj.maxWeight_kg=38294.640625
    dbObj.moveTime=45.000000
    dbObj.compatibleItems=['Fuel']
    dbObj.CalculateParams()
    return dbObj
