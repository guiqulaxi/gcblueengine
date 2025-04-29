# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='BGM-71A TOW'
    dbObj.natoClass='BGM-71A TOW'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=19.000000
    dbObj.volume_m3=0.250000
    dbObj.initialYear=1970.000000
    dbObj.finalYear=1987.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoBGM71.jpg'
    dbObj.mz3DModelFileName='roland-sam.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=180.000000
    dbObj.damageModel='Blast4kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=5
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=4.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=1.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-19.000000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=0.000000
    airDetectionDBObject.irSignature_dB=30.000000
    airDetectionDBObject.IR_ModelA='MissileIR1'
    airDetectionDBObject.IR_ModelB='MissileIR1'
    airDetectionDBObject.IR_ModelC='MissileIR1'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=8.000000
    dbObj.mfMaxTurnRate_degps=97.089996
    dbObj.mfCdpsub=0.004400
    dbObj.mfCdptran=0.006000
    dbObj.mfCdpsup=0.004000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=3650.000000
    dbObj.mfBoostTime_s=1.500000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=100.000000
    dbObj.maSensorClass='TOW Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=3.215278
    dbObj.invMass_kg=0.052632
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=80.000000
    dbObj.maFlightProfile[0].mfRange_km=0.500000
    dbObj.CalculateParams()
    return dbObj
