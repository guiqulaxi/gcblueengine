import pygcb
def CreateDBObject():
    dbObj=pygcb.tcStoresDBObject()
    dbObj.mzClass='C-130J Cargo Bay'
    dbObj.natoClass='C-130J Cargo Bay'
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
    dbObj.notes='[greengills]'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.displayName='Cargo Bay'
    dbObj.capacity=10000
    dbObj.maxVolume_m3=0.000000
    dbObj.maxWeight_kg=14000.000000
    dbObj.moveTime=5400.000000
    dbObj.compatibleItems=[]
    dbObj.CalculateParams()
    return dbObj
