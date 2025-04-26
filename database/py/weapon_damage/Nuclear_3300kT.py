# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-3300kT'
    dbObj.maxRange_m=45458.402344
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=3630000128.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1650000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
