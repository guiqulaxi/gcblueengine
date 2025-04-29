# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag260kg'
    dbObj.maxRange_m=2617.167725
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=93.462860
    dbObj.fragCharge_kg=80.691429
    dbObj.radCharge_kg=9.346286
    dbObj.fragMetal_kg=85.845711
    dbObj.fragFragment_kg=0.019726
    dbObj.fragSpread=0.300000
    return dbObj
