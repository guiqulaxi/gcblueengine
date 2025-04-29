# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis34kg'
    dbObj.maxRange_m=3218.715088
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.242994
    dbObj.fragCharge_kg=14.891337
    dbObj.radCharge_kg=0.724299
    dbObj.fragMetal_kg=11.865668
    dbObj.fragFragment_kg=0.028118
    dbObj.fragSpread=0.300000
    return dbObj
