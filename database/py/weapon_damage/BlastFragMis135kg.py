# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis135kg'
    dbObj.maxRange_m=4101.864746
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=24.167841
    dbObj.fragCharge_kg=62.188107
    dbObj.radCharge_kg=2.416784
    dbObj.fragMetal_kg=48.644054
    dbObj.fragFragment_kg=0.046240
    dbObj.fragSpread=0.300000
    return dbObj
