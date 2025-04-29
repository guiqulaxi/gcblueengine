# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag285kg'
    dbObj.maxRange_m=2715.883057
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=102.460594
    dbObj.fragCharge_kg=88.442940
    dbObj.radCharge_kg=10.246059
    dbObj.fragMetal_kg=94.096466
    dbObj.fragFragment_kg=0.021231
    dbObj.fragSpread=0.300000
    return dbObj
