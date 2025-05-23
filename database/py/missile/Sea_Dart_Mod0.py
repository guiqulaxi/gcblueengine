# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Sea Dart Mod0'
    dbObj.natoClass='Sea Dart Mod0'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=100000.000000
    dbObj.weight_kg=544.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSEA DART M1.jpg'
    dbObj.mz3DModelFileName='seadart.xml'
    dbObj.notes='this missile is setup as an odd case considering how most other weapons have been spec\'d, and may trigger a review of the other ramjet powered weapons.  I had originally setup the weapons much as i would have done firing in initial numbers that should approximate the desired performance, and then doubled the run of the sustainer, tweaked thrust and drag to remain within speed bounds, and achieve the desired range, and then called her ready.  Further reading has suggested the quoted ranges for the Sea Dart do not include her ballistic end phase, because the missile is hardly effective once without power due to its unfavorable aerodynamics, bleeding off speed at a very rapid pace compared to rocket powered missiles.  The quoted range is often 25-30nm, as such I have assumed powered flight to 25nm.  The result is a kinetic range of 59.1km and an engagement range of 83.4km against 550kt closing targets.  The missile sustains a very high average speed, due entirely to the sustainer keeping its speed high for nearly all of its flight.  In close it is inferior to SM1/SM2, the standard series achieving a far higher peak speed and thus close in reaction time.  For ranges approaching 64km the playing field is much more level if not in favour of the Sea Dart.  For engagement ranges in excess of 64km the tables again turn as this is the furthest range to engage a 550kt target at 10km alt and still be powered for the duration, any further and the intercept itself is unpowered, speed is very rapidly bled, and the better missile rapidly becomes the SM2.  As a starting point I took the originally assigned drag and quadrupled it, then weakened the booster to just reach mach two under any conditions(thrust down from 130kN to 122kN, same duration), then improved the sustainer from 23kN for 11 seconds to 32kN for 58 seconds, and reduced the minspeed from 500m/s to 400m/s.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=4.000000
    dbObj.damageModel='BlastFragAir24kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=59.099998
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=7.909763
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
    dbObj.mfCdpsub=0.020000
    dbObj.mfCdptran=0.090000
    dbObj.mfCdpsup=0.060000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=122000.000000
    dbObj.mfBoostTime_s=3.500000
    dbObj.mfSustThrust_N=32000.000000
    dbObj.mfSustTime_s=58.000000
    dbObj.mfShutdownSpeed_mps=400.000000
    dbObj.maSensorClass='Sea Dart Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.714815
    dbObj.invMass_kg=0.001838
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=10000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.000000
    dbObj.CalculateParams()
    return dbObj
