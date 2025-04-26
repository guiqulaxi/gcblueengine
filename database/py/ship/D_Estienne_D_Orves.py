# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='D Estienne D Orves'
    dbObj.natoClass='D Estienne D Orves'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1330000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1976.670044
    dbObj.finalYear=2999.000000
    dbObj.country='France'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes='Reality is that the ships are only fitted with Exocets according to operational needs, generally just those deployed to hostile environments will have them.  in GCB any environment they will be used it is likely to be a hostile environment, likewise GCB usually assumes forces are at war(or about to be), thus i have simply assigned all ships with Exocets full time.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ARBR 17','DRBV 51A','DUBA-25A Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=24.000000
    dbObj.mfAccel_ktsps=0.104716
    dbObj.mfTurnRate_degps=2.862659
    dbObj.mfFuelCapacity_kg=186200.000000
    dbObj.mfFuelRate_kgps=0.172406
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='D Estienne D Orves durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Exocet Twin Launcher','Exocet Twin Launcher','Mistral Simbad','100mm/55 (3.9in) model 1968 CADAM','20 mm F2 Cannon','20 mm F2 Cannon','KD59E Torp Launcher','KD59E Torp Launcher']
    dbObj.maMagazineClass=['French Combat Stores','Mistral Simbad Mag x1','100mm/55 Model 1968 600 rounds']
    dbObj.magazineId=[4,3,2]
    dbObj.launcherId=[0,1,3,5,6,7,8,9]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[30.000000,30.000000,330.000000,330.000000,200.000000,200.000000,180.000000,180.000000]
    dbObj.launcherAz_deg=[30.000000,330.000000,180.000000,0.000000,270.000000,90.000000,180.000000,90.000000]
    dbObj.launcherEl_deg=[12.000000,12.000000,40.000000,0.000000,30.000000,30.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=23.393000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.877001
    airDetectionDBObject.irSignature_dB=9.863000
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
    dbObj.draft_m=5.500000
    dbObj.beam_m=10.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=12000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
