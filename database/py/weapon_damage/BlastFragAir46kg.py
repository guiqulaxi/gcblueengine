# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir46kg'
    dbObj.maxRange_m=3388.536621
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.456408
    dbObj.fragCharge_kg=20.375729
    dbObj.radCharge_kg=0.945641
    dbObj.fragMetal_kg=16.167864
    dbObj.fragFragment_kg=0.031212
    dbObj.fragSpread=0.300000
    return dbObj
