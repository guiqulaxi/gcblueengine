# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='Ka-50A 12in Vigi Photo-2'
    dbObj.natoClass='Ka-50A 12in Vigi Photo-2'
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
    dbObj.notes='this camera has a focal length of 12in, and is mounted at a 90° depression angle, this camera station has 20% overlap in high altitude mode, and a 60% overlap in low altitude mode, going to work with 40% across the board, assumed to be at its peak velocity of 590m/s at an altitude of 12200m.  this results in a field of view of 36.79°.  nominal scan rate for no overlap would be 14.72seconds, 40% overlap is then 8.83s.  as the 12in camera is quoted to be capable of resolving a tennis ball from 40,000ft, this equates to a ref range of 46.5 for the 12in focal length, assuming equivalent film is used.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=225.000000
    dbObj.mfRefRange_km=46.500000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=-71.605003
    dbObj.mfScanPeriod_s=23.559999
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
