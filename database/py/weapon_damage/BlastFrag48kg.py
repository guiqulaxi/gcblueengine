# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag48kg'
    dbObj.maxRange_m=1202.239624
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.184525
    dbObj.fragCharge_kg=14.943650
    dbObj.radCharge_kg=1.718452
    dbObj.fragMetal_kg=15.871825
    dbObj.fragFragment_kg=0.004550
    dbObj.fragSpread=0.300000
    return dbObj
