# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen4000kg'
    dbObj.maxRange_m=175.879288
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2800.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=400.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
