# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast8.8kg'
    dbObj.maxRange_m=25.812130
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=8.800000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.880000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
