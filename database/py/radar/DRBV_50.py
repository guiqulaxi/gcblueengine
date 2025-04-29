# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='DRBV 50'
    dbObj.natoClass='DRBV 50'
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
    dbObj.notes='250 kW peak power 28 dB gain pw/prfs: 1.25 us 750 Hz or 0.25 us 2-4 kHz modes. Intended to detect 1 m2 targets out to 10 nm.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=50.000000
    dbObj.mfRefRange_km=18.520000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=10.000000
    dbObj.mfScanPeriod_s=4.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=99.000000
    dbObj.minFrequency_Hz=5350000128.000000
    dbObj.maxFrequency_Hz=5750000128.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=4.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=82.000000
    dbObj.ERPaverage_dBW=54.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=4.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=4000000.000000
    dbObj.azimuthBeamwidth_deg=1.300000
    dbObj.elevationBeamwidth_deg=20.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
