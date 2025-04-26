# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir3.4kg'
    dbObj.maxRange_m=1495.323120
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.917381
    dbObj.fragCharge_kg=1.360413
    dbObj.radCharge_kg=0.091738
    dbObj.fragMetal_kg=1.122206
    dbObj.fragFragment_kg=0.006340
    dbObj.fragSpread=0.060434
    return dbObj
