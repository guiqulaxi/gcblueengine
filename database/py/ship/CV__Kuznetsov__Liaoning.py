# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='CV (Kuznetsov) Liaoning'
    dbObj.natoClass='CV (Kuznetsov) Liaoning'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=59100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=2999.000000
    dbObj.finalYear=2999.000000
    dbObj.country='China'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes='[greengills]  -Amram-not so hypothetical anymore, she\'s in service, but still she lacks an airwing.'
    dbObj.length_m=305.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Flat Track ESM','MP-407E ECM','MR-212 Nvada','MR-302M Topaz','MR-350 Podkat (Port Pair)','MR-350 Podkat (Stbd Pair)','MR-352 Positiv ME-1.2 (Port Array)','MR-352 Positiv ME-1.2 (Stbd Array)','MR-750 Fregat M2EM','SJD-8/9 Active Modes','SJD-8/9 Passive Modes','Type 346']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,270.000000,90.000000,270.000000,90.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.019794
    dbObj.mfTurnRate_degps=0.646661
    dbObj.mfFuelCapacity_kg=6501000.000000
    dbObj.mfFuelRate_kgps=4.414528
    dbObj.mfToughness=1086.000000
    dbObj.damageEffect='CV (Kuznetsov) Liaoning durability'
    dbObj.mnNumLaunchers=11
    dbObj.maLauncherClass=['SS-N-19 x12 Launcher','SA-N-9 Revolver Launcher x 12','SA-N-9 Revolver Launcher x 12','Kashtan SA-N-11 Mount x 4','Kashtan 30mm Gun Mount x 4','Kashtan SA-N-11 Mount x 4','Kashtan 30mm Gun Mount x 4','30 mm/54 (1.2in) AK-630M x 3','30 mm/54 (1.2in) AK-630M x 3','PK-10 Chaff Launcher x 5 (Port)','PK-10 Chaff Launcher x 5 (Stbd)']
    dbObj.maMagazineClass=['Shi Lang Aviation Fuel Bunker','Shi Lang Airwing Magazine I','Shi Lang Airwing Magazine II','Kashtan SA-N-11 Magazine x 8','Shi Lang Gun/CM Magazine']
    dbObj.mnNumMagazines=5
    dbObj.magazineId=[0,1,2,3,4]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10]
    dbObj.launcherName=['','Port SA-N-9 Launcher','Stbd SA-N-9 Launcher','Port Kashtan SAM Array','Port Kashtan 30mm Array','Stbd Kashtan SAM Array','Stbd Kashtan 30mm Array','Port 30mm CIWS Array','Stbd 30mm CIWS Array','','']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,180.000000,180.000000,180.000000,180.000000,180.000000,180.000000,90.000000,90.000000]
    dbObj.launcherAz_deg=[0.000000,270.000000,90.000000,270.000000,270.000000,90.000000,90.000000,270.000000,90.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[20.000000,90.000000,90.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,60.000000,60.000000]
    dbObj.launcherFireControl=['','MR-350 Podkat (Port Pair)','MR-350 Podkat (Stbd Pair)','MR-352 Positiv ME-1.2 (Port Array)','MR-352 Positiv ME-1.2 (Port Array)','MR-352 Positiv ME-1.2 (Stbd Array)','MR-352 Positiv ME-1.2 (Stbd Array)','','','','Irbis-E']
    dbObj.launcherFireControl2=['','','','','','','','','','','OEPS-30 IRST']
    dbObj.launcherIsReloadable=[False,False,False,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=61.118999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=34.837002
    airDetectionDBObject.irSignature_dB=25.392000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=25.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=11.000000
    dbObj.beam_m=72.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=200000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Kuznetsov Flightdeck'
    dbObj.CalculateParams()
    return dbObj
