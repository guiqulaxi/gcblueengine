# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='Eyeball-2'
    dbObj.natoClass='Eyeball-2'
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
    dbObj.notes='equivalent to 20/10 vision.  should only be assigned to aircraft, as they generally screen for less than excellent eyesight.  20/10 eyesight allows for discrimination of a 1m² target at 6.8754km, as pilots would have to cope with unaided views(they do not get the benefit of 20x binoculars, such as the lookouts on a ship do), this entry does appear to be for weaker eyes, this definitely is not true, altho their performance in GCB will suffer as a result of not having the binoculars.  This will be offset by a higher rate of update, and in greater angular acuracy.  1 arc minute is 1/60 of a degree, or 0.1667°. this full accuracy is available to a pilot.  Asumed to be capable of estimating range to within 5%'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=225.000000
    dbObj.mfRefRange_km=6.875500
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=4.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=0.001000
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
    dbObj.isIR=False
    dbObj.nightFactor=0.600000
    dbObj.CalculateParams()
    return dbObj
