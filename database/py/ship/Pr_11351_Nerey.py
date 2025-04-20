import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 11351 Nerey'
    dbObj.natoClass='Krivak III'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2935000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1983.989990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='wFF'
    dbObj.imageList='krivak3.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=123.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Bell Shroud','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-335 Platina Active','MG-335 Platina Passive','Peel Cone AS/SS','Top Plate AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.209908
    dbObj.mfTurnRate_degps=2.280078
    dbObj.mfFuelCapacity_kg=410900.000000
    dbObj.mfFuelRate_kgps=0.439475
    dbObj.mfToughness=279.000000
    dbObj.damageEffect='Pr 11351 Nerey durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['100 mm/70 (3.9in) AK-100','30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230','533mm torpedo x4 tubes','533mm torpedo x4 tubes','SA-N-4 x2 Launcher']
    dbObj.maMagazineClass=['KA-25 1.1 Support','Pr11351 Ammo Mag','AK-230 x2 Store']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['','','','','','']
    dbObj.launcherFOV_deg=[240.000000,170.000000,170.000000,40.000000,40.000000,300.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,90.000000,270.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,40.000000]
    dbObj.launcherFireControl=['','','','','','Top Plate AS/SS']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.560001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.406000
    airDetectionDBObject.irSignature_dB=23.597000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=5.800000
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
    dbObj.beam_m=14.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=48000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
