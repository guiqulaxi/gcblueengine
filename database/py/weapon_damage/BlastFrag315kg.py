# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag315kg'
    dbObj.maxRange_m=2825.028076
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=113.258125
    dbObj.fragCharge_kg=97.744583
    dbObj.radCharge_kg=11.325812
    dbObj.fragMetal_kg=103.997292
    dbObj.fragFragment_kg=0.022968
    dbObj.fragSpread=0.300000
    return dbObj
