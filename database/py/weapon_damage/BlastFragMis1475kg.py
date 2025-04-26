# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis1475kg'
    dbObj.maxRange_m=7877.740234
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=177.071259
    dbObj.fragCharge_kg=737.452515
    dbObj.radCharge_kg=17.707125
    dbObj.fragMetal_kg=560.476257
    dbObj.fragFragment_kg=0.187137
    dbObj.fragSpread=0.300000
    return dbObj
