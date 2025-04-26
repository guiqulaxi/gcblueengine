# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='ARGS-14E Seeker'
    dbObj.natoClass='ARGS-14E Seeker'
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
    dbObj.notes='maximum detection range of over 20km, sectoer width of ±45°, vertical scanning of +10°, -20°.   Assuming 30dB destroyer at 20km even.  it first attempts to lock up a target at 40km.  As 30dB at 20km results in 3.557 km ref range, this also results in a 42dB target requirement for detectin at 40km, this IS achievable, leaving it as is.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=40.000000
    dbObj.mfRefRange_km=1.524000
    dbObj.mfFieldOfView_deg=90.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=20.000000
    dbObj.mfScanPeriod_s=1.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.370000
    dbObj.elevationError_deg=0.250000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=60.000000
    dbObj.ERPaverage_dBW=50.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=0.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=5.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
