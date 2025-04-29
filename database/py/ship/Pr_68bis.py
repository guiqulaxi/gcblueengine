# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 68bis'
    dbObj.natoClass='Sverdlov CL'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=13818238.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1952.369995
    dbObj.finalYear=2999.000000
    dbObj.country='Russia'
    dbObj.designation='CL'
    dbObj.imageList='sverdlov.jpg'
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='These ships were improved and slightly enlarged versions of the Chapayev class cruisers. They had the same main armament, machinery and side protection as the earlier ships, but had increased fuel capacity for greater range, an all welded hull, improved underwater protection, increased anti aircraft artillery and radar.The Admiral Nakhimov had an SS-N-1 anti-ship missile launcher installed in place of A and B turrets as a trial in 1957. This installation was not successful, the ship was rapidly decommissioned and was used as a target ship in 1961.The Dzerzhinsky had a SAM launcher for the SA-2 missile, replacing the aft turrets in 1960-62. This conversion was also not successful and no further ships were converted.The Senyavin and Zhdanov were converted into command ships in 1971 by replacing the aft turrets with extra accommodation and electronics. The two command ships were fitted with a helicopter deck and hangar together with a SA-N-4 SAM missile system and 4 twin 30mm guns.'
    dbObj.length_m=210.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Gyuys-2','Rif-A','Tamir-5N Active']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.700001
    dbObj.mfAccel_ktsps=0.030895
    dbObj.mfTurnRate_degps=1.203063
    dbObj.mfFuelCapacity_kg=1934553.375000
    dbObj.mfFuelRate_kgps=1.074743
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Pr 68bis durability'
    dbObj.mnNumLaunchers=20
    dbObj.maLauncherClass=['152mm/57 (6in) B-38 Pattern 1938 Mk5 Turret','152mm/57 (6in) B-38 Pattern 1938 Mk5 Turret','152mm/57 (6in) B-38 Pattern 1938 Mk5 Turret','152mm/57 (6in) B-38 Pattern 1938 Mk5 Turret','100mm/70 (3.9in) CM-5 Turret','100mm/70 (3.9in) CM-5 Turret','100mm/70 (3.9in) CM-5 Turret','100mm/70 (3.9in) CM-5 Turret','100mm/70 (3.9in) CM-5 Turret','100mm/70 (3.9in) CM-5 Turret','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','37mm/67 (1.5in) V-11 x2','533mm torpedo x5 tubes','533mm torpedo x5 tubes']
    dbObj.maMagazineClass=['Sverdlov Tertiary Magazine','Sverdlov Secondary Magazine','Sverdlov Primary Magazine']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,270.000000,270.000000,300.000000,170.000000,170.000000,170.000000,170.000000,150.000000,150.000000,270.000000,270.000000,190.000000,190.000000,290.000000,310.000000,325.000000,340.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,180.000000,85.000000,275.000000,95.000000,265.000000,90.000000,270.000000,0.000000,180.000000,90.000000,270.000000,180.000000,180.000000,180.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[50.000000,50.000000,50.000000,50.000000,85.000000,85.000000,85.000000,85.000000,85.000000,85.000000,80.000000,80.000000,80.000000,80.000000,80.000000,80.000000,80.000000,80.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=51.652000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=28.683001
    airDetectionDBObject.irSignature_dB=27.025999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=13.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.380000
    dbObj.beam_m=21.990000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=110000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
