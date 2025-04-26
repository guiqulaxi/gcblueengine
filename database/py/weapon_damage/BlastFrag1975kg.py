# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1975kg'
    dbObj.maxRange_m=5970.530273
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=710.812866
    dbObj.fragCharge_kg=612.374756
    dbObj.radCharge_kg=71.081284
    dbObj.fragMetal_kg=651.812378
    dbObj.fragFragment_kg=0.108635
    dbObj.fragSpread=0.300000
    return dbObj
