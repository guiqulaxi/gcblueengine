# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcWeaponDamage()
    dbObj.databaseClass='Nuclear-640kT'
    dbObj.maxRange_m=27791.626953
    dbObj.probDetonate=0.900000
    dbObj.blastCharge_kg=704000000.000000
    dbObj.fragCharge_kg=0.000000
    dbObj.radCharge_kg=320000000.000000
    dbObj.fragMetal_kg=0.000000
    dbObj.fragFragment_kg=0.000000
    dbObj.fragSpread=1.000000
    return dbObj
