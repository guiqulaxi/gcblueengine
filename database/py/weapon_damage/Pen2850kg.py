# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen2850kg'
    dbObj.maxRange_m=157.105743
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1995.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=285.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
