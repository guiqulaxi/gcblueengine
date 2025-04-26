# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='EL/M-2022'
    dbObj.natoClass='EL/M-2022'
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
    dbObj.notes='ref range extrapolated from (v)3 based on power.  tranmistter is 1.8km instead of 8kw, all else assumed equal.  to receive equivalent power at 30nm the target must be a 4.4444m² target instead of 1m², this yields a ref range of 38.266km.  smallest targets een to maximum range on (v)3 is 1967m², this size target is only seen at 255km if correct about extrapolation, this is 137.6nm, set maximum range to 130nm.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=240.759995
    dbObj.mfRefRange_km=38.265999
    dbObj.mfFieldOfView_deg=240.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=15.000000
    dbObj.mfScanPeriod_s=4.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=9150000128.000000
    dbObj.maxFrequency_Hz=9649999872.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=68.849998
    dbObj.ERPaverage_dBW=51.860001
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=3.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-9.000000
    dbObj.bandwidth_Hz=96000000.000000
    dbObj.azimuthBeamwidth_deg=3.800000
    dbObj.elevationBeamwidth_deg=8.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
