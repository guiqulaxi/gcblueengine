# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 61 Kashin'
    dbObj.natoClass='Kashin'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=4750000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1963.000000
    dbObj.finalYear=2999.899902
    dbObj.country='Russia'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Gerkules Active','MG-325 Vega TA','MR-310U Angara M(Head Net C)','MR-500 Kliver','Watch Dog']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=35.500000
    dbObj.mfAccel_ktsps=0.044211
    dbObj.mfTurnRate_degps=1.966434
    dbObj.mfFuelCapacity_kg=665000.000000
    dbObj.mfFuelRate_kgps=0.949992
    dbObj.mfToughness=356.000000
    dbObj.damageEffect='Pr 61 Kashin durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm torpedo x5 tubes','533mm torpedo x5 tubes','76 mm/59 (3in) AK-726','SA-N-1 x2 Launcher','SA-N-1 x2 Launcher','SS-N-25 x4 Launcher x2']
    dbObj.maMagazineClass=['Pr61 Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[40.000000,40.000000,240.000000,300.000000,300.000000,0.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,40.000000,40.000000,20.000000]
    dbObj.launcherFireControl=['','','MR-310U Angara M(Head Net C)','MR-310U Angara M(Head Net C)','MR-310U Angara M(Head Net C)','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=44.695999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.424999
    airDetectionDBObject.irSignature_dB=26.735001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=8.200000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.470000
    dbObj.beam_m=15.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=72000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
