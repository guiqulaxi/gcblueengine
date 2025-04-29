# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1000kg'
    dbObj.maxRange_m=6691.807129
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=129.633789
    dbObj.fragCharge_kg=493.577484
    dbObj.radCharge_kg=12.963379
    dbObj.fragMetal_kg=376.788727
    dbObj.fragFragment_kg=0.130966
    dbObj.fragSpread=0.300000
    return dbObj
