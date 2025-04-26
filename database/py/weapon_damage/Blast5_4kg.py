# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast5.4kg'
    dbObj.maxRange_m=21.938061
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.400000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.540000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
