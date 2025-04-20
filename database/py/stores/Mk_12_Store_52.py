import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Mk-12 Store 52'
    dbObj.natoClass='Mk-12 Store 52'
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
    dbObj.notes='Mk-11 Rotary Store'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Mk-12 Missile Store'
    dbObj.capacity=52
    dbObj.maxVolume_m3=52.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-8A','RIM-8C','RIM-8E','RIM-8F','RIM-8J','SAM-N-6b','SAM-N-6b1','SAM-N-6c1','SAM-N-6b1(CW)']
    dbObj.CalculateParams()
    return dbObj
