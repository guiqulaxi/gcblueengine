# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='SJD-7 Active'
    dbObj.natoClass='SJD-7 Active'
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
    dbObj.notes='assumed powerful enough to peg a diesel to its instrumented range, which is 9000yds, 8.3km.  can detect a kilo 877E 50/50 at 8400m.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=8.300000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=270.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=10.650000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.150000
    dbObj.angleError_deg=1.000000
    dbObj.elevationError_deg=1.000000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=192.727280
    dbObj.DI=19.272728
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
