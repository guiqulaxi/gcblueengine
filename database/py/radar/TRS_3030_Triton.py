# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcRadarDBObject()
    dbObj.mzClass='TRS 3030 Triton'
    dbObj.natoClass='TRS 3030 Triton'
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
    dbObj.notes='Triton TRS 3030 surface/air search radar.  is capable of detecting a 2m² target at 30-45km, will align for 37.5km, results in a ref range of 31.534km.  As no instrumented range is given, will assume the detection range of a 100m² target plus 20%.  Amusingly enough, this results in detecting a 100m² target at 100km, so, will set instrumented at 120km.  Gives no indication of scanned height, or if its a stacked beam or not, just that its beam is 22° in the vertical.  As it is surface/air, will assume at least 3 stacked beams for 66°. assuming half widths for elevation and azimuth beam errors.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=120.000000
    dbObj.mfRefRange_km=37.840302
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=75.000000
    dbObj.mfScanPeriod_s=2.500000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.000000
    dbObj.angleError_deg=0.057140
    dbObj.elevationError_deg=0.628570
    dbObj.minFrequency_Hz=5394999808.000000
    dbObj.maxFrequency_Hz=5424999936.000000
    dbObj.idThreshold_dB=9999.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.ERPpeak_dBW=91.980003
    dbObj.ERPaverage_dBW=76.008003
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.blindSpeed_mps=2.500000
    dbObj.lookdownWater_dB=-24.000000
    dbObj.lookdownLand_dB=-36.000000
    dbObj.bandwidth_Hz=3000000.000000
    dbObj.azimuthBeamwidth_deg=2.000000
    dbObj.elevationBeamwidth_deg=22.000000
    dbObj.effectiveSidelobes_dB=-30.000000
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.CalculateParams()
    return dbObj
