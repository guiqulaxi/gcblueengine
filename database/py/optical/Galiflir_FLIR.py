# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='Galiflir FLIR'
    dbObj.natoClass='Galiflir FLIR'
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
    dbObj.notes='The Naval Institute guide WNWS 97-98 can detect destroyer at 39 NM and identify it at 15 NM. If typical \'optical cross section\' is 1000 m^2 for destroyer then reference range is 39 NM / sqrt(1000) = 1.2 NM or 2.3 km.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=100.000000
    dbObj.mfRefRange_km=2.300000
    dbObj.mfFieldOfView_deg=120.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=12.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.500000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.isDesignator=False
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.isIR=True
    dbObj.nightFactor=1.000000
    dbObj.CalculateParams()
    return dbObj
