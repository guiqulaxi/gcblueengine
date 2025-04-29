# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Hai Shih SS'
    dbObj.natoClass='Hai Shih SS'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=100000.000000
    dbObj.weight_kg=1975000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.277222
    dbObj.finalYear=2999.997314
    dbObj.country='Taiwan'
    dbObj.designation='SSK'
    dbObj.imageList='haishih.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='guppy.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Generic radar','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=15.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=600000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=60.000000
    dbObj.damageEffect='Hai Shih SS durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm torpedo x3 tubes','533mm torpedo x3 tubes','533mm torpedo x4 tubes','127mm/54 (5in) Mk42','Bofors 40 mm/70 Mark 3','20mm/70 Oerlikon Mk1/2/3/4']
    dbObj.maMagazineClass=['Hai Shih Magazine','127mm Mk-42 500 Rounds','Hai Shih Torpedo Magazine']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,40.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,360.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=8.300000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=2.300000
    airDetectionDBObject.irSignature_dB=6.300000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.486000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AK145'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.500000
    dbObj.surfaceSpeed_kts=18.000000
    dbObj.mfMaxDepth_m=65.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.500000
    dbObj.CalculateParams()
    return dbObj
