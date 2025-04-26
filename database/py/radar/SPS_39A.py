# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPS-39A'
    dbObj.natoClass='SPS-39A'
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
    dbObj.notes='http://www.scribd.com/doc/65788019/Naval-Radar , page 227.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=296.000000
    dbObj.mfRefRange_km=151.011002
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=48.000000
    dbObj.mfScanPeriod_s=12.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.120000
    dbObj.elevationError_deg=0.150000
    dbObj.minFrequency_Hz=215000000.000000
    dbObj.maxFrequency_Hz=225000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=94.000000
    dbObj.ERPaverage_dBW=69.680000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-10.300000
    dbObj.lookdownLand_dB=-18.000000
    dbObj.bandwidth_Hz=1000000.000000
    dbObj.azimuthBeamwidth_deg=2.400000
    dbObj.elevationBeamwidth_deg=3.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
