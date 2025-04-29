# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag205kg'
    dbObj.maxRange_m=2369.088867
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=73.668716
    dbObj.fragCharge_kg=63.637520
    dbObj.radCharge_kg=7.366872
    dbObj.fragMetal_kg=67.693764
    dbObj.fragFragment_kg=0.016210
    dbObj.fragSpread=0.300000
    return dbObj
