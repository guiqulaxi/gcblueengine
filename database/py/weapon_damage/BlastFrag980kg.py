# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag980kg'
    dbObj.maxRange_m=4526.079102
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=352.630127
    dbObj.fragCharge_kg=303.913239
    dbObj.radCharge_kg=35.263012
    dbObj.fragMetal_kg=323.456635
    dbObj.fragFragment_kg=0.060346
    dbObj.fragSpread=0.300000
    return dbObj
