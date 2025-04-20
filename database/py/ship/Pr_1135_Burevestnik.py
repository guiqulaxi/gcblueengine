import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1135 Burevestnik'
    dbObj.natoClass='Krivak I'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2835000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1970.239990
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='FF'
    dbObj.imageList='krivak1.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes=''
    dbObj.length_m=123.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Bell Shroud','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Head Net AS/SS','MG-325 Vega TA','MG-335 Platina Active','MG-335 Platina Passive','Palm Frond SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=0.215810
    dbObj.mfTurnRate_degps=2.306577
    dbObj.mfFuelCapacity_kg=396900.000000
    dbObj.mfFuelRate_kgps=0.385872
    dbObj.mfToughness=276.000000
    dbObj.damageEffect='Pr 1135 Burevestnik durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['533mm torpedo x4 tubes','533mm torpedo x4 tubes','76 mm/59 (3in) AK-176','76 mm/59 (3in) AK-176','SA-N-4 x2 Launcher','SA-N-4 x2 Launcher','SS-N-14 x4 Launcher']
    dbObj.maMagazineClass=['Pr1135 Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[40.000000,40.000000,240.000000,270.000000,300.000000,300.000000,0.000000]
    dbObj.launcherAz_deg=[90.000000,270.000000,180.000000,180.000000,0.000000,180.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,40.000000,40.000000,20.000000]
    dbObj.launcherFireControl=['','','','','Head Net AS/SS','Head Net AS/SS','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.334000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.406000
    airDetectionDBObject.irSignature_dB=23.587999
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
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
