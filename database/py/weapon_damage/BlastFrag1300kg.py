# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1300kg'
    dbObj.maxRange_m=5082.650879
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=467.823151
    dbObj.fragCharge_kg=403.117889
    dbObj.radCharge_kg=46.782318
    dbObj.fragMetal_kg=429.058960
    dbObj.fragFragment_kg=0.077058
    dbObj.fragSpread=0.300000
    return dbObj
