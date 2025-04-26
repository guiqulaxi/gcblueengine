# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-42500kT'
    dbObj.maxRange_m=97853.570312
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=46749999104.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=21250000896.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
