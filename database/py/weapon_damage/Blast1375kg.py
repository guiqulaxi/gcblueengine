# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1375kg'
    dbObj.maxRange_m=138.792465
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1375.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=137.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
