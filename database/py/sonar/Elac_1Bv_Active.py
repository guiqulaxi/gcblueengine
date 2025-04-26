# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='Elac 1Bv Active'
    dbObj.natoClass='Elac 1Bv Active'
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
    dbObj.notes='accurate source level, and range.  Otherwise assumed equivalent to SPS-4'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=12.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=80.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=70.000000
    dbObj.mfScanPeriod_s=15.386000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.075000
    dbObj.angleError_deg=3.750000
    dbObj.elevationError_deg=10.000000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=136.000000
    dbObj.DI=13.600000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=False
    dbObj.maxScope_m=0.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
