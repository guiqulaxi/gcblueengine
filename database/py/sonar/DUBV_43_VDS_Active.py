# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSonarDBObject()
    dbObj.mzClass='DUBV-43 VDS Active'
    dbObj.natoClass='DUBV-43 VDS Active'
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
    dbObj.notes='contributed by greengills  has equivalent performance to DUBV-23, but is a VDS.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=35.000000
    dbObj.mfRefRange_km=1.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=44.869999
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.009290
    dbObj.angleError_deg=1.000000
    dbObj.elevationError_deg=1.000000
    dbObj.minFrequency_Hz=-0.001327
    dbObj.maxFrequency_Hz=-0.001327
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.SL=193.500000
    dbObj.DI=19.350000
    dbObj.maxFrequency_Hz=1000.000000
    dbObj.isPassive=False
    dbObj.isActive=True
    dbObj.isTowed=True
    dbObj.maxScope_m=700.000000
    dbObj.isWakeHoming=False
    dbObj.CalculateParams()
    return dbObj
