# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag240kg'
    dbObj.maxRange_m=2532.342529
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=86.264832
    dbObj.fragCharge_kg=74.490112
    dbObj.radCharge_kg=8.626483
    dbObj.fragMetal_kg=79.245056
    dbObj.fragFragment_kg=0.018481
    dbObj.fragSpread=0.300000
    return dbObj
