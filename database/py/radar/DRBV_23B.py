# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='DRBV 23B'
    dbObj.natoClass='DRBV 23B'
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
    dbObj.notes='2000 kW peak power with 29 dBi antenna gain. 7.5 RPM scan. About 50 ms of effective dwell time.  160nm vs 10m² target.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=350.000000
    dbObj.mfRefRange_km=166.630005
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=15.000000
    dbObj.mfScanPeriod_s=8.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.125000
    dbObj.elevationError_deg=99.000000
    dbObj.minFrequency_Hz=1300000000.000000
    dbObj.maxFrequency_Hz=1390000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=92.000000
    dbObj.ERPaverage_dBW=63.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=4.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=2000000.000000
    dbObj.azimuthBeamwidth_deg=2.500000
    dbObj.elevationBeamwidth_deg=50.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
