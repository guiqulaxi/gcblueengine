# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast1800kg'
    dbObj.maxRange_m=151.815750
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=1800.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=180.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
