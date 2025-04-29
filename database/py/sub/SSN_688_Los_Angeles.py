# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='SSN 688 Los Angeles'
    dbObj.natoClass='SSN 688 Los Angeles'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=6082000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1976.869995
    dbObj.finalYear=2999.989990
    dbObj.country='USA'
    dbObj.designation='SSN'
    dbObj.imageList='688-1.jpg;688-2.jpg'
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes='No VLS in original 688 class. Tube launched versions of harpoon and ugm-109 should be included? Leaving it as just torpedoes for now'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['BPS-15F','BQQ-5D Active','BQQ-5D Bow Passive','BQQ-5D Port Flank Passive','BQQ-5D Stbd Flank Passive','ESM-1','Periscope-1','TB-16 TA']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,270.000000,90.000000,0.000000,0.000000,180.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.000000
    dbObj.mfAccel_ktsps=1.250000
    dbObj.mfTurnRate_degps=2.000000
    dbObj.mfFuelCapacity_kg=0.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='SSN 688 Los Angeles durability'
    dbObj.mnNumLaunchers=6
    dbObj.maLauncherClass=['533mm 688 Tube','533mm 688 Tube','533mm 688 Tube','533mm 688 Tube','CSA Mk1','CSA Mk1']
    dbObj.maMagazineClass=['688 magazine']
    dbObj.mnNumMagazines=1
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','CM','CM']
    dbObj.launcherFOV_deg=[360.000000,360.000000,360.000000,360.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','']
    dbObj.launcherFireControl2=['','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=6.000000
    airDetectionDBObject.irSignature_dB=10.000000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=12.000000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='AN175'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=9.400000
    dbObj.surfaceSpeed_kts=20.000000
    dbObj.mfMaxDepth_m=375.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=64.000000
    dbObj.CalculateParams()
    return dbObj
