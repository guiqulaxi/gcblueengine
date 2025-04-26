# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='RAN-11L/X'
    dbObj.natoClass='RAN-11L/X'
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
    dbObj.notes='Marcos -amram, operates in a dual mode, both L band and x band, as GCB can only do one or the other, im siding with x-band.  this band performs far far better for this radar.  performance is 12+nm for 11x, and 14nm for 12x, both in l band, 12x achieves 20+nm in x band, scaling 11x appropriately.  In the end, this radar pretty much keeps its ref range, but suffers a loss of instrumented range.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=74.000000
    dbObj.mfRefRange_km=24.100000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=80.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.055000
    dbObj.elevationError_deg=0.300000
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10549999616.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=86.303001
    dbObj.ERPaverage_dBW=73.300003
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=1.100000
    dbObj.elevationBeamwidth_deg=6.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
