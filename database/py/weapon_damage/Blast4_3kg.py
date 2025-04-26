# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast4.3kg'
    dbObj.maxRange_m=20.335560
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.300000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.430000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
