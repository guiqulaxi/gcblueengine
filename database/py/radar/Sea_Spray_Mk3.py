# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Sea Spray Mk3'
    dbObj.natoClass='Sea Spray Mk3'
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
    dbObj.notes='Im facing a near complete lack of information regarding performance of the Sea Spray.  Instrumented range is 100nm(185.2km).  The Sea king AEW radar SearchWater(Ari 5980) detects a medium sized warship at 130nm.  since carriers at around 30-35dB, medium sized warships should be found around 27-30dB, assuming 28.5dB.  Thats puts Searchwater\'s ref range at 46.675km.  It(searchwater) also quotes a range of 28+nm for a snorkel and this ref range approximates this as well putting range to a  1m² target at 25.2nm.  Will use a vaule less than this for the Sea spray, again as it isn\'t intended for EW purposes and more for target acquisition.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=185.199997
    dbObj.mfRefRange_km=10.367000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=10.000000
    dbObj.mfScanPeriod_s=2.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.170000
    dbObj.elevationError_deg=0.210000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=54.750000
    dbObj.ERPaverage_dBW=44.750000
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=3.300000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
