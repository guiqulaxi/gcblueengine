# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-6800kT'
    dbObj.maxRange_m=56469.332031
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=7480000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3400000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
