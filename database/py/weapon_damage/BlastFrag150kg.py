# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag150kg'
    dbObj.maxRange_m=2062.600586
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=53.876423
    dbObj.fragCharge_kg=46.582386
    dbObj.radCharge_kg=5.387642
    dbObj.fragMetal_kg=49.541191
    dbObj.fragFragment_kg=0.012385
    dbObj.fragSpread=0.300000
    return dbObj
