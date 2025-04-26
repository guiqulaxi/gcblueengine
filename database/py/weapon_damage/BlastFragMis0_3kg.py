# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis0.3kg'
    dbObj.maxRange_m=499.145233
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.090000
    dbObj.fragCharge_kg=0.114000
    dbObj.radCharge_kg=0.009000
    dbObj.fragMetal_kg=0.096000
    dbObj.fragFragment_kg=0.001000
    dbObj.fragSpread=0.017778
    return dbObj
