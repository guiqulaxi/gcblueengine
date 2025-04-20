import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Sea Sparrow Reloads'
    dbObj.natoClass='Sea Sparrow Reloads'
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
    dbObj.displayName='Sea Sparrow Reloads'
    dbObj.capacity=32
    dbObj.maxVolume_m3=16.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-7M(v1)','RIM-7P(v1)','RIM-7H','RIM-7F','RIM-7E','RIM-162D','ASPIDE-1A']
    dbObj.CalculateParams()
    return dbObj
