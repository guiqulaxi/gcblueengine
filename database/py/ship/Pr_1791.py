# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1791'
    dbObj.natoClass='Amga AEM'
    dbObj.mnModelType=1
    dbObj.mnType=18
    dbObj.cost=0.000000
    dbObj.weight_kg=6350000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1900.099976
    dbObj.finalYear=3000.000000
    dbObj.country='Russia'
    dbObj.designation='AEM'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='Need photo for this one'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','ESM-6','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Strut Curve AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=15.800000
    dbObj.mfAccel_ktsps=0.018542
    dbObj.mfTurnRate_degps=1.291192
    dbObj.mfFuelCapacity_kg=698500.000000
    dbObj.mfFuelRate_kgps=0.287932
    dbObj.mfToughness=93.000000
    dbObj.damageEffect='Pr 1791 durability'
    dbObj.mnNumLaunchers=2
    dbObj.maLauncherClass=['25 mm MGS','25 mm MGS']
    dbObj.maMagazineClass=['Pr1791 Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1]
    dbObj.launcherName=['','']
    dbObj.launcherFOV_deg=[360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000]
    dbObj.launcherFireControl=['','']
    dbObj.launcherFireControl2=['','']
    dbObj.launcherIsReloadable=[True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=46.587002
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=24.224001
    airDetectionDBObject.irSignature_dB=21.223000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=14.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S002.Merchant Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=3.590000
    dbObj.beam_m=17.559999
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=7500.000000
    dbObj.ExhaustStacks=1.000000
    dbObj.PropulsionShafts=2.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
