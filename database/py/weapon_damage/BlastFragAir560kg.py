# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir560kg'
    dbObj.maxRange_m=5610.066895
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=80.602974
    dbObj.fragCharge_kg=271.064697
    dbObj.radCharge_kg=8.060297
    dbObj.fragMetal_kg=208.332336
    dbObj.fragFragment_kg=0.089528
    dbObj.fragSpread=0.300000
    return dbObj
