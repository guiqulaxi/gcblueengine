# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFragAir7.6kg'
    dbObj.maxRange_m=2111.470459
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1.899846
    dbObj.fragCharge_kg=3.141436
    dbObj.radCharge_kg=0.189985
    dbObj.fragMetal_kg=2.558718
    dbObj.fragFragment_kg=0.012184
    dbObj.fragSpread=0.085069
    return dbObj
