# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1350kg'
    dbObj.maxRange_m=5159.965332
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=485.822235
    dbObj.fragCharge_kg=418.618500
    dbObj.radCharge_kg=48.582222
    dbObj.fragMetal_kg=445.559265
    dbObj.fragFragment_kg=0.079564
    dbObj.fragSpread=0.300000
    return dbObj
