# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-5kT'
    dbObj.maxRange_m=6482.626465
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=5500000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2500000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
