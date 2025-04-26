# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1025kT'
    dbObj.maxRange_m=32009.371094
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1127500032.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=512500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
