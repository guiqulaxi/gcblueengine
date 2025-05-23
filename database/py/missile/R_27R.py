# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='R-27R'
    dbObj.natoClass='AA-10 Alamo'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=200000.000000
    dbObj.weight_kg=253.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1982.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList='r27.jpg;r27-1.jpg'
    dbObj.iconFileName='mis/icoR-27R.jpg'
    dbObj.mz3DModelFileName='aa-10.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=39.000000
    dbObj.damageModel='BlastFragAir40kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=2
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=2.000000
    dbObj.maxRange_km=60.799999
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=9.436683
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-11.700000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-0.860000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_S_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=15.000000
    dbObj.mfMaxTurnRate_degps=79.639999
    dbObj.mfCdpsub=0.031200
    dbObj.mfCdptran=0.039000
    dbObj.mfCdpsup=0.026000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=90000.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=15750.000000
    dbObj.mfSustTime_s=10.750000
    dbObj.mfShutdownSpeed_mps=400.000000
    dbObj.maSensorClass='R-27R Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.714815
    dbObj.invMass_kg=0.003953
    dbObj.mnNumSegments=2
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*2
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_ASL
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_COMMAND
    dbObj.maFlightProfile[0].mfAltitude_m=13000.000000
    dbObj.maFlightProfile[0].mfRange_km=15.000000
    dbObj.maFlightProfile[1].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[1].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[1].mfAltitude_m=5000.000000
    dbObj.maFlightProfile[1].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
