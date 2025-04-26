# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-70kT'
    dbObj.maxRange_m=14308.344727
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=77000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=35000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
