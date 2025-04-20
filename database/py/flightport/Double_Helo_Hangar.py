import pygcb
def CreateDBObject():
    dbObj=pygcb.tcFlightportDBObject()
    dbObj.mzClass='Double Helo Hangar'
    dbObj.natoClass='Double Helo Hangar'
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
    dbObj.heloOnly=1
    dbObj.hangarCapacity=2
    dbObj.spotInfo=[pygcb.spotDBInfo()]*2
    dbObj.spotInfo[0].isLaunch=1
    dbObj.spotInfo[0].x=0.000000
    dbObj.spotInfo[0].y=-47.000000
    dbObj.spotInfo[0].z=10.200000
    dbObj.spotInfo[0].orientation_deg=135.000000
    dbObj.spotInfo[0].length=0.000000
    dbObj.spotInfo[1].isLaunch=0
    dbObj.spotInfo[1].x=0.000000
    dbObj.spotInfo[1].y=-47.000000
    dbObj.spotInfo[1].z=10.200000
    dbObj.spotInfo[1].orientation_deg=135.000000
    dbObj.spotInfo[1].length=0.000000
    dbObj.CalculateParams()
    return dbObj
