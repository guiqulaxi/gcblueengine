# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast7.4kg'
    dbObj.maxRange_m=24.364929
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.740000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
