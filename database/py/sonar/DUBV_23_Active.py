import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='DUBV-23 Active'
    dbObj.natoClass='DUBV-23 Active'
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
    dbObj.notes='contributed by greengills  capable of detecting a 200ft target at 14000yds, tweaked capable of detecting a kilo 50/50 at 12.7km, upper limit on detection range is 35kyds, 32km, range accuracy is 150yds ±1%, bearing accuracy is 1°.  Assigning range accuracy of 150yds plus 1% of 17500yds.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=32.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=270.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=44.869999
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.009290
    dbObj.angleError_deg=1.000000
    dbObj.elevationError_deg=1.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=193.500000
    dbObj.DI=19.350000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
