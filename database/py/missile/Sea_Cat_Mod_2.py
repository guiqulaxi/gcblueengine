# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Sea Cat Mod.2'
    dbObj.natoClass='Sea Cat Mod.2'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=100000.000000
    dbObj.weight_kg=68.000000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoSEA CAT.jpg'
    dbObj.mz3DModelFileName='seacat.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=3.000000
    dbObj.damageModel='BlastFragAir18kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=0.250000
    dbObj.maxRange_km=3.500000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=7.210452
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-12.100000
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
    dbObj.mfGmax=4.000000
    dbObj.mfMaxTurnRate_degps=28.299999
    dbObj.mfCdpsub=0.036000
    dbObj.mfCdptran=0.045000
    dbObj.mfCdpsup=0.030000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.150000
    dbObj.mfBoostThrust_N=17500.000000
    dbObj.mfBoostTime_s=1.000000
    dbObj.mfSustThrust_N=3100.000000
    dbObj.mfSustTime_s=14.600000
    dbObj.mfShutdownSpeed_mps=150.000000
    dbObj.maSensorClass='Sea Cat Mod2 Seeker'
    dbObj.needsFireControl=True
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=6.430555
    dbObj.invMass_kg=0.014706
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=3000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.000000
    dbObj.CalculateParams()
    return dbObj
