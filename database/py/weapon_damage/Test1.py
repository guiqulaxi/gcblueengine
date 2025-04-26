# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Test1'
    dbObj.maxRange_m=1000.000000
    dbObj.probDetonate=0.950000
    dbObj.blastCharge_kg=10.000000
    dbObj.fragCharge_kg=10.000000
    dbObj.radCharge_kg=0.000000
    dbObj.fragMetal_kg=10.000000
    dbObj.fragFragment_kg=0.010000
    dbObj.fragSpread=1.000000
    return dbObj
