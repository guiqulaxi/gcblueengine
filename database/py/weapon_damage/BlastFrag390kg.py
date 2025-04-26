# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag390kg'
    dbObj.maxRange_m=3062.098633
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=140.252853
    dbObj.fragCharge_kg=120.998093
    dbObj.radCharge_kg=14.025286
    dbObj.fragMetal_kg=128.749054
    dbObj.fragFragment_kg=0.027003
    dbObj.fragSpread=0.300000
    return dbObj
