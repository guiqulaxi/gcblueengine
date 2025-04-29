# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen42kg'
    dbObj.maxRange_m=38.571880
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=29.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=4.200000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
