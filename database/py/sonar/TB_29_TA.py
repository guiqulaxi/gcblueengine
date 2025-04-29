# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='TB-29 TA'
    dbObj.natoClass='TB-29 TA'
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
    dbObj.notes='3 times as sensitive as TB-23'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=200.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=320.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=10.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.090000
    dbObj.angleError_deg=0.500000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=500.000000
    dbObj.maxFrequency_Hz=10000.000000
    dbObj.idThreshold_dB=10.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=0.000000
    dbObj.DI=38.299999
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=True
    dbObj.isActive=False
    dbObj.isTowed=True
    dbObj.maxScope_m=1000.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
