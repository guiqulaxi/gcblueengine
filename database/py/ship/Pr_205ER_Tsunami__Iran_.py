# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 205ER Tsunami (Iran)'
    dbObj.natoClass='Osa II (Iran)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=20000000.000000
    dbObj.weight_kg=171500.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Iran'
    dbObj.designation='PTG'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=38.599998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MR-104 Rys','MR-331 Rangout']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=42.000000
    dbObj.mfAccel_ktsps=0.393216
    dbObj.mfTurnRate_degps=8.993805
    dbObj.mfFuelCapacity_kg=24010.000000
    dbObj.mfFuelRate_kgps=0.061754
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Pr 205ER Tsunami(Libya) durability'
    dbObj.mnNumLaunchers=3
    dbObj.maLauncherClass=['P-15 Termit x4 Launcher','30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2]
    dbObj.launcherName=['','','']
    dbObj.launcherFOV_deg=[0.000000,320.000000,240.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[20.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','']
    dbObj.launcherFireControl2=['','','']
    dbObj.launcherIsReloadable=[False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=23.059999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=16.533001
    airDetectionDBObject.irSignature_dB=17.232000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.000000
    dbObj.beam_m=7.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=15000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
