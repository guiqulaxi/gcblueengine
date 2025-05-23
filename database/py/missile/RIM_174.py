# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='RIM-174'
    dbObj.natoClass='RIM-174'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=5000000.000000
    dbObj.weight_kg=1500.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=2012.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoRIM-174.jpg'
    dbObj.mz3DModelFileName='roland-sam.xml'
    dbObj.notes='Contributed by greengills'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=62.000000
    dbObj.damageModel='BlastFragAir62.5kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=11
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=370.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=11.247567
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-8.300000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=1.120000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_L_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_L_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_L_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=30.000000
    dbObj.mfMaxTurnRate_degps=90.000000
    dbObj.mfCdpsub=0.100000
    dbObj.mfCdptran=0.200000
    dbObj.mfCdpsup=0.600000
    dbObj.mfMcm=0.010000
    dbObj.mfMsupm=0.020000
    dbObj.mfBoostThrust_N=190000.000000
    dbObj.mfBoostTime_s=330.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=100.000000
    dbObj.maSensorClass='AIM-120 Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.000667
    dbObj.mnNumSegments=4
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*4
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[0].mfAltitude_m=14000.000000
    dbObj.maFlightProfile[0].mfRange_km=355.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[1].mfAltitude_m=14000.000000
    dbObj.maFlightProfile[1].mfRange_km=37.000000
    dbObj.maFlightProfile[2].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[2].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[2].mfAltitude_m=14000.000000
    dbObj.maFlightProfile[2].mfRange_km=15.000000
    dbObj.maFlightProfile[3].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[3].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[3].mfAltitude_m=14000.000000
    dbObj.maFlightProfile[3].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
