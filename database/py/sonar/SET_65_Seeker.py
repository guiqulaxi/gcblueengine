import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='SET-65 Seeker'
    dbObj.natoClass='SET-65 Seeker'
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
    dbObj.notes='assumed to be capable of active acquisition at 800m.  Tagged for 800m on 30° aspect vs TS=8 target.  Vs LA with TS of 12 this results in 1270.  broadside this is 5120 to 6390.  a broadside target is almost always prefered.  Maximum range set to permit a TS=16 broadside at 8000m.  Since torpedoes would switch to faster and faster pulse rates as they close with the target, I have chosen to set a scan rate that exceeds the speed of sound in sea water at 8000m range.  scan rate chosen for 2500m range.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=7.500000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=60.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=3.590000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=1.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=174.550003
    dbObj.DI=17.455000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
