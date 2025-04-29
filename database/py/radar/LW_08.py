# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='LW-08'
    dbObj.natoClass='LW-08'
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
    dbObj.notes='150kW peak power, 5.2kW average power, 145nm claimed for 2m² target, 2.2 degree resolution in azimuth, 300m in range.  150,000w is 51.761dB, 30dB gain, for a P_erp of 81.761.  Antenna is a little shorter in height than it is wide, assuming 3° vertical beam width.  Ref range of an astounding 225.814km.  Will assume a 600km range as this corresponds to a radar horizon at 50,000ft/15,200m, and a target size of 49.85m, or 50m².'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=600.000000
    dbObj.mfRefRange_km=225.813995
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=60.000000
    dbObj.mfScanPeriod_s=8.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=1.100000
    dbObj.elevationError_deg=1.500000
    dbObj.minFrequency_Hz=1250000000.000000
    dbObj.maxFrequency_Hz=1350000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=81.761002
    dbObj.ERPaverage_dBW=67.160004
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=69000000.000000
    dbObj.azimuthBeamwidth_deg=2.200000
    dbObj.elevationBeamwidth_deg=3.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
