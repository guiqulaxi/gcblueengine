# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1164 Atlant'
    dbObj.natoClass='Slava'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=11490000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.989990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='CG'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MGK-365 Zvezda-2 Active','MGK-365 Zvezda-2 Passive','MR-710 Fregat-M2','MR-800 Flag','Rum Tub','SSN-137 VDS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.500000
    dbObj.mfAccel_ktsps=0.037659
    dbObj.mfTurnRate_degps=1.314752
    dbObj.mfFuelCapacity_kg=1608600.000000
    dbObj.mfFuelRate_kgps=0.830538
    dbObj.mfToughness=872.000000
    dbObj.damageEffect='Pr 1164 Atlant durability'
    dbObj.mnNumLaunchers=13
    dbObj.maLauncherClass=['SA-N-6 x8 VLS Launcher x8','SA-N-4 x2 Launcher','SA-N-4 x2 Launcher','130 mm/70 (5.1in) AK-130 Twin Barrel','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','533mm torpedo x5 tubes','533mm torpedo x5 tubes','SS-N-19 x2 Launcher x8']
    dbObj.maMagazineClass=['KA-25 1.3 Support','AK-630 x6 Store','Pr1164 Ammo Mag']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    dbObj.launcherName=['','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,270.000000,270.000000,240.000000,270.000000,270.000000,170.000000,170.000000,200.000000,200.000000,40.000000,40.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,225.000000,135.000000,0.000000,0.000000,0.000000,90.000000,270.000000,120.000000,240.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[90.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000]
    dbObj.launcherFireControl=['MR-710 Fregat-M2','MR-710 Fregat-M2','MR-710 Fregat-M2','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=50.450001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.802000
    airDetectionDBObject.irSignature_dB=23.973000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=6.280000
    dbObj.beam_m=20.799999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=142000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
