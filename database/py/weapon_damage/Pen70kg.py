# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen70kg'
    dbObj.maxRange_m=45.724232
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=49.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=7.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
