import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Iowa BB'
    dbObj.natoClass='Iowa BB'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=100000000.000000
    dbObj.weight_kg=45000000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1943.140015
    dbObj.finalYear=1982.000000
    dbObj.country='USA'
    dbObj.designation='BB'
    dbObj.imageList='iowa1984.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=270.299988
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk13 MBFC SS','Mk3 MBFC SS','OD.2 25x Central Iowa 8.1m','OD.2 25x Local Iowa Main 1 15.6m','OD.2 25x Local Iowa Main 2 15.6m','OD.2 25x Local Iowa Main 3 15.6m','OD.2 25x Local Iowa Secondary 3m']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=0.025803
    dbObj.mfTurnRate_degps=0.741940
    dbObj.mfFuelCapacity_kg=3150000.000000
    dbObj.mfFuelRate_kgps=1.123301
    dbObj.mfToughness=685.000000
    dbObj.damageEffect='Iowa BB durability'
    dbObj.mnNumLaunchers=23
    dbObj.maLauncherClass=['16in Triple Mk-7','16in Triple Mk-7','16in Triple Mk-7','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','5/38 Mark 12 Twin','40mm Bofors Mk12 x8','40mm Bofors Mk12 x8','40mm Bofors Mk12 x8','40mm Bofors Mk12 x8','40mm Bofors Mk12 x8','20mm/70 Oerlikon Mk1/2/3/4 x10','20mm/70 Oerlikon Mk1/2/3/4 x10','20mm/70 Oerlikon Mk1/2/3/4 x10','20mm/70 Oerlikon Mk1/2/3/4 x10','20mm/70 Oerlikon Mk1/2/3/4 x10']
    dbObj.maMagazineClass=['Iowa Tertiary Magazine','Iowa Secondary Magazine','Iowa Main Ammo Mag']
    dbObj.magazineId=[2,1,0]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,136.000000,136.000000,90.000000,90.000000,80.000000,80.000000,70.000000,70.000000,136.000000,136.000000,130.000000,130.000000,220.000000,220.000000,300.000000,130.000000,130.000000,220.000000,220.000000,300.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,180.000000,68.000000,292.000000,45.000000,315.000000,135.000000,225.000000,50.000000,310.000000,158.000000,202.000000,45.000000,315.000000,110.000000,250.000000,180.000000,45.000000,315.000000,110.000000,250.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','Mk13 MBFC SS','','','','','','','','','','']
    dbObj.launcherFireControl2=['Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','Mk8 MBFC SS','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=59.344002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=31.584999
    airDetectionDBObject.irSignature_dB=25.315001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=15.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=23.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S09.Battle Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=11.330000
    dbObj.beam_m=32.970001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=212000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
