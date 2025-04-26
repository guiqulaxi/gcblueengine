# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-6400kT'
    dbObj.maxRange_m=55451.585938
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=7040000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=3200000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
