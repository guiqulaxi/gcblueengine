# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragMis2000kg'
    dbObj.maxRange_m=8893.160156
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=225.077362
    dbObj.fragCharge_kg=1009.948425
    dbObj.radCharge_kg=22.507736
    dbObj.fragMetal_kg=764.974243
    dbObj.fragFragment_kg=0.244635
    dbObj.fragSpread=0.300000
    return dbObj
