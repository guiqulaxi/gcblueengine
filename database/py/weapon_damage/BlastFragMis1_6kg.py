# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1.6kg'
    dbObj.maxRange_m=1021.185059
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.461453
    dbObj.fragCharge_kg=0.620364
    dbObj.radCharge_kg=0.046145
    dbObj.fragMetal_kg=0.518182
    dbObj.fragFragment_kg=0.003199
    dbObj.fragSpread=0.050625
    return dbObj
