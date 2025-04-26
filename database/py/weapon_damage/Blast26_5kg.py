# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast26.5kg'
    dbObj.maxRange_m=37.260780
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=26.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.650000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
