# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Type 341'
    dbObj.natoClass='Type 341'
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
    dbObj.notes='C band(upper end of G band), 2.7°x1.4° beam, 150kW, 2.2kW average power, 5RPM scan rate, maximum tracking range of 180km, 28.8° elevation limit, 100m range accuracy, 0.8° angular accuracy, 10% bandwidth.  Lacking better info, assuming 120m² target at instrumented.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=180.000000
    dbObj.mfRefRange_km=54.384762
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=28.799999
    dbObj.mfScanPeriod_s=5.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.800000
    dbObj.elevationError_deg=0.800000
    dbObj.minFrequency_Hz=5249999872.000000
    dbObj.maxFrequency_Hz=5280000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=81.760910
    dbObj.ERPaverage_dBW=63.424229
    dbObj.maxFireControlTracks=1
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=-9.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=53000000.000000
    dbObj.azimuthBeamwidth_deg=2.700000
    dbObj.elevationBeamwidth_deg=1.400000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
