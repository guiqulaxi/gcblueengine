# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='Type-909 FC'
    dbObj.natoClass='Type-909 FC'
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
    dbObj.notes='ref_range adjusted to permit detection of a 25m² target out to 150km.  It was set for a 400m² target acquired at just 150km.  This adjustment may be too much.  I want an exocet to get dangerously close as they did in the falklands war.  The Exocet has an assigned RCS of -9.47, aspect 0 is -3dB, so -12.47.  Lookdown water is -30, so the missile has an efective RCS of -42.47 when on the deck.  to detect at 6km, the effective RCS needs to be -41.35.  For this to apply only to aircraft at or under 50m altitude, at 14000m range, the elevation beam width must be no larger than 0.204627°.  I will use 0.2 instead of the current value of 5.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=150.000000
    dbObj.mfRefRange_km=64.846001
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=70.000000
    dbObj.mfScanPeriod_s=1.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.420000
    dbObj.elevationError_deg=0.280000
    dbObj.minFrequency_Hz=3000000000.000000
    dbObj.maxFrequency_Hz=3500000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=False
    dbObj.ERPpeak_dBW=60.000000
    dbObj.ERPaverage_dBW=50.000000
    dbObj.maxFireControlTracks=2
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=0.000000
    dbObj.lookdownWater_dB=-30.000000
    dbObj.lookdownLand_dB=-40.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=0.500000
    dbObj.elevationBeamwidth_deg=0.500000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=False
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=False
    dbObj.CalculateParams()
    return dbObj
