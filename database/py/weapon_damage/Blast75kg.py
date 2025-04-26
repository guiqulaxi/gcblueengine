# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast75kg'
    dbObj.maxRange_m=52.687370
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=75.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=7.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
