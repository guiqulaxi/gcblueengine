# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcECMDBObject()
    dbObj.mzClass='SPECTRA ECM'
    dbObj.natoClass='SPECTRA ECM'
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
    dbObj.notes='No data just arbitrary numbers  this combined with the reduced ECM of the aircraft may be quite a bit too much, I do not know the effect this jammer has on its overall RCS, and therefore cannot begin to comprehend the overall stealth this aircraft gains from it.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=75.000000
    dbObj.mfRefRange_km=0.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=30.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=6000000000.000000
    dbObj.maxFrequency_Hz=36999999488.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ecmType='Jammer'
    dbObj.ERP_dBW=20.000000
    dbObj.effectivenessRating=0.600000
    dbObj.isEffectiveVsSurveillance=True
    dbObj.isEffectiveVsSeeker=True
    dbObj.CalculateParams()
    return dbObj
