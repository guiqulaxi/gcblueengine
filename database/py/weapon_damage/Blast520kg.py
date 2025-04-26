# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast520kg'
    dbObj.maxRange_m=100.401497
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=520.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=52.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
