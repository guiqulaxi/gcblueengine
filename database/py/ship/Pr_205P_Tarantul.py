# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 205P Tarantul'
    dbObj.natoClass='Stenka'
    dbObj.mnModelType=1
    dbObj.mnType=17
    dbObj.cost=0.000000
    dbObj.weight_kg=253000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1967.000000
    dbObj.finalYear=2013.660034
    dbObj.country='Russia'
    dbObj.designation='wPT'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='sovremenny.xml'
    dbObj.notes='the USSR built 137 of these, but while I can find their names, I cannot find service entry or exit, even so much as the year.  I do know Primorskiy shipyard in leningrad built 105 of them between 1967 and 1989.  will space their entries evenly across this.  Spaced the first group by 90 days each, spaced the second grouping by 130 days each.  Each group is from a different ship yard, and the spacing allows them to cover their full range evenly.  Knowing only 19 remain in soviet service, i can space out the exit dates to be fairly consistent, yet leave 19 still operating by 2011.  Of course this will not be random, the oldest will go first, etc.  Exit from service will be over a 6 year period.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['ESM-4','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','MG-329 Shelon VDS','Palm Frond SS','Peel Cone AS/SS']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=36.000000
    dbObj.mfAccel_ktsps=0.284999
    dbObj.mfTurnRate_degps=7.250546
    dbObj.mfFuelCapacity_kg=35420.000000
    dbObj.mfFuelRate_kgps=0.091100
    dbObj.mfToughness=18.980000
    dbObj.damageEffect='Pr 205P Tarantul durability'
    dbObj.mnNumLaunchers=4
    dbObj.maLauncherClass=['30 mm/63 (1.2in) AK-230','30 mm/63 (1.2in) AK-230','406mm torpedo x2 tubes','406mm torpedo x2 tubes']
    dbObj.maMagazineClass=['Pr205P Ammo Mag']
    dbObj.magazineId=[0]
    dbObj.launcherId=[0,1,2,3]
    dbObj.launcherName=['','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[0.000000,180.000000,90.000000,270.000000]
    dbObj.launcherEl_deg=[0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['','','','']
    dbObj.launcherFireControl2=['','','','']
    dbObj.launcherIsReloadable=[True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=25.591999
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=16.798000
    airDetectionDBObject.irSignature_dB=17.337000
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=2.400000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=15.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S02.Frigate'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=1.960000
    dbObj.beam_m=7.910000
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=15000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=3.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass=''
    dbObj.CalculateParams()
    return dbObj
