# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcOpticalDBObject()
    dbObj.mzClass='OD.2 25x 3m'
    dbObj.natoClass='OD.2 25x 3m'
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
    dbObj.notes='human eye accurracy at any task is limited to 10 arc seconds.  the error inherent to such a system can be figured as follows.  25x magnification means the apparent base length is 3m*25x, or 75m.  from here its straight trig.  We also need to remove the arc seconds and convert them to degrees, there are 3600 seconds in one hour, and there are 3600 seconds of arc in one degree, so, 10/3600=0.002777778.  Large decimal places WILL be important.  Hypoteneuse of this setup then becomes equal (baselength^2+range^2)^0.5.  This is 2001.405756m if the target is 2000m away.  the sine of that is range/hypoteneuse, of 2000/2001.405756=0.999297616.  In degrees it is equal to 87.8524158°, add to this our optical error of 0.002777775, for 87.85519235.  Now work back towards a range.  The tangent of that angle is 26.70123547, the baselength is 75m(3m*25x optics), angle times baselength then is 2002.59266.  2.6m error.  This is a theoretical maximum.  Training and human error now finds its way in to things.  Range cannot match the human eye against things like aircrafr because while ships are larger, they are rapidly below the horizon. The horizon is 3.8568*sqrt(height_m), assume 30m for a battleship, then the horizon is 21.12km away.  Then add some more for the height of your target, you need the hull to be visible for good solutions, so assume just a 5m height.  the the same calculation, then add them, for a total range of 29.74km, assume 30km is a directors maximum range then.  Error at 30km is then 593.3m.  However, GCB is flawed here.  Stereoscopic optical errors are not linear.  While the error is 600m exactly at 30167.64m.  This is an error 0.01978 in GCB terms.  Now, 300m error is found at 21393.285m, GCb finds it at 15166.835, a rather large difference.  I will of course have to use a flawed value in GCB in order to try and coerce better accuracy at shorter ranges.  Sicne the range of reality worsens with range faster than GCb does, I will peg GCB nice and close in, and then let reality get wonkier the farther out you are.  So, if I match GCB to reality at 10km, then at 20km real error would be 260, and GCB 130.  At 30km its 593.3 and 195.2.  However at 5km real is 16.2m and GCB is 32.5.  Now, to worsen things a bit more, while the Human eye is indeed capable of 10 arc seconds I will assume a worse value, of 10.5 arc seconds, 5% error introduced by the operator if the navy is VERY highly trained, 11.25 if well trained, 12.5 if ok trained, 14 is poorly trained.  Against a target at 10km, the error values would then be...65.1m theoretical maximum, 68.3 very trained, 73.3 well trained, 81.5 ok trained, 91.3 poorly trained.  As the human operator influences the sensor performance, multiple versions will of course be necessary for these.  Angular error will be assumed to simply be twice the 10 arc second human maximum, or 0.55°'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfMaxRange_km=30.000000
    dbObj.mfRefRange_km=12.017000
    dbObj.mfFieldOfView_deg=360.000000
    dbObj.minElevation_deg=-90.000000
    dbObj.maxElevation_deg=90.000000
    dbObj.mfScanPeriod_s=20.000000
    dbObj.damageEffect='GenericSensor'
    dbObj.rangeError=0.007330
    dbObj.angleError_deg=0.550000
    dbObj.elevationError_deg=0.001000
    dbObj.minFrequency_Hz=75000002379776.000000
    dbObj.maxFrequency_Hz=800000003014656.000000
    dbObj.idThreshold_dB=6.000000
    dbObj.counterMeasureFactor=0.000000
    dbObj.isSurveillance=False
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
