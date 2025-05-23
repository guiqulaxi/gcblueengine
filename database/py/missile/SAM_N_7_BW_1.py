# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='SAM-N-7 BW-1'
    dbObj.natoClass='SAM-N-7 BW-1'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=300000.000000
    dbObj.weight_kg=1064.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1956.000000
    dbObj.finalYear=1963.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSAM-N-7_BW-1.jpg'
    dbObj.mz3DModelFileName='aim-9.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=27.000000
    dbObj.damageModel='BlastFragAir100kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=10.700000
    dbObj.probNoFaults=0.700000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=13.923346
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-8.300000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-1.600000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_M_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_M_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_M_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=10.000000
    dbObj.mfMaxTurnRate_degps=49.390999
    dbObj.mfCdpsub=0.072000
    dbObj.mfCdptran=0.090000
    dbObj.mfCdpsup=0.060000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=225000.000000
    dbObj.mfBoostTime_s=2.500000
    dbObj.mfSustThrust_N=32000.000000
    dbObj.mfSustTime_s=14.300000
    dbObj.mfShutdownSpeed_mps=430.000000
    dbObj.maSensorClass='RIM-2B Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=2.572222
    dbObj.invMass_kg=0.000940
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=8000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.100000
    dbObj.CalculateParams()
    return dbObj
