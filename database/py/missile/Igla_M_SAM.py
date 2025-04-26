# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Igla-M SAM'
    dbObj.natoClass='SA-N-10 Grouse'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=50000.000000
    dbObj.weight_kg=10.800000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1980.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoIGLA-M.jpg'
    dbObj.mz3DModelFileName='rapier-sam.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=3.000000
    dbObj.damageModel='BlastFragAir1.2kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=-1.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=3.500000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=4.711468
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-21.799999
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-8.160000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VS_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=15.000000
    dbObj.mfMaxTurnRate_degps=91.021004
    dbObj.mfCdpsub=0.001800
    dbObj.mfCdptran=0.002250
    dbObj.mfCdpsup=0.001500
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.100000
    dbObj.mfBoostThrust_N=2850.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=350.000000
    dbObj.maSensorClass='Igla-M Infrared'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.714815
    dbObj.invMass_kg=0.092593
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=2000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.000000
    dbObj.CalculateParams()
    return dbObj
