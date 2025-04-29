# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='ANZAC FFH'
    dbObj.natoClass='ANZAC FFH'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=3600000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1996.290039
    dbObj.finalYear=3000.000000
    dbObj.country='Australia'
    dbObj.designation='FF'
    dbObj.imageList='anzac.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=109.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['9LV 453 TIR','Centaur ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Kariwarra Towed Array Sonar','Petrel MOAS 5425','SPS-49(V)8','Sea Giraffe 150','Spherion B Mod 5','VAMPIR IIRST']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=27.000000
    dbObj.mfAccel_ktsps=0.156646
    dbObj.mfTurnRate_degps=2.016561
    dbObj.mfFuelCapacity_kg=504000.000000
    dbObj.mfFuelRate_kgps=0.419996
    dbObj.mfToughness=276.000000
    dbObj.damageEffect='ANZAC FFH durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['5/54 Mark 45 Mods 0 - 2','ANZAC Mk-141 Launcher','ANZAC Mk-141 Launcher','ANZAC Mk-41 Mod 5 VLS','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-160 EDL x 4','Mk-137 SRBOC Launcher','Mk-137 SRBOC Launcher']
    dbObj.maMagazineClass=['ANZAC Helo Fuel Bunker','ANZAC Torpedo Magazine','ANZAC Gun/CM Magazine','Ship Helo Stores']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','Port Torpedo Tubes','Stbd Torpedo Tubes','','','']
    dbObj.launcherFOV_deg=[300.000000,0.000000,0.000000,360.000000,45.000000,45.000000,360.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,315.000000,45.000000,0.000000,270.000000,90.000000,0.000000,45.000000,135.000000]
    dbObj.launcherEl_deg=[0.000000,4.000000,4.000000,0.000000,0.000000,0.000000,0.000000,30.000000,30.000000]
    dbObj.launcherFireControl=['9LV 453 TIR','','','9LV 453 TIR','','','','','']
    dbObj.launcherFireControl2=['VAMPIR IIRST','','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,False,True,False,False,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.889999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.997000
    airDetectionDBObject.irSignature_dB=26.659000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.350000
    dbObj.beam_m=14.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=39012.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
