# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast45kg'
    dbObj.maxRange_m=44.445808
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=45.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=4.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
