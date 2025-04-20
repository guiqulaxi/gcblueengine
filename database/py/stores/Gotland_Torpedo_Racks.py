import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Gotland Torpedo Racks'
    dbObj.natoClass='Gotland Torpedo Racks'
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
    dbObj.displayName='Torpedo Racks'
    dbObj.capacity=20
    dbObj.maxVolume_m3=48.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=360.000000
    dbObj.compatibleItems=['Type-613 Torpedo','Type-431 Torpedo']
    dbObj.CalculateParams()
    return dbObj
