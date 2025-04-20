import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='US Ship Torpedo Racks'
    dbObj.natoClass='US Ship Torpedo Racks'
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
    dbObj.displayName='SH-60 Helo Support Stores'
    dbObj.capacity=18
    dbObj.maxVolume_m3=36.000000
    dbObj.maxWeight_kg=6120.000000
    dbObj.moveTime=45.000000
    dbObj.compatibleItems=['Mk-50','Mk-54','Mk-46 Mod5','Mk-44']
    dbObj.CalculateParams()
    return dbObj
