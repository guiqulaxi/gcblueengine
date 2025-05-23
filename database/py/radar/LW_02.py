# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='LW-02'
    dbObj.natoClass='LW-02'
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
    dbObj.notes='500kW peak power, 100nm claimed for aircraft target, 2.2 degree resolution in azimuth, 500,000w is 56.99dB, 30dB gain, for a P_erp of 86.99.  Antenna is a little shorter in height than it is wide, assuming 3° vertical beam width.  Ref range of 104.15km(aircraft at 100nm, aqssumed 10m²)km.  Will assume a 350km range as this corresponds to a target size of 127.56m, or 130m².'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=300.000000
    dbObj.mfRefRange_km=104.150002
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=60.000000
    dbObj.mfScanPeriod_s=8.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=1.100000
    dbObj.elevationError_deg=1.500000
    dbObj.minFrequency_Hz=1215000064.000000
    dbObj.maxFrequency_Hz=1390000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=86.989998
    dbObj.ERPaverage_dBW=72.978699
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-15.000000
    dbObj.lookdownLand_dB=-24.000000
    dbObj.bandwidth_Hz=5000000.000000
    dbObj.azimuthBeamwidth_deg=2.200000
    dbObj.elevationBeamwidth_deg=3.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
