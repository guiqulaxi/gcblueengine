# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-950kT'
    dbObj.maxRange_m=31287.947266
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=1045000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=475000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
