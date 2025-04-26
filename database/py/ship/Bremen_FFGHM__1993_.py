# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Bremen FFGHM (1993)'
    dbObj.natoClass='Bremen FFGHM (1993)'
    dbObj.mnModelType=2
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=2997338.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1993.000000
    dbObj.finalYear=2999.000000
    dbObj.country='Germany'
    dbObj.designation='FF'
    dbObj.imageList='bremen_07.jpg'
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='type-22.xml'
    dbObj.notes='RIM-166A, although high capacity, is still essentially a point defense system.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['DSQS-21BZ Active','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','STIR 240','TRS 3D/32']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=30.000000
    dbObj.mfAccel_ktsps=0.302368
    dbObj.mfTurnRate_degps=2.160063
    dbObj.mfFuelCapacity_kg=419627.312500
    dbObj.mfFuelRate_kgps=0.524530
    dbObj.mfToughness=140.000000
    dbObj.damageEffect='Bremen FFGHM (1982) durability'
    dbObj.mnNumLaunchers=8
    dbObj.maLauncherClass=['SeaSparrow x8 Launcher','RIM-116A RAM x21','RIM-116A RAM x21','Mk-141 Harpoon Launcher','Mk-141 Harpoon Launcher','76 mm/62 Mark 75','Mk-32 2 Torpedo Mount','Mk-32 2 Torpedo Mount']
    dbObj.maMagazineClass=['Lynx 1.1 Support','76mm/62 mk75 240 rounds','RIM-116 21 x2 Store']
    dbObj.magazineId=[0,1,2]
    dbObj.launcherId=[0,1,2,3,4,5,6,7]
    dbObj.launcherName=['','','','','','','','']
    dbObj.launcherFOV_deg=[330.000000,345.000000,345.000000,30.000000,30.000000,300.000000,30.000000,30.000000]
    dbObj.launcherAz_deg=[0.000000,195.000000,165.000000,90.000000,270.000000,0.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[40.000000,40.000000,40.000000,20.000000,20.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['STIR 240','STIR 240','STIR 240','','','','','']
    dbObj.launcherFireControl2=['','','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,False,False,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=41.696999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=25.171000
    airDetectionDBObject.irSignature_dB=23.604000
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
    dbObj.draft_m=6.300000
    dbObj.beam_m=14.600000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=61875.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.510000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Double Helo Hangar'
    dbObj.CalculateParams()
    return dbObj
