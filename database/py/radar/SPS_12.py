# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPS-12'
    dbObj.natoClass='SPS-12'
    dbObj.mnModelType=0
    dbObj.mnType=0
    dbObj.cost=1.000000
    dbObj.weight_kg=0.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName=''
    dbObj.notes='http://radar.tpub.com/TM-11-487C-1/TM-11-487C-11233.htm   ,     http://www.scribd.com/doc/65788019/Naval-Radar  Dwell increases from 4µs at 150pps to 4µs at 300pps, or double the dwell considering all else is equal.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=280.000000
    dbObj.mfRefRange_km=72.459999
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=28.000000
    dbObj.mfScanPeriod_s=24.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=1.000000
    dbObj.minFrequency_Hz=1250000000.000000
    dbObj.maxFrequency_Hz=1350000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=77.800003
    dbObj.ERPaverage_dBW=64.800003
    dbObj.maxFireControlTracks=5
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-30.799999
    dbObj.lookdownLand_dB=-39.799999
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=3.300000
    dbObj.elevationBeamwidth_deg=30.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
