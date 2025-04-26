# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Sabalo SSK'
    dbObj.natoClass='Sabalo SSK'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=1285000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.997925
    dbObj.finalYear=2999.997314
    dbObj.country='Venezuela'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='guppy.xml'
    dbObj.notes='Marcos Viniegra'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['40 Stab','Calypso-III','DR-2000U','ISUS-83-13 ACT','ISUS-83-13 PAS','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=1.000000
    dbObj.mfFuelCapacity_kg=108000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=80.000000
    dbObj.damageEffect='Sabalo SSK durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['TS-1','TS-1','TS-1','TS-1','TS-1','TS-1','TS-1','TS-1']
    dbObj.maMagazineClass=['U209 santabarbara']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=6.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=0.900000
    airDetectionDBObject.irSignature_dB=4.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=8.025000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='GK170'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.500000
    dbObj.surfaceSpeed_kts=11.500000
    dbObj.mfMaxDepth_m=190.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=4.000000
    dbObj.CalculateParams()
    return dbObj
