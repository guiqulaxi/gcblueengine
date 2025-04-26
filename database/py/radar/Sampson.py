# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Sampson'
    dbObj.natoClass='Sampson'
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
    dbObj.notes='Plessey claims a pidgeon(0.008m²) can be detected at 105km in clear conditions.  That produces an enormously huge ref range of 351.0887.  Going to assume some marketing at work there, and will spec for a 0.01m² target at 100km.  25kW transmitter, 256 PCR, 0.1µs to 1µs pulses at a duty cycle of up to 25%.  Assigning this radar a duty cycle of 12.5%.  Unknown gain, using the editors estimated gain.  It is a smaller array antennae compared to SPY-1, while operating in a similar frequency band, assuming roughly equivalent gain given its much newer design, so assuming 40dB gain.  Assuming slightly weaker beam forming capability, but only just.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=400.000000
    dbObj.mfRefRange_km=316.227814
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=80.000000
    dbObj.mfScanPeriod_s=1.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.090000
    dbObj.elevationError_deg=0.090000
    dbObj.minFrequency_Hz=2304999936.000000
    dbObj.maxFrequency_Hz=3175000064.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=43.979401
    dbObj.ERPaverage_dBW=34.948502
    dbObj.maxFireControlTracks=32
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=175000000.000000
    dbObj.azimuthBeamwidth_deg=1.800000
    dbObj.elevationBeamwidth_deg=1.800000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
