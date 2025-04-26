# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPG-34'
    dbObj.natoClass='SPG-34'
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
    dbObj.notes='Same as Mk-34 FCS, except introduces a new parabolic reflector, achieves a 2.2°x2.2° beam, higher gain, transpits at 50kW.  Given a higher gain(40.355 vs 37.661, calculated from beamwidths), and a higher power, ref range is increased.  Overall yield is roughly a 4.24dB improvement, so setting this ref range to detect a 37.644m² target.  This is basically the 100m² target from Mk-34 FCS, reduced by the improvements in SPG-34.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=25.000000
    dbObj.mfRefRange_km=9.156000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=85.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.106496
    dbObj.elevationError_deg=0.106496
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10499999744.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=87.344910
    dbObj.ERPaverage_dBW=54.668839
    dbObj.maxFireControlTracks=1
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=2.200000
    dbObj.elevationBeamwidth_deg=2.200000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
