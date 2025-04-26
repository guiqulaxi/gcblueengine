# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SC-2'
    dbObj.natoClass='SC-2'
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
    dbObj.notes='http://www.hnsa.org/doc/radar/index.htm, http://pwencycl.kgbudge.com/R/a/Radar.htm, unknown gain, assumed to be 25dB.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=150.000000
    dbObj.mfRefRange_km=23.400999
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=8.000000
    dbObj.mfScanPeriod_s=12.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=3.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=191000000.000000
    dbObj.maxFrequency_Hz=198000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=78.010002
    dbObj.ERPaverage_dBW=65.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-30.687000
    dbObj.lookdownLand_dB=-39.687000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=10.000000
    dbObj.elevationBeamwidth_deg=10.000000
    dbObj.effectiveSidelobes_dB=-15.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
