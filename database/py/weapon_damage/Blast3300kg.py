# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Blast3300kg'
    dbObj.maxRange_m=185.770279
    dbObj.probDetonate=0.850000
    dbObj.blastCharge_kg=3300.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=330.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=0.000000
    return dbObj
