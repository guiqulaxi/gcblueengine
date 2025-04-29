# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='RTN-20X x3'
    dbObj.natoClass='RTN-20X x3'
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
    dbObj.notes='Marcos  -Amram -beam is 2.2°, gain 37dB, target acquisition is usually 2-6nm, 3 arc minutes of angular accuracy, 3m range accuracy.  200kW power, 0.5µs pulses at 2000pps.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=25.000000
    dbObj.mfRefRange_km=17.830000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=45.000000
    dbObj.mfScanPeriod_s=0.500000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.050000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=8999999488.000000
    dbObj.maxFrequency_Hz=10000000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=2.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=90.000000
    dbObj.ERPaverage_dBW=60.000000
    dbObj.maxFireControlTracks=3
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=40.000000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=2.200000
    dbObj.elevationBeamwidth_deg=2.200000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
