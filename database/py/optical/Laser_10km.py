# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='Laser-10km'
    dbObj.natoClass='Laser-10km'
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
    dbObj.mfMaxRange_km=10.000000
    dbObj.mfRefRange_km=20.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=30.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.maxFireControlTracks=10
    dbObj.isSemiactive=False
    dbObj.isDesignator=True
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=True
    dbObj.isIR=True
    dbObj.nightFactor=1.000000
    dbObj.CalculateParams()
    return dbObj
