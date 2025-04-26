# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='OQS-4 Active'
    dbObj.natoClass='OQS-4 Active'
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
    dbObj.notes='Japanese SQS-23 with improved SNR'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=25.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=300.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=32.060001
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.032000
    dbObj.angleError_deg=4.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=199.645462
    dbObj.DI=19.964546
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
