# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='SAM-N-6c1'
    dbObj.natoClass='SAM-N-6c1'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=300000.000000
    dbObj.weight_kg=1540.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1962.000000
    dbObj.finalYear=1979.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSAM-N-6C1.jpg'
    dbObj.mz3DModelFileName='aim-9.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=27.000000
    dbObj.damageModel='BlastFragAir105kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=120.199997
    dbObj.probNoFaults=0.800000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=14.120403
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=0.900000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-1.600000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VL_LP_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VL_LP_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VL_LP_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=10.000000
    dbObj.mfMaxTurnRate_degps=47.195999
    dbObj.mfCdpsub=0.072000
    dbObj.mfCdptran=0.090000
    dbObj.mfCdpsup=0.060000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=140000.000000
    dbObj.mfBoostTime_s=7.000000
    dbObj.mfSustThrust_N=40000.000000
    dbObj.mfSustTime_s=31.000000
    dbObj.mfShutdownSpeed_mps=450.000000
    dbObj.maSensorClass='RIM-2B Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=2.572222
    dbObj.invMass_kg=0.000649
    dbObj.mnNumSegments=2
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*2
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_AGL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[0].mfAltitude_m=14850.000000
    dbObj.maFlightProfile[0].mfRange_km=15.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[1].mfAltitude_m=0.010000
    dbObj.maFlightProfile[1].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
