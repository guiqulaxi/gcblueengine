# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='DRBV 13'
    dbObj.natoClass='DRBV 13'
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
    dbObj.notes='I know nothing of this radars performance other than it was replaced on Aconit by DRBV 15.  Presumably then it must either be similar performance at lesser MTBF, MTBR, mass, cost, or DRBC 15 offers an increase in operational performance that made it a worthy upgrade, this is what im assuming.  knocking 20% off the ref range, knocking instrumented down to 150km, increasing error values slightly, boosting ERP values slightly.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=150.000000
    dbObj.mfRefRange_km=81.000000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=60.000000
    dbObj.mfScanPeriod_s=3.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.900000
    dbObj.elevationError_deg=0.270000
    dbObj.minFrequency_Hz=2400000000.000000
    dbObj.maxFrequency_Hz=2600000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=78.000000
    dbObj.ERPaverage_dBW=67.300003
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=2000000.000000
    dbObj.azimuthBeamwidth_deg=1.650000
    dbObj.elevationBeamwidth_deg=8.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
