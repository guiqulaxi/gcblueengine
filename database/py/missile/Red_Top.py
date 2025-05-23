# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Red Top'
    dbObj.natoClass='Red Top'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=90000.000000
    dbObj.weight_kg=150.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1958.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoREDTOP.jpg'
    dbObj.mz3DModelFileName='AIM-9LandM.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=4.500000
    dbObj.damageModel='BlastFragAir31kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=2
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=0.900000
    dbObj.maxRange_km=4.850000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=8.683843
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-11.700000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-4.200000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_S_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_S_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=7.000000
    dbObj.mfMaxTurnRate_degps=36.169998
    dbObj.mfCdpsub=0.108000
    dbObj.mfCdptran=0.135000
    dbObj.mfCdpsup=0.090000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=92500.000000
    dbObj.mfBoostTime_s=1.500000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=400.000000
    dbObj.maSensorClass='RedTop IR Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=3.674603
    dbObj.invMass_kg=0.006667
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=12000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
