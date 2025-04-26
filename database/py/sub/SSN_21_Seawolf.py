# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='SSN 21 Seawolf'
    dbObj.natoClass='SSN 21 Seawolf'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=8060000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1995.477051
    dbObj.finalYear=2999.997314
    dbObj.country='USA'
    dbObj.designation='SSN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes='USS Jimmy Carter not modeled with ROV bay'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['BPS-15F','BQQ-5D Active','BQQ-5D Bow Passive','BQQ-5D Port Flank Passive','BQQ-5D Stbd Flank Passive','ESM-1','Periscope-1','TB-29 TA']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=35.000000
    dbObj.mfAccel_ktsps=1.500000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='SSN 21 Seawolf durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','660mm Seawolf Tube','CSA Mk1','CSA Mk1']
    dbObj.maMagazineClass=['Seawolf magazine']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','Tube 1','Tube 2','Tube 3','Tube 4','CM','CM']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.900000
    airDetectionDBObject.irSignature_dB=10.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=8.203000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AN195'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=10.700000
    dbObj.surfaceSpeed_kts=20.000000
    dbObj.mfMaxDepth_m=375.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=0.000000
    dbObj.batteryCharge_kW=0.000000
    dbObj.CalculateParams()
    return dbObj
