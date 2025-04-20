import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Alpinist Ammo Mag'
    dbObj.natoClass='Alpinist Ammo Mag'
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
    dbObj.displayName='Ammunition Magazines'
    dbObj.capacity=32
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=313.600006
    dbObj.moveTime=60.000000
    dbObj.compatibleItems=[]
    dbObj.CalculateParams()
    return dbObj
