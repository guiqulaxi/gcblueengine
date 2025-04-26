# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag50kg'
    dbObj.maxRange_m=1223.760498
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=17.903517
    dbObj.fragCharge_kg=15.564322
    dbObj.radCharge_kg=1.790352
    dbObj.fragMetal_kg=16.532162
    dbObj.fragFragment_kg=0.004697
    dbObj.fragSpread=0.300000
    return dbObj
