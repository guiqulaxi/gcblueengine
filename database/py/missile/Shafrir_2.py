# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Shafrir 2'
    dbObj.natoClass='Shafrir 2'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=85.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=1982.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSHAFRIR2.jpg'
    dbObj.mz3DModelFileName='AIM-9LandM.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=12.000000
    dbObj.damageModel='BlastFragAir11kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=2
    dbObj.minLaunchAlt_m=30.000000
    dbObj.maxLaunchAlt_m=17000.000000
    dbObj.minRange_km=0.300000
    dbObj.maxRange_km=3.500000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=6.281494
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-15.400000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-3.000000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_S_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=20.000000
    dbObj.mfMaxTurnRate_degps=94.391998
    dbObj.mfCdpsub=0.041250
    dbObj.mfCdptran=0.049500
    dbObj.mfCdpsup=0.033000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=19550.000000
    dbObj.mfBoostTime_s=2.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=450.000000
    dbObj.maSensorClass='Shafrir-2 IR Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.011765
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=5000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.300000
    dbObj.CalculateParams()
    return dbObj
