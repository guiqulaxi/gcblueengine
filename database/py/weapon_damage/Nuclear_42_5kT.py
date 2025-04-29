# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-42.5kT'
    dbObj.maxRange_m=12319.034180
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=46750000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=21250000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
