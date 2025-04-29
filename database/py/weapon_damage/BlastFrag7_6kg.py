# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag7.6kg'
    dbObj.maxRange_m=495.600739
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.685980
    dbObj.fragCharge_kg=2.389347
    dbObj.radCharge_kg=0.268598
    dbObj.fragMetal_kg=2.524673
    dbObj.fragFragment_kg=0.001066
    dbObj.fragSpread=0.300000
    return dbObj
