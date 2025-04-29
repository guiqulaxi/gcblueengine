# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1475kg'
    dbObj.maxRange_m=142.075378
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1475.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=147.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
