# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='Type 177 Active'
    dbObj.natoClass='Type 177 Active'
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
    dbObj.notes='Due to a shortage of time, im cheating, this is essentially a renamed SQS-53B modified to taste.  Range to a sub hit beam on is best case 18kyds(isothermal water, sea state 2 or less, own speed 12kts or less), 8kyds(negative temperature gradient, sea state 2-3), 3kyds(surface layer, sea state 4-5).  I do not have the time to empirically strike this balance, nor do I know the math to reach these numbers rapidly.  the radar scans an 80° sector and takes 6 minutes to do so(7.5 seconds per ping at 5kyds, 15 seconds per ping at 10kyds, 30 seconds per ping at 20kyds, it pings at 10kyds, then 5kyds in normal sweep, takes 4 minutes to complete a sweep at 10kyds, and 2 minutes to complete the sweep at 5kyds).  Time to cover 10kyds distance at 12kts is 30 minutes, at 18 kts(own ship at 12, target sube closing at 6) it takes 20 minutes.this is rather...unresonable the way GCB currently functions.  THis is 6 minutes to search the entire sector, but updatesd at 20kyds as rapidly as every 30 seconds, going to work with 30 second ping times.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=18.290001
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=80.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=0.000000
    dbObj.mfScanPeriod_s=30.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=236.363632
    dbObj.DI=23.636364
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
