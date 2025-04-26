# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPG-51C 2'
    dbObj.natoClass='SPG-51C 2'
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
    dbObj.notes='-51D has more than 5x more power, assuming all else equal this is a 7.16dBsm gain in target strength, accordingly then SPG-51C has a ref range of 61.5443 compared to -51D\'s 92.937'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=183.000000
    dbObj.mfRefRange_km=61.544300
    dbObj.mfFieldOfView_deg=360.000000
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
    dbObj.maxFireControlTracks=2
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
