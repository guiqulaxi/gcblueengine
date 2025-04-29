# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir47kg'
    dbObj.maxRange_m=3399.683838
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.637053
    dbObj.fragCharge_kg=20.835299
    dbObj.radCharge_kg=0.963705
    dbObj.fragMetal_kg=16.527649
    dbObj.fragFragment_kg=0.031421
    dbObj.fragSpread=0.300000
    return dbObj
