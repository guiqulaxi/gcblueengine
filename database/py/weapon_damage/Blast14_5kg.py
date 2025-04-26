# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast14.5kg'
    dbObj.maxRange_m=30.482220
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=14.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1.450000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
