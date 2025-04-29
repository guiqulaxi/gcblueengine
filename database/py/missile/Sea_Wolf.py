# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Sea Wolf'
    dbObj.natoClass='Sea Wolf'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=100000.000000
    dbObj.weight_kg=82.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSEAWOLF.jpg'
    dbObj.mz3DModelFileName='seawolf.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=3.000000
    dbObj.damageModel='BlastFragMis14kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=3.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=4.734828
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-9.400000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=1.210000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VS_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=0.000000
    dbObj.mfGmax=25.000000
    dbObj.mfMaxTurnRate_degps=54.599998
    dbObj.mfCdpsub=0.008400
    dbObj.mfCdptran=0.010500
    dbObj.mfCdpsup=0.007000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=32000.000000
    dbObj.mfBoostTime_s=2.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=500.000000
    dbObj.maSensorClass='Seawolf-SAM Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.012195
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=3000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.000000
    dbObj.CalculateParams()
    return dbObj
