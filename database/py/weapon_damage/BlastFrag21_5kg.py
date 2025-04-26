# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag21.5kg'
    dbObj.maxRange_m=836.009277
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.664332
    dbObj.fragCharge_kg=6.715445
    dbObj.radCharge_kg=0.766433
    dbObj.fragMetal_kg=7.120223
    dbObj.fragFragment_kg=0.002432
    dbObj.fragSpread=0.300000
    return dbObj
