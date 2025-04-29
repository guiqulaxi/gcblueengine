# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir1575kg'
    dbObj.maxRange_m=8090.520020
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=186.528000
    dbObj.fragCharge_kg=789.148010
    dbObj.radCharge_kg=18.652800
    dbObj.fragMetal_kg=599.323975
    dbObj.fragFragment_kg=0.198452
    dbObj.fragSpread=0.300000
    return dbObj
