# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3450kg'
    dbObj.maxRange_m=7454.272949
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1241.799072
    dbObj.fragCharge_kg=1069.633911
    dbObj.radCharge_kg=124.179909
    dbObj.fragMetal_kg=1138.567017
    dbObj.fragFragment_kg=0.175705
    dbObj.fragSpread=0.300000
    return dbObj
