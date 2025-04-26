# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='DE-1160B Passive'
    dbObj.natoClass='DE-1160B Passive'
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
    dbObj.notes='copied from SQS-505 passive'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=200.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=300.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=10.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.200000
    dbObj.angleError_deg=3.500000
    dbObj.elevationError_deg=0.110000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=10.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=0.000000
    dbObj.DI=26.000000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=True
    dbObj.isActive=False
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
