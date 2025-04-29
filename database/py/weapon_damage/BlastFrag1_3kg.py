# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.3kg'
    dbObj.maxRange_m=173.152908
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.461529
    dbObj.fragCharge_kg=0.407314
    dbObj.radCharge_kg=0.046153
    dbObj.fragMetal_kg=0.431157
    dbObj.fragFragment_kg=0.000282
    dbObj.fragSpread=0.300000
    return dbObj
