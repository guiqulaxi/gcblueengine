# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag5.6kg'
    dbObj.maxRange_m=421.673340
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.973511
    dbObj.fragCharge_kg=1.764326
    dbObj.radCharge_kg=0.197351
    dbObj.fragMetal_kg=1.862163
    dbObj.fragFragment_kg=0.000843
    dbObj.fragSpread=0.300000
    return dbObj
