# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Reya'
    dbObj.natoClass='Pot Head'
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
    dbObj.notes='I lack reference ranges, so im basing this of Zarnitsa.  25% more power, more focused beam, same pulse length, but much higher pulse rate, will simply scale Zarnitsa performance accordingly.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=47.200001
    dbObj.mfRefRange_km=14.100000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=21.000000
    dbObj.mfScanPeriod_s=10.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10499999744.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=0.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=82.533302
    dbObj.ERPaverage_dBW=53.738998
    dbObj.maxFireControlTracks=100
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-35.000000
    dbObj.lookdownLand_dB=-44.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=3.000000
    dbObj.elevationBeamwidth_deg=3.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
