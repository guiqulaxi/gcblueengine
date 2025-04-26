# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Kobben'
    dbObj.natoClass='Kobben'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=0.000000
    dbObj.weight_kg=477000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1964.266357
    dbObj.finalYear=2003.997925
    dbObj.country='Norway'
    dbObj.designation='SSK'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='kilo.xml'
    dbObj.notes='Data from Combat Fleets of the World 1990/1991. This is the original version before modernization. Names aren\'t complete, but I added 3 of the boats that were later modernized'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Calypso-III','MSI-70U Active','MSI-70U Bow Passive','Periscope-1']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=17.000000
    dbObj.mfAccel_ktsps=1.000000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=600000.000000
    dbObj.mfFuelRate_kgps=0.500000
    dbObj.mfToughness=120.000000
    dbObj.damageEffect='Kobben durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube','533mm Kobben Tube']
    dbObj.maMagazineClass=['Sub 12']
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
    airDetectionDBObject.RCS_dBsm=3.700000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=-2.300000
    airDetectionDBObject.irSignature_dB=1.700000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=3.378000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='GK165'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.800000
    dbObj.surfaceSpeed_kts=13.500000
    dbObj.mfMaxDepth_m=150.000000
    dbObj.isDieselElectric=True
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=4.000000
    dbObj.CalculateParams()
    return dbObj
