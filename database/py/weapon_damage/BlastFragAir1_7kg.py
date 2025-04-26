# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1.7kg'
    dbObj.maxRange_m=1054.546509
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.487752
    dbObj.fragCharge_kg=0.660832
    dbObj.radCharge_kg=0.048775
    dbObj.fragMetal_kg=0.551416
    dbObj.fragFragment_kg=0.003383
    dbObj.fragSpread=0.051252
    return dbObj
