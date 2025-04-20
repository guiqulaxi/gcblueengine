import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Oslo FFGM (1987)'
    dbObj.natoClass='Oslo FFGM (1987)'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=1762841.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1987.910034
    dbObj.finalYear=2007.579956
    dbObj.country='Norway'
    dbObj.designation='FF'
    dbObj.imageList='oslo_87.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='burke.xml'
    dbObj.notes='[kbluck] Second modernization 87-91. Fitted with TSM 2633 hull and VDS sonar. 2x Penguin and DC rail removed to make room for VDS. Aft 76mm replaced with 40mm/70.'
    dbObj.length_m=96.599998
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['9LV 200 FCS','DRBV 22','Decca 1226','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Mk-91 FCS','TSM 2633 Active','TSM 2633 Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=25.000000
    dbObj.mfAccel_ktsps=0.054955
    dbObj.mfTurnRate_degps=2.537319
    dbObj.mfFuelCapacity_kg=246797.734375
    dbObj.mfFuelRate_kgps=0.228514
    dbObj.mfToughness=0.000000
    dbObj.damageEffect='Oslo FFGM (1977) durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['Penguin SSM Launcher x4','SeaSparrow x8 Launcher','3/50 Mark 33','Bofors 40 mm/70 Mark 3','20mm Rh 202','20mm Rh 202','Mk-32 3 Torpedo Mount','Mk-32 3 Torpedo Mount']
    dbObj.maMagazineClass=['Oslo Magazine','Mk-32 Torpedo Racks','Sea Sparrow Reloads']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[0.000000,320.000000,240.000000,240.000000,180.000000,180.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,0.000000,180.000000,90.000000,90.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[20.000000,0.000000,85.000000,90.000000,55.000000,55.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','Mk-91 FCS','9LV 200 FCS','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[False,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=38.238998
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=22.909000
    airDetectionDBObject.irSignature_dB=21.422001
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.600000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=5.500000
    dbObj.beam_m=11.200000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=20000.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='None'
    dbObj.CalculateParams()
    return dbObj
