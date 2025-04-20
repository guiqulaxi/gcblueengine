import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='DASH 3.1 Support'
    dbObj.natoClass='DASH 3.1 Support'
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
    dbObj.displayName='DASH Stores'
    dbObj.capacity=1717
    dbObj.maxVolume_m3=633.299988
    dbObj.maxWeight_kg=11818.799805
    dbObj.moveTime=45.000000
    dbObj.compatibleItems=['Mk-44','Mk-46 Mod5','Fuel']
    dbObj.CalculateParams()
    return dbObj
