# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Type 982'
    dbObj.natoClass='Type 982'
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
    dbObj.notes='http://navalhistory.flixco.info/H/148498x119821/8330/a0.htm  http://www.scribd.com/doc/65788019/Naval-Radar   some details known, others fudged accordingly.  using dBedit estimated gain, most other details pulled from given source.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=160.000000
    dbObj.mfRefRange_km=49.694000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=19.000000
    dbObj.mfScanPeriod_s=2.500000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=0.950000
    dbObj.minFrequency_Hz=2995000064.000000
    dbObj.maxFrequency_Hz=2998000128.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=90.389999
    dbObj.ERPaverage_dBW=60.169998
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-15.000000
    dbObj.lookdownLand_dB=-21.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=1.000000
    dbObj.elevationBeamwidth_deg=19.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
