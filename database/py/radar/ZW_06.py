# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='ZW-06'
    dbObj.natoClass='ZW-06'
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
    dbObj.notes='60kW, 0.6µs pulses, PRF 2000, 32dB gain, 0.9°x19° beam, 2.4° az resolution, range on 10m² tarfget is 14nm, 26km. 24rpm.  Assuming 80km instrumented.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=80.000000
    dbObj.mfRefRange_km=6.248000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=19.000000
    dbObj.mfScanPeriod_s=2.500000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.045000
    dbObj.elevationError_deg=0.950000
    dbObj.minFrequency_Hz=9324999680.000000
    dbObj.maxFrequency_Hz=9475000320.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=79.781998
    dbObj.ERPaverage_dBW=53.584000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-0.460000
    dbObj.lookdownLand_dB=-3.460000
    dbObj.bandwidth_Hz=10000000.000000
    dbObj.azimuthBeamwidth_deg=0.900000
    dbObj.elevationBeamwidth_deg=19.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
