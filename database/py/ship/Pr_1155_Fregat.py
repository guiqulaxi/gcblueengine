# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1155 Fregat'
    dbObj.natoClass='Udaloy'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=8500000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1981.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='DD'
    dbObj.imageList='udaloy.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=163.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MGK-355 Polinom Active','MGK-355 Polinom Passive','MGK-355TA Polinom TA','Strut Pair II AS','Top Plate AS/SS','Wine Glass']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.500000
    dbObj.mfAccel_ktsps=0.111125
    dbObj.mfTurnRate_degps=1.431456
    dbObj.mfFuelCapacity_kg=1190000.000000
    dbObj.mfFuelRate_kgps=0.672441
    dbObj.mfToughness=685.000000
    dbObj.damageEffect='Pr 1155 Fregat durability'
    dbObj.mnNumLaunchers=10
    dbObj.maLauncherClass=['SA-N-9 x8 VLS Launcher','100 mm/70 (3.9in) AK-100','100 mm/70 (3.9in) AK-100','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','SS-N-14 x4 Launcher x2','533mm torpedo x4 tubes','533mm torpedo x4 tubes']
    dbObj.maMagazineClass=['KA-25 1.2 Support','AK-630 x4 Store','Pr1155 Ammo Mag']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,270.000000,300.000000,170.000000,170.000000,170.000000,170.000000,0.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,80.000000,100.000000,260.000000,280.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Top Plate AS/SS','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True,True,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=48.487000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.737000
    airDetectionDBObject.irSignature_dB=26.893000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.200000
    dbObj.beam_m=19.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=62000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
