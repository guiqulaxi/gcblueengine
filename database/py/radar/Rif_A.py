# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Rif-A'
    dbObj.natoClass='Ball End/Sea Gull'
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
    dbObj.notes='Old soviet surface search.  quoted capable of a cruiser at 20-22nm, destroyer at 14-16nm, periscopt(1.5m height) at 1-1.5nm.  Range accurate to 15m/nm.  scan rate of 6 seconds, 7 degree beam, 150kW, 2950-3020Mhz, 427pps at 1µs  Assuming 30dB for the destroyer at 16nm, is 5.2694.  Low PPS suggests a fairly long unambiguous range, 48dB equates to 45nm/83.5km.  using that as instrumented until further information is known.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=83.500000
    dbObj.mfRefRange_km=2.258000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=45.000000
    dbObj.mfScanPeriod_s=6.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=90.000000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=55.000000
    dbObj.ERPaverage_dBW=45.000000
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=0.000000
    dbObj.lookdownLand_dB=0.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=5.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
