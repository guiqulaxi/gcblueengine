import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='127mm Mk-45 1200 rounds'
    dbObj.natoClass='127mm Mk-45 1200 rounds'
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
    dbObj.displayName='2 Deck Gun store'
    dbObj.capacity=1200
    dbObj.maxVolume_m3=1200.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['127mm mk 80 HE-PD EX-175','127mm mk 80 HE-PD mk 67','127mm mk 127 HE-CVT mk 67','127mm mk 127 HE-CVT EX-175']
    dbObj.CalculateParams()
    return dbObj
