import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='OD.2 25x Local Iowa Main 3 15.6m'
    dbObj.natoClass='OD.2 25x Local Iowa Main 3 15.6m'
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
    dbObj.notes='See OD.2 25x 3m for how these values are arrived at.  Well trained.  Assumed to be 10m high.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=20.820000
    dbObj.mfRefRange_km=12.017000
    dbObj.mfFieldOfView_deg=270.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=20.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.001400
    dbObj.angleError_deg=0.550000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=0.000000
    dbObj.isSurveillance=True
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.isDesignator=False
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=False
    dbObj.mbDetectsMissile=False
    dbObj.mbDetectsGround=True
    dbObj.isIR=False
    dbObj.nightFactor=0.400000
    dbObj.CalculateParams()
    return dbObj
