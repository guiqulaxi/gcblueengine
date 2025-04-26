# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 12660 Rubin'
    dbObj.natoClass='Gorya MHOM'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1130000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.989990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='MH'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Cross Loop','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Generic Mine Hunting Sonar','Palm Frond SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=15.700000
    dbObj.mfAccel_ktsps=0.058782
    dbObj.mfTurnRate_degps=2.547827
    dbObj.mfFuelCapacity_kg=158200.000000
    dbObj.mfFuelRate_kgps=0.195307
    dbObj.mfToughness=87.000000
    dbObj.damageEffect='Pr 12660 Rubin durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher x2']
    dbObj.maMagazineClass=['AK-630 x2 Store','Strela2 x16 Mag']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[270.000000,240.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=35.341999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=20.618000
    airDetectionDBObject.irSignature_dB=17.761999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=11.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S001.Merchant Small'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.120000
    dbObj.beam_m=10.950000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=5000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
