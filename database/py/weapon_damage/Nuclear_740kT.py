# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-740kT'
    dbObj.maxRange_m=29028.828125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=814000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=370000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
