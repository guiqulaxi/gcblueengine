# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1100kg'
    dbObj.maxRange_m=4748.205566
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=395.827271
    dbObj.fragCharge_kg=341.115143
    dbObj.radCharge_kg=39.582729
    dbObj.fragMetal_kg=363.057587
    dbObj.fragFragment_kg=0.066739
    dbObj.fragSpread=0.300000
    return dbObj
