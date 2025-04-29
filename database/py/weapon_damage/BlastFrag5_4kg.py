# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag5.4kg'
    dbObj.maxRange_m=413.127533
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.902408
    dbObj.fragCharge_kg=1.701728
    dbObj.radCharge_kg=0.190241
    dbObj.fragMetal_kg=1.795864
    dbObj.fragFragment_kg=0.000819
    dbObj.fragSpread=0.300000
    return dbObj
