# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Sea Dart Mod2'
    dbObj.natoClass='Sea Dart Mod2'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=100000.000000
    dbObj.weight_kg=544.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1990.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSEA DART M2.jpg'
    dbObj.mz3DModelFileName='seadart.xml'
    dbObj.notes='Mod2 has guidance updates that permit the missile to achieve far better range than previously managed.  The missile itself is otherwise unchanged.  the maximum effective range is expected to increase to nearly double as a result.  I set a guidance mode than put the missile up to a cruising alt chosen to reach the desired range increase.  I have found it necessary to rework the sustainer however, as the missile was achieving speeds FAR too high at higher altitudes.  the impulse of the sustainer is unchanged.  it was 32knx58s=1856kNs.  Thrust has been reduced, and duration increased accordingly to maintain this impulse value.  Doing so necessitated an alteration of the booster as well to prevent an odd seeming loss of speed when the stages changed.  Booster cutout occurs at 665m/s, mach 2.013 @ 2470m, continuing the climb speed bleeds down to 631.1m/s or mach 1.963(each occurs at a different altitude).  minimum missile speed prior to burnout is 573.2m/s, mach 1.68, over a 20km intercept.  Powered flight ends at 79.8km from launch point, Mod0 currently expires at 46.3km, this puts the range improvement at 172.4% greater powered range.  kinematic range is 99km, mod 0 kinematic range is 59.1km, an improvement of 167.5%.  Missile speed is a peak of 1040.3m/s(mach 3) at burnout, this compares to 913.083m/s(mach 2.68).  Average speed throughout the flight is 756.6m/s compared to 697.6m/s.  intercept occurs in 132 seconds compared to 86 seconds.  Average speed at 86 seconds is 851.9m/s.  The missile engages a target at 83.4km(the limit for the mod0) in 80 seconds with an average speed of 774.5m/s, the intercept occuring 7.5% sooner.  The range itself comes to equal to the RIM-66H(100km) at 99km.  Compared to RIM-66H, peak speed is approximately equal, close in reaction is considerably weaker however at range the Sea Dart is definitely the superior weapon.  Effective range of the RIM-66 is larger, only because its average speed is lower, allowing the target to cover more ground before the intercept occurs.  At ranges of less than 48km RIM-66 achieves intercept in less time than Sea Dart.  At 24km RIM-66 is 8.25 seconds faster, at 18km it is 8.76 seconds faster.  At any range over 48km Sea dart arrives first, at 50km it is  1.65 seconds faster, by 75 km it is 21.9 seconds faster, and by maximum range of 99km it is 36.54 seconds faster than RIM-66H.  This disparity in performance will be studied further at a later date.  I may be back to this, and the Sea dart might well be in for a significant reworking of its performance.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=4.000000
    dbObj.damageModel='BlastFragMis24kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=99.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.593047
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-4.700000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=2.000000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_S_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=0.000000
    dbObj.mfGmax=15.000000
    dbObj.mfMaxTurnRate_degps=54.599998
    dbObj.mfCdpsub=0.072000
    dbObj.mfCdptran=0.090000
    dbObj.mfCdpsup=0.060000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=61500.000000
    dbObj.mfBoostTime_s=8.000000
    dbObj.mfSustThrust_N=22000.000000
    dbObj.mfSustTime_s=84.300003
    dbObj.mfShutdownSpeed_mps=400.000000
    dbObj.maSensorClass='Sea Dart Mod3 Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.714815
    dbObj.invMass_kg=0.001838
    dbObj.mnNumSegments=2
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*2
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[0].mfAltitude_m=11500.000000
    dbObj.maFlightProfile[0].mfRange_km=20.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[1].mfAltitude_m=0.000000
    dbObj.maFlightProfile[1].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
