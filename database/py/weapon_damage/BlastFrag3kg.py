# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3kg'
    dbObj.maxRange_m=304.547485
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.052905
    dbObj.fragCharge_kg=0.948063
    dbObj.radCharge_kg=0.105290
    dbObj.fragMetal_kg=0.999032
    dbObj.fragFragment_kg=0.000543
    dbObj.fragSpread=0.300000
    return dbObj
