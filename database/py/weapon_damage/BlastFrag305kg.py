# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag305kg'
    dbObj.maxRange_m=2789.686279
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=109.658920
    dbObj.fragCharge_kg=94.644051
    dbObj.radCharge_kg=10.965892
    dbObj.fragMetal_kg=100.697029
    dbObj.fragFragment_kg=0.022397
    dbObj.fragSpread=0.300000
    return dbObj
