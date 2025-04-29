# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Descubierta FFG (Morocco)'
    dbObj.natoClass='Descubierta FFG (Morocco)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=2470000128.000000
    dbObj.weight_kg=1482000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.239990
    dbObj.finalYear=2999.000000
    dbObj.country='Morocco'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=88.800003
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DA-05','DE-1160B Active','DE-1160B Passive','ELT 211 ESM','ELT 318 ECM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','WM-25','ZW-06']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.091899
    dbObj.mfTurnRate_degps=2.745603
    dbObj.mfFuelCapacity_kg=207480.000000
    dbObj.mfFuelRate_kgps=0.128836
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Descubierta FFG durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','76 mm/62 Mark 75 Compact','MM-38 Exocet Quad Launcher','MM-38 Exocet Quad Launcher','40mm L70 Sea Trinity','40mm L70 Sea Trinity','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['40mm/70 x2 Magazine','76mm/62 mk75 240 rounds','Sea Sparrow Reloads','Mk-32 Torpedo Racks']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,320.000000,0.000000,0.000000,330.000000,330.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,90.000000,270.000000,180.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,1.000000,20.000000,20.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['WM-25','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=37.108002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.811001
    airDetectionDBObject.irSignature_dB=17.843000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.800000
    dbObj.beam_m=10.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=16000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
