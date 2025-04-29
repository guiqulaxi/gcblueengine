# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2.6kg'
    dbObj.maxRange_m=17.198759
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2.600000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.260000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
