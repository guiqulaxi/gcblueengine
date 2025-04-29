# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='BlastFrag0.2kg'
    dbObj.maxRange_m=100.586266
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=0.072000
    dbObj.fragCharge_kg=0.062000
    dbObj.radCharge_kg=0.007200
    dbObj.fragMetal_kg=0.066000
    dbObj.fragFragment_kg=0.000172
    dbObj.fragSpread=0.300000
    return dbObj
