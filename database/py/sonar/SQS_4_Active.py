# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='SQS-4 Active'
    dbObj.natoClass='SQS-4 Active'
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
    dbObj.notes='csi.whoi.edu/sites/default/files/literature/Full%20Text.pdf'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=15.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=80.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=70.000000
    dbObj.mfScanPeriod_s=19.232000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.055000
    dbObj.angleError_deg=3.250000
    dbObj.elevationError_deg=10.000000
    dbObj.minFrequency_Hz=8000.000000
    dbObj.maxFrequency_Hz=14000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=198.181824
    dbObj.DI=19.818182
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
