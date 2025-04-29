# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag560kg'
    dbObj.maxRange_m=3587.643799
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=201.443939
    dbObj.fragCharge_kg=173.704041
    dbObj.radCharge_kg=20.144394
    dbObj.fragMetal_kg=184.852020
    dbObj.fragFragment_kg=0.037269
    dbObj.fragSpread=0.300000
    return dbObj
