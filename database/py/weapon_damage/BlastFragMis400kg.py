# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis400kg'
    dbObj.maxRange_m=5123.507812
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=60.892921
    dbObj.fragCharge_kg=191.404724
    dbObj.radCharge_kg=6.089292
    dbObj.fragMetal_kg=147.702362
    dbObj.fragFragment_kg=0.073777
    dbObj.fragSpread=0.300000
    return dbObj
