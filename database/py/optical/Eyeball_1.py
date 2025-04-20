import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='Eyeball-1'
    dbObj.natoClass='Eyeball-1'
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
    dbObj.notes='the human eye at 20/20 can resolve 1 arc minute of detail, the E on the 20/20 line of a snell chart is 5 arc miutes in size, with three horizontal lines and 2 spaces, each of 1 arc minute in width.  1 meter at 3.43775km is equal to 1 arc minute.  however, this is straight trig, it doesn\'t take into account how GCB will treat this value in its formulae.  Since this could be the equivalent of just making out a dark spec in the distance, its a valid target imo.  Oddly enough, for a 0dB target, which 1m² is, the trig result matches the ref range necessary in GCB to detect with a 50% chance, or an SNR of 0.  It is important to note that few ship\'s lookouts are using their own unaided eyesight, it is generally boosted by optics of some sort, such as binoculars.  if we assume 20x magnification as standard fit, then we are looking for a target that at 3.43775km is equal to 1/20 of 1m², or 0.05m².  to resolve that at that range, a ref range of 12.0117 is necessary.  and this is why I have assigned it a such.  1 arc minute is 1/60 of a degree, or 0.1667°.  lookouts must relay info, and so the full angular resolution will be lost to calls of bearing, assumed to be in 5° allotments.  Assumed to be capable of accurate ranging(more than one lookout, rangefinders, etc.)'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=225.000000
    dbObj.mfRefRange_km=12.011700
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=16.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=1.500000
    dbObj.angleError_deg=0.001000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=1.000000
    dbObj.isSurveillance=True
    dbObj.maxFireControlTracks=0
    dbObj.isSemiactive=False
    dbObj.isDesignator=False
    dbObj.mbDetectsSurface=True
    dbObj.mbDetectsAir=True
    dbObj.mbDetectsMissile=True
    dbObj.mbDetectsGround=True
    dbObj.isIR=False
    dbObj.nightFactor=0.500000
    dbObj.CalculateParams()
    return dbObj
