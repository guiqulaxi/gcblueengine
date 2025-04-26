# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag3.4kg'
    dbObj.maxRange_m=326.583435
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.193818
    dbObj.fragCharge_kg=1.074121
    dbObj.radCharge_kg=0.119382
    dbObj.fragMetal_kg=1.132061
    dbObj.fragFragment_kg=0.000595
    dbObj.fragSpread=0.300000
    return dbObj
