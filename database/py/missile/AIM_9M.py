# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='AIM-9M'
    dbObj.natoClass='AIM-9M'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=90000.000000
    dbObj.weight_kg=86.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1983.000000
    dbObj.finalYear=2011.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoAIM-9M.jpg'
    dbObj.mz3DModelFileName='AIM-9M Sidewinder.xml'
    dbObj.notes='the replacement of the AIM-9L, main model for some time, production started in 1982, continued until replaced on the line by the AIM-9P.  Roughly 7000 were produced.  will assume gradually dwindling numbers, seeing as how it was still around for the 1991 gulf war.  It maintains its position in service with the navy until replaced by the AIM-9X in may 2004, and then is phased out as the AIM-9X comes on line in units.  by mid 2008, 4 years, only 3000 have been delivered, the take over of AIM-9X will be slow.  Will assume an out date of 2011.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=10.200000
    dbObj.damageModel='BlastFragAir10.5kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=2
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=1.000000
    dbObj.maxRange_km=14.800000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=6.228484
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-16.900000
    airDetectionDBObject.RCS_Model='MissileRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-4.200000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelB='IR_M_VS_R_M0.85'
    airDetectionDBObject.IR_ModelC='IR_M_VS_R_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    dbObj.mfDragArea_sm=1.000000
    dbObj.mfGmax=40.000000
    dbObj.mfMaxTurnRate_degps=188.783997
    dbObj.mfCdpsub=0.017400
    dbObj.mfCdptran=0.021750
    dbObj.mfCdpsup=0.014500
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=11500.000000
    dbObj.mfBoostTime_s=6.500000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=450.000000
    dbObj.maSensorClass='AIM-9M Seeker'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.011628
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=12000.000000
    dbObj.maFlightProfile[0].mfRange_km=0.010000
    dbObj.CalculateParams()
    return dbObj
