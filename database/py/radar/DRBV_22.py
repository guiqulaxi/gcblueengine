# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='DRBV 22'
    dbObj.natoClass='DRBV 22'
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
    dbObj.notes='smaller export version of DRBV23.  600kW peak power, 26dB gain, 12RPM, 70nm vs a 10m² target'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=350.000000
    dbObj.mfRefRange_km=72.910004
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=15.000000
    dbObj.mfScanPeriod_s=5.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.125000
    dbObj.elevationError_deg=99.000000
    dbObj.minFrequency_Hz=1300000000.000000
    dbObj.maxFrequency_Hz=1390000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=83.800003
    dbObj.ERPaverage_dBW=54.799999
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=4.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=2000000.000000
    dbObj.azimuthBeamwidth_deg=3.500000
    dbObj.elevationBeamwidth_deg=16.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
