# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag160kg'
    dbObj.maxRange_m=2123.926025
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=57.474831
    dbObj.fragCharge_kg=49.683445
    dbObj.radCharge_kg=5.747483
    dbObj.fragMetal_kg=52.841724
    dbObj.fragFragment_kg=0.013106
    dbObj.fragSpread=0.300000
    return dbObj
