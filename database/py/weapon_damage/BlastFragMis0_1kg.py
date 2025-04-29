# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.1kg'
    dbObj.maxRange_m=499.145233
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.030000
    dbObj.fragCharge_kg=0.038000
    dbObj.radCharge_kg=0.003000
    dbObj.fragMetal_kg=0.032000
    dbObj.fragFragment_kg=0.001000
    dbObj.fragSpread=0.001975
    return dbObj
