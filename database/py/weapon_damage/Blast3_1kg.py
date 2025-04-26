# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3.1kg'
    dbObj.maxRange_m=18.236210
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.100000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.310000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
