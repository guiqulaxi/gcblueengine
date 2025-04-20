import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='NT37C Seeker'
    dbObj.natoClass='NT37C Seeker'
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
    dbObj.mfMaxRange_km=3.000000
    dbObj.mfRefRange_km=0.500000
    dbObj.mfFieldOfView_deg=90.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=5.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.330000
    dbObj.angleError_deg=5.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=10.000000
    dbObj.counterMeasureFactor=1.800000
    dbObj.isSurveillance=False
    dbObj.SL=220.909088
    dbObj.DI=22.090910
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=True
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
