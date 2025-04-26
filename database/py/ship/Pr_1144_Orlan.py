# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1144 Orlan'
    dbObj.natoClass='Kirov'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=24300000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.989990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='CG'
    dbObj.imageList='kirov.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-325 Vega TA','MG-342 Orion Active','Top Pair AS','Top Plate AS/SS','Wine Flask']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.064558
    dbObj.mfTurnRate_degps=0.928975
    dbObj.mfFuelCapacity_kg=3402000.000000
    dbObj.mfFuelRate_kgps=0.674994
    dbObj.mfToughness=1866.000000
    dbObj.damageEffect='Pr 1144 Orlan durability'
    dbObj.mnNumLaunchers=20
    dbObj.maLauncherClass=['SA-N-6 x8 VLS Launcher x12','SA-N-4 x2 Launcher','SA-N-4 x2 Launcher','SA-N-9 x8 VLS Launcher x2','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','SS-N-19 x20 Launcher','130 mm/70 (5.1in) AK-130 Twin Barrel','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','533mm torpedo x5 tubes','533mm torpedo x5 tubes']
    dbObj.maMagazineClass=['KA-25 3.3 Support','Kashtan x6 Store','Pr1144 Ammo Mag','AK-630 x6 Store']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,200.000000,200.000000,0.000000,270.000000,270.000000,270.000000,270.000000,170.000000,170.000000,0.000000,240.000000,270.000000,270.000000,270.000000,270.000000,170.000000,170.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,45.000000,315.000000,0.000000,225.000000,135.000000,225.000000,135.000000,110.000000,250.000000,0.000000,180.000000,225.000000,135.000000,225.000000,135.000000,110.000000,250.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,40.000000,40.000000,90.000000,40.000000,40.000000,40.000000,40.000000,40.000000,40.000000,45.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','Top Plate AS/SS','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,False,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=55.330002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=30.355000
    airDetectionDBObject.irSignature_dB=22.170000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=13.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S09.Battle Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.800000
    dbObj.beam_m=28.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=140000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Triple Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
