# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcECMDBObject()
    dbObj.mzClass='SLQ-32(v)3 ECM'
    dbObj.natoClass='SLQ-32(v)3 ECM'
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
    dbObj.notes='Jams on H thorugh J bands, capable of range gate pull off and azimuth gate pull off.  Each 90° sector is covered continuously by 32 beams, with a total radiated power of 1MW, yielding 31.25kW per beam, or 44.95dB radiated power in each beam.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=700.000000
    dbObj.mfRefRange_km=0.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=80.000000
    dbObj.mfScanPeriod_s=20.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=60000000.000000
    dbObj.maxFrequency_Hz=20000000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ecmType='Jammer'
    dbObj.ERP_dBW=44.950001
    dbObj.effectivenessRating=0.500000
    dbObj.isEffectiveVsSurveillance=True
    dbObj.isEffectiveVsSeeker=True
    dbObj.CalculateParams()
    return dbObj
