# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag400kg'
    dbObj.maxRange_m=3090.479248
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=143.852234
    dbObj.fragCharge_kg=124.098511
    dbObj.radCharge_kg=14.385223
    dbObj.fragMetal_kg=132.049255
    dbObj.fragFragment_kg=0.027510
    dbObj.fragSpread=0.300000
    return dbObj
