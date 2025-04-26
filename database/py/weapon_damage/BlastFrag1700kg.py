# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1700kg'
    dbObj.maxRange_m=5644.907227
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=611.816528
    dbObj.fragCharge_kg=527.122314
    dbObj.radCharge_kg=61.181656
    dbObj.fragMetal_kg=561.061157
    dbObj.fragFragment_kg=0.096336
    dbObj.fragSpread=0.300000
    return dbObj
