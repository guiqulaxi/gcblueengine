import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Mk-41 VLS Mod2 90 Cell'
    dbObj.natoClass='Mk-41 VLS Mod2 90 Cell'
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
    dbObj.displayName='90 Cell VLS'
    dbObj.capacity=360
    dbObj.maxVolume_m3=90.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-66C','RIM-66H','RIM-66M','RIM-156','RIM-162A','RIM-7P(v2)','RIM-7M(v2)','RUM-139 Mod4 ASROC','BGM-109 TLAM','BGM-109 TASM','BGM-109G TLAM-N']
    dbObj.CalculateParams()
    return dbObj
