# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-30250kT'
    dbObj.maxRange_m=88364.453125
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=33275000832.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=15125000192.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
