# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcECMDBObject()
    dbObj.mzClass='Baikal ECM'
    dbObj.natoClass='Baikal ECM'
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
    dbObj.notes='Contributed by greengills'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=50.000000
    dbObj.mfRefRange_km=0.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=400000000.000000
    dbObj.maxFrequency_Hz=99999997952.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ecmType='Jammer'
    dbObj.ERP_dBW=52.000000
    dbObj.effectivenessRating=0.600000
    dbObj.isEffectiveVsSurveillance=False
    dbObj.isEffectiveVsSeeker=True
    dbObj.CalculateParams()
    return dbObj
