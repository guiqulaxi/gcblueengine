# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcShipDBObject()
    dbObj.mzClass='Pr 1143 Krechet'
    dbObj.natoClass='Kiev'
    dbObj.mnModelType=2
    dbObj.mnType=22
    dbObj.cost=0.000000
    dbObj.weight_kg=41370000.000000
    dbObj.volume_m3=0.000000
    dbObj.initialYear=1975.989990
    dbObj.finalYear=2004.180054
    dbObj.country='Russia'
    dbObj.designation='CV'
    dbObj.imageList=''
    dbObj.iconFileName='none'
    dbObj.mz3DModelFileName='hermes.xml'
    dbObj.notes='Some ships sold to China and India. Also has Moose Jaw LF sonar but didnt include.   bumped up the flight deck according to Janes ships 81-82.  normal compliment is 32 aircraft, provided room for 34. bumped up the number of stage 2 aircraft from 2 to 8.  provided a generational loadout.'
    dbObj.length_m=0.000000
    dbObj.width_m=1.000000
    dbObj.height_m=1.000000
    sensorPlatformDBObject=pygcb.tcSensorPlatformDBObject()
    sensorPlatformDBObject.sensorClass=['Don 2 SS','Eyeball 20/20','Eyeball 20/20b','Eyeball 20/20c','Eyeball 20/20d','Head Lights FC','MG-325 Vega TA','MG-335 Platina Active','MG-335 Platina Passive','MR-123 Vympel FC','MR-600 Voskhod AS','Pop Group FC','Rum Tub']
    sensorPlatformDBObject.sensorAz=[0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,180.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.AddComponent(sensorPlatformDBObject)
    dbObj.mfMaxSpeed_kts=32.500000
    dbObj.mfAccel_ktsps=0.022280
    dbObj.mfTurnRate_degps=0.779267
    dbObj.mfFuelCapacity_kg=4550700.000000
    dbObj.mfFuelRate_kgps=2.795969
    dbObj.mfToughness=1512.000000
    dbObj.damageEffect='Pr 1143 Krechet durability'
    dbObj.mnNumLaunchers=19
    dbObj.maLauncherClass=['SA-N-3 x2 launcher','SA-N-3 x2 launcher','P-500 launcher x8','9K33 Osa Launcher','9K33 Osa Launcher','76 mm/59 (3in) AK-726','76 mm/59 (3in) AK-726','76 mm/59 (3in) AK-726','76 mm/59 (3in) AK-726','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','30 mm/54 (1.2in) AK-630M','533mm torpedo x5 tubes','533mm torpedo x5 tubes']
    dbObj.maMagazineClass=['Carrier Fuel Supply','Carrier Magazine']
    dbObj.magazineId=[0,1]
    dbObj.launcherId=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    dbObj.launcherName=['','','','','','','','','','','','','','','','','','','']
    dbObj.launcherFOV_deg=[270.000000,270.000000,0.000000,270.000000,270.000000,320.000000,270.000000,180.000000,220.000000,200.000000,180.000000,200.000000,170.000000,180.000000,160.000000,180.000000,160.000000,40.000000,40.000000]
    dbObj.launcherAz_deg=[135.000000,225.000000,0.000000,45.000000,315.000000,0.000000,0.000000,180.000000,180.000000,45.000000,65.000000,315.000000,295.000000,110.000000,150.000000,250.000000,210.000000,270.000000,90.000000]
    dbObj.launcherEl_deg=[10.000000,10.000000,10.000000,10.000000,10.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
    dbObj.launcherFireControl=['Head Lights FC','Head Lights FC','','Pop Group FC','Pop Group FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','MR-123 Vympel FC','','']
    dbObj.launcherFireControl2=['','','','','','','','','','','','','','','','','','','']
    dbObj.launcherIsReloadable=[False,False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,True]
    airDetectionDBObject=pygcb.tcAirDetectionDBObject()
    airDetectionDBObject.RCS_dBsm=58.796001
    airDetectionDBObject.RCS_Model='ShipRCS1'
    airDetectionDBObject.opticalCrossSection_dBsm=32.797001
    airDetectionDBObject.irSignature_dB=22.334999
    airDetectionDBObject.IR_ModelA='ShipIR1'
    airDetectionDBObject.IR_ModelB='ShipIR1'
    airDetectionDBObject.IR_ModelC='ShipIR1'
    airDetectionDBObject.effectiveHeight_m=20.000000
    airDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(airDetectionDBObject)
    waterDetectionDBObject=pygcb.tcWaterDetectionDBObject()
    waterDetectionDBObject.TS=20.000000
    waterDetectionDBObject.TS_Model='Default'
    waterDetectionDBObject.acousticModel='S11.Carrier Medium'
    waterDetectionDBObject.SL_Model='Default'
    waterDetectionDBObject.BindSignatureModels()
    dbObj.AddComponent(waterDetectionDBObject)
    dbObj.draft_m=8.950000
    dbObj.beam_m=49.200001
    dbObj.PowerPlantType=0.000000
    dbObj.TotalShaft_HP=180000.000000
    dbObj.ExhaustStacks=2.000000
    dbObj.PropulsionShafts=4.000000
    dbObj.PropulsiveEfficiency=0.470000
    dbObj.CivilianPaintScheme=0.000000
    dbObj.FlashyPaintScheme=0.000000
    dbObj.flightportClass='Kiev Flightdeck'
    dbObj.CalculateParams()
    return dbObj
