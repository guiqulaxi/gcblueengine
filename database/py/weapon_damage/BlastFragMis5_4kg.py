# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis5.4kg'
    dbObj.maxRange_m=1838.529419
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.395405
    dbObj.fragCharge_kg=2.201730
    dbObj.radCharge_kg=0.139540
    dbObj.fragMetal_kg=1.802865
    dbObj.fragFragment_kg=0.009341
    dbObj.fragSpread=0.071854
    return dbObj
