# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag55kg'
    dbObj.maxRange_m=1284.007080
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=19.701166
    dbObj.fragCharge_kg=17.115889
    dbObj.radCharge_kg=1.970117
    dbObj.fragMetal_kg=18.182945
    dbObj.fragFragment_kg=0.005119
    dbObj.fragSpread=0.300000
    return dbObj
