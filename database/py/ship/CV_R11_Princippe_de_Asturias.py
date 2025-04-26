# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV R11 Princippe de Asturias'
    dbObj.natoClass='CV R11 Princippe de Asturias'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=16700000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1988.411011
    dbObj.finalYear=2999.000000
    dbObj.country='Spain'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ELT 211 ESM','ELT 318 ECM','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SPS-52C AS','SPS-55']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.067675
    dbObj.mfTurnRate_degps=1.004869
    dbObj.mfFuelCapacity_kg=1837000.000000
    dbObj.mfFuelRate_kgps=0.872262
    dbObj.mfToughness=1000.000000
    dbObj.damageEffect='CV R11 Princippe de Asturias durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['20mm Meroka CIWS','20mm Meroka CIWS','20mm Meroka CIWS','20mm Meroka CIWS']
    dbObj.maMagazineClass=['Princippe de Asturias Magazine','Princippe de Asturias Fuel Supply']
    dbObj.magazineId=[1,0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[300.000000,300.000000,170.000000,170.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,85.000000,275.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['RTN-20X x3','RTN-20X x3','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=52.886002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=29.014000
    airDetectionDBObject.irSignature_dB=24.076000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=12.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.400000
    dbObj.beam_m=24.299999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=46400.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Princippe de Asturias Flightdeck'
    dbObj.CalculateParams()
    return dbObj
