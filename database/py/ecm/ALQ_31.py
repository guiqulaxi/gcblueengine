# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcECMDBObject()
    dbObj.mzClass='ALQ-31'
    dbObj.natoClass='ALQ-31'
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
    dbObj.notes='Normally the ALQ-31A is any two of ALQ-32/35/41/51/55.  ALQ-31B is any two of ALT-16/17/19/21.  GCB does not support band specirfic jamming, nor does it support launcher mounted sensors yet, and so, this is being treated as an all in one unit for now.  being configured as fairly weak, I do not like how current jammers make the host invulnerable to radar.  Will try 20dB to start.  to be effective as a jammer, range MUST be larger than the radars it can expect to face as otherwise you are tracked entering before you drop off their screen.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=500.000000
    dbObj.mfRefRange_km=0.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=10.000000
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
    dbObj.ERP_dBW=-12.000000
    dbObj.effectivenessRating=13280.000000
    dbObj.isEffectiveVsSurveillance=True
    dbObj.isEffectiveVsSeeker=True
    dbObj.CalculateParams()
    return dbObj
