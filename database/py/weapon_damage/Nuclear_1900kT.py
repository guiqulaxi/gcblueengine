# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-1900kT'
    dbObj.maxRange_m=38519.980469
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=2090000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=950000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
