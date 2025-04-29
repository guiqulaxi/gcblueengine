# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis820kg'
    dbObj.maxRange_m=6327.383789
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=110.313118
    dbObj.fragCharge_kg=402.057922
    dbObj.radCharge_kg=11.031312
    dbObj.fragMetal_kg=307.628967
    dbObj.fragFragment_kg=0.115999
    dbObj.fragSpread=0.300000
    return dbObj
