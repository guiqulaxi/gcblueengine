# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='KLJ-10'
    dbObj.natoClass='KLJ-10'
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
    dbObj.notes='copied from KLJ-7.  This is the radar for the J-10 fighter, essentially unchanged from the KLJ-7 except for a larger aperture array.  I do not know the difference in size, assuming  25% increased diameter, which yields a 56% larger aperture by area.  Since a rough means to estimate fighter performance is power times aperture, and power is unchanged, then this radar should detect a 3m² target at the same range that KLJ-7 detects a 3m² target, or 89.443km.  This yields a ref range of 67.962.  Assuming the same deal regarding instrumented range as with KLJ-7, this yields 177km instrumented.  Boosting ERP values by 56% as well, or a bit under 2dB.  Otherwise assuming unchanged.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=180.000000
    dbObj.mfRefRange_km=67.961998
    dbObj.mfFieldOfView_deg=170.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=56.000000
    dbObj.mfScanPeriod_s=7.760000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.100000
    dbObj.elevationError_deg=0.650000
    dbObj.minFrequency_Hz=8499999744.000000
    dbObj.maxFrequency_Hz=10499999744.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=39.810001
    dbObj.ERPaverage_dBW=29.809999
    dbObj.maxFireControlTracks=4
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=5.000000
    dbObj.elevationBeamwidth_deg=10.390000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
