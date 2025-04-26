# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='MGK-540 Active'
    dbObj.natoClass='Shark Gill Active'
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
    dbObj.notes='MGK-540 Skat-3 active mode.  K in MGK indicates integrated system. -M modernized/upgraded'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=50.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=300.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=64.102997
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.023750
    dbObj.angleError_deg=3.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=204.181824
    dbObj.DI=20.418182
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
