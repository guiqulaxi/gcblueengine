import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Fletcher(Japan)'
    dbObj.natoClass='Fletcher(Japan)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2050000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1959.189941
    dbObj.finalYear=1974.180054
    dbObj.country='Japan'
    dbObj.designation='DD'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes=''
    dbObj.length_m=114.800003
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','QHBa Active','SPS-12','SPS-6B','SPS-8A']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=34.500000
    dbObj.mfAccel_ktsps=0.086037
    dbObj.mfTurnRate_degps=2.714729
    dbObj.mfFuelCapacity_kg=287000.000000
    dbObj.mfFuelRate_kgps=0.250172
    dbObj.mfToughness=126.099998
    dbObj.damageEffect='Fletcher durability'
    dbObj.mnNumLaunchers=23
    dbObj.maLauncherClass=['5/38 Mark 12','5/38 Mark 12','5/38 Mark 12','5/38 Mark 12','5/38 Mark 12','Mk-32 5 Torpedo Mount','Mk-32 5 Torpedo Mount','40mm Bofors Mk12 x2','40mm Bofors Mk12 x2','40mm Bofors Mk12 x2','40mm Bofors Mk12 x2','40mm Bofors Mk12 x2','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','20mm/70 Oerlikon Mk1/2/3/4','Kgun','Kgun','DC Rack 12']
    dbObj.maMagazineClass=['Fletcher Secondary Magazine','Fletcher Primary Magazine','Fletcher Torpedo Racks']
    dbObj.magazineId=[1,0,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,22,23,24,25]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','','','Kgun','Kgun','Rack']
    dbObj.launcherFOV_deg=[270.000000,270.000000,270.000000,270.000000,270.000000,360.000000,360.000000,310.000000,310.000000,200.000000,200.000000,200.000000,310.000000,310.000000,200.000000,200.000000,200.000000,200.000000,310.000000,310.000000,1.000000,1.000000,1.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,180.000000,180.000000,90.000000,270.000000,160.000000,200.000000,90.000000,90.000000,270.000000,160.000000,200.000000,90.000000,90.000000,270.000000,270.000000,20.000000,340.000000,150.000000,210.000000,180.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,45.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=39.222000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=23.785999
    airDetectionDBObject.irSignature_dB=24.466999
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
    dbObj.draft_m=5.300000
    dbObj.beam_m=12.000000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=60000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
