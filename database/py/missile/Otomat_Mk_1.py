# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Otomat Mk-1'
    dbObj.natoClass='Otomat Mk-1'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=670.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoOTOMAT MK1.jpg'
    dbObj.mz3DModelFileName='mm-38.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='Pen220kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=6.000000
    dbObj.maxRange_km=180.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-2.700000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-2.000000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_M_LP_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_M_LP_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_M_LP_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=8.000000
    dbObj.mfMaxTurnRate_degps=15.000000
    dbObj.mfCdpsub=0.440000
    dbObj.mfCdptran=1.000000
    dbObj.mfCdpsup=3.000000
    dbObj.mfMcm=0.900000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=100000.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=50000.000000
    dbObj.mfSustTime_s=602.000000
    dbObj.mfShutdownSpeed_mps=100.000000
    dbObj.maSensorClass='ST-2'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=3.215278
    dbObj.invMass_kg=0.001493
    dbObj.mnNumSegments=5
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*5
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[0].mfAltitude_m=20.000000
    dbObj.maFlightProfile[0].mfRange_km=180.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[1].mfAltitude_m=20.000000
    dbObj.maFlightProfile[1].mfRange_km=90.000000
    dbObj.maFlightProfile[2].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[2].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[2].mfAltitude_m=20.000000
    dbObj.maFlightProfile[2].mfRange_km=45.000000
    dbObj.maFlightProfile[3].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[3].meGuidanceMode=pygcb.teGuidanceMode.GM_NAV
    dbObj.maFlightProfile[3].mfAltitude_m=20.000000
    dbObj.maFlightProfile[3].mfRange_km=22.000000
    dbObj.maFlightProfile[4].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[4].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[4].mfAltitude_m=10.000000
    dbObj.maFlightProfile[4].mfRange_km=10.000000
    dbObj.CalculateParams()
    return dbObj
