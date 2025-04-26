# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='STIR 180'
    dbObj.natoClass='STIR 180'
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
    dbObj.notes='I don\'t know much about this system, but its peak range is 1/3 that of the Stir 240, going to scale details that i don\'t know accordingly, setting them at 1/4 of SIR 240 values.  STIR 240 has 25 times the averager power, which is the same as 25 times larger target at the same power.  so, 25m² target at 140km.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=60.000000
    dbObj.mfRefRange_km=62.610001
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=60.000000
    dbObj.mfScanPeriod_s=1.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.070000
    dbObj.elevationError_deg=0.070000
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10549999616.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=85.424004
    dbObj.ERPaverage_dBW=55.009998
    dbObj.maxFireControlTracks=2
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=0.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=1.400000
    dbObj.elevationBeamwidth_deg=1.400000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
