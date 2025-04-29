# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='APG-65(h)'
    dbObj.natoClass='APG-65(h)'
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
    dbObj.notes='The modified APG-65 for the Harrier is essentially the APG-65 taken from F/A-18 Hornets when they received their upgrade, except with a smaller aperture.  Performance has been quoted in various places as between 10% and 20% weaker than in the F/A-18, as such, using a 15% performance reduction.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=251.600006
    dbObj.mfRefRange_km=51.000000
    dbObj.mfFieldOfView_deg=140.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=60.000000
    dbObj.mfScanPeriod_s=13.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.170000
    dbObj.elevationError_deg=0.210000
    dbObj.minFrequency_Hz=9500000256.000000
    dbObj.maxFrequency_Hz=10000000000.000000
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
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
