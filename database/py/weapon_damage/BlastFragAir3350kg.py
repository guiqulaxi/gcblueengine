# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3350kg'
    dbObj.maxRange_m=10755.071289
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=334.387482
    dbObj.fragCharge_kg=1720.074951
    dbObj.radCharge_kg=33.438747
    dbObj.fragMetal_kg=1295.537476
    dbObj.fragFragment_kg=0.374000
    dbObj.fragSpread=0.300000
    return dbObj
