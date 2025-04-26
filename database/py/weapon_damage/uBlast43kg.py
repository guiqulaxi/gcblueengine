# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='uBlast43kg'
    dbObj.maxRange_m=297.828430
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=43.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
