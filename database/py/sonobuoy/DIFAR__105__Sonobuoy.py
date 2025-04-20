import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonobuoyDBObject()
    dbObj.mzClass='DIFAR (105) Sonobuoy'
    dbObj.natoClass='DIFAR (105) Sonobuoy'
    dbObj.mnModelType=15
    dbObj.mnType=132
    dbObj.cost=12000.000000
    dbObj.weight_kg=10.000000
    dbObj.volume_m3=0.012080
    dbObj.initialYear=2007.000000
    dbObj.finalYear=2017.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='sonobuoyDIFAR.jpg'
    dbObj.mz3DModelFileName='buoy.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Difar 12']
    sensorPlatformDBObject.sensorAz=[0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-999.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Sonobuoy'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.batteryLife_s=7200.000000
    dbObj.commRange_km=16.000000
    dbObj.CalculateParams()
    return dbObj
