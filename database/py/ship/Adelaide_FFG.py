# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Adelaide FFG'
    dbObj.natoClass='Adelaide FFG'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4200000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1980.869995
    dbObj.finalYear=3000.000000
    dbObj.country='Australia'
    dbObj.designation='FF'
    dbObj.imageList='adelaide.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='ffg-7.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['C-Pearl ESM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Kariwarra Towed Array Sonar','Mk-92 Mod 12 STIR-HP','Petrel MOAS 5425','Radamec 2500 Optronic Sensor','SPG-60','SPS-49A(V)1','SPS-55','Spherion B Mod 5']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.192041
    dbObj.mfTurnRate_degps=1.871204
    dbObj.mfFuelCapacity_kg=574000.000000
    dbObj.mfFuelRate_kgps=0.708636
    dbObj.mfToughness=312.000000
    dbObj.damageEffect='Adelaide FFG durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['76 mm/62 Mark 75 Compact','Mk-13 Mod4 GMLS','Adelaide Mk-41 Mod 5 VLS','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-160 EDL x 4','Mk-137 SRBOC Launcher','Mk-137 SRBOC Launcher']
    dbObj.maMagazineClass=['Adelaide Helo Fuel Bunker','Adelaide Torpedo Magazine','Adelaide Gun/CM Magazine','Ship Helo Stores']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','Phalanx CIWS','Port Torpedo Tubes','Stbd Torpedo Tubes','','','']
    dbObj.launcherFOV_deg=[180.000000,360.000000,360.000000,270.000000,45.000000,45.000000,360.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,270.000000,90.000000,0.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,80.000000,60.000000,60.000000]
    dbObj.launcherFireControl=['SPG-60','Mk-92 Mod 12 STIR-HP','SPG-60','','','','','','']
    dbObj.launcherFireControl2=['Radamec 2500 Optronic Sensor','SPG-60','Mk-92 Mod 12 STIR-HP','','','','','','']
    dbObj.launcherIsReloadable=[False,True,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=43.737000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.485001
    airDetectionDBObject.irSignature_dB=23.688999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S03.Frigate Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.500000
    dbObj.beam_m=13.700000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=41650.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='OHP Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
