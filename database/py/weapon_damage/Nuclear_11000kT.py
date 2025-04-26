# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-11000kT'
    dbObj.maxRange_m=65234.570312
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=12099999744.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=5500000256.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
