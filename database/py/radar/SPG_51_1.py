# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPG-51 1'
    dbObj.natoClass='SPG-51 1'
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
    dbObj.notes='capability extrapolated from a reference given.  Was quoted as capable of tracking an F6F out to a range of 120kyds(109.74km), I am assuming the F6F to be a 15m² target.  this puts the ref range at 55.7625km.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=183.000000
    dbObj.mfRefRange_km=55.762501
    dbObj.mfFieldOfView_deg=340.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=83.000000
    dbObj.mfScanPeriod_s=3.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.450000
    dbObj.elevationError_deg=0.450000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=0.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=42.910000
    dbObj.ERPaverage_dBW=31.580000
    dbObj.maxFireControlTracks=1
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=0.900000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
