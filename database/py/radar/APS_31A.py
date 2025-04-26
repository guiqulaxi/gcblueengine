# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='APS-31A'
    dbObj.natoClass='APS-31A'
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
    dbObj.notes='http://radar.tpub.com/TM-11-487C-1/TM-11-487C-10867.htm, assuming 20dBsm gain, ref set to detect 60dBsm at max range assuming over water.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=370.000000
    dbObj.mfRefRange_km=19.642719
    dbObj.mfFieldOfView_deg=150.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=20.000000
    dbObj.mfScanPeriod_s=8.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.460000
    dbObj.elevationError_deg=0.310000
    dbObj.minFrequency_Hz=9374999552.000000
    dbObj.maxFrequency_Hz=9374999552.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=67.160004
    dbObj.ERPaverage_dBW=36.700001
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-9.000000
    dbObj.lookdownLand_dB=-18.000000
    dbObj.bandwidth_Hz=1000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=20.000000
    dbObj.effectiveSidelobes_dB=-20.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
