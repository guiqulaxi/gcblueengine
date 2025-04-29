# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-72.5kT'
    dbObj.maxRange_m=14459.770508
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=79750000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=36250000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
