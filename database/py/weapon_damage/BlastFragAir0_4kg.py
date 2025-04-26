# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir0.4kg'
    dbObj.maxRange_m=499.145233
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.120000
    dbObj.fragCharge_kg=0.152000
    dbObj.radCharge_kg=0.012000
    dbObj.fragMetal_kg=0.128000
    dbObj.fragFragment_kg=0.001000
    dbObj.fragSpread=0.031605
    return dbObj
