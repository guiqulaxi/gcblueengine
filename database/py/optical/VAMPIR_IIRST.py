import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='VAMPIR IIRST'
    dbObj.natoClass='VAMPIR IIRST'
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
    dbObj.notes='-20° to +45°, scans in 5° bands at 90rpm, so, it needs 9 scans to complete a horizon to max_el scan, so cut RPM from 90 to 10, and we get a 6 second update rate.  However, while it can scan in either wide or narrow band IR, it can do so in only one band a'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=160.000000
    dbObj.mfRefRange_km=19.500000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=45.000000
    dbObj.mfScanPeriod_s=12.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.085900
    dbObj.elevationError_deg=0.085900
    dbObj.minFrequency_Hz=0.000000
    dbObj.maxFrequency_Hz=0.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.maxFireControlTracks=1
    dbObj.isSemiactive=False
    dbObj.isDesignator=True
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.isIR=True
    dbObj.nightFactor=1.000000
    dbObj.CalculateParams()
    return dbObj
