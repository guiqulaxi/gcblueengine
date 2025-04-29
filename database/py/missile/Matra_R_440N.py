# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcMissileDBObject()
    dbObj.mzClass='Matra R.440N'
    dbObj.natoClass='Matra R.440N'
    dbObj.mnModelType=5
    dbObj.mnType=64
    dbObj.cost=50000.000000
    dbObj.weight_kg=80.000000
    dbObj.volume_m3=1.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country=''
    dbObj.designation=''
    dbObj.imageList=''
    dbObj.iconFileName='mis/icoR.440N.jpg'
    dbObj.mz3DModelFileName='roland-sam.xml'
    dbObj.notes='a pretty decent amount of info on this missile for a change.  2.3 second burn ending at mach 2.3, boost glide, subsonic 20 seconds after launch, 13+km vs helicopters, 10km+ vs planes,   its rare to have info to assist in determining the correct deceleration rate/drag values.  As configured it peaks at mach 2.339, reaches 6.1km range at 10km alt to intercept a headon aircraft that was engaged at 14.2km range, and can reach an intercept 13.2km distant at an altitude of 3.65km satisfying the helo kill at 13km+ as well.  Will give it the full 13km range, since crossing or retreating targets within this range should be rare, allowing the missile to generally be capable of meeting the target.'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    dbObj.mfDamage=0.600000
    dbObj.damageModel='BlastFragAir3kg'
    dbObj.damageEffect='TestMissileDmg'
    dbObj.launchSpeed_mps=0.000000
    dbObj.targetFlags=10
    dbObj.minLaunchAlt_m=0.000000
    dbObj.maxLaunchAlt_m=34567.000000
    dbObj.minRange_km=0.300000
    dbObj.maxRange_km=13.000000
    dbObj.probNoFaults=0.850000
    dbObj.payloadClass=''
    dbObj.payloadQuantity=1
    dbObj.datalinkRange_km=0.000000
    dbObj.acceptsUserCommands=False
    dbObj.detonationRange_m=5.063756
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=-15.400000
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
    dbObj.mfGmax=50.000000
    dbObj.mfMaxTurnRate_degps=531.000000
    dbObj.mfCdpsub=0.007000
    dbObj.mfCdptran=0.010500
    dbObj.mfCdpsup=0.007000
    dbObj.mfMcm=0.800000
    dbObj.mfMsupm=1.200000
    dbObj.mfBoostThrust_N=30000.000000
    dbObj.mfBoostTime_s=2.300000
    dbObj.mfSustThrust_N=0.000000
    dbObj.mfSustTime_s=0.000000
    dbObj.mfShutdownSpeed_mps=200.000000
    dbObj.maSensorClass='R.440N Guidance'
    dbObj.needsFireControl=False
    dbObj.acceptsWaypoints=False
    dbObj.fireAndForget=-1
    dbObj.isARM=-1
    dbObj.seekerFOV_rad=-1.000000
    dbObj.aczConstant_kts=1.286111
    dbObj.invMass_kg=0.012500
    dbObj.mnNumSegments=1
    dbObj.maFlightProfile=[pygcb.tsMissileFlightSegment()]*1
    dbObj.maFlightProfile[0].meAltitudeMode=pygcb.teAltitudeMode.AM_INTERCEPT
    dbObj.maFlightProfile[0].meGuidanceMode=pygcb.teGuidanceMode.GM_SENSOR1
    dbObj.maFlightProfile[0].mfAltitude_m=1500.000000
    dbObj.maFlightProfile[0].mfRange_km=4.000000
    dbObj.CalculateParams()
    return dbObj
