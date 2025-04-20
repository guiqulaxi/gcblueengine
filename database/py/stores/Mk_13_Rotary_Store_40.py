import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Mk-13 Rotary Store 40'
    dbObj.natoClass='Mk-13 Rotary Store 40'
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
    dbObj.notes='Mk-13 Rotary Store'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Mk-13 Rotary Store'
    dbObj.capacity=40
    dbObj.maxVolume_m3=52.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-66L','RIM-66G','RIM-66E','RIM-66B','RIM-66A','RGM-84A Harpoon','RGM-84C Harpoon','RGM-84D Harpoon','RGM-84F Harpoon','RGM-84G Harpoon','RIM-24A','RIM-24B','RIM-24C']
    dbObj.CalculateParams()
    return dbObj
