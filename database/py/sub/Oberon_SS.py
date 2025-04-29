# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Oberon SS'
    dbObj.natoClass='Oberon SS'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=1610000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.000000
    dbObj.finalYear=2999.997314
    dbObj.country='UK'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes='Royal Navy configuration'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Periscope-1','Type 1002','Type 187 Active','Type 2007 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=17.000000
    dbObj.mfAccel_ktsps=0.900000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=500000.000000
    dbObj.mfFuelRate_kgps=0.190000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Oberon SS durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['533mm Oberon Tube','533mm Oberon Tube','533mm Oberon Tube','533mm Oberon Tube','533mm Oberon Tube','533mm Oberon Tube','CSA Mk1','CSA Mk1']
    dbObj.maMagazineClass=['Oberon Torpedo Racking']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','Tube 5','Tube 6','CM','CM']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,180.000000,180.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=7.700000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=1.700000
    airDetectionDBObject.irSignature_dB=5.700000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.342000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='BK160'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.500000
    dbObj.surfaceSpeed_kts=12.000000
    dbObj.mfMaxDepth_m=275.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.500000
    dbObj.CalculateParams()
    return dbObj
