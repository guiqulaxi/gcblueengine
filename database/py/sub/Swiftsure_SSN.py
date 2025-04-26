# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcSubDBObject()
    dbObj.mzClass='Swiftsure SSN'
    dbObj.natoClass='Swiftsure SSN'
    dbObj.mnModelType=8
    dbObj.mnType=129
    dbObj.cost=900000000.000000
    dbObj.weight_kg=4400000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1973.290894
    dbObj.finalYear=2010.939819
    dbObj.country='UK'
    dbObj.designation='SSN'
    dbObj.imageList=''
    dbObj.iconFileName=''
    dbObj.mz3DModelFileName='688.xml'
    dbObj.notes=''
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-1','Periscope-1','Type 1007(s)','Type 2046 TA','Type 2074 Active','Type 2074 Bow Passive','Type 2074 Port Flank Passive','Type 2074 Stbd Flank Passive']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,270.000000,90.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=31.000000
    dbObj.mfAccel_ktsps=1.100000
    dbObj.mfTurnRate_degps=3.000000
    dbObj.mfFuelCapacity_kg=1.000000
    dbObj.mfFuelRate_kgps=0.000000
    dbObj.mfToughness=100.000000
    dbObj.damageEffect='Swiftsure SSN durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['533mm Swiftsure tube','533mm Swiftsure tube','533mm Swiftsure tube','533mm Swiftsure tube','533mm Swiftsure tube','CSA Mk1','CSA Mk1']
    dbObj.maMagazineClass=['Switsure Torpedo Racking']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['Tube 1','Tube 2','Tube 3','Tube 4','Tube 5','CM','CM']
    dbObj.launcherFOV_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,360.000000,360.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,45.000000,315.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','','']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[True,True,True,True,True,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=10.900000
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.900000
    airDetectionDBObject.irSignature_dB=8.900000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=4.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=11.497000
    waterDetectionDBObject.TS_Model='SubTSDefault'
    waterDetectionDBObject.acousticModel='BN175'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.500000
    dbObj.surfaceSpeed_kts=20.000000
    dbObj.mfMaxDepth_m=355.000000
    dbObj.isDieselElectric=False
    dbObj.batteryRate_kW=1.000000
    dbObj.batteryCharge_kW=3.500000
    dbObj.CalculateParams()
    return dbObj
