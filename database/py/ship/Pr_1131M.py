import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1131M'
    dbObj.natoClass='Parchim II'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=960000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1986.319946
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FF'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=75.199997
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Cross Dome AS/SS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','Oka-2 DS','Watch Dog']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=26.000000
    dbObj.mfAccel_ktsps=0.148955
    dbObj.mfTurnRate_degps=3.373356
    dbObj.mfFuelCapacity_kg=134400.000000
    dbObj.mfFuelRate_kgps=0.179198
    dbObj.mfToughness=74.000000
    dbObj.damageEffect='Pr 1131M durability'
    dbObj.mnNumLaunchers=5
    dbObj.maLauncherClass=['30 mm/54 (1.2in) AK-630M','533mm torpedo x2 tubes','533mm torpedo x2 tubes','76 mm/59 (3in) AK-176','SA-N-5 x4 launcher x2']
    dbObj.maMagazineClass=['AK-630 x1 Store','Pr1131M Ammo Mag']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4]
    dbObj.launcherName=['','','','','']
    dbObj.launcherFOV_deg=[300.000000,0.000000,0.000000,300.000000,300.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,180.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','','','']
    dbObj.launcherFireControl2=['','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=34.279999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=21.160000
    airDetectionDBObject.irSignature_dB=17.718000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=3.500000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=4.500000
    dbObj.beam_m=9.800000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=14250.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
