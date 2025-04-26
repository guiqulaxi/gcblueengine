# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Agrion 15'
    dbObj.natoClass='Agrion 15'
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
    dbObj.notes='1.5µs and 0.25µs pulses @ 1200, 600, and 300pps.  peak power of 108kWclaimed range is 28nm on a periscope, 60nm on a patrol boat, and 130nm on a medium sized ship, all in sea state 3 or 4.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=240.000000
    dbObj.mfRefRange_km=23.890800
    dbObj.mfFieldOfView_deg=240.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=20.000000
    dbObj.mfScanPeriod_s=4.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.320000
    dbObj.elevationError_deg=0.220000
    dbObj.minFrequency_Hz=8949999616.000000
    dbObj.maxFrequency_Hz=9249999872.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=78.334244
    dbObj.ERPaverage_dBW=44.866360
    dbObj.maxFireControlTracks=2
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-6.000000
    dbObj.bandwidth_Hz=30000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=5.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
