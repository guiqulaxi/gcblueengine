# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.4kg'
    dbObj.maxRange_m=186.014374
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.495702
    dbObj.fragCharge_kg=0.439532
    dbObj.radCharge_kg=0.049570
    dbObj.fragMetal_kg=0.464766
    dbObj.fragFragment_kg=0.000304
    dbObj.fragSpread=0.300000
    return dbObj
