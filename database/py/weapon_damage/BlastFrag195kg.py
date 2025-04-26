# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag195kg'
    dbObj.maxRange_m=2318.433838
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=70.069954
    dbObj.fragCharge_kg=60.536697
    dbObj.radCharge_kg=7.006995
    dbObj.fragMetal_kg=64.393349
    dbObj.fragFragment_kg=0.015539
    dbObj.fragSpread=0.300000
    return dbObj
