# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast5.8kg'
    dbObj.maxRange_m=22.466351
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=5.800000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.580000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
