# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='PN-A(Down Beat)'
    dbObj.natoClass='PN-A(Down Beat)'
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
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=324.000000
    dbObj.mfRefRange_km=21.848000
    dbObj.mfFieldOfView_deg=240.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=0.000000
    dbObj.mfScanPeriod_s=7.760000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=0.650000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=47.470001
    dbObj.ERPaverage_dBW=37.470001
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.000000
    dbObj.lookdownWater_dB=-8.000000
    dbObj.lookdownLand_dB=-24.090000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=10.390000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
