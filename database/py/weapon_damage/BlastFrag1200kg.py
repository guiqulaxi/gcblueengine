# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1200kg'
    dbObj.maxRange_m=4920.783691
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=431.825134
    dbObj.fragCharge_kg=372.116577
    dbObj.radCharge_kg=43.182514
    dbObj.fragMetal_kg=396.058289
    dbObj.fragFragment_kg=0.071958
    dbObj.fragSpread=0.300000
    return dbObj
