# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='DRBC 32B'
    dbObj.natoClass='DRBC 32B'
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
    dbObj.notes='shares entry with DRBC 31.  -32 use casegrain antennae while others use lightweight dishes, otherwise the same.  1.5° wide beam, 80kw peak power, 0.1m² tracked at 15km.  Being a gun FCS, assuming a max instrumented of 20nm, or 37km'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=37.000000
    dbObj.mfRefRange_km=26.700001
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=10.000000
    dbObj.mfScanPeriod_s=3.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=99.000000
    dbObj.minFrequency_Hz=5350000128.000000
    dbObj.maxFrequency_Hz=5750000128.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=4.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=79.000000
    dbObj.ERPaverage_dBW=66.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=4.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=4000000.000000
    dbObj.azimuthBeamwidth_deg=1.500000
    dbObj.elevationBeamwidth_deg=20.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
