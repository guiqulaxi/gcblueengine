# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir370kg'
    dbObj.maxRange_m=5024.250977
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=57.037376
    dbObj.fragCharge_kg=176.575089
    dbObj.radCharge_kg=5.703738
    dbObj.fragMetal_kg=136.387543
    dbObj.fragFragment_kg=0.070777
    dbObj.fragSpread=0.300000
    return dbObj
