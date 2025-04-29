# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11551 Fregat-M'
    dbObj.natoClass='Udaloy II'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=8900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1999.069946
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='DD'
    dbObj.imageList='udaloy2.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=162.860001
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MGK-355 Polinom Active','MGK-355 Polinom Passive','MGK-355TA Polinom TA','Strut Pair II AS','Top Plate AS/SS','Wine Glass']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.100000
    dbObj.mfAccel_ktsps=0.114848
    dbObj.mfTurnRate_degps=1.424251
    dbObj.mfFuelCapacity_kg=1246000.000000
    dbObj.mfFuelRate_kgps=0.704085
    dbObj.mfToughness=685.000000
    dbObj.damageEffect='Pr 11551 Fregat-M durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['130 mm/70 (5.1in) AK-130 Twin Barrel','533mm torpedo x4 tubes','533mm torpedo x4 tubes','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','SA-N-9 x8 VLS Launcher','SS-N-22 x4 Launcher x2']
    dbObj.maMagazineClass=['KA-25 1.2 Support','Kashtan x2 Store','AK-630 x2 Store','Pr11551 Ammo Mag']
    dbObj.mnNumMagazines=4
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,40.000000,40.000000,220.000000,220.000000,220.000000,220.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,115.000000,245.000000,115.000000,245.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,40.000000,40.000000,90.000000,20.000000]
    dbObj.launcherFireControl=['','','','','','','','Top Plate AS/SS','']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=48.785999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.712000
    airDetectionDBObject.irSignature_dB=26.905001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.100000
    dbObj.beam_m=18.990000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=72000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
