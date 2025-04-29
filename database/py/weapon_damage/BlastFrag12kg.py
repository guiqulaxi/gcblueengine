# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag12kg'
    dbObj.maxRange_m=624.503357
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.258715
    dbObj.fragCharge_kg=3.760857
    dbObj.radCharge_kg=0.425871
    dbObj.fragMetal_kg=3.980428
    dbObj.fragFragment_kg=0.001517
    dbObj.fragSpread=0.300000
    return dbObj
