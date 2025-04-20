import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='Mk-11 Rotary Store 42'
    dbObj.natoClass='Mk-11 Rotary Store 42'
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
    dbObj.displayName='Mk-11 Rotary Store'
    dbObj.capacity=42
    dbObj.maxVolume_m3=50.000000
    dbObj.maxWeight_kg=0.000000
    dbObj.moveTime=0.000000
    dbObj.compatibleItems=['RIM-66L','RIM-66G','RIM-66E','RIM-66B','RIM-66A','RIM-24A','RIM-24B','RIM-24C','RGM-84A Harpoon','RGM-84C Harpoon','RGM-84D Harpoon','RGM-84F Harpoon','RGM-84G Harpoon']
    dbObj.CalculateParams()
    return dbObj
