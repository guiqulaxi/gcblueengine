# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcESMDBObject()
    dbObj.mzClass='ALQ-99(OR-40)'
    dbObj.natoClass='ALQ-99(OR-40)'
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
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=500.000000
    dbObj.mfRefRange_km=0.255000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=5.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.140000
    dbObj.angleError_deg=2.500000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=30000000.000000
    dbObj.maxFrequency_Hz=10000000000.000000
    dbObj.idThreshold_dB=0.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.mfMaxRange_km=True
    dbObj.CalculateParams()
    return dbObj
