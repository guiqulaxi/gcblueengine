# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='R-4RM Seeker'
    dbObj.natoClass='R-4RM Seeker'
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
    dbObj.notes='Aligned to detect a 100m² target(large bomber) at 48km, but capable of exceeding this, the missile itself can headon a 550kt target from 77km...Also features better resistance to ground/surface clutter'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=80.000000
    dbObj.mfRefRange_km=15.200000
    dbObj.mfFieldOfView_deg=90.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=45.000000
    dbObj.mfScanPeriod_s=3.750000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=6.790000
    dbObj.elevationError_deg=4.520000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=-99.000000
    dbObj.ERPaverage_dBW=-109.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=True
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=0.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=5.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
