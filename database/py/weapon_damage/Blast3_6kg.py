# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3.6kg'
    dbObj.maxRange_m=19.167250
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.360000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
