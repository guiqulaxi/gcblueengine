# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir7.4kg'
    dbObj.maxRange_m=2087.024902
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.854717
    dbObj.fragCharge_kg=3.055522
    dbObj.radCharge_kg=0.185472
    dbObj.fragMetal_kg=2.489761
    dbObj.fragFragment_kg=0.011913
    dbObj.fragSpread=0.084261
    return dbObj
