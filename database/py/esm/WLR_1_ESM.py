import pygcb
def CreateDBObject():
    dbObj=pygcb.tcESMDBObject()
    dbObj.mzClass='WLR-1 ESM'
    dbObj.natoClass='WLR-1 ESM'
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
    dbObj.mfMaxRange_km=400.000000
    dbObj.mfRefRange_km=0.090000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=50.000000
    dbObj.mfScanPeriod_s=10.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=25.000000
    dbObj.elevationError_deg=80.000000
    dbObj.minFrequency_Hz=50000000.000000
    dbObj.maxFrequency_Hz=10750000128.000000
    dbObj.idThreshold_dB=0.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.mfMaxRange_km=False
    dbObj.CalculateParams()
    return dbObj
