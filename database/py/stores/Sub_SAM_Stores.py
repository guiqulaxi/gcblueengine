import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Sub SAM Stores'
    dbObj.natoClass='Sub SAM Stores'
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
    dbObj.notes='Generic stores'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='SAM Stores'
    dbObj.capacity=8
    dbObj.maxVolume_m3=25.000000
    dbObj.maxWeight_kg=200.000000
    dbObj.moveTime=60.000000
    dbObj.compatibleItems=[]
    dbObj.CalculateParams()
    return dbObj
