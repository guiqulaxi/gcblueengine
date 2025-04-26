# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast4.5kg'
    dbObj.maxRange_m=20.645760
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=4.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.450000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
