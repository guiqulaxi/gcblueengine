# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir175kg'
    dbObj.maxRange_m=4285.969238
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=30.208624
    dbObj.fragCharge_kg=81.360916
    dbObj.radCharge_kg=3.020862
    dbObj.fragMetal_kg=63.430458
    dbObj.fragFragment_kg=0.050663
    dbObj.fragSpread=0.300000
    return dbObj
