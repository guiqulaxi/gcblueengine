# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='KSR-2'
    dbObj.natoClass='AS-5 Kelt'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=4000.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1965.000000
    dbObj.finalYear=1991.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoKSR2.jpg'
    dbObj.mz3DModelFileName='as-4.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=450.000000
    dbObj.damageModel='Pen950kg'
    dbObj.damageEffect='TestMissileDmg2'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=500.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=170.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=6.000000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=3.650000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VL_LP_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VL_LP_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VL_LP_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=19.570000
    dbObj.mfGmax=5.000000
    dbObj.mfMaxTurnRate_degps=53.099998
    dbObj.mfCdpsub=0.090000
    dbObj.mfCdptran=0.162000
    dbObj.mfCdpsup=0.135000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=16900.000000
    dbObj.mfBoostTime_s=495.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=200.000000
    dbObj.maSensorClass='KSR-2 AR Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=5.144444
    dbObj.invMass_kg=0.000250
    dbObj.mnNumSegments=2
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*2
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[0].mfAltitude_m=500.000000
    dbObj.maFlightProfile[0].mfRange_km=30.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[1].mfAltitude_m=0.000000
    dbObj.maFlightProfile[1].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
