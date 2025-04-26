# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Type 23 FF'
    dbObj.natoClass='Type 23 FF'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1990.410034
    dbObj.finalYear=3000.000000
    dbObj.country='UK'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-5','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Type 1007','Type 2031 TA','Type 2050 Active','Type 2050 Passive','Type 996']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.400002
    dbObj.mfAccel_ktsps=0.202175
    dbObj.mfTurnRate_degps=2.057249
    dbObj.mfFuelCapacity_kg=588000.000000
    dbObj.mfFuelRate_kgps=0.314100
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Type 23 FF durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Sea Wolf 6pack','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','114mm/55(4.5in) Mark 8 Mod 0','30mm/75 GCM-AO3-2','30mm/75 GCM-AO3-2','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 2.2 Support','Type 23 Ammo Mag','Sea Wolf Store 20','114mm/55(4.5in) mk8 800 rounds']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[320.000000,0.000000,0.000000,320.000000,320.000000,340.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,0.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Type 996','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.894001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.761000
    airDetectionDBObject.irSignature_dB=26.701000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.300000
    dbObj.beam_m=16.100000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=47100.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
