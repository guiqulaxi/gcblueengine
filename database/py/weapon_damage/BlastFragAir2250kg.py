# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir2250kg'
    dbObj.maxRange_m=9305.285156
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=246.676025
    dbObj.fragCharge_kg=1140.549316
    dbObj.radCharge_kg=24.667603
    dbObj.fragMetal_kg=862.774658
    dbObj.fragFragment_kg=0.270547
    dbObj.fragSpread=0.300000
    return dbObj
