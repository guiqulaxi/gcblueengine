# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag57.5kg'
    dbObj.maxRange_m=1312.748169
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=20.600071
    dbObj.fragCharge_kg=17.891619
    dbObj.radCharge_kg=2.060007
    dbObj.fragMetal_kg=19.008310
    dbObj.fragFragment_kg=0.005327
    dbObj.fragSpread=0.300000
    return dbObj
