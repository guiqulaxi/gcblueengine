# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1159TR Koni'
    dbObj.natoClass='Koni'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1900000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Special'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=96.510002
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Gerkules Active','MR-302M Topaz','MR-500 Kliver','Ros'-K VDS','Watch Dog']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.173682
    dbObj.mfTurnRate_degps=2.619621
    dbObj.mfFuelCapacity_kg=266000.000000
    dbObj.mfFuelRate_kgps=0.229875
    dbObj.mfToughness=74.000000
    dbObj.damageEffect='Pr 1159TR Koni durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['SS-N-2D x2 Launcher x2','SA-N-4 x2(16) Launcher','76 mm/59 (3in) AK-726','76 mm/59 (3in) AK-726','30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230','406mm torpedo tube x2','406mm torpedo tube x2']
    dbObj.maMagazineClass=['AK-230 x2 Store','AK-726 x2 Store']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[20.000000,340.000000,300.000000,300.000000,170.000000,170.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,270.000000,90.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[20.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.727001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.628000
    airDetectionDBObject.irSignature_dB=23.478001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.280000
    dbObj.beam_m=12.560000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=34000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
