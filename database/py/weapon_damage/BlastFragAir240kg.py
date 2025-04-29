# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir240kg'
    dbObj.maxRange_m=4479.577637
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=39.559395
    dbObj.fragCharge_kg=112.827072
    dbObj.radCharge_kg=3.955940
    dbObj.fragMetal_kg=87.613533
    dbObj.fragFragment_kg=0.055557
    dbObj.fragSpread=0.300000
    return dbObj
