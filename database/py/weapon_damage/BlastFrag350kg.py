# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag350kg'
    dbObj.maxRange_m=2941.381104
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=125.855522
    dbObj.fragCharge_kg=108.596313
    dbObj.radCharge_kg=12.585552
    dbObj.fragMetal_kg=115.548157
    dbObj.fragFragment_kg=0.024903
    dbObj.fragSpread=0.300000
    return dbObj
