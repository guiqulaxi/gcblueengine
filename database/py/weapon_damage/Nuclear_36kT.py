# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-36kT'
    dbObj.maxRange_m=11720.624023
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=39600000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=18000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
