import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Karel Doorman DDG'
    dbObj.natoClass='Karel Doorman DDG'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=3320000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1991.411987
    dbObj.finalYear=1994.000000
    dbObj.country='Netherlands'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='NONE'
    dbObj.mz3DModelFileName='type-42.xml'
    dbObj.notes=''
    dbObj.length_m=122.300003
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Decca 1229','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','LW-08','PHS-32 Active','PHS-32 Passive','SMART-S','STIR 180']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.205921
    dbObj.mfTurnRate_degps=2.121835
    dbObj.mfFuelCapacity_kg=464800.000000
    dbObj.mfFuelRate_kgps=0.464796
    dbObj.mfToughness=200.000000
    dbObj.damageEffect='Karel Doorman DDG durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['Mk-48 Mod1 VLS','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','76mm/62 Mark 100 Compact','30mm/77 GAU-8/A Goalkeeper','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 1.2 Support','Mk-48 VLS Mod1 16 Cell','Goalkeeper x1 Store','76mm/62 mk75 240 rounds']
    dbObj.magazineId=[3,1,2,0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[360.000000,0.000000,0.000000,320.000000,340.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,90.000000,270.000000,0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[90.000000,45.000000,45.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['STIR 180','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,False,False,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=42.362999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.742001
    airDetectionDBObject.irSignature_dB=23.631001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=7.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=10.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S04.Destroyer'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.800000
    dbObj.beam_m=14.400000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=43190.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Single Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
