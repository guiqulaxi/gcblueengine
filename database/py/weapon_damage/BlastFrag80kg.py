# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag80kg'
    dbObj.maxRange_m=1538.699219
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=28.691925
    dbObj.fragCharge_kg=24.872049
    dbObj.radCharge_kg=2.869193
    dbObj.fragMetal_kg=26.436026
    dbObj.fragFragment_kg=0.007122
    dbObj.fragSpread=0.300000
    return dbObj
