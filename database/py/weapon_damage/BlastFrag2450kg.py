# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag2450kg'
    dbObj.maxRange_m=6518.382812
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=881.807556
    dbObj.fragCharge_kg=759.628296
    dbObj.radCharge_kg=88.180756
    dbObj.fragMetal_kg=808.564148
    dbObj.fragFragment_kg=0.131260
    dbObj.fragSpread=0.300000
    return dbObj
