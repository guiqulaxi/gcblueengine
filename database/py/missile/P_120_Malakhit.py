# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='P-120 Malakhit'
    dbObj.natoClass='SS-N-9 Siren'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=2952.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoP-120.jpg'
    dbObj.mz3DModelFileName='mm-38.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=750.000000
    dbObj.damageModel='Blast500kg'
    dbObj.damageEffect='TestMissileDmg2'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=-50.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=150.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=1.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=2.100000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.580000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_L_LP_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_L_LP_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_L_LP_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=5.000000
    dbObj.mfMaxTurnRate_degps=21.850000
    dbObj.mfCdpsub=0.025200
    dbObj.mfCdptran=0.031500
    dbObj.mfCdpsup=0.021000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=300000.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=3600.000000
    dbObj.mfSustTime_s=434.000000
    dbObj.mfShutdownSpeed_mps=250.000000
    dbObj.maSensorClass='SS-N-9 seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=5.144444
    dbObj.invMass_kg=0.000339
    dbObj.mnNumSegments=2
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*2
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[0].mfAltitude_m=100.000000
    dbObj.maFlightProfile[0].mfRange_km=40.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[1].mfAltitude_m=60.000000
    dbObj.maFlightProfile[1].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
