# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir20.5kg'
    dbObj.maxRange_m=2882.685791
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.622897
    dbObj.fragCharge_kg=8.808069
    dbObj.radCharge_kg=0.462290
    dbObj.fragMetal_kg=7.069035
    dbObj.fragFragment_kg=0.022513
    dbObj.fragSpread=0.190193
    return dbObj
