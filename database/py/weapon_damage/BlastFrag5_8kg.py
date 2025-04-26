# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag5.8kg'
    dbObj.maxRange_m=429.977661
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.044646
    dbObj.fragCharge_kg=1.826903
    dbObj.radCharge_kg=0.204465
    dbObj.fragMetal_kg=1.928451
    dbObj.fragFragment_kg=0.000867
    dbObj.fragSpread=0.300000
    return dbObj
