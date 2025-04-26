# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis460kg'
    dbObj.maxRange_m=5296.499023
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=68.441261
    dbObj.fragCharge_kg=221.172501
    dbObj.radCharge_kg=6.844126
    dbObj.fragMetal_kg=170.386246
    dbObj.fragFragment_kg=0.079176
    dbObj.fragSpread=0.300000
    return dbObj
