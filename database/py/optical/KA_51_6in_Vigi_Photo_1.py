# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='KA-51 6in Vigi Photo-1'
    dbObj.natoClass='KA-51 6in Vigi Photo-1'
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
    dbObj.notes='this camera has a focal length of 6in, and is mounted at a 16° depression angle, this camera station has 50% overlap, assumed to be at its peak velocity of 590m/s at an altitude of 12200m.  this results in a field of view of 56.2°.  nominal scan rate for no overlap would be 29.4seconds, 50% overlap is then 14.72s.  as the 12in camera is quoted to be capable of resolving a tennis ball from 40,000ft, this equates to a ref range of 30.75 for the 6in focal length, assuming equivalent film is used.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=225.000000
    dbObj.mfRefRange_km=30.750000
    dbObj.mfFieldOfView_deg=56.200001
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=12.100000
    dbObj.mfScanPeriod_s=14.720000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=12.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.isDesignator=False
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.isIR=False
    dbObj.nightFactor=0.000000
    dbObj.CalculateParams()
    return dbObj
