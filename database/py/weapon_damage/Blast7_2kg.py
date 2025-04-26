# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast7.2kg'
    dbObj.maxRange_m=24.143641
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=7.200000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=0.720000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
