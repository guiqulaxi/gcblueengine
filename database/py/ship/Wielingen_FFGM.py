import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Wielingen FFGM'
    dbObj.natoClass='Wielingen FFGM'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2319635.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1978.060059
    dbObj.finalYear=2007.760010
    dbObj.country='Belgium'
    dbObj.designation='FF'
    dbObj.imageList='wielingen.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes='[kbluck]'
    dbObj.length_m=106.379997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DA-05','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','SQS-505 Active','SQS-505 Passive','WM-27']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=28.000000
    dbObj.mfAccel_ktsps=0.190190
    dbObj.mfTurnRate_degps=2.392092
    dbObj.mfFuelCapacity_kg=324748.906250
    dbObj.mfFuelRate_kgps=0.240553
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Wielingen FFGM durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['MM-38 Exocet Quad Launcher','SeaSparrow x8 Launcher','100mm/55 (3.9in) model 1968','KD59E Torp Launcher','KD59E Torp Launcher']
    dbObj.maMagazineClass=['100mm/55 Model 1968 600 rounds','L5 Torpedo Racks']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[180.000000,240.000000,240.000000,90.000000,90.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[20.000000,0.000000,80.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','WM-27','WM-27','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=40.027000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.621000
    airDetectionDBObject.irSignature_dB=23.532000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.600000
    dbObj.beam_m=12.300000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=31775.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=1.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
