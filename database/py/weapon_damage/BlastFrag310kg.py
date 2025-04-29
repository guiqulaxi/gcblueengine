# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag310kg'
    dbObj.maxRange_m=2807.481445
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=111.458519
    dbObj.fragCharge_kg=96.194321
    dbObj.radCharge_kg=11.145852
    dbObj.fragMetal_kg=102.347160
    dbObj.fragFragment_kg=0.022683
    dbObj.fragSpread=0.300000
    return dbObj
