# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='SQS-17 Active'
    dbObj.natoClass='SQS-17 Active'
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
    dbObj.notes='Essentially an SQS-36 sans preformed beams, or rather, the SQS-36 is an SQS-17 with pre-formed beams.  Preformed beams improves bearing accuracy, scan rate, and range.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=20.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=280.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=36.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.038000
    dbObj.angleError_deg=6.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=11900.000000
    dbObj.maxFrequency_Hz=14100.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=200.000000
    dbObj.DI=20.000000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
