# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag8.8kg'
    dbObj.maxRange_m=532.128357
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3.114364
    dbObj.fragCharge_kg=2.763757
    dbObj.radCharge_kg=0.311436
    dbObj.fragMetal_kg=2.921879
    dbObj.fragFragment_kg=0.001186
    dbObj.fragSpread=0.300000
    return dbObj
