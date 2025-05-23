# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='KLJ-7'
    dbObj.natoClass='KLJ-7'
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
    dbObj.notes='very little is known of this radar it seems.  microwave Journal 401 suggests a range of 80km, and engaging up to 4 at once.   Overscan\'s guide to russian military avionics roughly confirms, suggesting detection at 80km, and tracking at 60km.  non offers any information regarding power, pulse rates, scan sectors, and instrumented range.   Since the Chinese selected it for the J-17, and the Chinese PL-13 has a maximum engagement range of 148km, I will assume this radar has an instrumented range of either 90NM(167km), or its detection range of a 15dBsm target +10%, which ever is larger.  Based off a fighter at 3m², the end result is that it will detect a 15dBsm(31.63m²) target at 144km, add on the 10% headroom and we arrive at 158.6km, or 85.6nm.  Copied from N-010 Zhuk-M as it is derived from this family, aside from instrumented and ref ranges, nothing else is changed.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=160.000000
    dbObj.mfRefRange_km=60.786999
    dbObj.mfFieldOfView_deg=170.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=56.000000
    dbObj.mfScanPeriod_s=7.760000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=0.650000
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10499999744.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=37.880001
    dbObj.ERPaverage_dBW=27.879999
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=10.390000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
