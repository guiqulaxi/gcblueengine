# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='FIM-92 Stinger'
    dbObj.natoClass='FIM-92 Stinger'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=50000.000000
    dbObj.weight_kg=10.100000
    dbObj.volume_m3=3.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoFIM-92.jpg'
    dbObj.mz3DModelFileName='roland-sam.xml'
    dbObj.notes='finally got around to editing this missile.  modified from Mistral which met given specs.  Stinger was given slightly lower drag, much less thrust power over a slightly longer duration, and a more normal shutdown speed.  achieves mach 2.2, and has highly variable range depending on target alt.  3.1km @ 3000m alt, 4km @ 1500m, 4.15km @ 15m.  the motor is dual pulse, which i assume means boost sustain, however I am treating it like the Mistral in this case, in that the booster is only used to exit the launch tube.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.600000
    dbObj.damageModel='BlastFragAir2kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=40.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=0.500000
    dbObj.maxRange_km=3.400000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=4.878683
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-22.100000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-7.870000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VS_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=25.000000
    dbObj.mfMaxTurnRate_degps=133.000000
    dbObj.mfCdpsub=0.001980
    dbObj.mfCdptran=0.002250
    dbObj.mfCdpsup=0.001800
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=2900.000000
    dbObj.mfBoostTime_s=3.000000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=400.000000
    dbObj.maSensorClass='FIM-92 IR Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.099010
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=1000.000000
    dbObj.maFlightProfile[0].mfRange_km=5.000000
    dbObj.CalculateParams()
    return dbObj
