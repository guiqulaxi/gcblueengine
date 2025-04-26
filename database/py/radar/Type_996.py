# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Type 996'
    dbObj.natoClass='Type 996'
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
    dbObj.notes='Due to a shortage of time, shortcuts were taken with this radar.  I know only that its scan rate is 14rpm, and that it can track a fighter out to 115km, and a maritime aircraft(P-3 Orion/IL-76 May?) out to more than 150km.  These details aside, the radar is a direct copy of the SPS-58A.  Aligned for a 50m² target at 160km.  This is apparantly a 3D radar with surface search capabilities.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=241.000000
    dbObj.mfRefRange_km=60.169998
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=18.000000
    dbObj.mfScanPeriod_s=4.290000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.200000
    dbObj.elevationError_deg=1.130000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=49.369999
    dbObj.ERPaverage_dBW=39.369999
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=18.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
