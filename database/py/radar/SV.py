# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SV'
    dbObj.natoClass='SV'
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
    dbObj.notes='http://pwencycl.kgbudge.com/S/v/SV_air_search_radar.htm    Aligned to peg a 10m fighter, and 63m naval bomber to 12km and 19km respectively, also, lookdown penalty used to restrain the horizon search such that a 2kton destroyer is detected at 16km, and a 6kton cruiser is detected at 24km.  Assumed 29.4dB gain based on 5° wide beam, and estimated 30° tall beam'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=30.000000
    dbObj.mfRefRange_km=6.800000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=20.000000
    dbObj.mfScanPeriod_s=6.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=2.000000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=191000000.000000
    dbObj.maxFrequency_Hz=198000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=86.355003
    dbObj.ERPaverage_dBW=51.125999
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=-24.000000
    dbObj.lookdownLand_dB=-31.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=30.000000
    dbObj.effectiveSidelobes_dB=-15.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
