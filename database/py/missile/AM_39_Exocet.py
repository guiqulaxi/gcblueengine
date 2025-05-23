# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='AM-39 Exocet'
    dbObj.natoClass='AM-39 Exocet'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=400000.000000
    dbObj.weight_kg=655.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1979.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoAM-39.jpg'
    dbObj.mz3DModelFileName='am-39.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=50.000000
    dbObj.damageModel='Pen165kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=100.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=70.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-8.100000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=1.370000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_M_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_M_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_M_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=0.010000
    dbObj.mfGmax=15.000000
    dbObj.mfMaxTurnRate_degps=65.599998
    dbObj.mfCdpsub=0.060000
    dbObj.mfCdptran=0.075000
    dbObj.mfCdpsup=0.050000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=9200.000000
    dbObj.mfBoostTime_s=204.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=250.000000
    dbObj.maSensorClass='AM-39 Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.714815
    dbObj.invMass_kg=0.001527
    dbObj.mnNumSegments=3
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*3
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[0].mfAltitude_m=3.000000
    dbObj.maFlightProfile[0].mfRange_km=20.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[1].mfAltitude_m=3.000000
    dbObj.maFlightProfile[1].mfRange_km=10.000000
    dbObj.maFlightProfile[2].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[2].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[2].mfAltitude_m=0.010000
    dbObj.maFlightProfile[2].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
