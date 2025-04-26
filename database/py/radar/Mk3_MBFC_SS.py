# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Mk3 MBFC SS'
    dbObj.natoClass='Mk3 MBFC SS'
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
    dbObj.notes='http://www.kbismarck.org/forum/viewtopic.php?f=1&t=3265&start=30, BB at 28kyds, roughly 37km, using Iowa as the incident BB, so 44.6dBm.  Aircraft at roughly 40kyds.  This defines a lookdown penalty.  Assuming 20dB aircraft target.   -30.8db lookdown over water pegs the 28kyd ship range for a 44.6dBm BB.http://www.navweaps.com/Weapons/WNUS_Radar_WWII.htm'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=37.000000
    dbObj.mfRefRange_km=11.570000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=70.000000
    dbObj.mfScanPeriod_s=8.630000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.114000
    dbObj.elevationError_deg=0.150000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=84.470001
    dbObj.ERPaverage_dBW=74.470001
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=True
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-30.799999
    dbObj.lookdownLand_dB=-39.799999
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=2.000000
    dbObj.elevationBeamwidth_deg=4.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
