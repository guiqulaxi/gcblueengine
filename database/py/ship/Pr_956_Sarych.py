# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 956 Sarych'
    dbObj.natoClass='Sovremenny'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=6200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.980957
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='DDG'
    dbObj.imageList='sovremenny-1.jpg;sovremenny-4.jpg;sovremenny-5.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=156.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Bell Shroud','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','MR-700A Fregat AS/SS','Palm Frond SS','Vinyetka EM TA Active','Vinyetka EM TA Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.051931
    dbObj.mfTurnRate_degps=1.674494
    dbObj.mfFuelCapacity_kg=868000.000000
    dbObj.mfFuelRate_kgps=1.107133
    dbObj.mfToughness=608.000000
    dbObj.damageEffect='Pr 956 Sarych durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['SA-N-7 Uragan Launcher','SA-N-7 Uragan Launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','SS-N-22 x4 Launcher x2','130 mm/70 (5.1in) AK-130 Twin Barrel','130 mm/70 (5.1in) AK-130 Twin Barrel','533mm torpedo x2 tubes','533mm torpedo x2 tubes']
    dbObj.maMagazineClass=['KA-25 1.2 Support','AK-630 x4 Store','Pr956 Ammo Mag']
    dbObj.mnNumMagazines=3
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','','','','','','','','','','']
    dbObj.launcherFOV_deg=[300.000000,270.000000,190.000000,190.000000,190.000000,190.000000,0.000000,300.000000,300.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,80.000000,280.000000,100.000000,260.000000,0.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,20.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','','MR-700A Fregat AS/SS','MR-700A Fregat AS/SS','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.431999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.496000
    airDetectionDBObject.irSignature_dB=23.802999
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
    dbObj.draft_m=6.500000
    dbObj.beam_m=17.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=99500.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Sovremenny Hangar'
    dbObj.CalculateParams()
    return dbObj
