# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 183'
    dbObj.natoClass='Pr 183'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=67100.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1953.000000
    dbObj.finalYear=1978.000000
    dbObj.country='Russia'
    dbObj.designation='PTB'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=25.500000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Zarnitsa']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=43.000000
    dbObj.mfAccel_ktsps=0.354489
    dbObj.mfTurnRate_degps=13.801046
    dbObj.mfFuelCapacity_kg=9394.000000
    dbObj.mfFuelRate_kgps=0.089440
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Pr 183 durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['25mm 2M-3 Twin','25mm 2M-3 Twin','533mm TTKA-53 Torpedo Tube','533mm TTKA-53 Torpedo Tube','BB1 DCx8']
    dbObj.maMagazineClass=['2M3 x2 Magazine']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['0','0','0','0','0']
    dbObj.launcherFOV_deg=[270.000000,300.000000,0.000000,0.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,0.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,45.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=16.945999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=13.611000
    airDetectionDBObject.irSignature_dB=16.167000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.120000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S01.Patrol Craft'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.240000
    dbObj.beam_m=6.180000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=6000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
