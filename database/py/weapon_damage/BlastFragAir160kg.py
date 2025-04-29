# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir160kg'
    dbObj.maxRange_m=4224.946289
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=27.972931
    dbObj.fragCharge_kg=74.151382
    dbObj.radCharge_kg=2.797293
    dbObj.fragMetal_kg=57.875690
    dbObj.fragFragment_kg=0.049172
    dbObj.fragSpread=0.300000
    return dbObj
