# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-3600kT'
    dbObj.maxRange_m=46660.644531
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=3960000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=1800000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
