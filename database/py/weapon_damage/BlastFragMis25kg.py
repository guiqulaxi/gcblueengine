# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis25kg'
    dbObj.maxRange_m=3021.629150
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.515319
    dbObj.fragCharge_kg=10.823121
    dbObj.radCharge_kg=0.551532
    dbObj.fragMetal_kg=8.661560
    dbObj.fragFragment_kg=0.024747
    dbObj.fragSpread=0.236304
    return dbObj
