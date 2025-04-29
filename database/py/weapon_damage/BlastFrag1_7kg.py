# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag1.7kg'
    dbObj.maxRange_m=209.604324
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.598913
    dbObj.fragCharge_kg=0.535725
    dbObj.radCharge_kg=0.059891
    dbObj.fragMetal_kg=0.565362
    dbObj.fragFragment_kg=0.000346
    dbObj.fragSpread=0.300000
    return dbObj
