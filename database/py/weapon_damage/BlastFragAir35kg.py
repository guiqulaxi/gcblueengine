# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir35kg'
    dbObj.maxRange_m=3236.055664
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.431002
    dbObj.fragCharge_kg=15.345999
    dbObj.radCharge_kg=0.743100
    dbObj.fragMetal_kg=12.223000
    dbObj.fragFragment_kg=0.028426
    dbObj.fragSpread=0.300000
    return dbObj
