# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Damsah FACM'
    dbObj.natoClass='Damsah FACM'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=430000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1982.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Qatar'
    dbObj.designation='PGG'
    dbObj.imageList='boat.jpg'
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='pg-84.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','TRS 3033 Triton S','Decca 1226','TRS 3203 Castor IIB','Cutlass 2-7.5','Cutlass 7.5-18']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=39.000000
    dbObj.mfAccel_ktsps=0.241969
    dbObj.mfTurnRate_degps=5.812766
    dbObj.mfFuelCapacity_kg=43540.000000
    dbObj.mfFuelRate_kgps=0.100786
    dbObj.mfToughness=25.000000
    dbObj.damageEffect='Damsah FACM durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Exocet Quad Launcher','Exocet Quad Launcher','76 mm/62 Mark 75 Compact','40mm L70 Sea Trinity','30mm/75 GCM-AO3-2','30mm/75 GCM-AO3-2','Dagaie Chaff Launcher','Dagaie Flares Launcher']
    dbObj.maMagazineClass=['30mm GCM-A03-2 x2 Store','40mm L70 Trinity magazine','76mm/62 mk75 240 rounds','Dagaie CM Mag 231']
    dbObj.magazineId=[2,1,0,3]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,240.000000,340.000000,185.000000,185.000000,300.000000,300.000000]
    dbObj.launcherAz_deg=[30.000000,330.000000,0.000000,180.000000,90.000000,270.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[20.000000,20.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=26.937000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=18.414000
    airDetectionDBObject.irSignature_dB=17.395000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=2.150000
    dbObj.beam_m=8.160000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=19300.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
