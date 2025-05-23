# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcJetDBObject()
    dbObj.mzClass='F3H-2'
    dbObj.natoClass='F3H-2'
    dbObj.mnModelType=12
    dbObj.mnType=33
    dbObj.cost=0.000000
    dbObj.weight_kg=10040.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1957.000000
    dbObj.finalYear=1962.000000
    dbObj.country='USA'
    dbObj.designation='Fighter'
    dbObj.imageList=''
    dbObj.iconFileName='air/AdvicoF3H2.jpg'
    dbObj.mz3DModelFileName='harrier-gr3.xml'
    dbObj.notes='560kt max speed at altitude, 2205km range, 716mph sl and 643mph 35kft'
    dbObj.length_m=1.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['APG-51B','Eyeball 20/10','Eyeball 20/10d','Eyeball 20/10e','Eyeball 20/10f']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=725.000000
    dbObj.mfAccel_ktsps=22.389999
    dbObj.mfTurnRate_degps=14.000000
    dbObj.mfFuelCapacity_kg=4576.080078
    dbObj.mfFuelRate_kgps=0.950000
    dbObj.mfToughness=1.000000
    dbObj.damageEffect='F3H-2 durability'
    dbObj.mnNumLaunchers=7
    dbObj.maLauncherClass=['20mm Colt Mk-12 Cannon (150)','20mm Colt Mk-12 Cannon (150)','20mm Colt Mk-12 Cannon (150)','20mm Colt Mk-12 Cannon (150)','F3H Fuselage','F3H Wing2','F3H Wing1']
    dbObj.maMagazineClass=[]
    dbObj.mnNumMagazines=0
    dbObj.magazineId=[]
    dbObj.launcherId=[0,1,2,3,4,5,6]
    dbObj.launcherName=['','','','','','','']
    dbObj.launcherFOV_deg=[10.000000,10.000000,10.000000,10.000000,0.000000,0.000000,0.000000]
    dbObj.launcherAz_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','','','APG-51B','APG-51B']
    dbObj.launcherFireControl2=['','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=12.000000
    airDetectionDBObject.RCS_Model='AirRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=4.300000
    airDetectionDBObject.irSignature_dB=0.000000
    airDetectionDBObject.IR_ModelA='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelB='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.IR_ModelC='IR_FW_M_F_HP_1_M0.85'
    airDetectionDBObject.effectiveHeight_m=0.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=-999.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='Default'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.maxTakeoffWeight_kg=15950.000000
    dbObj.maxAltitude_m=13000.000000
    dbObj.climbRate_mps=74.000000
    dbObj.gmax=6.000000
    dbObj.minimumRunway_m=0.000000
    dbObj.isCarrierCompatible=True
    dbObj.outFuelPods=0
    dbObj.fuelOut_kgps=0.000000
    dbObj.fuelIn_kgps=20.000000
    dbObj.maintenanceMin_s=3600.000000
    dbObj.maintenanceMax_s=10800.000000
    dbObj.militaryThrust_N=44500.000000
    dbObj.militaryThrustSpeedSlope=0.004080
    dbObj.mfAfterburnThrust_N=64100.000000
    dbObj.abThrustSpeedSlope=0.005100
    dbObj.mfAfterburnFuelRate_kgps=2.196000
    dbObj.mfCdpsub=1.066700
    dbObj.mfCdptran=1.600000
    dbObj.mfCdpsup=1.280000
    dbObj.mfMcm=0.850000
    dbObj.mfMsupm=1.200000
    dbObj.cruiseSpeed_mps=90.000000
    dbObj.stallSpeed_mps=45.000000
    dbObj.thrustTable=[0.810000,0.645000,0.510000,0.406000,0.319500,0.235500,0.080000,0.000000,0.000000,0.000000]
    dbObj.fuelEfficiencyTable=[0.980000,0.950000,0.900000,0.950000,1.100000,1.500000,2.500000,5.000000,20.000000,40.000000]
    dbObj.CalculateParams()
    return dbObj
