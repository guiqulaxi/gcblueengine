# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='AS.37 Martel'
    dbObj.natoClass='AS.37 Martel'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=0.000000
    dbObj.weight_kg=530.700012
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.599976
    dbObj.finalYear=1994.300049
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoAS37.jpg'
    dbObj.mz3DModelFileName='mm-38.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=100.000000
    dbObj.damageModel='Pen70kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=1
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=74.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=0.000000
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-9.000000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-2.000000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='MissileIR1'
    airDetectionDBObject.IR_ModelB='MissileIR1'
    airDetectionDBObject.IR_ModelC='MissileIR1'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=10.000000
    dbObj.mfMaxTurnRate_degps=118.000000
    dbObj.mfCdpsub=0.016800
    dbObj.mfCdptran=0.021000
    dbObj.mfCdpsup=0.036000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=60000.000000
    dbObj.mfBoostTime_s=2.400000
    dbObj.mfSustThrust_N=2400.000000
    dbObj.mfSustTime_s=22.200001
    dbObj.mfShutdownSpeed_mps=180.000000
    dbObj.maSensorClass='AGM-45 Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=2.572222
    dbObj.invMass_kg=0.001884
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=0.010000
    dbObj.maFlightProfile[0].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
