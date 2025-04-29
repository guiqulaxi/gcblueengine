# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir8.4kg'
    dbObj.maxRange_m=2188.735840
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.079095
    dbObj.fragCharge_kg=3.485936
    dbObj.radCharge_kg=0.207910
    dbObj.fragMetal_kg=2.834968
    dbObj.fragFragment_kg=0.013064
    dbObj.fragSpread=0.090835
    return dbObj
