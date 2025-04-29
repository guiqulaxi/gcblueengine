# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2800kg'
    dbObj.maxRange_m=6875.254883
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1007.804260
    dbObj.fragCharge_kg=868.130493
    dbObj.radCharge_kg=100.780426
    dbObj.fragMetal_kg=924.065247
    dbObj.fragFragment_kg=0.147332
    dbObj.fragSpread=0.300000
    return dbObj
