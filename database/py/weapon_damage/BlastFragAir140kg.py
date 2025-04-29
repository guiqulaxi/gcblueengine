# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir140kg'
    dbObj.maxRange_m=4129.017090
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=24.937374
    dbObj.fragCharge_kg=64.575081
    dbObj.radCharge_kg=2.493737
    dbObj.fragMetal_kg=50.487541
    dbObj.fragFragment_kg=0.046878
    dbObj.fragSpread=0.300000
    return dbObj
