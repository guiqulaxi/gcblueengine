# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Type 518'
    dbObj.natoClass='Type 518'
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
    dbObj.notes='range is just 280km, not 400, 34 or 38 dB gain antenna, 3 or 6 rpm scan rate, accuracy of 1.2° bearing, 300m range, 1.1° wide beamm resolution of 4° and 400m, maximum elevation of 28.8°.  unknown power outputs.  Assuming 120kW peak with similar duty cycle to LW-08 given Type 518\'s heritage.  Claimed range is 150km for a 2m² target.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=280.000000
    dbObj.mfRefRange_km=126.134499
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=28.799999
    dbObj.mfScanPeriod_s=20.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=1.200000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=1220000000.000000
    dbObj.maxFrequency_Hz=1350000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=84.791809
    dbObj.ERPaverage_dBW=70.190933
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=0.000000
    dbObj.bandwidth_Hz=12000000.000000
    dbObj.azimuthBeamwidth_deg=1.100000
    dbObj.elevationBeamwidth_deg=28.799999
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
