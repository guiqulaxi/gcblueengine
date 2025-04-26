# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='APS-705'
    dbObj.natoClass='APS-705'
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
    dbObj.notes='Marcos  -Amram-I lack enough info to do a full rebalance of the radar, but I do know some things.  50kW transmitter, 1.5µs at 650pps, 20 or 40 rpm scan rates, 2°x7° beam, x band.  These man a peak power of 50kW, but an average power of just 49w, the beamwidth yields an estimated gain of 35.74, and my radar sheet estimates it at 19.3km ref range, a value close to Sea Spray which is an alternative fit, so im leaving it in place.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=148.000000
    dbObj.mfRefRange_km=8.271000
    dbObj.mfFieldOfView_deg=300.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=45.000000
    dbObj.mfScanPeriod_s=3.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.350000
    dbObj.elevationError_deg=0.100000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=82.699997
    dbObj.ERPaverage_dBW=52.599998
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-3.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=2.000000
    dbObj.elevationBeamwidth_deg=7.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
