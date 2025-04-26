# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Canberra LHD'
    dbObj.natoClass='Canberra LHD'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=27100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2014.040039
    dbObj.finalYear=2999.989990
    dbObj.country='Australia'
    dbObj.designation='LHD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes='[greengills]'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Petrel MOAS 5425','SPS-49(V)8','Sea Giraffe 150']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=20.500000
    dbObj.mfAccel_ktsps=0.032115
    dbObj.mfTurnRate_degps=0.743229
    dbObj.mfFuelCapacity_kg=2981000.000000
    dbObj.mfFuelRate_kgps=0.992690
    dbObj.mfToughness=550.000000
    dbObj.damageEffect='Canberra LHD durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['20mm/76 M-61A1 Gatling Mark 15 Block 1','20mm/76 M-61A1 Gatling Mark 15 Block 1','Mk-160 EDL x 4','Mk-137 SRBOC Launcher','Mk-137 SRBOC Launcher']
    dbObj.maMagazineClass=[]
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,8,9,10]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[180.000000,180.000000,360.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,60.000000,60.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=56.040001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=30.329000
    airDetectionDBObject.irSignature_dB=24.212999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=7.080000
    dbObj.beam_m=32.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=35678.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Canberra Flightdeck'
    dbObj.CalculateParams()
    return dbObj
