# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag24.5kg'
    dbObj.maxRange_m=886.354309
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.741111
    dbObj.fragCharge_kg=7.647593
    dbObj.radCharge_kg=0.874111
    dbObj.fragMetal_kg=8.111297
    dbObj.fragFragment_kg=0.002682
    dbObj.fragSpread=0.300000
    return dbObj
