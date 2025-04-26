# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast28.5kg'
    dbObj.maxRange_m=38.174591
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=28.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=2.850000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
