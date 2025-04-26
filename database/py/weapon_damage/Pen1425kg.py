# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen1425kg'
    dbObj.maxRange_m=124.723732
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=997.500000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=142.500000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
