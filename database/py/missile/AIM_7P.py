# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='AIM-7P'
    dbObj.natoClass='AIM-7P'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=300000.000000
    dbObj.weight_kg=225.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1987.000000
    dbObj.finalYear=2010.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoAIM-7P.jpg'
    dbObj.mz3DModelFileName='aim-9.xml'
    dbObj.notes='the final production model of the AIM-7, it enters production in 1987, and stays until fully replaced by the AIM-120, will see this missile still in significant service until at least the mid 2000\'s, but with the balance shifting in favor of the AIM-120.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=27.000000
    dbObj.damageModel='BlastFragAir40kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=2
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=53.200001
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=9.436683
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-12.800000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-1.600000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_S_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=20.000000
    dbObj.mfMaxTurnRate_degps=54.599998
    dbObj.mfCdpsub=0.024000
    dbObj.mfCdptran=0.030000
    dbObj.mfCdpsup=0.020000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=70000.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=17000.000000
    dbObj.mfSustTime_s=16.000000
    dbObj.mfShutdownSpeed_mps=450.000000
    dbObj.maSensorClass='AIM-7M Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.004444
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=8000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.100000
    dbObj.CalculateParams()
    return dbObj
