# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Hai Lung SS'
    dbObj.natoClass='Hai Lung SS'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=250000000.000000
    dbObj.weight_kg=2376000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1987.770020
    dbObj.finalYear=2999.997314
    dbObj.country='Taiwan'
    dbObj.designation='SSK'
    dbObj.imageList='hailung-25602.jpg;hailung.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='zwaardvis.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Periscope-1','SIASS-Z Active','SIASS-Z Passive','ZW-07 SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=600000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Hai Lung SS durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['Hai Lung Torpedo Tube','Hai Lung Torpedo Tube','Hai Lung Torpedo Tube','Hai Lung Torpedo Tube','Hai Lung Torpedo Tube','Hai Lung Torpedo Tube']
    dbObj.maMagazineClass=['Hai Lung magazine']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','Tube 5','Tube 6']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=8.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=2.900000
    airDetectionDBObject.irSignature_dB=6.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.486000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='GK185'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.700000
    dbObj.surfaceSpeed_kts=12.000000
    dbObj.mfMaxDepth_m=250.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.500000
    dbObj.CalculateParams()
    return dbObj
