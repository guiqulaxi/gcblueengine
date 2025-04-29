# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='BQQ-2 Active'
    dbObj.natoClass='BQQ-2 Active'
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
    dbObj.notes='Proper range calc would involve tracking the speed of sound and not scanning again until the previous is finished.  the ranges can be set to one of several, short to long.  at the upper end permitting a 40km active range, 80,000 yds.  Speed of sound taken to be 1560m/s, two way then is 1.2821s per km, 51.282 for 40km.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=40.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=300.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=51.282001
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.045000
    dbObj.angleError_deg=4.050000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=192.000000
    dbObj.DI=19.200001
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
