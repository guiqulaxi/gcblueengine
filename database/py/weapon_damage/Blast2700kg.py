# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast2700kg'
    dbObj.maxRange_m=173.762177
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=2700.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=270.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
