# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='AIM-9P Seeker'
    dbObj.natoClass='AIM-9P Seeker'
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
    dbObj.mfMaxRange_km=18.000000
    dbObj.mfRefRange_km=4.700000
    dbObj.mfFieldOfView_deg=30.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.isDesignator=False
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.isIR=True
    dbObj.nightFactor=1.000000
    dbObj.CalculateParams()
    return dbObj
