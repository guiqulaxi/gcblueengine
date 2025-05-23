# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='SPG-62 8'
    dbObj.natoClass='SPG-62 8'
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
    dbObj.notes='test version of SPG-62 illuminator for SM-2 Aegis.  Naval institute Guide to World naval Weapons systems cties RIM-156 as nearly exceeding the limits of the illuminator.  As such an maximum effective engagement range of 240km is then nearly beyond what the illuminator can do.  I have adjusted the illuminator for a 20dBsm target like a Tu-95 to be illuminated at up to 260km, a 10dBsm target like many early cold war fighters engaged at up to 147km, a 5 dBsm(like many late cold war fighters) target at 110.6km, 2dBsm(like the F-16) at 93.1km, -7dBsm(like the Rafale) at 55km. This means many missiles will not be illuminated to extreme ranges, but missiles like the Kh-22(5.33 dBsm:8.33 RCS, -3dB signature) can be pegged out to 112.8km.  GCB cannot cope with multiple sensors with multiple FC\'s with the same name on one ship, nor can it cope with more than two FC\'s applicable to one function, for now these illuminator/FC\'s must be combined into 360° arcs'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=300.000000
    dbObj.mfRefRange_km=83.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=87.000000
    dbObj.mfScanPeriod_s=1.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.004500
    dbObj.elevationError_deg=0.016250
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=0.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=41.580002
    dbObj.ERPaverage_dBW=31.580000
    dbObj.maxFireControlTracks=8
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=0.500000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
