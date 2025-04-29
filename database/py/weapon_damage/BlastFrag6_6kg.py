# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag6.6kg'
    dbObj.maxRange_m=461.011902
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.329459
    dbObj.fragCharge_kg=2.077027
    dbObj.radCharge_kg=0.232946
    dbObj.fragMetal_kg=2.193514
    dbObj.fragFragment_kg=0.000959
    dbObj.fragSpread=0.300000
    return dbObj
