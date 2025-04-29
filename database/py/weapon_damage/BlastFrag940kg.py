# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag940kg'
    dbObj.maxRange_m=4456.057617
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=338.231171
    dbObj.fragCharge_kg=291.512573
    dbObj.radCharge_kg=33.823116
    dbObj.fragMetal_kg=310.256287
    dbObj.fragFragment_kg=0.058407
    dbObj.fragSpread=0.300000
    return dbObj
