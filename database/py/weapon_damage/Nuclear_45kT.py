# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-45kT'
    dbObj.maxRange_m=12532.096680
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=49500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=22500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
