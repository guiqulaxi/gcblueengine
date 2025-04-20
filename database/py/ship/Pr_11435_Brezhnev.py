import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11435 Brezhnev'
    dbObj.natoClass='Kuznetsov'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=59100000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1990.979980
    dbObj.finalYear=2999.899902
    dbObj.country='Russia'
    dbObj.designation='CVN'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes=''
    dbObj.length_m=306.450012
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','Palm Frond SS','Sky Watch AS/SS','Wine Flask']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=29.000000
    dbObj.mfAccel_ktsps=0.018565
    dbObj.mfTurnRate_degps=0.635039
    dbObj.mfFuelCapacity_kg=6501000.000000
    dbObj.mfFuelRate_kgps=1.504848
    dbObj.mfToughness=1086.000000
    dbObj.damageEffect='Pr 11435 Brezhnev durability'
    dbObj.mnNumLaunchers=24
    dbObj.maLauncherClass=['SA-N-9 x6 Launcher x4','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','Kashtan-M SA-N-11 x8 Missile Launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','SS-N-19 x12 Launcher']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Carrier Magazine']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,300.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,270.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,45.000000,45.000000,315.000000,315.000000,135.000000,135.000000,225.000000,225.000000,90.000000,90.000000,270.000000,270.000000,135.000000,225.000000,45.000000,45.000000,315.000000,315.000000,135.000000,135.000000,225.000000,225.000000,0.000000]
    dbObj.launcherEl_deg=[90.000000,40.000000,40.000000,40.000000,40.000000,40.000000,40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000]
    dbObj.launcherFireControl=['Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','Sky Watch AS/SS','','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=61.118999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=34.776001
    airDetectionDBObject.irSignature_dB=22.430000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=25.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S12.Carrier Large'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.760000
    dbObj.beam_m=71.949997
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=200000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Kuznetsov Flightdeck'
    dbObj.CalculateParams()
    return dbObj
