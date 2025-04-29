# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag780kg'
    dbObj.maxRange_m=4128.966797
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=280.635773
    dbObj.fragCharge_kg=241.909485
    dbObj.radCharge_kg=28.063576
    dbObj.fragMetal_kg=257.454742
    dbObj.fragFragment_kg=0.049817
    dbObj.fragSpread=0.300000
    return dbObj
