# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast9.2kg'
    dbObj.maxRange_m=26.197050
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=9.200000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.920000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
