# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='APG-63(v)1'
    dbObj.natoClass='APG-63(v)1'
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
    dbObj.notes='Copied from APG-63 and incrementally uprated.  No figures as yet.  Providing boost in maximum range from 115nm to 135nm(250km),  boosting ref range by 15% more than proportional(IE, 130@213 is equal to 7.2m² @ max range, 7.2m² @ 250km is a ref range of 152.58km, 15% greater than that is 175.47km), widening the field of view a little, shortening the update rate, tightening the beam widths.  If anyone has details specific to the APG-63(v)1 do let me know.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=250.000000
    dbObj.mfRefRange_km=175.470001
    dbObj.mfFieldOfView_deg=140.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=70.000000
    dbObj.mfScanPeriod_s=6.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.120000
    dbObj.elevationError_deg=0.190000
    dbObj.minFrequency_Hz=8999999488.000000
    dbObj.maxFrequency_Hz=10000000000.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=69.309998
    dbObj.ERPaverage_dBW=59.310001
    dbObj.maxFireControlTracks=6
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-3.000000
    dbObj.lookdownLand_dB=-12.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=3.000000
    dbObj.elevationBeamwidth_deg=2.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
