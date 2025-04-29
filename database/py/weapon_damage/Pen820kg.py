# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Pen820kg'
    dbObj.maxRange_m=103.759712
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=574.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=82.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
