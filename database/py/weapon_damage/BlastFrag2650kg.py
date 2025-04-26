# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2650kg'
    dbObj.maxRange_m=6726.759277
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=953.805603
    dbObj.fragCharge_kg=821.629578
    dbObj.radCharge_kg=95.380562
    dbObj.fragMetal_kg=874.564819
    dbObj.fragFragment_kg=0.140515
    dbObj.fragSpread=0.300000
    return dbObj
