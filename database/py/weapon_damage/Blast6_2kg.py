# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast6.2kg'
    dbObj.maxRange_m=22.970869
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=6.200000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.620000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
