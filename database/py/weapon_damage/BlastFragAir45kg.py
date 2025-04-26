# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir45kg'
    dbObj.maxRange_m=3377.015625
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.275227
    dbObj.fragCharge_kg=19.916515
    dbObj.radCharge_kg=0.927523
    dbObj.fragMetal_kg=15.808258
    dbObj.fragFragment_kg=0.030997
    dbObj.fragSpread=0.300000
    return dbObj
