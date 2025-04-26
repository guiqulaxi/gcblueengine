# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-26500kT'
    dbObj.maxRange_m=84924.648438
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=29149999104.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=13249999872.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
