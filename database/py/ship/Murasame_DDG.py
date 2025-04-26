# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Murasame DDG'
    dbObj.natoClass='Murasame DDG'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=5100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1996.194946
    dbObj.finalYear=2999.000000
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','FCS-2-21 1','NOLQ-3','OLT-3','OLT-5','OPS-20','OPS-24','OPS-28','OQR-2 TA','OQS-5 Active','OQS-5 Passive','Phalanx FC']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.164308
    dbObj.mfTurnRate_degps=1.829685
    dbObj.mfFuelCapacity_kg=714000.000000
    dbObj.mfFuelRate_kgps=0.991658
    dbObj.mfToughness=35.000000
    dbObj.damageEffect='Murasame DDG durability'
    dbObj.mnNumLaunchers=9
    dbObj.maLauncherClass=['SSM-1B Quad','SSM-1B Quad','Mk-41 Mod9 VLS','76 mm/62 Mark 75','20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount','Mk-41 Mod9 VLS']
    dbObj.maMagazineClass=['SH-60 1.2 Support','76mm/62 mk75 240 rounds','Phalanx 0 x2 Store','Mk-41 VLS Mod9 32 Cell']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8]
    dbObj.launcherName=['','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,360.000000,340.000000,240.000000,340.000000,30.000000,30.000000,360.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,0.000000,0.000000,180.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,90.000000,0.000000,0.000000,0.000000,0.000000,0.000000,90.000000]
    dbObj.launcherFireControl=['','','FCS-2-21 1','','','','','','FCS-2-21 1']
    dbObj.launcherFireControl2=['','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=45.159000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=26.114000
    airDetectionDBObject.irSignature_dB=21.656000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S05.Destroyer Silenced'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.200000
    dbObj.beam_m=17.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
