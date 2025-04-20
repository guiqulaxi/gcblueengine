import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1134B Berkut B'
    dbObj.natoClass='Kara'
    dbObj.mnModelType=2
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=6670000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1972.000000
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='CG'
    dbObj.imageList='kara.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=173.399994
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Flat Screen AS','Head Net AS/SS','MG-325 Vega TA','MG-332 Titan-2 Active','Rum Tub']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=33.000000
    dbObj.mfAccel_ktsps=0.043939
    dbObj.mfTurnRate_degps=1.616242
    dbObj.mfFuelCapacity_kg=933800.000000
    dbObj.mfFuelRate_kgps=0.675867
    dbObj.mfToughness=747.000000
    dbObj.damageEffect='Pr 1134B Berkut B durability'
    dbObj.mnNumLaunchers=13
    dbObj.maLauncherClass=['SA-N-4 x2 Launcher','SA-N-4 x2 Launcher','SA-N-3 x2 launcher','SA-N-3 x2 launcher','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','76 mm/59 (3in) AK-726','76 mm/59 (3in) AK-726','SS-N-14 x4 Launcher x2','533mm torpedo x5 tubes','533mm torpedo x5 tubes']
    dbObj.maMagazineClass=['KA-25 2.2 Support','Pr1134B Ammo Mag','AK-630 x4 Store']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    dbObj.launcherName=['','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[200.000000,200.000000,300.000000,300.000000,170.000000,170.000000,170.000000,170.000000,170.000000,170.000000,0.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,0.000000,180.000000,90.000000,90.000000,270.000000,270.000000,75.000000,285.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,40.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,20.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Head Net AS/SS','Head Net AS/SS','Head Net AS/SS','Head Net AS/SS','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,False,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.908001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=27.014000
    airDetectionDBObject.irSignature_dB=23.823999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=10.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S06.Cruiser'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.740000
    dbObj.beam_m=18.500000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=92000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
