# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis43kg'
    dbObj.maxRange_m=3352.772217
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.911208
    dbObj.fragCharge_kg=18.999195
    dbObj.radCharge_kg=0.891121
    dbObj.fragMetal_kg=15.089598
    dbObj.fragFragment_kg=0.030546
    dbObj.fragSpread=0.300000
    return dbObj
