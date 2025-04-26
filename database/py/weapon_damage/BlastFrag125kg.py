# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag125kg'
    dbObj.maxRange_m=1895.320557
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=44.880920
    dbObj.fragCharge_kg=38.829388
    dbObj.radCharge_kg=4.488092
    dbObj.fragMetal_kg=41.289692
    dbObj.fragFragment_kg=0.010533
    dbObj.fragSpread=0.300000
    return dbObj
